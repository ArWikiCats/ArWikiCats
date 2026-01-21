"""
Base resolver functions that don't depend on other resolver bots.

This module contains pure functions that serve as the foundation for category
label resolution. Moving these functions here helps break circular import
dependencies between modules.
"""

from ..legacy_utils.regex_hub import REGEX_SUB_CATEGORY_LOWERCASE, REGEX_SUB_MILLENNIUM_CENTURY


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
    "get_cats",
]
