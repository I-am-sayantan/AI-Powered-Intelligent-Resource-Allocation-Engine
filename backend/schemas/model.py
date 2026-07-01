"""Model training, evaluation, and prediction schemas."""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from schemas.assignment import FeatureContribution
from schemas.common import ModelType


class ConfusionMatrix(BaseModel):
    """Binary confusion matrix counts."""

    true_negative: int = Field(..., ge=0)
    false_positive: int = Field(..., ge=0)
    false_negative: int = Field(..., ge=0)
    true_positive: int = Field(..., ge=0)


class ModelMetrics(BaseModel):
    """Classification metrics for a trained model."""

    model_config = ConfigDict(protected_namespaces=())

    model_type: ModelType
    accuracy: float = Field(..., ge=0, le=1)
    precision: float = Field(..., ge=0, le=1)
    recall: float = Field(..., ge=0, le=1)
    f1: float = Field(..., ge=0, le=1)
    roc_auc: float = Field(..., ge=0, le=1)
    confusion_matrix: ConfusionMatrix


class FeatureImportance(BaseModel):
    """Global importance of a single feature."""

    feature: str
    importance: float = Field(..., ge=0)


class TrainRequest(BaseModel):
    """Request body for POST /train-model."""

    model_config = ConfigDict(protected_namespaces=())

    model_type: ModelType = ModelType.random_forest
    test_size: float = Field(0.2, gt=0, lt=1)
    random_state: int = 42
    hyperparameters: dict = Field(default_factory=dict)


class TrainResponse(BaseModel):
    """Response body for POST /train-model."""

    model_config = ConfigDict(protected_namespaces=())

    model_type: ModelType
    n_samples: int
    metrics: ModelMetrics
    trained_at: datetime


class PredictRequest(BaseModel):
    """Request body for POST /predict.

    Provide either an explicit technician/request pair or a raw feature vector.
    """

    technician_id: Optional[str] = None
    request_id: Optional[str] = None
    features: dict[str, float] = Field(default_factory=dict)


class PredictResponse(BaseModel):
    """Response body for POST /predict."""

    predicted_success: float = Field(..., ge=0, le=1)
    explanation: list[FeatureContribution] = Field(default_factory=list)
