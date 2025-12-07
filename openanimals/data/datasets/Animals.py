# encoding: utf-8
"""
@author:  Saihui Hou
@contact: hshustc@gmail.com
"""

import glob
import os.path as osp
import re
import warnings
import numpy as np
import json

from .bases import ImageDataset
from ..datasets import DATASET_REGISTRY

from wildlife_datasets import datasets, splits

@DATASET_REGISTRY.register()
class Animals(ImageDataset):
    """Animals ReID Dataset

    Reference:
        WildlifeDatasets: An Open-Source Toolkit for Animal Re-Identification, WACV 2024.

    URL: `https://github.com/WildlifeDatasets/wildlife-datasets`
    """

    def __init__(self, root='datasets', species='HyenaID2022', partition='partition.json', img_load='bbox', random_seed=666, **kwargs):
        self.root = root
        self.species = species
        self.dataset_dir = osp.join(root, species)
        self.partition = osp.join(root, species, partition)
        assert(img_load in ['full', 'bbox'])
        self.img_load = img_load
        np.random.seed(random_seed)

        dataset_func = getattr(datasets, self.species)
        # dataset_func.download(self.dataset_dir) # some links in wildlife_datasets failed
        # dataset_func.extract(self.dataset_dir)
        self.metadata = dataset_func(self.dataset_dir).df

        if osp.exists(self.partition):
            print('Partition File {} Exists'.format(self.partition))
            with open(self.partition, 'r') as f:
                cache = json.load(f)
            idx_train = np.asarray(cache['IDX_TRAIN'])
            idx_query = np.asarray(cache['IDX_QUERY'])
            idx_gallery = np.asarray(cache['IDX_GALLERY'])
        else:
            '''
            class DisjointSetSplit(IdentitySplit):
                def __init__(
                        self,
                        ratio_class_test: float = None, # *Approximate* ratio of samples of individuals only in the testing set.
                        n_class_test: int = None, # Number of individuals only in the testing set.
                        seed: int = 666, # Initial seed for the LCG random generator.
                        identity_skip: str = 'unknown', # Name of the identities to ignore.
                        ) -> None:
            '''
            splitter = splits.DisjointSetSplit(0.5, seed=random_seed) # ratio_class_test as default
            idx_train, idx_test = splitter.split(self.metadata)[0]
            idx_query, idx_gallery = self.process_probe_gallery(sorted(idx_test))
            cache = {
                'IDX_TRAIN': idx_train.tolist(), 
                'IDX_QUERY': idx_query.tolist(),
                'IDX_GALLERY': idx_gallery.tolist()
            }
            with open(self.partition, 'w') as f:
                f.write(json.dumps(cache))
            print('Partition File {} Saved'.format(self.partition))

        train = self.process_split(idx_train, split='train')
        query = self.process_split(idx_query, split='query')
        gallery = self.process_split(idx_gallery, split='gallery')
        super(Animals, self).__init__(train, query, gallery, **kwargs)
    
    def process_split(self, idx_list, split='train'):
        identity_list = sorted(self.metadata['identity'].unique())
        split_list = ['train', 'query', 'gallery']
        assert(split in split_list)

        split_data = []
        drop_nobbox = 0
        for idx in idx_list:
            data = self.metadata.iloc[idx]
            img_path = data['path']
            img_path = osp.join(self.dataset_dir, img_path)

            if split == 'train':
                pid = self.species + '_' + str(data['identity'])
                camid = self.species + '_' + str(split_list.index(split)) # 0 for train, 1 for query, 2 for gallery
            else:
                pid = identity_list.index(data['identity'])
                camid = split_list.index(split)
            
            if self.img_load == 'bbox' and 'bbox' not in data:
                warn_info = 'BBOX IS NOT SUPPORTED FOR {}'.format(self.species)
                warnings.warn(warn_info)
            if self.img_load == 'bbox' and 'bbox' in data:
                if type(data["bbox"]) == str:
                    bbox = json.loads(data["bbox"]) # refer to wilelife_tools/data/dataset.py
                else:
                    bbox = data["bbox"]
                if (isinstance(bbox, tuple) or isinstance(bbox, list)) and len(bbox) == 4:
                    bbox = np.asarray(bbox).astype('int')
                else:
                    # warn_info = 'Unknown BBOX={} FOR {} IN {}'.format(bbox, img_path, self.species)
                    # warnings.warn(warn_info)
                    drop_nobbox += 1 # drop samples due to invalid bbox
                    continue
            else:
                bbox = None
            
            # print('img_path={}, pid={}, camid={}, bbox={}'.format(img_path, pid, camid, bbox))
            split_data.append((img_path, pid, camid, bbox))

        print('PROCESS_SPLIT: SPLIT={}, TOTAL={}, VALID={}, DROP_NOBBOX={}'.format(split, len(idx_list), len(split_data), drop_nobbox))

        return split_data

    def process_probe_gallery(self, idx_list):
        pid_query_index = {}
        pid_query_count = {}
        npquery_pid = []
        idx_query = []
        idx_gallery = []
        for idx in idx_list:
            data = self.metadata.iloc[idx]
            pid = data['identity']
            pid_num_samples = (self.metadata['identity'] == pid).sum()
            # if pid not in pid_query_index.keys():
            #     print('identity={}, num_samples={}'.format(pid, pid_num_samples))
            if pid_num_samples < 3:
                if pid not in npquery_pid:
                    npquery_pid.append(pid)
                idx_gallery.append(idx) # those samples are treated as gallery
            else:
                if pid not in pid_query_index.keys():
                    pid_query_index[pid] = np.random.choice(np.arange(pid_num_samples), 2, replace=False)
                    pid_query_count[pid] = 0
                # print('identity={}, num_samples={}, pid_query_index={}, pid_query_count={}'.format(pid, pid_num_samples, pid_query_index[pid], pid_query_count[pid]))
                if pid_query_count[pid] in pid_query_index[pid]:
                    idx_query.append(idx)
                else:
                    idx_gallery.append(idx)
                pid_query_count[pid] +=1 

        test_metadata = self.metadata.iloc[idx_list]
        test_ids = test_metadata['identity'].unique()
        print('PROCESS_PROBE_GALLERY: TEST_ID={}, QUERY_ID={}, NOQUERY_ID={}'.format(len(test_ids), len(pid_query_index.keys()), len(npquery_pid)))
        assert(len(test_ids) == len(pid_query_index.keys()) +  len(npquery_pid))
        
        return np.asarray(idx_query), np.asarray(idx_gallery)
