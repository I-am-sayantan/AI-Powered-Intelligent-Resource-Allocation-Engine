"""Pytest configuration and shared fixtures.

Adds the ``backend/`` directory to ``sys.path`` so tests import backend modules
the same way the app does when run with ``uvicorn main:app`` from ``backend/``.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

BACKEND_DIR = Path(__file__).resolve().parent.parent / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from fastapi.testclient import TestClient  # noqa: E402  (import after sys.path setup)

from main import app  # noqa: E402


@pytest.fixture
def client() -> TestClient:
    """Return a FastAPI test client for the app."""
    with TestClient(app) as test_client:
        yield test_client
