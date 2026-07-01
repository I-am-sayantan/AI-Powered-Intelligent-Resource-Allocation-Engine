"""Pydantic schema contracts for the allocation engine API.

Importing from this package gives access to every request/response model.
"""

from __future__ import annotations

from schemas.allocation import (
    AlgorithmComparisonRow,
    AllocationRequest,
    AllocationResult,
    CompareRequest,
    CompareResult,
)
from schemas.assignment import Assignment, FeatureContribution
from schemas.common import AlgorithmType, GeoPoint, ModelType, RequestStatus
from schemas.data import GenerateDataRequest, GenerateDataResponse
from schemas.metrics import KpiSummary, MetricsResponse
from schemas.model import (
    ConfusionMatrix,
    FeatureImportance,
    ModelMetrics,
    PredictRequest,
    PredictResponse,
    TrainRequest,
    TrainResponse,
)
from schemas.request import ServiceRequest
from schemas.technician import Technician

__all__ = [
    "AlgorithmComparisonRow",
    "AlgorithmType",
    "AllocationRequest",
    "AllocationResult",
    "Assignment",
    "CompareRequest",
    "CompareResult",
    "ConfusionMatrix",
    "FeatureContribution",
    "FeatureImportance",
    "GenerateDataRequest",
    "GenerateDataResponse",
    "GeoPoint",
    "KpiSummary",
    "MetricsResponse",
    "ModelMetrics",
    "ModelType",
    "PredictRequest",
    "PredictResponse",
    "RequestStatus",
    "ServiceRequest",
    "TrainRequest",
    "TrainResponse",
    "Technician",
]
