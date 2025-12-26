#!/usr/bin/python3
"""
"""
from ..helps import logger


def normalize_text(text: str) -> str:
    text = text.lower().replace("category:", "")
    # text = text.replace("sportspeople", "sports-people")
    text = text.replace(" the ", " ")
    # text = text.replace("republic of", "republic-of")
    if text.startswith("the "):
        text = text[4:]
    return text.strip()


def combine_value_and_label(
    value: str,
    new_label: str,
    format_key: str="",
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
    data: dict[str, str],
    callback: callable,
    fix_result_callable: callable = None,
    format_key: str = "",
) -> str:
    """."""
    logger.debug(f"<<yellow>> start resolve_suffix_with_mapping_genders: {category=}")

    result = ""

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

    logger.debug(f"<<yellow>> end resolve_suffix_with_mapping_genders: {category=}, {result=}")
    return result


def resolve_sport_category_suffix_with_mapping(
    category: str,
    data: dict[str, str],
    callback: callable,
    fix_result_callable: callable = None,
    format_key: str = "",
) -> str:
    """."""
    logger.debug(f"<<yellow>> start resolve_sport_category_suffix_with_mapping: {category=}")

    result = ""

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

    logger.debug(f"<<yellow>> end resolve_sport_category_suffix_with_mapping: {category=}, {result=}")
    return result


__all__ = [
    "resolve_sport_category_suffix_with_mapping",
]
