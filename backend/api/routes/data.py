"""Data endpoints: synthetic-data generation and entity listings."""

from __future__ import annotations

from fastapi import APIRouter

from api.deps import StoreDep
from schemas.assignment import Assignment
from schemas.data import GenerateDataRequest, GenerateDataResponse
from schemas.request import ServiceRequest
from schemas.technician import Technician
from services import data_service

router = APIRouter(tags=["data"])


@router.post("/generate-data", response_model=GenerateDataResponse)
def generate_data(request: GenerateDataRequest, store: StoreDep) -> GenerateDataResponse:
    """Generate synthetic technicians, requests, and assignments."""
    return data_service.generate_data(request, store)


@router.get("/technicians", response_model=list[Technician])
def get_technicians(store: StoreDep) -> list[Technician]:
    """List all technicians."""
    return data_service.list_technicians(store)


@router.get("/requests", response_model=list[ServiceRequest])
def get_requests(store: StoreDep) -> list[ServiceRequest]:
    """List all service requests."""
    return data_service.list_requests(store)


@router.get("/assignments", response_model=list[Assignment])
def get_assignments(store: StoreDep) -> list[Assignment]:
    """List all assignments."""
    return data_service.list_assignments(store)
