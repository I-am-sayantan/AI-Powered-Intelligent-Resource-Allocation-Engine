"""Application settings and filesystem paths.

Settings can be overridden with environment variables prefixed ``REALC_``
(e.g. ``REALC_CORS_ORIGINS``) or via a ``.env`` file in the backend directory.
"""

from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR: Path = Path(__file__).resolve().parent


class Settings(BaseSettings):
    """Runtime configuration for the FastAPI backend."""

    model_config = SettingsConfigDict(
        env_prefix="REALC_",
        env_file=".env",
        extra="ignore",
        protected_namespaces=(),
    )

    app_name: str = "AI Resource Allocation Engine"
    version: str = "0.1.0"
    description: str = (
        "Intelligently assigns field-service engineers to service requests "
        "using optimization, ML, and explainable AI."
    )

    # CORS origins allowed to call the API (Vite dev server by default).
    cors_origins: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

    # Artifact directories (created on startup).
    data_dir: Path = BACKEND_DIR / "data"
    models_dir: Path = BACKEND_DIR / "models"

    def ensure_dirs(self) -> None:
        """Create artifact directories if they do not yet exist."""
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.models_dir.mkdir(parents=True, exist_ok=True)


settings = Settings()
