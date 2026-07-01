"""Customer service request schema."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from schemas.common import GeoPoint, RequestStatus


class ServiceRequest(BaseModel):
    """A customer service request awaiting technician assignment."""

    id: str
    customer_name: str
    location: GeoPoint
    required_skill: str
    priority: int = Field(..., ge=1, le=5, description="1 = lowest, 5 = highest")
    created_at: datetime
    sla_deadline: datetime
    estimated_duration_min: int = Field(..., ge=0)
    status: RequestStatus = RequestStatus.pending
