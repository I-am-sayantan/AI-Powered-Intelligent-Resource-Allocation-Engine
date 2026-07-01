"""Metrics endpoint: executive KPIs plus ML metrics and feature importance."""

from __future__ import annotations

from fastapi import APIRouter

from api.deps import StoreDep
from schemas.metrics import MetricsResponse
from services import metrics_service

router = APIRouter(tags=["metrics"])


@router.get("/metrics", response_model=MetricsResponse)
def get_metrics(store: StoreDep) -> MetricsResponse:
    """Return executive KPIs, model metrics, and feature importance."""
    return metrics_service.get_metrics(store)
