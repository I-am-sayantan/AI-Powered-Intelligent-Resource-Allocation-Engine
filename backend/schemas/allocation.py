"""Allocation and algorithm-comparison schemas."""

from __future__ import annotations

from pydantic import BaseModel, Field

from schemas.assignment import Assignment
from schemas.common import AlgorithmType
from schemas.metrics import KpiSummary


class AllocationRequest(BaseModel):
    """Request body for POST /allocate."""

    algorithm: AlgorithmType = AlgorithmType.greedy
    respect_hard_constraints: bool = True


class AllocationResult(BaseModel):
    """Result of running a single allocation algorithm."""

    algorithm: AlgorithmType
    assignments: list[Assignment] = Field(default_factory=list)
    total_score: float
    unassigned_request_ids: list[str] = Field(default_factory=list)
    kpis: KpiSummary
    runtime_ms: float = Field(..., ge=0)


class CompareRequest(BaseModel):
    """Request body for POST /compare."""

    algorithms: list[AlgorithmType] = Field(default_factory=lambda: list(AlgorithmType))


class AlgorithmComparisonRow(BaseModel):
    """One row in the algorithm-comparison table."""

    algorithm: AlgorithmType
    total_score: float
    assigned_count: int = Field(..., ge=0)
    avg_travel_km: float = Field(..., ge=0)
    avg_utilization: float = Field(..., ge=0, le=1)
    sla_met_pct: float = Field(..., ge=0, le=100)
    runtime_ms: float = Field(..., ge=0)


class CompareResult(BaseModel):
    """Response body for POST /compare."""

    rows: list[AlgorithmComparisonRow] = Field(default_factory=list)
    best_algorithm: AlgorithmType
