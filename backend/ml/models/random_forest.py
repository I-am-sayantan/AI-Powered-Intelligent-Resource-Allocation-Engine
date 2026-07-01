"""Random Forest allocation model (scikit-learn)."""

from __future__ import annotations

from pathlib import Path

import numpy as np

from ml.models.base_model import BaseAllocationModel
from schemas.common import ModelType


class RandomForestAllocationModel(BaseAllocationModel):
    """Wraps ``sklearn.ensemble.RandomForestClassifier``."""

    model_type = ModelType.random_forest

    def fit(self, X: np.ndarray, y: np.ndarray) -> "RandomForestAllocationModel":
        # TODO: from sklearn.ensemble import RandomForestClassifier
        #       self._model = RandomForestClassifier(**self.hyperparameters).fit(X, y)
        raise NotImplementedError("RandomForest training not yet implemented")

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        # TODO: return self._model.predict_proba(X)[:, 1]
        raise NotImplementedError("RandomForest inference not yet implemented")

    def feature_importances(self) -> dict[str, float]:
        # TODO: zip(FEATURE_NAMES, self._model.feature_importances_)
        raise NotImplementedError("RandomForest feature importances not yet implemented")

    def save(self, path: Path) -> None:
        # TODO: import joblib; joblib.dump(self._model, path)
        raise NotImplementedError("RandomForest serialization not yet implemented")

    @classmethod
    def load(cls, path: Path) -> "RandomForestAllocationModel":
        # TODO: instance = cls(); instance._model = joblib.load(path); return instance
        raise NotImplementedError("RandomForest deserialization not yet implemented")
