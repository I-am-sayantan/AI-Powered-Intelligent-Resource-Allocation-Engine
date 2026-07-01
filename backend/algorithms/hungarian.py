"""Hungarian algorithm allocation (global optimization).

Builds a cost matrix over technician/request pairs and solves the assignment
problem optimally with ``scipy.optimize.linear_sum_assignment``.
"""

from __future__ import annotations

from algorithms.base import Allocator
from fixtures.mock_data import mock_allocation_result
from schemas.allocation import AllocationResult
from schemas.common import AlgorithmType
from schemas.request import ServiceRequest
from schemas.technician import Technician


class HungarianAllocator(Allocator):
    """Optimal one-to-one assignment via the Hungarian method."""

    algorithm = AlgorithmType.hungarian

    def allocate(
        self,
        technicians: list[Technician],
        requests: list[ServiceRequest],
        respect_hard_constraints: bool = True,
    ) -> AllocationResult:
        # TODO: Implement the real Hungarian strategy:
        #   1. Build an (n_requests x n_technicians) cost matrix. Cost combines
        #      travel distance, workload balance, and (1 - predicted_success).
        #   2. Set infeasible pairs (hard-constraint violations) to a large cost.
        #   3. Solve with scipy.optimize.linear_sum_assignment and materialize
        #      the selected assignments.
        return mock_allocation_result(self.algorithm)
