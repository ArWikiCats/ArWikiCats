"""Build lookup tables for translating sport related keys.

The original implementation stored large dictionaries that were populated via
side effects at import time.  The refactored version moves the logic into
well-typed helper functions which improves readability and makes unit testing
possible.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from typing import Final, Mapping, MutableMapping, TypedDict

from ..utils.json_dir import open_json_file
from ._helpers import log_length_stats

LOGGER = logging.getLogger(__name__)


class SportKeyRecord(TypedDict, total=False):
    """Typed representation of a single sport key translation."""

    label: str
    jobs: str
    team: str
    olympic: str


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


@dataclass(frozen=True)
class SportKeyTables:
    """Container with convenience accessors for specific dictionaries."""

    label: dict[str, str]
    jobs: dict[str, str]
    team: dict[str, str]
    olympic: dict[str, str]


def _coerce_record(raw: Mapping[str, object]) -> SportKeyRecord:
    """Convert a raw JSON entry into a :class:`SportKeyRecord`."""

    return SportKeyRecord(
        label=str(raw.get("label", "")),
        jobs=str(raw.get("jobs", "")),
        team=str(raw.get("team", "")),
        olympic=str(raw.get("olympic", "")),
    )


def _load_base_records() -> dict[str, SportKeyRecord]:
    """Load sports key definitions from the JSON configuration file."""

    data = open_json_file("Sports_Keys_New") or {}
    records: dict[str, SportKeyRecord] = {}

    if not isinstance(data, Mapping):
        LOGGER.warning("Unexpected sports key payload type: %s", type(data))
        return records

    for key, value in data.items():
        if isinstance(key, str) and isinstance(value, Mapping):
            records[key] = _coerce_record(value)
        else:  # pragma: no cover - defensive branch
            LOGGER.debug("Skipping malformed sports key entry: %s", key)

    return records


def _copy_record(record: SportKeyRecord, **overrides: str) -> SportKeyRecord:
    """Return a shallow copy of ``record`` applying ``overrides``."""

    updated: SportKeyRecord = SportKeyRecord(
        label=record.get("label", ""),
        jobs=record.get("jobs", ""),
        team=record.get("team", ""),
        olympic=record.get("olympic", ""),
    )

    for field, value in overrides.items():
        if value:
            updated[field] = value

    return updated


def _apply_aliases(records: MutableMapping[str, SportKeyRecord]) -> None:
    """Populate alias keys by copying the values from the canonical entry."""

    for alias, source in ALIASES.items():
        record = records.get(source)
        if record is None:
            LOGGER.debug("Missing source record for alias: %s -> %s", alias, source)
            continue
        records[alias] = _copy_record(record)


def _generate_variants(records: Mapping[str, SportKeyRecord]) -> dict[str, SportKeyRecord]:
    """Create derived entries such as ``"{sport} racing"`` and wheelchair keys."""

    variants: dict[str, SportKeyRecord] = {}
    for sport, record in records.items():
        label = record.get("label", "")
        jobs = record.get("jobs", "")
        olympic = record.get("olympic", "")
        team = record.get("team", "")

        variants[f"{sport} racing"] = _copy_record(
            record,
            label=f"سباق {label}",
            team=f"لسباق {label}",
            jobs=f"سباق {jobs}",
            olympic=f"سباق {olympic}",
        )
        variants[f"wheelchair {sport}"] = _copy_record(
            record,
            label=f"{label} على الكراسي المتحركة",
            team=f"{team} على الكراسي المتحركة",
            jobs=f"{jobs} على كراسي متحركة",
            olympic=f"{olympic} على كراسي متحركة",
        )

    return variants


def _build_tables(records: Mapping[str, SportKeyRecord]) -> SportKeyTables:
    """Create lookups for each translation category."""

    tables: dict[str, dict[str, str]] = {
        "label": {},
        "jobs": {},
        "team": {},
        "olympic": {},
    }

    for sport, record in records.items():
        for field, mapping in tables.items():
            value = record.get(field, "")
            if value:
                mapping[sport.lower()] = value

    return SportKeyTables(
        label=tables["label"],
        jobs=tables["jobs"],
        team=tables["team"],
        olympic=tables["olympic"],
    )


def _build_regex(records: Mapping[str, SportKeyRecord]) -> str:
    """Create a regular expression matching any of the available sport keys."""

    sorted_keys = sorted(records.keys(), key=lambda name: (-len(name.split()), name))
    escaped_variants = "|".join(re.escape(name) for name in sorted_keys)
    # The regex preserves backwards compatibility with the loose matching used
    # by the legacy code while escaping special characters properly.
    return rf".*\s*({escaped_variants})\s*.*"


def _initialise_tables() -> tuple[SportKeyTables, dict[str, SportKeyRecord], str]:
    """Load data, expand aliases and variants, and build helper tables."""

    records = _load_base_records()
    _apply_aliases(records)

    # Variants are created in a separate dictionary to avoid modifying the
    # collection while iterating over it.
    records.update(_generate_variants(records))

    tables = _build_tables(records)
    regex = _build_regex(records)

    log_length_stats(
        "sports/Sport_key.py",
        {
            "sport_records": len(records),
            "labels": len(tables.label),
            "jobs": len(tables.jobs),
            "teams": len(tables.team),
        },
    )

    return tables, records, regex


SPORT_KEY_TABLES, SPORT_KEY_RECORDS, FANCO_LINE_PATTERN = _initialise_tables()

SPORTS_KEYS_FOR_LABEL: Final[dict[str, str]] = SPORT_KEY_TABLES.label
SPORTS_KEYS_FOR_JOBS: Final[dict[str, str]] = SPORT_KEY_TABLES.jobs
SPORTS_KEYS_FOR_TEAM: Final[dict[str, str]] = SPORT_KEY_TABLES.team
SPORTS_KEYS_FOR_OLYMPIC: Final[dict[str, str]] = SPORT_KEY_TABLES.olympic

# Backwards compatibility aliases for legacy imports.
Sports_Keys_For_Label = SPORTS_KEYS_FOR_LABEL
Sports_Keys_For_Jobs = SPORTS_KEYS_FOR_JOBS
Sports_Keys_For_Team = SPORTS_KEYS_FOR_TEAM
Sports_Keys_For_olympic = SPORTS_KEYS_FOR_OLYMPIC

fanco_line = FANCO_LINE_PATTERN

__all__ = [
    "FANCO_LINE_PATTERN",
    "SPORT_KEY_RECORDS",
    "SPORT_KEY_TABLES",
    "SPORTS_KEYS_FOR_LABEL",
    "SPORTS_KEYS_FOR_JOBS",
    "SPORTS_KEYS_FOR_OLYMPIC",
    "SPORTS_KEYS_FOR_TEAM",
    "fanco_line",
    "Sports_Keys_For_Label",
    "Sports_Keys_For_Jobs",
    "Sports_Keys_For_Team",
    "Sports_Keys_For_olympic",
]
