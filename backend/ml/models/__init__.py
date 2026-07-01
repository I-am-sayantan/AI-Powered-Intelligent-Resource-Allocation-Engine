"""Model implementations and the model registry.

``build_model`` returns an instance of the requested model type, all sharing the
:class:`~ml.models.base_model.BaseAllocationModel` interface.
"""

from __future__ import annotations

from typing import Any

from ml.models.base_model import BaseAllocationModel
from ml.models.catboost_model import CatBoostAllocationModel
from ml.models.ffnn import FFNNAllocationModel
from ml.models.lightgbm_model import LightGBMAllocationModel
from ml.models.random_forest import RandomForestAllocationModel
from ml.models.tabnet_model import TabNetAllocationModel
from ml.models.xgboost_model import XGBoostAllocationModel
from schemas.common import ModelType

#: Maps each model identifier to its implementation class.
MODEL_REGISTRY: dict[ModelType, type[BaseAllocationModel]] = {
    ModelType.random_forest: RandomForestAllocationModel,
    ModelType.xgboost: XGBoostAllocationModel,
    ModelType.lightgbm: LightGBMAllocationModel,
    ModelType.catboost: CatBoostAllocationModel,
    ModelType.ffnn: FFNNAllocationModel,
    ModelType.tabnet: TabNetAllocationModel,
}


def build_model(model_type: ModelType, **hyperparameters: Any) -> BaseAllocationModel:
    """Instantiate the model registered for ``model_type``."""
    return MODEL_REGISTRY[model_type](**hyperparameters)


__all__ = [
    "MODEL_REGISTRY",
    "BaseAllocationModel",
    "CatBoostAllocationModel",
    "FFNNAllocationModel",
    "LightGBMAllocationModel",
    "RandomForestAllocationModel",
    "TabNetAllocationModel",
    "XGBoostAllocationModel",
    "build_model",
]
