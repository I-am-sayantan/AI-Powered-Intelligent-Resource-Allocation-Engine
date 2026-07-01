"""Tests for the allocation algorithms and their registry."""

from __future__ import annotations

import pytest

from algorithms import ALLOCATORS, get_allocator
from algorithms.base import Allocator
from fixtures.mock_data import mock_requests, mock_technicians
from schemas.common import AlgorithmType


def test_registry_covers_all_algorithms() -> None:
    assert set(ALLOCATORS) == set(AlgorithmType)


@pytest.mark.parametrize("algorithm", list(AlgorithmType))
def test_allocator_returns_result(algorithm: AlgorithmType) -> None:
    allocator = get_allocator(algorithm)
    assert isinstance(allocator, Allocator)
    assert allocator.algorithm == algorithm

    result = allocator.allocate(mock_technicians(6), mock_requests(5))
    assert result.algorithm == algorithm
    assert result.assignments
    assert result.runtime_ms >= 0
    for assignment in result.assignments:
        assert assignment.algorithm == algorithm
