# encoding: utf-8
"""
@author:  OpenAnimals (Based on FastReID and WildlifeDatasets)
@contact: OpenAnimals Team
"""

from .build import REID_HEADS_REGISTRY, build_heads

# import all the meta_arch, so they will be registered
from .embedding_head import EmbeddingHead
