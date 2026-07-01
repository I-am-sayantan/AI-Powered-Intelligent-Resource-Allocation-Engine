"""Technician (field-service engineer) schema."""

from __future__ import annotations

from pydantic import BaseModel, Field

from schemas.common import GeoPoint


class Technician(BaseModel):
    """A field-service engineer available for assignment."""

    id: str
    name: str
    location: GeoPoint
    skills: list[str] = Field(default_factory=list)
    experience_years: float = Field(..., ge=0)
    completion_rate: float = Field(..., ge=0, le=1, description="Historical completion rate")
    customer_rating: float = Field(..., ge=0, le=5)
    current_workload: int = Field(..., ge=0, description="Jobs already assigned today")
    max_daily_jobs: int = Field(..., ge=1)
    available: bool = True
    utilization: float = Field(..., ge=0, le=1, description="current_workload / max_daily_jobs")
