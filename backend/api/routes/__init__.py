"""Route registration: exposes every router as ``all_routers``."""

from __future__ import annotations

from api.routes.allocation import router as allocation_router
from api.routes.data import router as data_router
from api.routes.metrics import router as metrics_router
from api.routes.models import router as models_router

#: All API routers, included by ``main.py`` in registration order.
all_routers = [data_router, models_router, allocation_router, metrics_router]

__all__ = ["all_routers"]
