#!/usr/bin/python3
"""
P17 nationality processing utilities.

This module handles nationality-based category translations,
particularly for sports-related categories using P17 (country) property.
"""

import functools
from ...helps.log import logger
from ...make_bots.matables_bots.bot import add_to_new_players
from ...translations import (
    sport_lab_nat_load,
    sport_lab_oioioi_load,
)


@functools.lru_cache(maxsize=None)
def find_nat_others(category: str) -> str:
    """Resolve fallback national labels for sport categories.

    Args:
        category: The category to resolve
        reference_category: Optional reference category (unused, kept for compatibility)

    Returns:
        Resolved category label or empty string
    """

    logger.info(f"<<lightblue>>>> vvvvvvvvvvvv find_nat_others {category=} vvvvvvvvvvvv ")

    normalized_category = category.lower()

    category_label = sport_lab_nat_load(normalized_category)

    if category_label == "":
        category_label = sport_lab_oioioi_load(normalized_category)
        if category_label:
            add_to_new_players(category, category_label)

    logger.info("<<lightblue>>>> ^^^^^^^^^ find_nat_others end ^^^^^^^^^ ")

    return category_label
