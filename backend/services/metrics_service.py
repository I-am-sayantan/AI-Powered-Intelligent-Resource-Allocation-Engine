"""Metrics service: aggregates executive KPIs and model metrics."""

from __future__ import annotations

from fixtures.mock_data import mock_feature_importance, mock_kpis, mock_model_metrics
from schemas.metrics import MetricsResponse
from services.data_service import ensure_seeded
from services.store import InMemoryStore


def get_metrics(store: InMemoryStore) -> MetricsResponse:
    """Return KPIs from the current store plus the active model's metrics."""
    ensure_seeded(store)
    technicians = list(store.technicians.values())
    requests = list(store.requests.values())
    assignments = list(store.assignments.values())

    kpis = mock_kpis(technicians, requests, assignments)
    if store.active_model_type and store.active_model_type in store.model_metrics:
        model_metrics = store.model_metrics[store.active_model_type]
    else:
        model_metrics = mock_model_metrics()

    return MetricsResponse(
        kpis=kpis,
        model_metrics=model_metrics,
        feature_importance=mock_feature_importance(),
    )
