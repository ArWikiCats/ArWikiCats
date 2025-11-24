#!/usr/bin/python3
"""
P17 nationality processing utilities.

This module handles nationality-based category translations,
particularly for sports-related categories using P17 (country) property.
"""

import functools
import re

from ...helps.log import logger
from ...translations import (
    NAT_P17_OIOI,
    SPORT_FORMATS_FOR_P17,
    SPORTS_KEYS_FOR_TEAM,
    All_Nat,
    sport_lab_nat_load,
    Get_sport_formts_female_nat,
    Nat_women,
    match_sport_key,
)
from ..jobs_bots.get_helps import get_con_3
from ..matables_bots.bot import add_to_new_players

# Placeholder used for sport key substitution in templates
SPORT_PLACEHOLDER = "oioioi"


@functools.lru_cache(maxsize=None)
def make_sport_formats_p17(category_key: str) -> str:
    """Resolve a sport format label for P17 lookups.

    Args:
        category_key: The category key to resolve

    Returns:
        Resolved sport format label or empty string
    """

    logger.info(f'<<lightblue>>>>>> make_sport_formats_p17: category_key:"{category_key}"')

    cached_label = SPORT_FORMATS_FOR_P17.get(category_key, "")
    if cached_label:
        logger.debug(f"\tfind lab in SPORT_FORMATS_FOR_P17: {cached_label}")
        return cached_label

    resolved_label = ""
    sport_key = match_sport_key(category_key)

    if not sport_key:
        return ""

    sport_label = ""
    placeholder_template = ""

    placeholder_key = category_key.replace(sport_key, SPORT_PLACEHOLDER)
    placeholder_key = re.sub(sport_key, SPORT_PLACEHOLDER, placeholder_key, flags=re.IGNORECASE)
    logger.debug(f'make_sport_formats_p17 category_key:"{category_key}", sport_key:"{sport_key}", placeholder_key:"{placeholder_key}"')

    if placeholder_key in NAT_P17_OIOI:
        sport_label = SPORTS_KEYS_FOR_TEAM.get(sport_key, "")
        if not sport_label:
            logger.debug(f' sport_key:"{sport_key}" not in SPORTS_KEYS_FOR_TEAM ')
        placeholder_template = NAT_P17_OIOI[placeholder_key]
        if placeholder_template and sport_label:
            formatted_label = placeholder_template.replace(SPORT_PLACEHOLDER, sport_label)
            if SPORT_PLACEHOLDER not in formatted_label:
                resolved_label = formatted_label
                logger.debug(f'make_sport_formats_p17 formatted_label:"{resolved_label}"')
    else:
        logger.debug(f'make_sport_formats_p17 placeholder_key:"{placeholder_key}" not in NAT_P17_OIOI')

    if resolved_label:
        logger.info(f'make_sport_formats_p17 category_key:"{category_key}", resolved_label:"{resolved_label}"')

    return resolved_label


@functools.lru_cache(maxsize=None)
def find_nat_others(category: str) -> str:
    """Resolve fallback national labels for sport categories.

    Args:
        category: The category to resolve
        reference_category: Optional reference category (unused, kept for compatibility)

    Returns:
        Resolved category label or empty string
    """

    logger.info(f"<<lightblue>>>> vvvvvvvvvvvv find_nat_others category:{category} vvvvvvvvvvvv ")

    normalized_category = category.lower()

    category_label = sport_lab_nat_load(normalized_category)
    if category_label:
        return category_label

    sport_format_key, country_start = get_con_3(normalized_category, "nat")

    if not country_start or not sport_format_key:
        return ""

    if category_label == "":
        sport_format_label = make_sport_formats_p17(sport_format_key)
        country_label = All_Nat[country_start].get("ar", "")
        if sport_format_label and country_label:
            category_label = sport_format_label.format(nat=country_label)
            logger.debug(f'<<lightblue>>>>>> SPORT_FORMATS_FOR_P17: new category_label  "{category_label}"')
            add_to_new_players(category, category_label)

    logger.info("<<lightblue>>>> ^^^^^^^^^ find_nat_others end ^^^^^^^^^ ")

    return category_label
