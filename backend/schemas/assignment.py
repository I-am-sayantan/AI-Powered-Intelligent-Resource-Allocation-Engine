"""Assignment schema linking a technician to a service request."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from schemas.common import AlgorithmType


class FeatureContribution(BaseModel):
    """A single feature's contribution to an assignment score (for XAI panels)."""

    feature: str
    contribution: float = Field(..., description="Signed contribution / weight")


class Assignment(BaseModel):
    """A technician-to-request assignment produced by an allocation algorithm."""

    id: str
    technician_id: str
    request_id: str
    distance_km: float = Field(..., ge=0)
    travel_time_min: float = Field(..., ge=0)
    predicted_success: float = Field(..., ge=0, le=1)
    algorithm: AlgorithmType
    score: float = Field(..., description="Objective/quality score for this assignment")
    assigned_at: datetime
    explanation: list[FeatureContribution] = Field(default_factory=list)
