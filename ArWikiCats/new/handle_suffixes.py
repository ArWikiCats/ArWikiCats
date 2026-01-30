"""
Utility for handling category suffixes and gendered labels.
This module provides functions to resolve categories by identifying suffixes
(like "players" or "coaches") and applying gender-specific Arabic translations.
"""

from typing import Dict, TypedDict

import logging

logger = logging.getLogger(__name__)


class GenderedLabel(TypedDict):
    """Represent an Arabic label split into masculine and feminine forms."""

    males: str
    females: str


def normalize_text(text: str) -> str:
    """Normalize category text by removing namespace and common words.

    Args:
        text: The raw category string.

    Returns:
        The normalized category string.
    """
    text = text.lower().replace("category:", "")
    # text = text.replace("sportspeople", "sports-people")
    text = text.replace(" the ", " ")
    # text = text.replace("republic of", "republic-of")
    text = text.removeprefix("the ")
    return text.strip()


def combine_value_and_label(
    value: str,
    new_label: str,
    format_key: str = "",
) -> str:
    """
    Combine value and new_label based on format_key.
    Examples:
    - If format_key is "", return "value new_label".
    - If format_key is "{}", return value formatted with new_label.
    - If format_key == "ar", return value formatted with new_label using format_map.
    """
    if not format_key:
        return f"{value} {new_label}"

    if format_key == "{}":
        return value.format(new_label)

    result = value.format_map({format_key: new_label})
    return result


def resolve_suffix_with_mapping_genders(
    category: str,
    data: Dict[str, GenderedLabel],
    callback: callable,
    fix_result_callable: callable = None,
    format_key: str = "",
) -> str:
    """Resolves a category label by finding a matching suffix with gender-specific translations.

    This function iterates through a mapping of suffixes to gendered labels. If a category
    ends with a known suffix, it determines the correct gendered form (male or female)
    based on the presence of 'womens' in the category string. It then recursively calls
    a callback function on the remainder of the category string and combines the results.

    Args:
        category: The input category string to translate.
        data: A dictionary mapping English suffixes to `GenderedLabel` objects.
        callback: A callable that will be used to translate the base category string
            after a suffix is stripped.
        fix_result_callable: An optional callable to apply final fixes to the result.
        format_key: A format string for combining the gendered value and the new label.

    Returns:
        The translated category label, or the result of the callback on the original
        category if no suffix matches.
    """
    logger.debug(f"<<yellow>> start: {category=}")

    result = ""

    # category = normalize_text(category)
    for key, value in data.items():
        gender_value = value["females"] if "womens" in category else value["males"]
        if category.endswith(key):
            new_category = category[: -len(key)].strip()
            new_label = callback(new_category)
            if new_label:
                result = combine_value_and_label(gender_value, new_label, format_key)
                if fix_result_callable:
                    result = fix_result_callable(result, category, key, gender_value)
            break

    if not result:
        result = callback(category)

    logger.info(f"<<yellow>> end: {category=}, {result=}")
    return result


def resolve_sport_category_suffix_with_mapping(
    category: str,
    data: dict[str, str],
    callback: callable,
    fix_result_callable: callable = None,
    format_key: str = "",
) -> str:
    """."""
    logger.debug(f"<<yellow>> start: {category=}")

    result = ""
    key = ""
    # category = normalize_text(category)
    for key, value in data.items():
        if category.endswith(key):
            new_category = category[: -len(key)].strip()
            new_label = callback(new_category)
            if new_label:
                result = combine_value_and_label(value, new_label, format_key)
                if fix_result_callable:
                    result = fix_result_callable(result, category, key, value)
            break

    if not result:
        result = callback(category)

    logger.info(f"<<yellow>> end resolve_sport_category_suffix_with_mapping({key=}), {category=}, {result=})")
    return result


__all__ = [
    "resolve_sport_category_suffix_with_mapping",
]
