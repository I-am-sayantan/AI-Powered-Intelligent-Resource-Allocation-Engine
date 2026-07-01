"""Allocation service: runs allocators and compares them.

Delegates to the allocator classes in ``algorithms`` (which currently return mock
results) so this layer already exercises the real interface.
"""

from __future__ import annotations

from algorithms import get_allocator
from core.logging import get_logger
from fixtures.mock_data import mock_compare_result
from schemas.allocation import (
    AllocationRequest,
    AllocationResult,
    CompareRequest,
    CompareResult,
)
from services.data_service import ensure_seeded
from services.store import InMemoryStore

logger = get_logger(__name__)


def allocate(request: AllocationRequest, store: InMemoryStore) -> AllocationResult:
    """Run the requested allocation algorithm and store the resulting assignments."""
    ensure_seeded(store)
    technicians = list(store.technicians.values())
    requests = list(store.requests.values())
    allocator = get_allocator(request.algorithm)
    result = allocator.allocate(technicians, requests, request.respect_hard_constraints)
    store.set_assignments(result.assignments)
    logger.info("Ran %s allocation: %d assignments", request.algorithm.value, len(result.assignments))
    return result


def compare(request: CompareRequest, store: InMemoryStore) -> CompareResult:
    """Compare all requested algorithms and return per-algorithm KPIs."""
    ensure_seeded(store)
    # TODO: run each requested allocator and aggregate real KPIs.
    return mock_compare_result()
