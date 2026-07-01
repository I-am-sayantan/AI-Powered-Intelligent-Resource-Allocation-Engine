"""Machine-learning allocation.

Uses a trained classifier to predict assignment-success probability for every
technician/request pair, then optimizes total predicted success under the hard
constraints.
"""

from __future__ import annotations

from algorithms.base import Allocator
from fixtures.mock_data import mock_allocation_result
from schemas.allocation import AllocationResult
from schemas.common import AlgorithmType
from schemas.request import ServiceRequest
from schemas.technician import Technician


class MLAllocator(Allocator):
    """Assignment that maximizes ML-predicted success probability."""

    algorithm = AlgorithmType.ml

    def allocate(
        self,
        technicians: list[Technician],
        requests: list[ServiceRequest],
        respect_hard_constraints: bool = True,
    ) -> AllocationResult:
        # TODO: Implement the real ML strategy:
        #   1. Engineer features for every feasible technician/request pair.
        #   2. Score pairs with the active trained model (predict_proba).
        #   3. Optimize the assignment (e.g. Hungarian on -success) to maximize
        #      total predicted success while respecting hard constraints.
        return mock_allocation_result(self.algorithm)
