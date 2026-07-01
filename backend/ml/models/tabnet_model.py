"""TabNet allocation model (pytorch-tabnet)."""

from __future__ import annotations

from pathlib import Path

import numpy as np

from ml.models.base_model import BaseAllocationModel
from schemas.common import ModelType


class TabNetAllocationModel(BaseAllocationModel):
    """Wraps ``pytorch_tabnet.tab_model.TabNetClassifier``."""

    model_type = ModelType.tabnet

    def fit(self, X: np.ndarray, y: np.ndarray) -> "TabNetAllocationModel":
        # TODO: from pytorch_tabnet.tab_model import TabNetClassifier
        #       self._model = TabNetClassifier(**self.hyperparameters)
        #       self._model.fit(X, y, ...)
        raise NotImplementedError("TabNet training not yet implemented")

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        # TODO: return self._model.predict_proba(X)[:, 1]
        raise NotImplementedError("TabNet inference not yet implemented")

    def feature_importances(self) -> dict[str, float]:
        # TODO: zip(FEATURE_NAMES, self._model.feature_importances_)
        raise NotImplementedError("TabNet feature importances not yet implemented")

    def save(self, path: Path) -> None:
        # TODO: self._model.save_model(str(path))
        raise NotImplementedError("TabNet serialization not yet implemented")

    @classmethod
    def load(cls, path: Path) -> "TabNetAllocationModel":
        raise NotImplementedError("TabNet deserialization not yet implemented")
