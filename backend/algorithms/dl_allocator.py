"""Deep-learning allocation.

Same optimization objective as :class:`MLAllocator` but backed by a neural
network (Feed-Forward NN or TabNet) for the success-probability scores.
"""

from __future__ import annotations

from algorithms.base import Allocator
from fixtures.mock_data import mock_allocation_result
from schemas.allocation import AllocationResult
from schemas.common import AlgorithmType
from schemas.request import ServiceRequest
from schemas.technician import Technician


class DLAllocator(Allocator):
    """Assignment driven by a deep-learning success predictor."""

    algorithm = AlgorithmType.dl

    def allocate(
        self,
        technicians: list[Technician],
        requests: list[ServiceRequest],
        respect_hard_constraints: bool = True,
    ) -> AllocationResult:
        # TODO: Implement the real DL strategy:
        #   1. Engineer features for every feasible technician/request pair.
        #   2. Score pairs with the trained neural network (FFNN / TabNet).
        #   3. Optimize the assignment to maximize total predicted success while
        #      respecting hard constraints.
        return mock_allocation_result(self.algorithm)
