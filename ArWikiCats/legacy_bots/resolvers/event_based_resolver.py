#!/usr/bin/python3
"""
Event-Based Resolver Module

Handles event-based category resolution.
Extracts event2_d2 logic from country_bot.py to avoid circular dependencies.
"""

import re

from ...helps import logger



def event2_d2(category_r: str) -> str:
    """
    Determine the category label based on the input string.

    This function handles categories that should NOT contain common separators.
    It's designed to catch simple country-based categories before they go through
    the more complex separator-based resolvers.

    Args:
        category_r: The raw category string to process

    Returns:
        The processed category label or an empty string if not found
    """
    from ..circular_dependency.country_bot import get_country_label
    cat3 = category_r.lower().replace("category:", "").strip()

    logger.info(f'<<lightred>>>>>> category33:"{cat3}" ')

    # Reject strings that contain common English prepositions
    # These will be handled by separator-based resolvers instead
    blocked = ("in", "of", "from", "by", "at")
    if any(f" {word} " in cat3.lower() for word in blocked):
        return ""

    category_lab = ""
    # If it doesn't start with a digit, try country resolution
    if re.sub(r"^\d", "", cat3) == cat3:
        category_lab = get_country_label(cat3)

    return category_lab


__all__ = [
    "event2_d2",
]
