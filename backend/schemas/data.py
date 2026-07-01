"""Synthetic-data generation schemas."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from core.constants import DEFAULT_N_ASSIGNMENTS, DEFAULT_N_TECHNICIANS


class GenerateDataRequest(BaseModel):
    """Request body for POST /generate-data."""

    n_technicians: int = Field(DEFAULT_N_TECHNICIANS, ge=1)
    n_requests: int = Field(200, ge=1)
    n_assignments: int = Field(DEFAULT_N_ASSIGNMENTS, ge=1)
    seed: int = 42


class GenerateDataResponse(BaseModel):
    """Response body for POST /generate-data."""

    n_technicians: int
    n_requests: int
    n_assignments: int
    generated_at: datetime
