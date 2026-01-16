#!/usr/bin/python3
"""Resolve media-related categories to their Arabic labels."""

import functools
import re

from ..helps import logger
from ..new.resolve_films_bots import resolve_films_main
from ..new_resolvers.reslove_all import new_resolvers_all

# from .bot_2018 import get_pop_All_18


def legacy_label_check(normalized_category):
    label = ""
    if re.match(r"^\d+$", normalized_category.strip()):
        label = normalized_category.strip()

    if normalized_category == "people":
        label = "أشخاص"
    return label


@functools.lru_cache(maxsize=None)
def te_films(category: str) -> str:
    """
    Resolve a media category into its Arabic label using multiple layered resolvers.

    """
    normalized_category = category.lower()
    label = (
        legacy_label_check(normalized_category)
        or new_resolvers_all(normalized_category)
        or resolve_films_main(normalized_category)
    )
    return label
