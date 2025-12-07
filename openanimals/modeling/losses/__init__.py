# encoding: utf-8
"""
@author:  OpenAnimals (Based on FastReID and WildlifeDatasets)
@contact: OpenAnimals Team
"""

from .circle_loss import *
from .cross_entroy_loss import cross_entropy_loss, log_accuracy
from .triplet_loss import triplet_loss

__all__ = [k for k in globals().keys() if not k.startswith("_")]