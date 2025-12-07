# encoding: utf-8
"""
@author:  OpenAnimals (Based on FastReID and WildlifeDatasets)
@contact: OpenAnimals Team
"""

from .batch_norm import *
from .gather_layer import GatherLayer
from .helpers import to_ntuple, to_2tuple, to_3tuple, to_4tuple, make_divisible
from .non_local import Non_local
from .se_layer import SELayer
from .weight_init import (
    trunc_normal_, variance_scaling_, lecun_normal_, weights_init_kaiming, weights_init_classifier
)
