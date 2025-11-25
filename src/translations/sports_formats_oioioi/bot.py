#!/usr/bin/python3
"""
TODO: use FormatData method
"""

import functools
import re
from typing import Dict, Tuple

from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ...translations_formats.format_2_data import FormatMultiData
from ..nats.Nationality import en_nats_to_ar_label
from ..sports.Sport_key import SPORTS_KEYS_FOR_TEAM
from ..utils.match_sport_keys import match_sport_key
from .data import NAT_P17_OIOI

# Placeholder used for sport key substitution in templates
SPORT_PLACEHOLDER = "oioioi"
LABEL_PLACEHOLDER = "ixix"

NAT_P17_OIOI_ADD = {
    "{nat} defunct oioioi coaches": "مدربو ixix {nat} سابقة",
    "{nat} defunct oioioi competitions": "منافسات ixix {nat} سابقة",
    "{nat} defunct oioioi cup competitions": "منافسات كؤوس ixix {nat} سابقة",
    "{nat} oioioi championships": "بطولة {nat} ixix",
    "{nat} oioioi clubs": "أندية ixix {nat}",
    "{nat} oioioi coaches": "مدربو ixix {nat}",
    "{nat} oioioi competitions": "منافسات ixix {nat}",
    "{nat} oioioi cup competitions": "منافسات كؤوس ixix {nat}",
    "{nat} oioioi cups": "كؤوس ixix {nat}",
    "{nat} oioioi indoor championship": "بطولة {nat} ixix داخل الصالات",
}

NAT_P17_OIOI.update(NAT_P17_OIOI_ADD)

both_bot = FormatMultiData(
    NAT_P17_OIOI,
    en_nats_to_ar_label,
    key_placeholder="{nat}",
    value_placeholder="{nat}",
    data_list2=SPORTS_KEYS_FOR_TEAM,
    key2_placeholder=SPORT_PLACEHOLDER,
    value2_placeholder=LABEL_PLACEHOLDER,
    # text_after=" people",
    # text_before="the ",
)


@functools.lru_cache(maxsize=None)
def get_start_p17(cate: str, check_the: bool=False) -> Tuple[str, str]:
    """
    Fast and optimized version of get_start_p17.

    Example:
        cate: "swiss wheelchair curling championship": result: ("{nat} wheelchair curling championship", "swiss"),
    """
    # Pre-lower cate once for speed
    cate_lower = cate.lower()

    category_suffix: str = ""
    country_prefix: str = ""

    cate2 = cate[4:] if cate.startswith("the ") else cate

    cate_lower2 = cate_lower[4:] if cate_lower.startswith("the ") else cate_lower

    for key in en_nats_to_ar_label:
        if category_suffix:
            # A match has already been found; exit early
            break

        # Pre-lower key only once
        key_lower = key.lower().strip()

        # Build minimal prefix options
        # Index meanings are kept exactly as original logic
        candidate_prefixes: Dict[int, str] = {
            1: f"{key_lower} people",
            2: f"{key_lower} ",
        }

        # Add the "the <country>" special case
        if key.startswith("the "):
            candidate_prefixes[3] = key[4:].lower()

        # Try each prefix option in fixed order
        for option_index in (1, 2, 3):
            prefix_candidate = candidate_prefixes.get(option_index)
            if not prefix_candidate:
                continue

            if cate_lower.startswith(prefix_candidate):
                country_prefix = key
                category_suffix = cate[len(prefix_candidate) :].strip()

                logger.debug(f'<<lightyellow>>>>>> {prefix_candidate=}, {category_suffix=}, {country_prefix=}')

                break

            if check_the and cate_lower2.startswith(prefix_candidate):
                country_prefix = key
                category_suffix = cate2[len(prefix_candidate) :].strip()

                logger.debug(f'<<lightyellow>>>>>> {prefix_candidate=}, {category_suffix=}, {country_prefix=}')

                break

    # Logging final result if match found
    if category_suffix and country_prefix:
        logger.debug(f'<<lightpurple>>>>>> bot_te_4.py country_start:"{country_prefix}",get_start_p17 fo_3:"{category_suffix}"')

    if category_suffix and not category_suffix.startswith("{nat}"):
        category_suffix = f"{{nat}} {category_suffix}"

    # TODO: Remove this
    sport_format_label = make_sport_formats_p17(category_suffix)
    if not sport_format_label:
        return "", ""

    return category_suffix, country_prefix


@functools.lru_cache(maxsize=None)
def make_sport_formats_p17(category_key: str) -> str:
    """Resolve a sport format label for P17 lookups.

    Args:
        category_key: The category key to resolve

    Returns:
        Resolved sport format label or empty string
    """
    logger.info(f'<<lightblue>>>>>> make_sport_formats_p17: category_key:"{category_key}"')

    resolved_label = ""
    sport_key = match_sport_key(category_key)

    if not sport_key:
        return ""

    sport_label = ""

    placeholder_key = category_key.replace(sport_key, SPORT_PLACEHOLDER)
    placeholder_key = re.sub(sport_key, SPORT_PLACEHOLDER, placeholder_key, flags=re.IGNORECASE)
    logger.debug(f'make_sport_formats_p17 category_key:"{category_key}", sport_key:"{sport_key}", placeholder_key:"{placeholder_key}"')

    placeholder_template = NAT_P17_OIOI.get(placeholder_key, "")

    if not placeholder_template:
        logger.debug(f'make_sport_formats_p17 placeholder_key:"{placeholder_key}" not in NAT_P17_OIOI')
        return ""

    sport_label = SPORTS_KEYS_FOR_TEAM.get(sport_key, "")
    if not sport_label:
        logger.debug(f' sport_key:"{sport_key}" not in SPORTS_KEYS_FOR_TEAM ')

    if not placeholder_template or not sport_label:
        return ""

    formatted_label = placeholder_template.replace(LABEL_PLACEHOLDER, sport_label)

    if LABEL_PLACEHOLDER not in formatted_label:
        resolved_label = formatted_label

    logger.info(f'make_sport_formats_p17 category_key:"{category_key}", resolved_label:"{resolved_label}"')

    return resolved_label


@functools.lru_cache(maxsize=None)
def sport_lab_oioioi_load(category: str, check_the: bool=False) -> str:
    """
    Example:
        category:Yemeni under-13 baseball teams", result: "فرق كرة قاعدة يمنية تحت 13 سنة"
    """
    normalized_category = category.lower()

    sport_format_key, country_start = get_start_p17(normalized_category, check_the=check_the)

    logger.debug(f"sport_lab_oioioi_load {normalized_category=}: {sport_format_key=} {country_start=}")

    if not country_start or not sport_format_key:
        return ""

    country_label = en_nats_to_ar_label.get(country_start, "")

    if not country_label:
        return ""

    sport_format_label = make_sport_formats_p17(sport_format_key)
    if not sport_format_label:
        return ""

    category_label = sport_format_label.format(nat=country_label)
    logger.debug(f'<<lightblue>>xxx sport_lab_oioioi_load: new category_label  "{category_label}"')

    return category_label


__all__ = [
    "sport_lab_oioioi_load",
    "get_start_p17",
]
