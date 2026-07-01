"""Executive KPI and aggregate metrics schemas."""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from schemas.model import FeatureImportance, ModelMetrics


class KpiSummary(BaseModel):
    """Executive KPI cards shown on the dashboard."""

    total_technicians: int = Field(..., ge=0)
    total_requests: int = Field(..., ge=0)
    total_assignments: int = Field(..., ge=0)
    avg_utilization: float = Field(..., ge=0, le=1)
    avg_travel_km: float = Field(..., ge=0)
    sla_met_pct: float = Field(..., ge=0, le=100)
    avg_predicted_success: float = Field(..., ge=0, le=1)
    customer_satisfaction: float = Field(..., ge=0, le=5)


class MetricsResponse(BaseModel):
    """Response body for GET /metrics."""

    model_config = ConfigDict(protected_namespaces=())

    kpis: KpiSummary
    model_metrics: Optional[ModelMetrics] = None
    feature_importance: list[FeatureImportance] = Field(default_factory=list)
