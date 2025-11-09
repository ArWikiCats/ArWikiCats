"""Canonical public API for gendered job datasets.

This package aggregates the typed datasets exposed across the refactored job
modules and publishes a stable import surface for downstream callers.  Importers
can rely on :mod:`ma_lists.jobs` to retrieve commonly used mappings without
pulling in individual module internals.
"""

from __future__ import annotations

from .Jobs import (
    Female_Jobs,
    Jobs_key,
    Jobs_key_mens,
    Jobs_key_womens,
    Jobs_new,
    Men_Womens_Jobs,
    Men_Womens_with_nato,
    Nat_Before_Occ,
    womens_Jobs_2017,
)
from .Jobs2 import JOBS_2, JOBS_3333, Jobs_2, Jobs_3333
from .jobs_data import (
    MEN_WOMENS_JOBS_2,
    RELIGIOUS_KEYS_PP,
)
from .jobs_players_list import (
    FEMALE_JOBS_TO,
    FOOTBALL_KEYS_PLAYERS,
    JOBS_PLAYERS,
    PLAYERS_TO_MEN_WOMENS_JOBS,
    Female_Jobs_to,
    Football_Keys_players,
    Jobs_players,
    players_to_Men_Womens_Jobs,
)
from .jobs_singers import (
    FILMS_TYPE,
    MEN_WOMENS_SINGERS,
    MEN_WOMENS_SINGERS,
    FILMS_TYPE,
)

__all__ = [
    # Core types and shared datasets
    "MEN_WOMENS_JOBS_2",
    "RELIGIOUS_KEYS_PP",
    "JOBS_2",
    "JOBS_3333",
    "Jobs_2",
    "Jobs_3333",
    # Primary job dictionaries
    "Female_Jobs",
    "Jobs_key",
    "Jobs_key_mens",
    "Jobs_key_womens",
    "Jobs_new",
    "Men_Womens_Jobs",
    "Men_Womens_with_nato",
    "Nat_Before_Occ",
    "womens_Jobs_2017",
    # Player utilities
    "FEMALE_JOBS_TO",
    "FOOTBALL_KEYS_PLAYERS",
    "JOBS_PLAYERS",
    "PLAYERS_TO_MEN_WOMENS_JOBS",
    "Female_Jobs_to",
    "Football_Keys_players",
    "Jobs_players",
    "players_to_Men_Womens_Jobs",
    # Singer utilities
    "MEN_WOMENS_SINGERS",
    "FILMS_TYPE",
]
