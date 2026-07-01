"""Common interface for all allocation success-prediction models."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import numpy as np

from schemas.common import ModelType


class BaseAllocationModel(ABC):
    """Uniform ``fit`` / ``predict`` / ``save`` interface for every model.

    Concrete subclasses wrap a specific library (scikit-learn, XGBoost, LightGBM,
    CatBoost, PyTorch, TabNet) but expose the same surface so training, inference,
    and serialization code stays model-agnostic.
    """

    #: The model identifier; set by each concrete subclass.
    model_type: ModelType

    def __init__(self, **hyperparameters: Any) -> None:
        self.hyperparameters = hyperparameters
        self._model: Any = None

    @abstractmethod
    def fit(self, X: np.ndarray, y: np.ndarray) -> "BaseAllocationModel":
        """Train the model on features ``X`` and binary labels ``y``."""
        raise NotImplementedError

    @abstractmethod
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Return the positive-class (assignment-success) probabilities."""
        raise NotImplementedError

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        """Return binary predictions by thresholding :meth:`predict_proba`."""
        return (self.predict_proba(X) >= threshold).astype(int)

    @abstractmethod
    def feature_importances(self) -> dict[str, float]:
        """Return a mapping of feature name to global importance."""
        raise NotImplementedError

    @abstractmethod
    def save(self, path: Path) -> None:
        """Persist the fitted model to ``path``."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def load(cls, path: Path) -> "BaseAllocationModel":
        """Load a previously saved model from ``path``."""
        raise NotImplementedError
