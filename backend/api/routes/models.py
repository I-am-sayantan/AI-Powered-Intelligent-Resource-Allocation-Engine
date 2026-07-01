"""Model endpoints: training and prediction."""

from __future__ import annotations

from fastapi import APIRouter

from api.deps import StoreDep
from schemas.model import PredictRequest, PredictResponse, TrainRequest, TrainResponse
from services import model_service

router = APIRouter(tags=["models"])


@router.post("/train-model", response_model=TrainResponse)
def train_model(request: TrainRequest, store: StoreDep) -> TrainResponse:
    """Train a model and return its evaluation metrics."""
    return model_service.train_model(request, store)


@router.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest, store: StoreDep) -> PredictResponse:
    """Predict assignment-success probability with an explanation."""
    return model_service.predict(request, store)
