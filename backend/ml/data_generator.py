"""Synthetic data generator.

Produces realistic historical data per the PRD: technicians, service requests,
and a labelled table of historical assignments used to train the models.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from core.constants import DEFAULT_N_ASSIGNMENTS, DEFAULT_N_TECHNICIANS
from schemas.request import ServiceRequest
from schemas.technician import Technician

if TYPE_CHECKING:  # heavy import kept out of runtime for the stub
    import pandas as pd


def generate_technicians(n: int = DEFAULT_N_TECHNICIANS, seed: int = 42) -> list[Technician]:
    """Generate ``n`` technicians with randomized skills, location, and history."""
    # TODO: sample locations, skills, experience, completion_rate, ratings,
    #       workload, and availability from realistic distributions.
    raise NotImplementedError("Technician generation not yet implemented")


def generate_requests(n: int = 200, seed: int = 42) -> list[ServiceRequest]:
    """Generate ``n`` service requests with priority, skill, and SLA deadlines."""
    # TODO: sample locations, required_skill, priority, created_at, sla_deadline.
    raise NotImplementedError("Request generation not yet implemented")


def generate_historical_assignments(
    technicians: list[Technician],
    n: int = DEFAULT_N_ASSIGNMENTS,
    seed: int = 42,
) -> "pd.DataFrame":
    """Generate a labelled table of ``n`` historical assignments.

    Columns include the raw inputs (distance, travel time, workload, priority,
    skill match, experience, completion rate, rating, delay) plus the binary
    ``assignment_success`` label.
    """
    # TODO: simulate assignments and derive the success label from a scoring rule
    #       plus noise, returning a pandas DataFrame.
    raise NotImplementedError("Historical assignment generation not yet implemented")


def generate_dataset(
    n_technicians: int = DEFAULT_N_TECHNICIANS,
    n_assignments: int = DEFAULT_N_ASSIGNMENTS,
    seed: int = 42,
) -> "pd.DataFrame":
    """Generate the full training dataset (technicians + labelled assignments)."""
    # TODO: orchestrate the generators above and return the joined DataFrame.
    raise NotImplementedError("Dataset generation not yet implemented")
