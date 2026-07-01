"""Preprocessing: cleaning, encoding, scaling, and train/test split."""

from __future__ import annotations

from typing import TYPE_CHECKING

from core.constants import TARGET_NAME

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd


def clean_data(df: "pd.DataFrame") -> "pd.DataFrame":
    """Handle missing values, duplicates, and out-of-range records."""
    # TODO: drop/imputate nulls, remove duplicates, clip outliers.
    raise NotImplementedError("Data cleaning not yet implemented")


def encode_categoricals(df: "pd.DataFrame") -> "pd.DataFrame":
    """Encode categorical columns (e.g. skill) into numeric form."""
    # TODO: one-hot / ordinal encode categorical features.
    raise NotImplementedError("Categorical encoding not yet implemented")


def scale_features(X_train: "np.ndarray", X_test: "np.ndarray") -> tuple["np.ndarray", "np.ndarray"]:
    """Fit a scaler on the training split and transform both splits."""
    # TODO: from sklearn.preprocessing import StandardScaler
    raise NotImplementedError("Feature scaling not yet implemented")


def split_dataset(
    df: "pd.DataFrame",
    target: str = TARGET_NAME,
    test_size: float = 0.2,
    random_state: int = 42,
) -> tuple["np.ndarray", "np.ndarray", "np.ndarray", "np.ndarray"]:
    """Split ``df`` into ``(X_train, X_test, y_train, y_test)``."""
    # TODO: from sklearn.model_selection import train_test_split
    raise NotImplementedError("Train/test split not yet implemented")
