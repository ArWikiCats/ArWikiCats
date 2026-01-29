"""
Configuration module for the ArWikiCats project.
This module handles environment variables and command-line arguments to configure
the application's behavior, including printing and application-specific settings.
"""

import logging
import os
import sys
from dataclasses import dataclass

argv_lower = [x.lower() for x in sys.argv]


all_params = ["NOKOOORA", "NOWIKIDATA"]


def one_req(name: str) -> bool:
    """Check if the given flag is active via env or command line."""
    all_params.append(name)
    return os.getenv(name.upper(), "false").lower() in ("1", "true", "yes") or name.lower() in argv_lower


@dataclass(frozen=True)
class PrintConfig:
    """Configuration for print-related settings.

    Attributes:
        noprint_formats (bool): Whether to suppress printing of formats.
        noprint (bool): Whether to suppress all printing.
    """

    noprint_formats: bool
    noprint: bool


@dataclass(frozen=True)
class AppConfig:
    """Configuration for application settings.

    Attributes:
        find_stubs (bool): Whether to find stub entries.
        makeerr (bool): Whether to generate error reports.
        save_data_path (str): Path to save data files.
    """

    find_stubs: bool
    makeerr: bool
    save_data_path: str


@dataclass(frozen=True)
class Config:
    """Main configuration class containing all app settings.

    Attributes:
        print (PrintConfig): Print-related configuration.
        app (AppConfig): Application-specific configuration.
    """

    print: PrintConfig
    app: AppConfig


settings = Config(
    print=PrintConfig(
        noprint=one_req("NOPRINT"),
        noprint_formats=one_req("NOPRINT_FORMATS"),
    ),
    app=AppConfig(
        find_stubs=one_req("-STUBS"),
        makeerr=one_req("MAKEERR"),
        save_data_path=os.getenv("SAVE_DATA_PATH", ""),
    ),
)
print_settings = settings.print
app_settings = settings.app

__all__ = [
    "settings",
    "print_settings",
    "app_settings",
    "all_params",
]
