"""Canonical public API for gendered job datasets.

This package aggregates the typed datasets exposed across the refactored job
modules and publishes a stable import surface for downstream callers.  Importers
can rely on :mod:`ma_lists.jobs` to retrieve commonly used mappings without
pulling in individual module internals.
"""

from __future__ import annotations

from .jobs_womens import Female_Jobs, short_womens_jobs

from .Jobs import (
    jobs_mens_data,
    Jobs_new,
)
from .Jobs2 import JOBS_2, JOBS_3333
from .jobs_data import (
    MEN_WOMENS_JOBS_2,
    NAT_BEFORE_OCC,
    RELIGIOUS_KEYS_PP,
    MEN_WOMENS_WITH_NATO,
)
from .jobs_players_list import (
    FOOTBALL_KEYS_PLAYERS,
    JOBS_PLAYERS,
    PLAYERS_TO_MEN_WOMENS_JOBS,
)
from .jobs_singers import (
    FILMS_TYPE,
    MEN_WOMENS_SINGERS,
)

__all__ = [
    # Core types and shared datasets
    "MEN_WOMENS_JOBS_2",
    "RELIGIOUS_KEYS_PP",
    "JOBS_3333",
    "JOBS_2",
    # Primary job dictionaries
    "Female_Jobs",
    "jobs_mens_data",
    "short_womens_jobs",
    "Jobs_new",
    "MEN_WOMENS_WITH_NATO",
    "NAT_BEFORE_OCC",
    # Player utilities
    "FOOTBALL_KEYS_PLAYERS",
    "JOBS_PLAYERS",
    "PLAYERS_TO_MEN_WOMENS_JOBS",
    # Singer utilities
    "MEN_WOMENS_SINGERS",
    "FILMS_TYPE",
]
