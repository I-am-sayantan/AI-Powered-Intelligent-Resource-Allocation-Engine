"""Allocation algorithms and the allocator registry."""

from __future__ import annotations

from algorithms.base import Allocator
from algorithms.dl_allocator import DLAllocator
from algorithms.greedy import GreedyAllocator
from algorithms.hungarian import HungarianAllocator
from algorithms.ml_allocator import MLAllocator
from schemas.common import AlgorithmType

#: Maps each algorithm identifier to its allocator class.
ALLOCATORS: dict[AlgorithmType, type[Allocator]] = {
    AlgorithmType.greedy: GreedyAllocator,
    AlgorithmType.hungarian: HungarianAllocator,
    AlgorithmType.ml: MLAllocator,
    AlgorithmType.dl: DLAllocator,
}


def get_allocator(algorithm: AlgorithmType) -> Allocator:
    """Instantiate the allocator registered for ``algorithm``."""
    return ALLOCATORS[algorithm]()


__all__ = [
    "ALLOCATORS",
    "Allocator",
    "DLAllocator",
    "GreedyAllocator",
    "HungarianAllocator",
    "MLAllocator",
    "get_allocator",
]
