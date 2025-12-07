# Installation

## Requirements (FastReID)

- Linux or macOS with python ≥ 3.6
- PyTorch ≥ 1.6
- torchvision that matches the Pytorch installation. You can install them together at [pytorch.org](https://pytorch.org/) to make sure of this.
- [yacs](https://github.com/rbgirshick/yacs)
- Cython (optional to compile evaluation code)
- tensorboard (needed for visualization): `pip install tensorboard`
- gdown (for automatically downloading pre-train model)
- sklearn
- termcolor
- tabulate
- [faiss](https://github.com/facebookresearch/faiss) `pip install faiss-cpu`

pip install yacs Cython tensorboard gdown termcolor tabulate faiss-cpu -i https://pypi.tuna.tsinghua.edu.cn/simple

## Requirements (WildlifeDatasets)

pip install wildlife-datasets==1.0.4
