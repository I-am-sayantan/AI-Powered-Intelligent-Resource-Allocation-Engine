"""FastAPI application entrypoint.

Run from the ``backend/`` directory:

    uvicorn main:app --reload
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from api.routes import all_routers
from config import settings
from core.logging import get_logger

logger = get_logger("app")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Create artifact directories on startup."""
    settings.ensure_dirs()
    logger.info("%s v%s started", settings.app_name, settings.version)
    yield


app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description=settings.description,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in all_routers:
    app.include_router(router)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    """Liveness probe."""
    return {"status": "ok", "app": settings.app_name, "version": settings.version}


@app.get("/", include_in_schema=False)
def root() -> RedirectResponse:
    """Redirect the root path to the interactive API docs."""
    return RedirectResponse(url="/docs")
