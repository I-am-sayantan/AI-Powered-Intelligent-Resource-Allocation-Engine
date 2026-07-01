"""CatBoost allocation model."""

from __future__ import annotations

from pathlib import Path

import numpy as np

from ml.models.base_model import BaseAllocationModel
from schemas.common import ModelType


class CatBoostAllocationModel(BaseAllocationModel):
    """Wraps ``catboost.CatBoostClassifier``."""

    model_type = ModelType.catboost

    def fit(self, X: np.ndarray, y: np.ndarray) -> "CatBoostAllocationModel":
        # TODO: from catboost import CatBoostClassifier
        #       self._model = CatBoostClassifier(**self.hyperparameters).fit(X, y)
        raise NotImplementedError("CatBoost training not yet implemented")

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        # TODO: return self._model.predict_proba(X)[:, 1]
        raise NotImplementedError("CatBoost inference not yet implemented")

    def feature_importances(self) -> dict[str, float]:
        raise NotImplementedError("CatBoost feature importances not yet implemented")

    def save(self, path: Path) -> None:
        # TODO: self._model.save_model(path)
        raise NotImplementedError("CatBoost serialization not yet implemented")

    @classmethod
    def load(cls, path: Path) -> "CatBoostAllocationModel":
        raise NotImplementedError("CatBoost deserialization not yet implemented")
