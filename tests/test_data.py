"""Tests for the deterministic mock-data fixtures."""

from __future__ import annotations

from fixtures.mock_data import (
    mock_assignments,
    mock_compare_result,
    mock_feature_importance,
    mock_metrics_response,
    mock_requests,
    mock_technicians,
)
from schemas.common import AlgorithmType


def test_mock_technicians_count_and_ranges() -> None:
    technicians = mock_technicians(10)
    assert len(technicians) == 10
    for tech in technicians:
        assert 0.0 <= tech.utilization <= 1.0
        assert 0.0 <= tech.completion_rate <= 1.0
        assert 0.0 <= tech.customer_rating <= 5.0
        assert tech.skills


def test_mock_requests_count_and_priority() -> None:
    requests = mock_requests(6)
    assert len(requests) == 6
    for req in requests:
        assert 1 <= req.priority <= 5
        assert req.sla_deadline >= req.created_at


def test_mock_assignments_are_valid() -> None:
    assignments = mock_assignments()
    assert assignments
    for assignment in assignments:
        assert assignment.distance_km >= 0
        assert 0.0 <= assignment.predicted_success <= 1.0


def test_fixtures_are_deterministic() -> None:
    first = mock_technicians(5)
    second = mock_technicians(5)
    assert [t.id for t in first] == [t.id for t in second]
    assert [t.name for t in first] == [t.name for t in second]


def test_compare_covers_all_algorithms() -> None:
    result = mock_compare_result()
    assert {row.algorithm for row in result.rows} == set(AlgorithmType)
    assert result.best_algorithm in set(AlgorithmType)


def test_metrics_has_thirteen_features() -> None:
    metrics = mock_metrics_response()
    assert len(metrics.feature_importance) == 13
    assert len(mock_feature_importance()) == 13
