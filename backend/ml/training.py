"""Training orchestration.

Ties the pipeline together: split -> fit -> evaluate -> return a fitted model and
its metrics. Hyperparameter tuning hooks live here as well.
"""

from __future__ import annotations

from typing import Optional

from ml.models import build_model
from ml.models.base_model import BaseAllocationModel
from schemas.common import ModelType
from schemas.model import ModelMetrics


def train_model(
    model_type: ModelType = ModelType.random_forest,
    test_size: float = 0.2,
    random_state: int = 42,
    hyperparameters: Optional[dict] = None,
) -> tuple[BaseAllocationModel, ModelMetrics]:
    """Train ``model_type`` on the generated dataset and return it with metrics.

    Steps: generate/load dataset -> engineer features -> preprocess -> split ->
    :meth:`BaseAllocationModel.fit` -> evaluate -> return.
    """
    # TODO: implement the full pipeline. Skeleton of the intended flow:
    #   model = build_model(model_type, **(hyperparameters or {}))
    #   X_train, X_test, y_train, y_test = split_dataset(...)
    #   model.fit(X_train, y_train)
    #   metrics = evaluate_model(model_type, y_test, model.predict(X_test),
    #                            model.predict_proba(X_test))
    #   return model, metrics
    raise NotImplementedError("Training pipeline not yet implemented")


def tune_hyperparameters(
    model_type: ModelType,
    param_grid: dict,
    random_state: int = 42,
) -> dict:
    """Return the best hyperparameters found via search (grid/random/Optuna)."""
    # TODO: implement hyperparameter search and return the best params.
    raise NotImplementedError("Hyperparameter tuning not yet implemented")
