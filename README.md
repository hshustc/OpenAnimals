
**OpenAnimals** is a flexible repository that aims to help researchers get started on **Animal Re-Identificatoin** quickly. 
This repository is built upon [FastReID](https://github.com/JDAI-CV/fast-reid) and [WildlifeDatasets](https://github.com/WildlifeDatasets/wildlife-datasets).


## Installation

Please refer to [INSTALL.md](INSTALL.md).

## Usage

1. Please refer to [README.md](datasets/README.md) for preparing the datasets.
2. Please refer to [run_animals.sh](run_animals.sh) for training and validation.

## Model Zoo

The pretrained models will be made publicly available later.

## Citation

If you use OpenAnimals in your research, please use the following BibTeX entry for [FastReID](https://github.com/JDAI-CV/fast-reid) and [WildlifeDatasets](https://github.com/WildlifeDatasets/wildlife-datasets).

```BibTeX
@inproceedings{he2023fastreid,
  title={Fastreid: A pytorch toolbox for general instance re-identification},
  author={He, Lingxiao and Liao, Xingyu and Liu, Wu and Liu, Xinchen and Cheng, Peng and Mei, Tao},
  booktitle={Proceedings of the 31st ACM International Conference on Multimedia},
  pages={9664--9667},
  year={2023}
}

@inproceedings{vcermak2024wildlifedatasets,
  title={WildlifeDatasets: An open-source toolkit for animal re-identification},
  author={{\v{C}}erm{\'a}k, Vojt{\v{e}}ch and Picek, Lukas and Adam, Luk{\'a}{\v{s}} and Papafitsoros, Kostas},
  booktitle={Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision},
  pages={5953--5963},
  year={2024}
}
```
