#!/usr/bin/python3
"""
Build lookup tables for translating sport related keys.
"""

from dataclasses import dataclass
from typing import Final, Mapping, MutableMapping, TypedDict

from ...helps import len_print, logger
from ..utils.json_dir import open_json_file


class SportKeyRecord(TypedDict, total=False):
    """Typed representation of a single sport key translation."""

    label: str
    team: str
    jobs: str
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

    data = open_json_file("sports/Sports_Keys_New.json") or {}
    records: dict[str, SportKeyRecord] = {}

    if not isinstance(data, Mapping):
        logger.warning("Unexpected sports key payload type: %s", type(data))
        return records

    multi_sport_key = {
        "multi-sport": {
            "label": "رياضية متعددة",
            "team": "",
            "jobs": "رياضية متعددة",
            "olympic": "رياضية متعددة أولمبية",
        },
        "sports": {
            "label": "ألعاب رياضية",
            "team": "للرياضة",
            "jobs_old": "رياضية",
            "jobs": "",
            "olympic": "رياضية أولمبية",
        },
    }
    # data.update(multi_sport_key)
    sports_key = {
        "sports": {"label": "رياضات", "team": "للرياضات", "jobs_old": "", "jobs": "رياضية", "olympic": "رياضات أولمبية"}
    }
    # data.update(sports_key)

    for key, value in data.items():
        if isinstance(key, str) and isinstance(value, Mapping):
            if value.get("ignore"):
                continue
            records[key] = _coerce_record(value)
        else:  # pragma: no cover - defensive branch
            logger.debug("Skipping malformed sports key entry: %s", key)

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
            logger.debug("Missing source record for alias: %s -> %s", alias, source)
            continue
        records[alias] = _copy_record(record)


def _generate_variants(records: Mapping[str, SportKeyRecord]) -> dict[str, SportKeyRecord]:
    """Create derived entries such as ``"{sport} racing"`` and wheelchair keys."""

    keys_to_wheelchair = [
        "sports",
        "basketball",
        "rugby league",
        "rugby",
        "tennis",
        "handball",
        "beach handball",
        "curling",
        "fencing",
    ]

    variants: dict[str, SportKeyRecord] = {}
    for sport, record in records.items():
        label = record.get("label", "")
        jobs = record.get("jobs", "")
        olympic = record.get("olympic", "")
        team = record.get("team", "")

        if not sport.endswith("racing") and not label.startswith("سباق") and not jobs.startswith("سباق"):
            variants[f"{sport} racing"] = _copy_record(
                record,
                label=f"سباق {label}",
                team=f"لسباق {label}",
                jobs=f"سباق {jobs}",
                olympic=f"سباق {olympic}",
            )

        if sport in keys_to_wheelchair:
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
        "team": {},
        "jobs": {},
        "olympic": {},
    }

    for sport, record in records.items():
        for field in tables.keys():
            value = record.get(field, "")
            if value:
                tables[field][sport.lower()] = value

    return SportKeyTables(
        label=tables["label"],
        jobs=tables["jobs"],
        team=tables["team"],
        olympic=tables["olympic"],
    )


def _initialise_tables() -> dict[str, SportKeyRecord]:
    """Load data, expand aliases and variants, and build helper tables."""

    records = _load_base_records()
    _apply_aliases(records)

    return records


SPORT_KEY_RECORDS_BASE: dict[str, SportKeyRecord] = _initialise_tables()
# Variants are created in a separate dictionary to avoid modifying the
# collection while iterating over it.
SPORT_KEY_RECORDS_VARIANTS = _generate_variants(SPORT_KEY_RECORDS_BASE)

SPORT_KEY_RECORDS = SPORT_KEY_RECORDS_BASE | SPORT_KEY_RECORDS_VARIANTS

SPORT_KEY_TABLES: SportKeyTables = _build_tables(SPORT_KEY_RECORDS)

SPORTS_KEYS_FOR_TEAM: Final[dict[str, str]] = SPORT_KEY_TABLES.team
SPORTS_KEYS_FOR_OLYMPIC: Final[dict[str, str]] = SPORT_KEY_TABLES.olympic

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
        "SPORTS_KEYS_FOR_OLYMPIC": SPORTS_KEYS_FOR_OLYMPIC,
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
    "SPORTS_KEYS_FOR_OLYMPIC",
    "SPORTS_KEYS_FOR_TEAM",
]
