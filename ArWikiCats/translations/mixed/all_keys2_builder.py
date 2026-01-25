"""
Key-label mappings for generic mixed categories.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Dict

from ..helps import logger


def handle_the_prefix(label_index: Dict[str, str]) -> Dict[str, str]:
    """Handle 'the ' prefix in country labels."""
    new_keys = {}
    for key, value in list(label_index.items()):
        if not key.lower().startswith("the ") or not value:
            continue

        trimmed_key = key[len("the ") :].strip()
        if trimmed_key in label_index:
            continue
        new_keys.setdefault(trimmed_key, value)

    logger.debug(f">> handle_the_prefix() Added {len(new_keys)} entries without 'the ' prefix.")
    return new_keys


def _build_of_variants(data, data_list, data_list2) -> Dict[str, str]:
    """Add "of" variants for categories and map them to Arabic labels."""
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
    ALBUMS_TYPE: Dict[str, str],
    BOOK_CATEGORIES: Dict[str, str],
    BOOK_TYPES: Dict[str, str],
) -> None:
    """Add literature related entries, including film/tv variants."""

    for category_key, category_label in BOOK_CATEGORIES.items():
        data[category_key] = category_label
        data[f"defunct {category_key}"] = f"{category_label} سابقة"
        data[f"{category_key} publications"] = f"منشورات {category_label}"
        lower_category = category_key.lower()
        for key, key_label in film_keys_for_female.items():
            data[f"{key.lower()} {lower_category}"] = f"{category_label} {key_label}"

        for book_type, book_label in BOOK_TYPES.items():
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

            for album_type, album_label in ALBUMS_TYPE.items():
                data[f"{singers_key} {album_type} albums"] = f"ألبومات {album_label} {singer_label}"
    return data


def _build_weapon_entries(WEAPON_CLASSIFICATIONS, WEAPON_EVENTS) -> Dict[str, str]:
    """Expand weapon classifications with related events."""
    data = {}
    for w_class, w_class_label in WEAPON_CLASSIFICATIONS.items():
        for event_key, event_label in WEAPON_EVENTS.items():
            data[f"{w_class} {event_key}"] = f"{event_label} {w_class_label}"

    return data


def _build_direction_region_entries(DIRECTIONS, REGIONS) -> Dict[str, str]:
    """Add entries that combine geographic directions with regions."""
    data = {}
    for direction_key, direction_label in DIRECTIONS.items():
        for region_key, region_label in REGIONS.items():
            data[f"{direction_key} {region_key}"] = f"{direction_label} {region_label}"
    return data


def _build_towns_entries(data, TOWNS_COMMUNITIES) -> None:
    """Add town and community variants for different descriptors."""

    for category, label in TOWNS_COMMUNITIES.items():
        data[f"{category} communities"] = f"مجتمعات {label}"
        data[f"{category} towns"] = f"بلدات {label}"
        data[f"{category} villages"] = f"قرى {label}"
        data[f"{category} cities"] = f"مدن {label}"


def _build_literature_area_entries(data, film_keys_for_male, LITERATURE_AREAS) -> None:
    """Add entries for literature and arts areas linked with film keys."""

    for area, area_label in LITERATURE_AREAS.items():
        data[f"children's {area}"] = f"{area_label} الأطفال"
        for key, key_label in film_keys_for_male.items():
            data[f"{key.lower()} {area.lower()}"] = f"{area_label} {key_label}"


def _build_cinema_entries(data, CINEMA_CATEGORIES) -> None:
    """Add mappings for cinema and television related categories."""

    for key, label in CINEMA_CATEGORIES.items():
        data[key] = label
        data[f"{key} set"] = f"{label} تقع أحداثها"
        data[f"{key} produced"] = f"{label} أنتجت"
        data[f"{key} filmed"] = f"{label} صورت"
        data[f"{key} basedon"] = f"{label} مبنية على"
        # data[f"{key} based on"] = f"{label} مبنية على"
        data[f"{key} based"] = f"{label} مبنية"
        data[f"{key} shot"] = f"{label} مصورة"


def update_keys_within(keys_of_with_in, keys_of_without_in, data):
    data.update(keys_of_with_in)
    keys_of_without_in = dict(keys_of_without_in)

    keys_of_without_in_del = {"explorers": "مستكشفون", "historians": "مؤرخون"}
    for key in keys_of_without_in_del:
        keys_of_without_in.pop(key, None)

    _update_lowercase(data, [keys_of_without_in], skip_existing=True)

    _build_of_variants(data, [keys_of_without_in], [keys_of_with_in])


def build_pf_keys2(
    ART_MOVEMENTS: Dict[str, str],
    BASE_LABELS: Dict[str, str],
    ctl_data: Dict[str, str],
    DIRECTIONS: Dict[str, str],
    keys2_py: Dict[str, str],
    keys_of_with_in: Dict[str, str],
    keys_of_without_in: Dict[str, str],
    pop_final_3: Dict[str, str],
    REGIONS: Dict[str, str],
    SCHOOL_LABELS: Dict[str, str],
    tato_type: Dict[str, str],
    TOWNS_COMMUNITIES: Dict[str, str],
    WEAPON_CLASSIFICATIONS: Dict[str, str],
    WEAPON_EVENTS: Dict[str, str],
    WORD_AFTER_YEARS: Dict[str, str],
) -> Dict[str, str]:
    """Build the master mapping used across the ``translations`` package."""

    data = {}

    data.update(ctl_data)

    for competition_key, competition_label in ctl_data.items():
        data[f"{competition_key} medalists"] = f"فائزون بميداليات {competition_label}"

    data.update(keys2_py)
    data.update(BASE_LABELS)
    data.update(_build_direction_region_entries(DIRECTIONS, REGIONS))

    update_keys_within(keys_of_with_in, keys_of_without_in, data)

    for school_category, school_template in SCHOOL_LABELS.items():
        data[f"private {school_category}"] = school_template.format("خاصة")
        data[f"public {school_category}"] = school_template.format("عامة")

    _update_lowercase(data, [WORD_AFTER_YEARS], skip_existing=False)

    _build_towns_entries(data, TOWNS_COMMUNITIES)

    data.update({key.lower(): value for key, value in ART_MOVEMENTS.items()})
    data.update({key.lower(): value for key, value in tato_type.items()})

    weapon_data = _build_weapon_entries(WEAPON_CLASSIFICATIONS, WEAPON_EVENTS)
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
