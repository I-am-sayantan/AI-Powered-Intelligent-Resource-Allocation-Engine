"""Model evaluation metrics."""

from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.common import ModelType
from schemas.model import ConfusionMatrix, ModelMetrics

if TYPE_CHECKING:
    import numpy as np


def compute_confusion_matrix(y_true: "np.ndarray", y_pred: "np.ndarray") -> ConfusionMatrix:
    """Compute the binary confusion matrix counts."""
    # TODO: from sklearn.metrics import confusion_matrix
    raise NotImplementedError("Confusion matrix not yet implemented")


def evaluate_model(
    model_type: ModelType,
    y_true: "np.ndarray",
    y_pred: "np.ndarray",
    y_proba: "np.ndarray",
) -> ModelMetrics:
    """Compute accuracy, precision, recall, F1, ROC-AUC, and confusion matrix."""
    # TODO: use sklearn.metrics (accuracy_score, precision_score, recall_score,
    #       f1_score, roc_auc_score) plus compute_confusion_matrix.
    raise NotImplementedError("Model evaluation not yet implemented")
