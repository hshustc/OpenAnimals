# encoding: utf-8
"""
@author:  OpenAnimals (Based on FastReID and WildlifeDatasets)
@contact: OpenAnimals Team
"""

from . import losses
from .backbones import (
    BACKBONE_REGISTRY,
    build_resnet_backbone,
    build_backbone,
)
from .heads import (
    REID_HEADS_REGISTRY,
    build_heads,
    EmbeddingHead,
)
from .meta_arch import (
    build_model,
    META_ARCH_REGISTRY,
)

__all__ = [k for k in globals().keys() if not k.startswith("_")]