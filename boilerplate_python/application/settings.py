"""Settings for System."""

import os

from functools import lru_cache

from boilerplate_python.infrastructure.logger.loguru_logger import Logger

from pydantic import BaseModel
from pydantic import BaseSettings


class GeneralSettings(BaseSettings):
    version: str = ""
    gcp_project_id: str = os.getenv("GCP_PROJECT_ID", "project-xxx")
    gcp_region: str = ""
    cors_origins: list[str] = [
        "http://localhost",
        "http://localhost:8080",
    ]
    logger = Logger


class Settings(BaseModel):
    general: GeneralSettings


@lru_cache()
def get_settings() -> Settings:
    """Get settings from app"""
    return Settings(
        general=GeneralSettings()
        #repository=RepositorySettings()
    )