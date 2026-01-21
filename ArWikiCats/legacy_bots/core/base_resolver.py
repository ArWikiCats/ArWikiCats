"""
Base resolver functions that don't depend on other resolver bots.

This module contains pure functions that serve as the foundation for category
label resolution. Moving these functions here helps break circular import
dependencies between modules.
"""

import re

from ...helps import logger
from ..legacy_utils.regex_hub import REGEX_SUB_CATEGORY_LOWERCASE, REGEX_SUB_MILLENNIUM_CENTURY


def fix_minor(ar: str, ar_separator: str = "", en: str = "") -> str:
    """
    Clean up duplicate spaces and repeated prepositions in Arabic labels.

    Parameters:
        ar (str): The Arabic label to clean.
        ar_separator (str): An optional separator to include in preposition deduplication.
        en (str): The English label for logging purposes.

    Returns:
        str: The cleaned Arabic label with normalized whitespace and deduplicated prepositions.
    """
    arlabel = " ".join(ar.strip().split())

    sps_list = [
        "من",
        "في",
        "و",
    ]

    ar_separator = ar_separator.strip()

    if ar_separator not in sps_list:
        sps_list.append(ar_separator)

    for ar_separator in sps_list:
        arlabel = re.sub(rf" {ar_separator}\s+{ar_separator} ", f" {ar_separator} ", arlabel)
        if ar_separator == "و":
            arlabel = re.sub(rf" {ar_separator} ", f" {ar_separator}", arlabel)

    arlabel = " ".join(arlabel.strip().split())

    logger.debug(f"fix_minor: {en=}| {ar=}  ==> {arlabel=}")

    return arlabel


def get_cats(category_r: str) -> tuple[str, str]:
    """
    Normalize category strings and return raw and lowercase variants.

    This function normalizes millennium/century dashes and removes the
    "category:" prefix from the input string.

    Parameters:
        category_r (str): The raw category string to normalize.

    Returns:
        tuple[str, str]: A tuple containing:
            - cate: The normalized category with fixed dashes
            - cate3: The lowercase version without "category:" prefix
    """
    cate = REGEX_SUB_MILLENNIUM_CENTURY.sub(r"-\g<1>", category_r)
    cate3 = REGEX_SUB_CATEGORY_LOWERCASE.sub("", cate.lower())
    return cate, cate3


__all__ = [
    "fix_minor",
    "get_cats",
]
