#!/usr/bin/python3
"""
"""

import functools
import re
from ..helps import logger
from ..translations import (
    Nat_mens,
)

# Template patterns for anti-sentiment categories
ANTI_SENTIMENT_PATTERNS: dict[str, str] = {
    r"^anti\-(\w+) sentiment$": "مشاعر معادية لل%s",
}


def _match_anti_sentiment_pattern(normalized_category: str) -> tuple[str, str]:
    """Match a category against anti-sentiment patterns.

    Args:
        normalized_category: The normalized category string.

    Returns:
        A tuple of (matched_country_key, template) or ("", "") if no match.
    """
    for pattern, template in ANTI_SENTIMENT_PATTERNS.items():
        match = re.match(pattern, normalized_category)
        if match:
            return match.group(1), template
    return "", ""


@functools.lru_cache(maxsize=10000)
def nat_match(category: str) -> str:
    """Match a category string to a localized anti-sentiment label.

    Processes categories like "anti-haitian sentiment" and returns the
    Arabic equivalent "مشاعر معادية للهايتيون".

    Args:
        category: The category string to be matched.

    Returns:
        The localized sentiment label, or empty string if no match.

    Example:
        >>> nat_match("anti-haitian sentiment")
        "مشاعر معادية للهايتيون"
    """
    normalized_category = category.lower().replace("category:", "")
    logger.debug(f'<<lightblue>> bot_te_4: nat_match normalized_category :: "{normalized_category}"')

    matched_country_key, template = _match_anti_sentiment_pattern(normalized_category)

    if not matched_country_key:
        return ""

    logger.debug(f'<<lightblue>> bot_te_4: nat_match country_key :: "{matched_country_key}"')

    nationality_label = Nat_mens.get(matched_country_key, "")
    if not nationality_label:
        return ""

    result = template % nationality_label
    logger.debug(f"<<lightblue>> bot_te_4: nat_match {result=}")
    return result


__all__ = [
    "nat_match",
]
