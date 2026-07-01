"""End-to-end API tests: every endpoint responds 200 with a valid shape."""

from __future__ import annotations

from fastapi.testclient import TestClient


def test_health(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_generate_data(client: TestClient) -> None:
    response = client.post("/generate-data", json={"n_technicians": 10, "n_requests": 6})
    assert response.status_code == 200
    body = response.json()
    assert body["n_technicians"] == 10
    assert body["n_requests"] == 6
    assert body["n_assignments"] >= 1


def test_list_technicians(client: TestClient) -> None:
    response = client.get("/technicians")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert body


def test_list_requests(client: TestClient) -> None:
    response = client.get("/requests")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_list_assignments(client: TestClient) -> None:
    response = client.get("/assignments")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_train_model(client: TestClient) -> None:
    response = client.post("/train-model", json={"model_type": "xgboost"})
    assert response.status_code == 200
    body = response.json()
    assert body["model_type"] == "xgboost"
    assert 0.0 <= body["metrics"]["roc_auc"] <= 1.0


def test_predict(client: TestClient) -> None:
    response = client.post("/predict", json={})
    assert response.status_code == 200
    body = response.json()
    assert 0.0 <= body["predicted_success"] <= 1.0
    assert body["explanation"]


def test_allocate(client: TestClient) -> None:
    response = client.post("/allocate", json={"algorithm": "greedy"})
    assert response.status_code == 200
    body = response.json()
    assert body["algorithm"] == "greedy"
    assert body["assignments"]


def test_compare(client: TestClient) -> None:
    response = client.post("/compare", json={})
    assert response.status_code == 200
    body = response.json()
    assert len(body["rows"]) == 4
    assert "best_algorithm" in body


def test_metrics(client: TestClient) -> None:
    response = client.get("/metrics")
    assert response.status_code == 200
    body = response.json()
    assert "kpis" in body
    assert body["kpis"]["total_technicians"] >= 1
    assert len(body["feature_importance"]) == 13
