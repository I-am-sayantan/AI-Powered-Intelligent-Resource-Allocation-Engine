"""Allocation endpoints: run an algorithm and compare algorithms."""

from __future__ import annotations

from fastapi import APIRouter

from api.deps import StoreDep
from schemas.allocation import (
    AllocationRequest,
    AllocationResult,
    CompareRequest,
    CompareResult,
)
from services import allocation_service

router = APIRouter(tags=["allocation"])


@router.post("/allocate", response_model=AllocationResult)
def allocate(request: AllocationRequest, store: StoreDep) -> AllocationResult:
    """Run a single allocation algorithm."""
    return allocation_service.allocate(request, store)


@router.post("/compare", response_model=CompareResult)
def compare(request: CompareRequest, store: StoreDep) -> CompareResult:
    """Compare all allocation algorithms."""
    return allocation_service.compare(request, store)
