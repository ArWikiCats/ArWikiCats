"""
Key-label mappings for generic mixed categories.
"""

from __future__ import annotations

import logging
from collections.abc import Mapping
from typing import Dict

logger = logging.getLogger(__name__)


def handle_the_prefix(label_index: Dict[str, str]) -> Dict[str, str]:
    """
    Create entries by removing a leading "the " from keys when the trimmed key is not already present.

    Scans the provided mapping and collects new key/value pairs where a key starts with "the " (case-insensitive) and the corresponding value is truthy; the returned dict maps the trimmed keys (without the leading "the ") to the same values.

    Parameters:
        label_index (Dict[str, str]): Mapping of original keys to values to inspect.

    Returns:
        Dict[str, str]: New mappings whose keys are the original keys with the leading "the " removed.
    """
    new_keys = {}
    for key, value in list(label_index.items()):
        if not key.lower().startswith("the ") or not value:
            continue

        trimmed_key = key[len("the ") :].strip()
        if trimmed_key in label_index:
            continue
        new_keys.setdefault(trimmed_key, value)

    # logger.debug(f">> handle_the_prefix() Added {len(new_keys)} entries without 'the ' prefix.")
    return new_keys


def _build_of_variants(data, data_list, data_list2) -> Dict[str, str]:
    """
    Add English "of" variants for keys from the provided mappings and map them to corresponding Arabic labels.

    For each mapping in `data_list`, adds entries with the key lowercased and suffixed by " of" that map to the original value. For each mapping in `data_list2`, adds the same suffixed keys but maps to the original value followed by the Arabic preposition " في". Existing keys and source keys that already end with " of" are not overwritten.

    Parameters:
        data (Dict[str, str]): Target mapping to be updated in-place and returned.
        data_list (Iterable[Mapping[str, str]]): Source mappings whose values are used directly for the new "of" keys.
        data_list2 (Iterable[Mapping[str, str]]): Source mappings whose values are appended with " في" for the new "of" keys.

    Returns:
        Dict[str, str]: The `data` mapping with the added "of" variants.
    """
    for tab in data_list:
        for key, value in tab.items():
            new_key = f"{key.lower()} of"
            if data.get(new_key) or key.endswith(" of"):
                continue
            data[new_key] = value

    for tab2 in data_list2:
        for key2, value2 in tab2.items():
            new_key2 = f"{key2} of"
            if data.get(new_key2) or key2.endswith(" of"):
                continue
            data[new_key2] = f"{value2} في"

    return data


def _update_lowercase(data: Dict[str, str], mapping: list[Mapping[str, str]], skip_existing: bool = False) -> None:
    """Populate ``data`` with lowercase keys from the provided mappings."""

    def check_skip_existing(key) -> bool:
        """Determine whether a lowercase entry should overwrite existing data."""
        if skip_existing:
            return data.get(key.lower()) is None
        return True

    for table in mapping:
        data.update(
            {
                key.lower(): v.strip()
                for key, v in table.items()
                if key.strip() and v.strip() and check_skip_existing(key)
            }
        )


def _build_book_entries(
    data: Dict[str, str],
    singers_tab: Dict[str, str],
    film_keys_for_female: Dict[str, str],
    albums_type: Dict[str, str],
    book_categories: Dict[str, str],
    book_types: Dict[str, str],
) -> None:
    """Add literature related entries, including film/tv variants."""

    for category_key, category_label in book_categories.items():
        data[category_key] = category_label
        data[f"defunct {category_key}"] = f"{category_label} سابقة"
        data[f"{category_key} publications"] = f"منشورات {category_label}"
        lower_category = category_key.lower()
        for key, key_label in film_keys_for_female.items():
            data[f"{key.lower()} {lower_category}"] = f"{category_label} {key_label}"

        for book_type, book_label in book_types.items():
            data[f"{book_type.lower()} {lower_category}"] = f"{category_label} {book_label}"

    data["musical compositions"] = "مؤلفات موسيقية"

    for singers_key, singer_label in singers_tab.items():
        key_lower = singers_key.lower()
        if key_lower not in data and singer_label:
            data[key_lower] = singer_label
            data[f"{key_lower} albums"] = f"ألبومات {singer_label}"
            data[f"{key_lower} songs"] = f"أغاني {singer_label}"
            data[f"{key_lower} groups"] = f"فرق {singer_label}"
            data[f"{key_lower} duos"] = f"فرق {singer_label} ثنائية"

            data[f"{singers_key} video albums"] = f"ألبومات فيديو {singer_label}"

            for album_type, album_label in albums_type.items():
                data[f"{singers_key} {album_type} albums"] = f"ألبومات {album_label} {singer_label}"
    return data


def _build_weapon_entries(weapon_classifications, weapon_events) -> Dict[str, str]:
    """Expand weapon classifications with related events."""
    data = {}
    for w_class, w_class_label in weapon_classifications.items():
        for event_key, event_label in weapon_events.items():
            data[f"{w_class} {event_key}"] = f"{event_label} {w_class_label}"

    return data


def _build_direction_region_entries(directions, regions) -> Dict[str, str]:
    """Add entries that combine geographic directions with regions."""
    data = {}
    for direction_key, direction_label in directions.items():
        for region_key, region_label in regions.items():
            data[f"{direction_key} {region_key}"] = f"{direction_label} {region_label}"
    return data


def _build_towns_entries(data, towns_communities) -> None:
    """Add town and community variants for different descriptors."""

    for category, label in towns_communities.items():
        data[f"{category} communities"] = f"مجتمعات {label}"
        data[f"{category} towns"] = f"بلدات {label}"
        data[f"{category} villages"] = f"قرى {label}"
        data[f"{category} cities"] = f"مدن {label}"


def _build_literature_area_entries(data, film_keys_for_male, literature_areas) -> None:
    """Add entries for literature and arts areas linked with film keys."""

    for area, area_label in literature_areas.items():
        data[f"children's {area}"] = f"{area_label} الأطفال"
        for key, key_label in film_keys_for_male.items():
            data[f"{key.lower()} {area.lower()}"] = f"{area_label} {key_label}"


def _build_cinema_entries(data, cinema_categories) -> None:
    """
    Add cinema and television category labels and common phrase variants to the provided mapping.

    This function updates `data` in place by inserting each category key from `cinema_categories` mapped to its label and by creating common derived keys (e.g., "set", "produced", "filmed", "basedon", "based", "shot") that map to appropriate Arabic phrase variants.

    Parameters:
        data (dict): Mutable mapping to receive new keys and labels; modified in place.
        cinema_categories (Mapping[str, str]): Mapping of category keys to their Arabic labels.
    """

    for key, label in cinema_categories.items():
        data[key] = label
        data[f"{key} set"] = f"{label} تقع أحداثها"
        data[f"{key} produced"] = f"{label} أنتجت"
        data[f"{key} filmed"] = f"{label} صورت"
        data[f"{key} basedon"] = f"{label} مبنية على"
        # data[f"{key} based on"] = f"{label} مبنية على"
        data[f"{key} based"] = f"{label} مبنية"
        data[f"{key} shot"] = f"{label} مصورة"


def update_keys_within(keys_of_with_in, keys_of_without_in, data):
    """
    Merge and normalize two related key mappings into the main data mapping.

    Updates `data` in place by adding all entries from `keys_of_with_in`, then incorporating normalized entries from `keys_of_without_in` (with keys lowercased and existing keys preserved). Removes the entries for "explorers" and "historians" from `keys_of_without_in` before merging. Also adds "of" variants derived from both sets into `data`.

    Parameters:
        keys_of_with_in (Mapping[str, str]): Mapping of keys that should be merged into `data` as-is and used to generate "of" variants.
        keys_of_without_in (Mapping[str, str]): Mapping of keys to normalize (lowercased) and merge into `data`; the keys "explorers" and "historians" are removed from this mapping before processing.
        data (Dict[str, str]): Target mapping to be updated in place with merged and derived entries.
    """
    data.update(keys_of_with_in)
    keys_of_without_in = dict(keys_of_without_in)

    keys_of_without_in_del = {"explorers": "مستكشفون", "historians": "مؤرخون"}
    for key in keys_of_without_in_del:
        keys_of_without_in.pop(key, None)

    _update_lowercase(data, [keys_of_without_in], skip_existing=True)

    _build_of_variants(data, [keys_of_without_in], [keys_of_with_in])


def build_pf_keys2(
    art_movements: dict[str, str],
    base_labels: dict[str, str],
    ctl_data: dict[str, str],
    directions: dict[str, str],
    keys2_py: dict[str, str],
    keys_of_with_in: dict[str, str],
    keys_of_without_in: dict[str, str],
    pop_final_3: dict[str, str],
    regions: dict[str, str],
    school_labels: dict[str, str],
    tato_type: dict[str, str],
    towns_communities: dict[str, str],
    weapon_classifications: dict[str, str],
    weapon_events: dict[str, str],
    word_after_years: dict[str, str],
) -> Dict[str, str]:
    """
    Constructs a consolidated mapping of English label keys to their translated labels.

    Merges the provided label dictionaries, adds generated variants (direction-region combinations, town/community forms, weapon and "of" variants, minister and competition medalist keys, and other normalized lowercase keys), and returns the complete mapping to be used by the translations package.

    Returns:
        dict: A mapping of normalized English keys (lowercased and variant forms) to their translated labels.
    """

    data = {}

    data.update(ctl_data)

    for competition_key, competition_label in ctl_data.items():
        data[f"{competition_key} medalists"] = f"فائزون بميداليات {competition_label}"

    data.update(keys2_py)
    data.update(base_labels)
    data.update(_build_direction_region_entries(directions, regions))

    update_keys_within(keys_of_with_in, keys_of_without_in, data)

    for school_category, school_template in school_labels.items():
        data[f"private {school_category}"] = school_template.format("خاصة")
        data[f"public {school_category}"] = school_template.format("عامة")

    _update_lowercase(data, [word_after_years], skip_existing=False)

    _build_towns_entries(data, towns_communities)

    data.update({key.lower(): value for key, value in art_movements.items()})
    data.update({key.lower(): value for key, value in tato_type.items()})

    weapon_data = _build_weapon_entries(weapon_classifications, weapon_events)
    data.update(weapon_data)

    _build_of_variants(data, [], [weapon_data])

    minister_keys_2 = {
        "ministers of": "وزراء",
        "government ministers of": "وزراء",
        "women's ministers of": "وزيرات",
        "deputy prime ministers of": "نواب رؤساء وزراء",
        "finance ministers of": "وزراء مالية",
        "foreign ministers of": "وزراء خارجية",
        "prime ministers of": "رؤساء وزراء",
        "sport-ministers": "وزراء رياضة",
        "sports-ministers": "وزراء رياضة",
        "ministers of power": "وزراء طاقة",
        "ministers-of power": "وزراء طاقة",
    }
    data.update(minister_keys_2)

    for key, value in pop_final_3.items():
        lower_key = key.lower()
        if lower_key not in data and value:
            data[lower_key] = value

    return data


__all__ = [
    "build_pf_keys2",
    "handle_the_prefix",
    "_update_lowercase",
    "_build_book_entries",
    "_build_literature_area_entries",
    "_build_cinema_entries",
]
