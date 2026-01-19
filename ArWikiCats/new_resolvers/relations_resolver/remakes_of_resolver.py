#!/usr/bin/python3
""" """

import functools

from ...helps import logger
from ...translations import All_Nat
from ...translations_formats import format_multi_data_v2


def fix_keys(category: str) -> str:
    """Fix known issues in category keys before searching.

    Args:
        category: The original category key.
    """
    # Fix specific known issues with category keys
    category = category.lower().replace("category:", "")
    category = category.replace("'", "")
    return category.strip()


@functools.lru_cache(maxsize=10000)
def resolve_remakes_of_resolver(category: str) -> str:
    category = fix_keys(category)
    logger.debug(f"<<yellow>> start resolve_remakes_of_resolver: {category=}")

    return ""


__all__ = [
    "resolve_remakes_of_resolver",
]
