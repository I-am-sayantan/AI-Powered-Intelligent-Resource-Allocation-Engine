"""LightGBM allocation model."""

from __future__ import annotations

from pathlib import Path

import numpy as np

from ml.models.base_model import BaseAllocationModel
from schemas.common import ModelType


class LightGBMAllocationModel(BaseAllocationModel):
    """Wraps ``lightgbm.LGBMClassifier``."""

    model_type = ModelType.lightgbm

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LightGBMAllocationModel":
        # TODO: from lightgbm import LGBMClassifier
        #       self._model = LGBMClassifier(**self.hyperparameters).fit(X, y)
        raise NotImplementedError("LightGBM training not yet implemented")

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        # TODO: return self._model.predict_proba(X)[:, 1]
        raise NotImplementedError("LightGBM inference not yet implemented")

    def feature_importances(self) -> dict[str, float]:
        raise NotImplementedError("LightGBM feature importances not yet implemented")

    def save(self, path: Path) -> None:
        # TODO: import joblib; joblib.dump(self._model, path)
        raise NotImplementedError("LightGBM serialization not yet implemented")

    @classmethod
    def load(cls, path: Path) -> "LightGBMAllocationModel":
        raise NotImplementedError("LightGBM deserialization not yet implemented")
