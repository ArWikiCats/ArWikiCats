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
    """
    Coerce a raw mapping (e.g., parsed JSON) into a SportKeyRecord.

    Parameters:
        raw (Mapping[str, object]): Source mapping containing optional keys "label", "jobs", "team", and "olympic".

    Returns:
        SportKeyRecord: Record with each field taken from `raw` and converted to a string; missing keys are set to an empty string.
    """

    return SportKeyRecord(
        label=str(raw.get("label", "")),
        jobs=str(raw.get("jobs", "")),
        team=str(raw.get("team", "")),
        olympic=str(raw.get("olympic", "")),
    )


def _load_base_records(data) -> dict[str, SportKeyRecord]:
    """
    Parse a mapping payload into a dictionary of sport key records.

    If `data` is not a mapping, an empty dict is returned. Top-level entries where the key is a string and the value is a mapping are converted to `SportKeyRecord` via `_coerce_record`. Entries whose value contains an `"ignore"` key are skipped; entries that are not string->mapping pairs are ignored.

    Returns:
        dict[str, SportKeyRecord]: Mapping from sport key to its coerced `SportKeyRecord`.
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
    """
    Create a shallow copy of a SportKeyRecord, applying any provided field overrides.

    Parameters:
        record (SportKeyRecord): Source record to copy.
        **overrides (str): Field replacements; for each provided field name, the value
            replaces the corresponding field in the copy only if the value is non-empty.

    Returns:
        SportKeyRecord: A new record containing the original fields with applicable overrides applied.
    """

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
    """
    Populate `records` with alias entries by copying the canonical record for each alias.

    Parameters:
        records (MutableMapping[str, SportKeyRecord]): Mapping of sport keys to records; aliases will be added or overwritten in-place.
        ALIASES (Mapping[str, str]): Mapping from alias key to canonical source key. If a source key is missing, the alias is skipped and a debug message is logged.
    """

    for alias, source in ALIASES.items():
        record = records.get(source)
        if record is None:
            logger.debug("Missing source record for alias: %s -> %s", alias, source)
            continue
        records[alias] = _copy_record(record)


def _generate_variants(records: Mapping[str, SportKeyRecord]) -> dict[str, SportKeyRecord]:
    """
    Generate derived sport key records for racing and wheelchair variants.

    Creates "{sport} racing" variants for sports that are not already racing and creates "wheelchair {sport}" variants for a predefined set of sports. The returned records use copies of the original SportKeyRecord with updated `label`, `team`, `jobs`, and `olympic` fields to reflect the variant.

    Parameters:
        records (Mapping[str, SportKeyRecord]): Mapping of canonical sport keys to their SportKeyRecord.

    Returns:
        dict[str, SportKeyRecord]: A mapping of generated variant sport keys to their corresponding SportKeyRecord.
    """

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
    """
    Build lookup tables mapping lowercased sport keys to their non-empty translation fields.

    Parameters:
        records (Mapping[str, SportKeyRecord]): Mapping of sport key names to their translation records.

    Returns:
        SportKeyTables: Container with `label`, `team`, `jobs`, and `olympic` dictionaries. Each dictionary maps the sport key in lowercase to the corresponding non-empty translation string.
    """

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
    """
    Load base sport records from the provided data and apply alias mappings.

    Parameters:
        data (Mapping | Any): JSON-like structure containing sport key definitions; malformed or non-mapping inputs result in an empty record set.
        ALIASES (Mapping[str, str]): Mapping of alias key -> canonical key; each alias will be added to the resulting records by copying the canonical record.

    Returns:
        dict[str, SportKeyRecord]: Mapping of sport keys (including applied aliases) to their corresponding SportKeyRecord entries.
    """

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
