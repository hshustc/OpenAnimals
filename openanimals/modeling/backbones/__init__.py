# encoding: utf-8
"""
@author:  OpenAnimals (Based on FastReID and WildlifeDatasets)
@contact: OpenAnimals Team
"""

from .build import build_backbone, BACKBONE_REGISTRY

from .resnet import build_resnet_backbone
