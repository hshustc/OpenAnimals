# encoding: utf-8
"""
@author:  OpenAnimals (Based on FastReID and WildlifeDatasets)
@contact: OpenAnimals Team
"""

from .autoaugment import AutoAugment
from .build import build_transforms
from .transforms import *

__all__ = [k for k in globals().keys() if not k.startswith("_")]
