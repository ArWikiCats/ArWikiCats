#!/usr/bin/python3
"""
Build lookup tables for translating sport related keys.
"""

from dataclasses import dataclass
from typing import Mapping, MutableMapping, TypedDict

from ..helps import logger


class SportKeyRecord(TypedDict, total=False):
    """Typed representation of a single sport key translation."""

    label: str
    team: str
    jobs: str
    olympic: str


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


def _load_base_records(data) -> dict[str, SportKeyRecord]:
    """
    Load and parse sport key definitions from the sports/Sports_Keys_New.json file.

    The function reads the JSON file and converts each top-level mapping entry into a SportKeyRecord. Entries whose value contains an `"ignore"` key are skipped. If the top-level JSON payload is not a mapping, a warning is logged and an empty dict is returned. Malformed entries that are not string->mapping pairs are skipped.

    Returns:
        dict[str, SportKeyRecord]: Mapping from sport key to its coerced SportKeyRecord.
    """

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
        "sports": {
            "label": "رياضات",
            "team": "للرياضات",
            "jobs_old": "",
            "jobs": "رياضية",
            "olympic": "رياضات أولمبية",
        }
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


def _apply_aliases(records: MutableMapping[str, SportKeyRecord], ALIASES) -> None:
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


def _initialise_tables(data, ALIASES) -> dict[str, SportKeyRecord]:
    """Load data, expand aliases and variants, and build helper tables."""

    records = _load_base_records(data)
    _apply_aliases(records, ALIASES)

    return records


__all__ = [
    "SportKeyRecord",
    "SportKeyTables",
    "_build_tables",
    "_generate_variants",
    "_initialise_tables",
]
