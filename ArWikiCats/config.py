"""
Configuration module for the ArWikiCats project.
This module handles environment variables and command-line arguments to configure
the application's behavior, including printing and application-specific settings.
"""

import os
import sys
from dataclasses import dataclass

argv_lower = [x.lower() for x in sys.argv]


def one_req(name: str) -> bool:
    """Check if the given flag is active via env or command line."""
    return os.getenv(name.upper(), "false").lower() in ("1", "true", "yes") or name.lower() in argv_lower


@dataclass(frozen=True)
class AppConfig:
    """Configuration for application settings.

    Attributes:
        save_data_path (str): Path to save data files.
    """

    save_data_path: str


@dataclass(frozen=True)
class Config:
    """Main configuration class containing all app settings.

    Attributes:
        app (AppConfig): Application-specific configuration.
    """

    app: AppConfig


settings = Config(
    app=AppConfig(
        save_data_path=os.getenv("SAVE_DATA_PATH", ""),
    ),
)
app_settings = settings.app

__all__ = [
    "settings",
    "app_settings",
]
