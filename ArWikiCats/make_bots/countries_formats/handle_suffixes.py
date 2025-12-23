#!/usr/bin/python3
"""
"""
from ...helps import logger


def normalize_text(text):
    text = text.lower().replace("category:", "")
    # text = text.replace("sportspeople", "sports-people")
    text = text.replace(" the ", " ")
    # text = text.replace("republic of", "republic-of")
    if text.startswith("the "):
        text = text[4:]
    return text.strip()


def resolve_sport_category_suffix_with_mapping(category: str, data: dict[str, str], callback: callable) -> str:
    """."""
    logger.debug(f"<<yellow>> start resolve_sport_category_suffix_with_mapping: {category=}")

    result = ""

    # category = normalize_text(category)
    for key, value in data.items():
        if category.endswith(key):
            new_category = category[: -len(key)].strip()
            new_label = callback(new_category)
            if new_label:
                result = f"{value} {new_label}"
            break
    if not result:
        result = callback(category)
    logger.debug(f"<<yellow>> end resolve_sport_category_suffix_with_mapping: {category=}, {result=}")
    return result


__all__ = [
    "resolve_sport_category_suffix_with_mapping",
]
