"""Feature engineering.

Transforms raw assignment records into the 13 engineered features consumed by
the models. The canonical feature list lives in :data:`core.constants.FEATURE_NAMES`.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from core.constants import FEATURE_NAMES

if TYPE_CHECKING:
    import pandas as pd


def build_features(df: "pd.DataFrame") -> "pd.DataFrame":
    """Return a DataFrame containing exactly the columns in ``FEATURE_NAMES``.

    Derives: distance, normalized_distance, travel_time, workload_ratio,
    technician_utilization, historical_completion_rate, experience_score,
    skill_score, priority_weight, sla_remaining_time, and the rush_hour /
    weekend / holiday flags.
    """
    # TODO: compute each engineered feature from the raw columns of ``df``.
    raise NotImplementedError(
        "Feature engineering not yet implemented; target features: "
        + ", ".join(FEATURE_NAMES)
    )
