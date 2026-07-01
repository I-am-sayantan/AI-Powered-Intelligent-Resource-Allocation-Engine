"""FastAPI dependencies shared across routes."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends

from services.store import InMemoryStore, get_store

#: Injects the process-wide in-memory store into route handlers.
StoreDep = Annotated[InMemoryStore, Depends(get_store)]
