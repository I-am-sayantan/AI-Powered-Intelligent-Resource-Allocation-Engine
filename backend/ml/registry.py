"""Model registry: serialization paths and load/save helpers."""

from __future__ import annotations

from pathlib import Path

from config import settings
from ml.models.base_model import BaseAllocationModel
from schemas.common import ModelType


def model_path(model_type: ModelType) -> Path:
    """Return the on-disk path for a serialized model of ``model_type``."""
    return settings.models_dir / f"{model_type.value}.joblib"


def save_model(model: BaseAllocationModel) -> Path:
    """Serialize ``model`` to its registry path and return that path."""
    # TODO: settings.ensure_dirs(); model.save(model_path(model.model_type))
    raise NotImplementedError("Model saving not yet implemented")


def load_model(model_type: ModelType) -> BaseAllocationModel:
    """Load a previously serialized model of ``model_type``."""
    # TODO: MODEL_REGISTRY[model_type].load(model_path(model_type))
    raise NotImplementedError("Model loading not yet implemented")
