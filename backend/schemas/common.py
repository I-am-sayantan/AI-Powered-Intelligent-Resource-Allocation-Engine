"""Shared enums and value objects used across schemas."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class AlgorithmType(str, Enum):
    """Allocation algorithms supported by the engine."""

    greedy = "greedy"
    hungarian = "hungarian"
    ml = "ml"
    dl = "dl"


class ModelType(str, Enum):
    """Machine-learning / deep-learning models available for training."""

    random_forest = "random_forest"
    xgboost = "xgboost"
    lightgbm = "lightgbm"
    catboost = "catboost"
    ffnn = "ffnn"
    tabnet = "tabnet"


class RequestStatus(str, Enum):
    """Lifecycle status of a service request."""

    pending = "pending"
    assigned = "assigned"
    completed = "completed"
    cancelled = "cancelled"


class GeoPoint(BaseModel):
    """A latitude/longitude coordinate."""

    lat: float = Field(..., ge=-90, le=90, description="Latitude in degrees")
    lon: float = Field(..., ge=-180, le=180, description="Longitude in degrees")
