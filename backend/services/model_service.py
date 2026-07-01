"""Model service: training and prediction orchestration.

Backed by fixtures for now; real training/inference will call ``ml.training`` and
``ml.registry`` while keeping these signatures.
"""

from __future__ import annotations

from core.constants import DEFAULT_N_ASSIGNMENTS
from core.logging import get_logger
from fixtures.mock_data import mock_predict_response, mock_train_response
from schemas.model import PredictRequest, PredictResponse, TrainRequest, TrainResponse
from services.store import InMemoryStore

logger = get_logger(__name__)


def train_model(request: TrainRequest, store: InMemoryStore) -> TrainResponse:
    """Train (mock) the requested model and record its metrics in the store."""
    response = mock_train_response(request.model_type, n_samples=DEFAULT_N_ASSIGNMENTS)
    store.record_model_metrics(response.metrics)
    logger.info("Trained mock model: %s", request.model_type.value)
    return response


def predict(request: PredictRequest, store: InMemoryStore) -> PredictResponse:
    """Return a (mock) assignment-success prediction with an explanation."""
    # TODO: load the active model via ml.registry, engineer features from the
    #       technician/request pair, and return real predict_proba + SHAP.
    return mock_predict_response()
