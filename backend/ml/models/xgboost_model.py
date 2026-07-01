"""XGBoost allocation model."""

from __future__ import annotations

from pathlib import Path

import numpy as np

from ml.models.base_model import BaseAllocationModel
from schemas.common import ModelType


class XGBoostAllocationModel(BaseAllocationModel):
    """Wraps ``xgboost.XGBClassifier``."""

    model_type = ModelType.xgboost

    def fit(self, X: np.ndarray, y: np.ndarray) -> "XGBoostAllocationModel":
        # TODO: from xgboost import XGBClassifier
        #       self._model = XGBClassifier(**self.hyperparameters).fit(X, y)
        raise NotImplementedError("XGBoost training not yet implemented")

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        # TODO: return self._model.predict_proba(X)[:, 1]
        raise NotImplementedError("XGBoost inference not yet implemented")

    def feature_importances(self) -> dict[str, float]:
        # TODO: zip(FEATURE_NAMES, self._model.feature_importances_)
        raise NotImplementedError("XGBoost feature importances not yet implemented")

    def save(self, path: Path) -> None:
        # TODO: self._model.save_model(path)  # or joblib.dump
        raise NotImplementedError("XGBoost serialization not yet implemented")

    @classmethod
    def load(cls, path: Path) -> "XGBoostAllocationModel":
        raise NotImplementedError("XGBoost deserialization not yet implemented")
