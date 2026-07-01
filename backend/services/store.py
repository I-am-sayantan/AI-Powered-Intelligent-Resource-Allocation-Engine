"""In-memory data store with optional file-based persistence.

The store is a lightweight singleton holding the current technicians, requests,
assignments, and trained-model metadata. It supports pickle snapshots so state can
be persisted between runs. Model artifacts themselves are handled by
``ml.registry`` (joblib / torch), keeping this store focused on tabular state.
"""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Optional

from core.logging import get_logger
from schemas.assignment import Assignment
from schemas.model import ModelMetrics
from schemas.request import ServiceRequest
from schemas.technician import Technician

logger = get_logger(__name__)


class InMemoryStore:
    """Holds the mutable application state for a single running backend."""

    def __init__(self) -> None:
        self.technicians: dict[str, Technician] = {}
        self.requests: dict[str, ServiceRequest] = {}
        self.assignments: dict[str, Assignment] = {}
        self.model_metrics: dict[str, ModelMetrics] = {}
        self.active_model_type: Optional[str] = None

    # --- Mutation helpers -------------------------------------------------
    def reset(self) -> None:
        """Clear all stored state."""
        self.technicians.clear()
        self.requests.clear()
        self.assignments.clear()
        self.model_metrics.clear()
        self.active_model_type = None

    def set_technicians(self, technicians: list[Technician]) -> None:
        self.technicians = {t.id: t for t in technicians}

    def set_requests(self, requests: list[ServiceRequest]) -> None:
        self.requests = {r.id: r for r in requests}

    def set_assignments(self, assignments: list[Assignment]) -> None:
        self.assignments = {a.id: a for a in assignments}

    def record_model_metrics(self, metrics: ModelMetrics) -> None:
        key = metrics.model_type.value
        self.model_metrics[key] = metrics
        self.active_model_type = key

    # --- Persistence ------------------------------------------------------
    def save_snapshot(self, path: Path) -> None:
        """Persist tabular state to a pickle file as plain dicts."""
        payload = {
            "technicians": [t.model_dump(mode="json") for t in self.technicians.values()],
            "requests": [r.model_dump(mode="json") for r in self.requests.values()],
            "assignments": [a.model_dump(mode="json") for a in self.assignments.values()],
            "model_metrics": {k: v.model_dump(mode="json") for k, v in self.model_metrics.items()},
            "active_model_type": self.active_model_type,
        }
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as fh:
            pickle.dump(payload, fh)
        logger.info("Saved store snapshot to %s", path)

    def load_snapshot(self, path: Path) -> None:
        """Restore tabular state previously written by :meth:`save_snapshot`."""
        with path.open("rb") as fh:
            payload = pickle.load(fh)
        self.set_technicians([Technician.model_validate(t) for t in payload["technicians"]])
        self.set_requests([ServiceRequest.model_validate(r) for r in payload["requests"]])
        self.set_assignments([Assignment.model_validate(a) for a in payload["assignments"]])
        self.model_metrics = {
            k: ModelMetrics.model_validate(v) for k, v in payload["model_metrics"].items()
        }
        self.active_model_type = payload.get("active_model_type")
        logger.info("Loaded store snapshot from %s", path)


# Module-level singleton and accessor (used as a FastAPI dependency).
_store = InMemoryStore()


def get_store() -> InMemoryStore:
    """Return the process-wide :class:`InMemoryStore` singleton."""
    return _store
