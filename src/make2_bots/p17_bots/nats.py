#!/usr/bin/python3
"""
P17 nationality processing utilities.

This module handles nationality-based category translations,
particularly for sports-related categories using P17 (country) property.
"""

import functools

from ...helps.log import logger
from ...translations import (
    sport_lab_oioioi_load,
    sport_lab_nat_load,
    SPORT_FORMATS_FOR_P17,
    en_nats_to_ar_label,
)

from ...make2_bots.matables_bots.bot import add_to_new_players
from ..jobs_bots.get_helps import get_suffix


@functools.lru_cache(maxsize=None)
def load_SPORT_FORMATS_FOR_P17(category: str, check_the: bool=False) -> str:
    """
    TODO: use FormatData method

    Example:
        category:Yemeni under-13 baseball teams", result: "فرق كرة قاعدة يمنية تحت 13 سنة"
    """
    normalized_category = category.lower()

    sport_format_key, country_start = get_suffix(normalized_category, "nat", check_the=check_the)

    logger.debug(f"sport_lab_oioioi_load {normalized_category=}: {sport_format_key=} {country_start=}")

    if not country_start or not sport_format_key:
        return ""

    country_label = en_nats_to_ar_label.get(country_start, "")

    if not country_label:
        return ""

    sport_format_label = SPORT_FORMATS_FOR_P17.get(sport_format_key, "")

    if not sport_format_label:
        return ""

    category_label = sport_format_label.format(nat=country_label)
    logger.debug(f'<<lightblue>>xxx sport_lab_oioioi_load: new category_label  "{category_label}"')

    return category_label


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

    if category_label == "":
        category_label = load_SPORT_FORMATS_FOR_P17(normalized_category)

    if category_label == "":
        category_label = sport_lab_oioioi_load(normalized_category)
        if category_label:
            add_to_new_players(category, category_label)

    logger.info("<<lightblue>>>> ^^^^^^^^^ find_nat_others end ^^^^^^^^^ ")

    return category_label
