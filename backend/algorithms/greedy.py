"""Greedy allocation (baseline).

Assign each request (highest priority first) to the nearest feasible technician.
Fast but locally optimal only -- used as the comparison baseline.
"""

from __future__ import annotations

from algorithms.base import Allocator
from fixtures.mock_data import mock_allocation_result
from schemas.allocation import AllocationResult
from schemas.common import AlgorithmType
from schemas.request import ServiceRequest
from schemas.technician import Technician


class GreedyAllocator(Allocator):
    """Greedy nearest-feasible-technician assignment."""

    algorithm = AlgorithmType.greedy

    def allocate(
        self,
        technicians: list[Technician],
        requests: list[ServiceRequest],
        respect_hard_constraints: bool = True,
    ) -> AllocationResult:
        # TODO: Implement the real greedy strategy:
        #   1. Sort requests by descending priority (then earliest SLA deadline).
        #   2. For each request, pick the nearest technician that satisfies the
        #      hard constraints and has remaining daily capacity.
        #   3. Update technician workload and accumulate the objective score.
        return mock_allocation_result(self.algorithm)
