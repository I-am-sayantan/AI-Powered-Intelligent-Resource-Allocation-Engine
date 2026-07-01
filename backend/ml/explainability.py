"""Explainable AI.

Produces per-assignment explanations and global feature importances using SHAP
where available, falling back to the model's native ``feature_importances``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.assignment import FeatureContribution
from schemas.model import FeatureImportance

if TYPE_CHECKING:
    import numpy as np

    from ml.models.base_model import BaseAllocationModel


def explain_assignment(
    model: "BaseAllocationModel",
    features: "np.ndarray",
) -> list[FeatureContribution]:
    """Return the per-feature contributions for a single assignment.

    Preferred: ``shap.Explainer(model)`` local values. Fallback: normalized
    global ``model.feature_importances()``.
    """
    # TODO: compute SHAP values for the single row and map them to
    #       FeatureContribution items (feature, signed contribution).
    raise NotImplementedError("Per-assignment explanation not yet implemented")


def global_feature_importance(model: "BaseAllocationModel") -> list[FeatureImportance]:
    """Return global feature importances as a sorted list."""
    # TODO: read model.feature_importances() and sort descending.
    raise NotImplementedError("Global feature importance not yet implemented")
