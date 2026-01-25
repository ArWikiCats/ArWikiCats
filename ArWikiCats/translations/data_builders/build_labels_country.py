"""Aggregate translation tables for country and region labels."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping

from ..helps import logger


def update_with_lowercased(target: MutableMapping[str, str], mapping: Mapping[str, str]) -> None:
    """Update ``target`` with a lower-cased version of ``mapping``."""

    for key, value in mapping.items():
        if not value:
            continue
        target[key.lower()] = value


def setdefault_with_lowercased(target: MutableMapping[str, str], mapping: Mapping[str, str], name: str = "") -> None:
    """Update ``target`` with a lower-cased version of ``mapping``."""
    added = 0
    for key, value in mapping.items():
        if not value or key.lower() in target:
            continue
        target.setdefault(key.lower(), value)
        added += 1

    logger.debug(f"Added {added} entries to the target mapping, source mapping({name}) {len(mapping)}.")


def _make_japan_labels(data: dict[str, str]) -> dict[str, str]:
    labels_index = {}
    for province_name, province_label in data.items():
        if province_label:
            normalized = province_name.lower()
            labels_index[normalized] = province_label
            labels_index[f"{normalized} prefecture"] = f"محافظة {province_label}"
            labels_index[f"{normalized} region"] = f"منطقة {province_label}"

    return labels_index


def _make_turkey_labels(data: dict[str, str]) -> dict[str, str]:
    labels_index = {}
    for province_name, province_label in data.items():
        if province_label:
            normalized = province_name.lower()
            labels_index[normalized] = province_label
            labels_index[f"{normalized} province"] = f"محافظة {province_label}"
            labels_index[f"districts of {normalized} province"] = f"أقضية محافظة {province_label}"

    return labels_index


def _handle_the_prefix(label_index: dict[str, str]) -> dict[str, str]:
    """Handle 'the ' prefix in country labels."""
    new_keys = {}
    for key, value in list(label_index.items()):
        if not key.lower().startswith("the ") or not value:
            continue

        trimmed_key = key[len("the ") :].strip()
        if trimmed_key in label_index:
            continue
        new_keys.setdefault(trimmed_key, value)

    logger.debug(f">> _handle_the_prefix() Added {len(new_keys)} entries without 'the ' prefix.")
    return new_keys


def _build_country_label_index(
    CITY_TRANSLATIONS_LOWER,
    all_country_ar,
    US_STATES,
    COUNTRY_LABEL_OVERRIDES,
    COUNTRY_ADMIN_LABELS,
    MAIN_REGION_TRANSLATIONS,
    raw_region_overrides,
    SECONDARY_REGION_TRANSLATIONS,
    INDIA_REGION_TRANSLATIONS,
    TAXON_TABLE,
    BASE_POP_FINAL_5,
) -> dict[str, str]:
    """Return the aggregated translation table for countries and regions."""

    label_index: dict[str, str] = {}

    label_index.update(CITY_TRANSLATIONS_LOWER)  # 10,788

    to_update = {
        "ALL_COUNTRY_AR": all_country_ar,  # 54
        "US_STATES": US_STATES,  # 54
        "COUNTRY_LABEL_OVERRIDES": COUNTRY_LABEL_OVERRIDES,  # 1778
        "COUNTRY_ADMIN_LABELS": COUNTRY_ADMIN_LABELS,  # 1782
        "MAIN_REGION_TRANSLATIONS": MAIN_REGION_TRANSLATIONS,  # 823
        "raw_region_overrides": raw_region_overrides,  # 1782
        "SECONDARY_REGION_TRANSLATIONS": SECONDARY_REGION_TRANSLATIONS,  # 176
        "INDIA_REGION_TRANSLATIONS": INDIA_REGION_TRANSLATIONS,  # 1424
    }
    for name, mapping in to_update.items():
        logger.debug(f">> _build_country_label_index() Updating labels for {name}, entries: {len(mapping)}")
        update_with_lowercased(label_index, mapping)

    label_index.update(  # Specific overrides used by downstream consumers.
        {
            "indycar": "أندي كار",
            "indiana": "إنديانا",
            "motorsport": "رياضة محركات",
            "indianapolis": "إنديانابوليس",
            "sports in indiana": "الرياضة في إنديانا",
            "igbo": "إغبو",
        }
    )
    no_prefix = _handle_the_prefix(label_index)  # 276
    label_index.update(no_prefix)

    setdefault_with_lowercased(label_index, TAXON_TABLE, "TAXON_TABLE")  # 5324

    setdefault_with_lowercased(label_index, BASE_POP_FINAL_5, "BASE_POP_FINAL_5")  # 124

    return label_index


__all__ = [
    "_make_japan_labels",
    "_build_country_label_index",
    "_make_turkey_labels",
]
