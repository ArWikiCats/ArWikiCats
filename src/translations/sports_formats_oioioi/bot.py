#!/usr/bin/python3
"""

"""

import functools
import re
from typing import Dict, Tuple

from ...helps.log import logger
from ..utils.match_sport_keys import match_sport_key
from ..sports.Sport_key import SPORTS_KEYS_FOR_TEAM
from ..nats.Nationality import en_nats_to_ar_label
from .data import NAT_P17_OIOI

# Placeholder used for sport key substitution in templates
SPORT_PLACEHOLDER = "oioioi"
LABEL_PLACEHOLDER = "ixix"


@functools.lru_cache(maxsize=None)
def get_start_p17(cate: str, category_type: str, check_the: bool=False) -> Tuple[str, str]:
    """Fast and optimized version of get_start_p17.

    This function identifies a matching prefix from the given keys and
    extracts the remaining suffix while preserving the original behavior.
    All comments are in English only as required.
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
        logger.debug(f'<<lightpurple>>>>>> bot_te_4.py country_start:"{country_prefix}",get_start_p17 fo_3:"{category_suffix}",lab_type:{category_type}')

    if not category_suffix.startswith("{nat}"):
        category_suffix = f"{{nat}} {category_suffix}"

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

    sport_format_key, country_start = get_start_p17(normalized_category, "nat", check_the=check_the)

    print(f"sport_lab_oioioi_load {normalized_category=}: {sport_format_key=} {country_start=}")

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
]
