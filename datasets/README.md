# Setup Animal Dataset (It is recommended to use [WildlifeDatasets](https://github.com/WildlifeDatasets/wildlife-datasets) to download and organize the animal datasets.)

## Expected dataset structure for HyenaID

1. Download dataset to `datasets/` from [this link](https://lila.science/datasets/hyena-id-2022/)
2. Extract dataset. The dataset structure would like:

```bash
datasets/
    HyenaID2022/
        already_downloaded
        hyena.coco
            annotations
            images
        partition.json
```

## Expected dataset structure for LeopardID

1. Download dataset to `datasets/` from [this link](https://lila.science/datasets/leopard-id-2022/)
2. Extract dataset. The dataset structure would like:

```bash
datasets/
    LeopardID2022/
        already_downloaded
        leopard.coco
            annotations
            images
        partition.json
```

## Expected dataset structure for SeaTurtleID

1. Download dataset to `datasets/` from [this link](https://www.kaggle.com/datasets/wildlifedatasets/seaturtleidheads/)
2. Extract dataset. The dataset structure would like:

```bash
datasets/
    SeaTurtleIDHeads/
        annotations.json
        images
        license.txt
        partition.json  
```

## Expected dataset structure for WhaleSharkID

1. Download dataset to `datasets/` from [this link](https://lila.science/datasets/whale-shark-id)
2. Extract dataset. The dataset structure would like:

```bash
datasets/
    WhaleSharkID/
        already_downloaded
        partition.json
        whaleshark.coco
```


# Setup Person Dataset (Referring to [FastReID](https://github.com/JDAI-CV/fast-reid))

## Expected dataset structure for [Market1501](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Zheng_Scalable_Person_Re-Identification_ICCV_2015_paper.pdf)

1. Download dataset to `datasets/` from [baidu pan](https://pan.baidu.com/s/1ntIi2Op) or [google driver](https://drive.google.com/file/d/0B8-rUzbwVRk0c054eEozWG9COHM/view)
2. Extract dataset. The dataset structure would like:

```bash
datasets/
    Market-1501-v15.09.15/
        bounding_box_test/
        bounding_box_train/
```

## Expected dataset structure for [DukeMTMC-reID](https://openaccess.thecvf.com/content_ICCV_2017/papers/Zheng_Unlabeled_Samples_Generated_ICCV_2017_paper.pdf)

1. Download datasets to `datasets/`
2. Extract dataset. The dataset structure would like:

```bash
datasets/
    DukeMTMC-reID/
        bounding_box_train/
        bounding_box_test/
```

## Expected dataset structure for [MSMT17](https://arxiv.org/abs/1711.08565)

1. Download datasets to `datasets/`
2. Extract dataset. The dataset structure would like:

```bash
datasets/
    MSMT17_V2/
        mask_train_v2/
        mask_test_v2/
```
