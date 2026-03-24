#!/usr/bin/python3
"""
Build lookup tables for translating sport related keys.
"""

from typing import Final, Mapping

from ..data_builders.build_sport_keys import (
    SportKeyRecord,
    SportKeyTables,
    _build_tables,
    _generate_variants,
    _initialise_tables,
)
from ..helps import len_print
from ..utils import open_json_file

ALIASES: Final[Mapping[str, str]] = {
    "kick boxing": "kickboxing",
    "sport climbing": "climbing",
    "aquatic sports": "aquatics",
    "shooting": "shooting sport",
    "motorsports": "motorsport",
    "road race": "road cycling",
    "cycling road race": "road cycling",
    "road bicycle racing": "road cycling",
    "auto racing": "automobile racing",
    "bmx racing": "bmx",
    "equestrianism": "equestrian",
    "mountain bike racing": "mountain bike",
}


data = open_json_file("sports/Sports_Keys_New.json") or {}
SPORT_KEY_RECORDS_BASE: dict[str, SportKeyRecord] = _initialise_tables(data, ALIASES)
# Variants are created in a separate dictionary to avoid modifying the
# collection while iterating over it.
SPORT_KEY_RECORDS_VARIANTS = _generate_variants(SPORT_KEY_RECORDS_BASE)

SPORT_KEY_RECORDS = SPORT_KEY_RECORDS_BASE | SPORT_KEY_RECORDS_VARIANTS

SPORT_KEY_TABLES: SportKeyTables = _build_tables(SPORT_KEY_RECORDS)

SPORTS_KEYS_FOR_TEAM: Final[dict[str, str]] = SPORT_KEY_TABLES.team
SPORTS_KEYS_FOR_LABEL: Final[dict[str, str]] = SPORT_KEY_TABLES.label
# SPORTS_KEYS_FOR_LABEL["sports"] = "رياضات"
# SPORTS_KEYS_FOR_LABEL["sports"] = "ألعاب رياضية"

SPORTS_KEYS_FOR_JOBS: Final[dict[str, str]] = SPORT_KEY_TABLES.jobs
SPORTS_KEYS_FOR_JOBS["sports"] = "رياضية"

len_print.data_len(
    "Sport_key.py",
    {
        "SPORT_KEY_RECORDS": SPORT_KEY_RECORDS,
        "SPORT_KEY_RECORDS_BASE": SPORT_KEY_RECORDS_BASE,
        "SPORT_KEY_RECORDS_VARIANTS": SPORT_KEY_RECORDS_VARIANTS,
        "SPORTS_KEYS_FOR_LABEL": SPORTS_KEYS_FOR_LABEL,
        "SPORTS_KEYS_FOR_JOBS": SPORTS_KEYS_FOR_JOBS,
        "SPORTS_KEYS_FOR_TEAM": SPORTS_KEYS_FOR_TEAM,
    },
)

__all__ = [
    "SPORT_KEY_RECORDS",
    "SPORT_KEY_RECORDS_BASE",
    "SPORT_KEY_RECORDS_VARIANTS",
    "SPORT_KEY_TABLES",
    "SPORTS_KEYS_FOR_LABEL",
    "SPORTS_KEYS_FOR_JOBS",
    "SPORTS_KEYS_FOR_TEAM",
]
