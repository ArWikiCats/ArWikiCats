"""Canonical public API for gendered job datasets.

This package aggregates the typed datasets exposed across the refactored job
modules and publishes a stable import surface for downstream callers.  Importers
can rely on :mod:`translations.jobs` to retrieve commonly used mappings without
pulling in individual module internals.
"""

from __future__ import annotations

from .Jobs import Jobs_new, jobs_mens_data, jobs_womens_data
from .Jobs2 import JOBS_2, JOBS_3333
from .jobs_data_basic import NAT_BEFORE_OCC, NAT_BEFORE_OCC_BASE, RELIGIOUS_KEYS_PP
from .jobs_players_list import PLAYERS_TO_MEN_WOMENS_JOBS, SPORT_JOB_VARIANTS
from .jobs_singers import SINGERS_TAB
from .jobs_womens import FEMALE_JOBS_BASE_EXTENDED, short_womens_jobs

__all__ = [
    "SINGERS_TAB",
    "Jobs_new",
    "jobs_mens_data",
    "JOBS_2",
    "JOBS_3333",
    "NAT_BEFORE_OCC",
    "jobs_womens_data",
    "NAT_BEFORE_OCC_BASE",
    "RELIGIOUS_KEYS_PP",
    "PLAYERS_TO_MEN_WOMENS_JOBS",
    "SPORT_JOB_VARIANTS",
    "FEMALE_JOBS_BASE_EXTENDED",
    "short_womens_jobs",
]
