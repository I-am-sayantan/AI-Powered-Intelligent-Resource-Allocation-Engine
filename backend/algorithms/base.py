"""Allocation algorithm interface.

All allocators implement :class:`Allocator` so the optimization service can treat
them interchangeably. Concrete allocators currently return mock results and mark
their real optimization logic with ``TODO``.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from schemas.allocation import AllocationResult
from schemas.common import AlgorithmType
from schemas.request import ServiceRequest
from schemas.technician import Technician


class Allocator(ABC):
    """Base class for technician-to-request allocation strategies."""

    #: The algorithm identifier; set by each concrete subclass.
    algorithm: AlgorithmType

    @abstractmethod
    def allocate(
        self,
        technicians: list[Technician],
        requests: list[ServiceRequest],
        respect_hard_constraints: bool = True,
    ) -> AllocationResult:
        """Assign technicians to requests and return the resulting allocation.

        Args:
            technicians: Candidate technicians available for assignment.
            requests: Service requests needing a technician.
            respect_hard_constraints: When ``True``, enforce hard constraints
                (skill match, availability, daily job cap, SLA, working hours).

        Returns:
            An :class:`AllocationResult` with assignments, unassigned requests,
            KPIs, the objective score, and runtime.
        """
        raise NotImplementedError
