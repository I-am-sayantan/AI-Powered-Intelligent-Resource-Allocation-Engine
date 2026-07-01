"""Deterministic mock data.

These builders return fully schema-valid objects so every stub endpoint can
respond with realistic data and the frontend runs end-to-end. Coordinates are
clustered around San Francisco so the Leaflet map renders nicely.

When the real data generator and models land, endpoints will switch from these
fixtures to live services -- the response *shapes* stay identical.
"""

from __future__ import annotations

import math
import random
from datetime import datetime, timedelta

from core.constants import AVG_SPEED_KMH, FEATURE_NAMES, SKILLS
from schemas.allocation import AlgorithmComparisonRow, AllocationResult, CompareResult
from schemas.assignment import Assignment, FeatureContribution
from schemas.common import AlgorithmType, GeoPoint, ModelType, RequestStatus
from schemas.metrics import KpiSummary, MetricsResponse
from schemas.model import (
    ConfusionMatrix,
    FeatureImportance,
    ModelMetrics,
    PredictResponse,
    TrainResponse,
)
from schemas.request import ServiceRequest
from schemas.technician import Technician

_CENTER_LAT = 37.7749
_CENTER_LON = -122.4194
_SEED = 42
_NOW = datetime(2026, 7, 1, 9, 0, 0)

_FIRST_NAMES = ["Ava", "Liam", "Noah", "Mia", "Ethan", "Zoe", "Kai", "Luca", "Nina", "Omar"]
_LAST_NAMES = ["Reyes", "Kim", "Patel", "Nguyen", "Silva", "Cohen", "Diaz", "Okafor", "Ito", "Brown"]
_CUSTOMERS = ["Acme Corp", "Globex", "Initech", "Umbrella", "Soylent", "Hooli", "Stark Ind.", "Wayne Ent."]


def _rng(seed: int = _SEED) -> random.Random:
    return random.Random(seed)


def _jitter(rng: random.Random, center: float, spread: float = 0.08) -> float:
    return round(center + rng.uniform(-spread, spread), 6)


def _haversine_km(a: GeoPoint, b: GeoPoint) -> float:
    radius = 6371.0
    d_lat = math.radians(b.lat - a.lat)
    d_lon = math.radians(b.lon - a.lon)
    lat1, lat2 = math.radians(a.lat), math.radians(b.lat)
    h = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2) ** 2
    return 2 * radius * math.asin(math.sqrt(h))


def mock_technicians(n: int = 8, seed: int = _SEED) -> list[Technician]:
    """Return ``n`` deterministic technicians clustered around the city center."""
    rng = _rng(seed)
    technicians: list[Technician] = []
    for i in range(n):
        max_jobs = rng.randint(5, 10)
        workload = rng.randint(0, max_jobs)
        technicians.append(
            Technician(
                id=f"tech-{i + 1:03d}",
                name=f"{rng.choice(_FIRST_NAMES)} {rng.choice(_LAST_NAMES)}",
                location=GeoPoint(lat=_jitter(rng, _CENTER_LAT), lon=_jitter(rng, _CENTER_LON)),
                skills=rng.sample(SKILLS, rng.randint(1, 3)),
                experience_years=round(rng.uniform(1, 20), 1),
                completion_rate=round(rng.uniform(0.70, 0.99), 3),
                customer_rating=round(rng.uniform(3.5, 5.0), 2),
                current_workload=workload,
                max_daily_jobs=max_jobs,
                available=rng.random() > 0.2,
                utilization=round(workload / max_jobs, 3),
            )
        )
    return technicians


def mock_requests(n: int = 6, seed: int = _SEED + 1) -> list[ServiceRequest]:
    """Return ``n`` deterministic pending service requests."""
    rng = _rng(seed)
    requests: list[ServiceRequest] = []
    for i in range(n):
        created = _NOW - timedelta(minutes=rng.randint(0, 120))
        requests.append(
            ServiceRequest(
                id=f"req-{i + 1:03d}",
                customer_name=rng.choice(_CUSTOMERS),
                location=GeoPoint(lat=_jitter(rng, _CENTER_LAT), lon=_jitter(rng, _CENTER_LON)),
                required_skill=rng.choice(SKILLS),
                priority=rng.randint(1, 5),
                created_at=created,
                sla_deadline=created + timedelta(hours=rng.randint(2, 8)),
                estimated_duration_min=rng.choice([30, 45, 60, 90, 120]),
                status=RequestStatus.pending,
            )
        )
    return requests


def mock_explanation() -> list[FeatureContribution]:
    """Return the PRD example explanation breakdown."""
    weights = [
        ("distance", 0.34),
        ("experience", 0.25),
        ("availability", 0.21),
        ("priority", 0.12),
        ("workload", 0.08),
    ]
    return [FeatureContribution(feature=f, contribution=c) for f, c in weights]


def mock_assignments(
    technicians: list[Technician] | None = None,
    requests: list[ServiceRequest] | None = None,
    algorithm: AlgorithmType = AlgorithmType.greedy,
    seed: int = _SEED + 2,
) -> list[Assignment]:
    """Pair each request with a technician round-robin and compute travel metrics."""
    technicians = technicians or mock_technicians()
    requests = requests or mock_requests()
    rng = _rng(seed)
    assignments: list[Assignment] = []
    for i, request in enumerate(requests):
        technician = technicians[i % len(technicians)]
        distance = _haversine_km(technician.location, request.location)
        travel = distance / AVG_SPEED_KMH * 60
        assignments.append(
            Assignment(
                id=f"asn-{i + 1:03d}",
                technician_id=technician.id,
                request_id=request.id,
                distance_km=round(distance, 2),
                travel_time_min=round(travel, 1),
                predicted_success=round(rng.uniform(0.80, 0.98), 3),
                algorithm=algorithm,
                score=round(rng.uniform(0.75, 0.97), 3),
                assigned_at=_NOW,
                explanation=mock_explanation(),
            )
        )
    return assignments


def mock_kpis(
    technicians: list[Technician],
    requests: list[ServiceRequest],
    assignments: list[Assignment],
) -> KpiSummary:
    """Aggregate KPI cards from the provided entities."""
    n_t, n_r, n_a = len(technicians), len(requests), len(assignments)
    avg_util = sum(t.utilization for t in technicians) / n_t if n_t else 0.0
    avg_travel = sum(a.distance_km for a in assignments) / n_a if n_a else 0.0
    avg_success = sum(a.predicted_success for a in assignments) / n_a if n_a else 0.0
    avg_rating = sum(t.customer_rating for t in technicians) / n_t if n_t else 0.0
    return KpiSummary(
        total_technicians=n_t,
        total_requests=n_r,
        total_assignments=n_a,
        avg_utilization=round(avg_util, 3),
        avg_travel_km=round(avg_travel, 2),
        sla_met_pct=92.5,
        avg_predicted_success=round(avg_success, 3),
        customer_satisfaction=round(avg_rating, 2),
    )


def mock_model_metrics(model_type: ModelType = ModelType.random_forest) -> ModelMetrics:
    """Return plausible classification metrics for a given model type."""
    presets: dict[ModelType, tuple[float, float, float, float, float]] = {
        ModelType.random_forest: (0.890, 0.880, 0.900, 0.890, 0.940),
        ModelType.xgboost: (0.910, 0.900, 0.920, 0.910, 0.960),
        ModelType.lightgbm: (0.900, 0.890, 0.910, 0.900, 0.950),
        ModelType.catboost: (0.905, 0.895, 0.915, 0.905, 0.955),
        ModelType.ffnn: (0.880, 0.870, 0.890, 0.880, 0.930),
        ModelType.tabnet: (0.885, 0.875, 0.895, 0.885, 0.935),
    }
    accuracy, precision, recall, f1, roc_auc = presets[model_type]
    return ModelMetrics(
        model_type=model_type,
        accuracy=accuracy,
        precision=precision,
        recall=recall,
        f1=f1,
        roc_auc=roc_auc,
        confusion_matrix=ConfusionMatrix(
            true_negative=890,
            false_positive=110,
            false_negative=90,
            true_positive=910,
        ),
    )


def mock_feature_importance() -> list[FeatureImportance]:
    """Return global feature importances over the 13 engineered features."""
    weights = [0.22, 0.16, 0.13, 0.11, 0.09, 0.08, 0.07, 0.05, 0.04, 0.02, 0.015, 0.01, 0.005]
    return [
        FeatureImportance(feature=f, importance=round(w, 3))
        for f, w in zip(FEATURE_NAMES, weights)
    ]


def mock_metrics_response(model_type: ModelType = ModelType.random_forest) -> MetricsResponse:
    """Return the full metrics payload for GET /metrics."""
    technicians = mock_technicians()
    requests = mock_requests()
    assignments = mock_assignments(technicians, requests)
    return MetricsResponse(
        kpis=mock_kpis(technicians, requests, assignments),
        model_metrics=mock_model_metrics(model_type),
        feature_importance=mock_feature_importance(),
    )


def mock_predict_response(seed: int = _SEED) -> PredictResponse:
    """Return a mock success prediction with an explanation."""
    rng = _rng(seed)
    return PredictResponse(
        predicted_success=round(rng.uniform(0.85, 0.97), 3),
        explanation=mock_explanation(),
    )


def mock_train_response(
    model_type: ModelType = ModelType.random_forest,
    n_samples: int = 10_000,
) -> TrainResponse:
    """Return a mock training result."""
    return TrainResponse(
        model_type=model_type,
        n_samples=n_samples,
        metrics=mock_model_metrics(model_type),
        trained_at=datetime.now(),
    )


_ALGORITHM_RUNTIME_MS: dict[AlgorithmType, float] = {
    AlgorithmType.greedy: 2.1,
    AlgorithmType.hungarian: 8.4,
    AlgorithmType.ml: 15.2,
    AlgorithmType.dl: 22.7,
}


def mock_allocation_result(algorithm: AlgorithmType = AlgorithmType.greedy) -> AllocationResult:
    """Return a mock allocation result for a single algorithm."""
    technicians = mock_technicians()
    requests = mock_requests()
    assignments = mock_assignments(technicians, requests, algorithm)
    return AllocationResult(
        algorithm=algorithm,
        assignments=assignments,
        total_score=round(sum(a.score for a in assignments), 3),
        unassigned_request_ids=[],
        kpis=mock_kpis(technicians, requests, assignments),
        runtime_ms=_ALGORITHM_RUNTIME_MS[algorithm],
    )


def mock_compare_result() -> CompareResult:
    """Return a mock comparison across all allocation algorithms."""
    technicians = mock_technicians()
    requests = mock_requests()
    # (score multiplier, sla_met_pct, runtime_ms) tuned so ML wins overall.
    presets: dict[AlgorithmType, tuple[float, float, float]] = {
        AlgorithmType.greedy: (0.90, 92.0, 2.1),
        AlgorithmType.hungarian: (1.00, 95.5, 8.4),
        AlgorithmType.ml: (1.05, 96.8, 15.2),
        AlgorithmType.dl: (1.02, 96.0, 22.7),
    }
    rows: list[AlgorithmComparisonRow] = []
    for algorithm, (factor, sla, runtime) in presets.items():
        assignments = mock_assignments(technicians, requests, algorithm)
        kpis = mock_kpis(technicians, requests, assignments)
        rows.append(
            AlgorithmComparisonRow(
                algorithm=algorithm,
                total_score=round(sum(a.score for a in assignments) * factor, 3),
                assigned_count=len(assignments),
                avg_travel_km=kpis.avg_travel_km,
                avg_utilization=kpis.avg_utilization,
                sla_met_pct=sla,
                runtime_ms=runtime,
            )
        )
    best = max(rows, key=lambda r: r.total_score).algorithm
    return CompareResult(rows=rows, best_algorithm=best)
