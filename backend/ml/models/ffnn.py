"""Feed-Forward Neural Network allocation model (PyTorch)."""

from __future__ import annotations

from pathlib import Path

import numpy as np

from ml.models.base_model import BaseAllocationModel
from schemas.common import ModelType


class FFNNAllocationModel(BaseAllocationModel):
    """A simple fully-connected binary classifier built with PyTorch.

    Intended architecture: ``Linear -> ReLU -> Dropout`` blocks ending in a
    single logit with a sigmoid, trained with ``BCEWithLogitsLoss`` and Adam.
    """

    model_type = ModelType.ffnn

    def fit(self, X: np.ndarray, y: np.ndarray) -> "FFNNAllocationModel":
        # TODO: import torch / torch.nn; build the MLP, create DataLoaders,
        #       and run the training loop (BCEWithLogitsLoss + Adam).
        raise NotImplementedError("FFNN training not yet implemented")

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        # TODO: torch.no_grad(); return torch.sigmoid(self._model(tensor)).numpy()
        raise NotImplementedError("FFNN inference not yet implemented")

    def feature_importances(self) -> dict[str, float]:
        # TODO: derive via permutation importance or SHAP DeepExplainer.
        raise NotImplementedError("FFNN feature importances not yet implemented")

    def save(self, path: Path) -> None:
        # TODO: torch.save(self._model.state_dict(), path)
        raise NotImplementedError("FFNN serialization not yet implemented")

    @classmethod
    def load(cls, path: Path) -> "FFNNAllocationModel":
        # TODO: rebuild architecture then load_state_dict(torch.load(path))
        raise NotImplementedError("FFNN deserialization not yet implemented")
