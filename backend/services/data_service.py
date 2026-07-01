"""Data service: synthetic-data generation and entity retrieval.

Currently backed by deterministic fixtures so the API runs end-to-end. When the
real generator (``ml.data_generator``) lands, only the bodies here change -- the
signatures and response shapes stay identical.
"""

from __future__ import annotations

from datetime import datetime

from core.logging import get_logger
from fixtures.mock_data import mock_assignments, mock_requests, mock_technicians
from schemas.assignment import Assignment
from schemas.data import GenerateDataRequest, GenerateDataResponse
from schemas.request import ServiceRequest
from schemas.technician import Technician
from services.store import InMemoryStore

logger = get_logger(__name__)

# Mock data is capped for responsiveness; the real generator produces the full
# 1,000 technicians / 10,000 assignments described in the PRD.
_MAX_MOCK_TECHNICIANS = 60
_MAX_MOCK_REQUESTS = 30


def ensure_seeded(store: InMemoryStore) -> None:
    """Populate the store with a small default dataset if it is empty."""
    if not store.technicians:
        technicians = mock_technicians(12)
        requests = mock_requests(8)
        store.set_technicians(technicians)
        store.set_requests(requests)
        store.set_assignments(mock_assignments(technicians, requests))


def generate_data(request: GenerateDataRequest, store: InMemoryStore) -> GenerateDataResponse:
    """Generate mock technicians/requests/assignments and load them into the store."""
    n_technicians = min(request.n_technicians, _MAX_MOCK_TECHNICIANS)
    n_requests = min(request.n_requests, _MAX_MOCK_REQUESTS)
    technicians = mock_technicians(n_technicians, seed=request.seed)
    requests = mock_requests(n_requests, seed=request.seed + 1)
    assignments = mock_assignments(technicians, requests)
    store.set_technicians(technicians)
    store.set_requests(requests)
    store.set_assignments(assignments)
    logger.info(
        "Generated mock data: %d technicians, %d requests, %d assignments",
        len(technicians),
        len(requests),
        len(assignments),
    )
    return GenerateDataResponse(
        n_technicians=len(technicians),
        n_requests=len(requests),
        n_assignments=len(assignments),
        generated_at=datetime.now(),
    )


def list_technicians(store: InMemoryStore) -> list[Technician]:
    """Return all technicians, seeding defaults if necessary."""
    ensure_seeded(store)
    return list(store.technicians.values())


def list_requests(store: InMemoryStore) -> list[ServiceRequest]:
    """Return all service requests, seeding defaults if necessary."""
    ensure_seeded(store)
    return list(store.requests.values())


def list_assignments(store: InMemoryStore) -> list[Assignment]:
    """Return all assignments, seeding defaults if necessary."""
    ensure_seeded(store)
    return list(store.assignments.values())
