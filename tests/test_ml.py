"""Tests for the ML model registry and pipeline stubs."""

from __future__ import annotations

import numpy as np
import pytest

from ml import data_generator, feature_engineering, preprocessing, training
from ml.models import MODEL_REGISTRY, build_model
from ml.models.base_model import BaseAllocationModel
from schemas.common import ModelType


def test_model_registry_covers_all_model_types() -> None:
    assert set(MODEL_REGISTRY) == set(ModelType)


@pytest.mark.parametrize("model_type", list(ModelType))
def test_build_model_returns_correct_type(model_type: ModelType) -> None:
    model = build_model(model_type)
    assert isinstance(model, BaseAllocationModel)
    assert model.model_type == model_type


@pytest.mark.parametrize("model_type", list(ModelType))
def test_model_fit_is_stubbed(model_type: ModelType) -> None:
    model = build_model(model_type)
    with pytest.raises(NotImplementedError):
        model.fit(np.zeros((2, 3)), np.zeros(2))


def test_pipeline_stubs_raise_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        data_generator.generate_dataset()
    with pytest.raises(NotImplementedError):
        feature_engineering.build_features(None)  # type: ignore[arg-type]
    with pytest.raises(NotImplementedError):
        preprocessing.clean_data(None)  # type: ignore[arg-type]
    with pytest.raises(NotImplementedError):
        training.train_model()
