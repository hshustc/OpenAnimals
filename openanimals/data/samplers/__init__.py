# encoding: utf-8
"""
@author:  OpenAnimals (Based on FastReID and WildlifeDatasets)
@contact: OpenAnimals Team
"""

from .triplet_sampler import NaiveIdentitySampler
from .data_sampler import TrainingSampler, InferenceSampler

__all__ = [
    "NaiveIdentitySampler",
    "TrainingSampler",
    "InferenceSampler",
]
