#!/usr/bin/python3
"""Resolve media-related categories to their Arabic labels."""

import functools
import re

from ..helps import logger
from ..new.resolve_films_bots import resolve_films_main
from ..new_resolvers.reslove_all import new_resolvers_all

# from .bot_2018 import get_pop_All_18


@functools.lru_cache(maxsize=None)
def te_films(category: str) -> str:
    """
    Resolve a media category into its Arabic label using multiple layered resolvers.

    Parameters:
        category (str): The media category to resolve; input is normalized before lookup. If the category consists only of digits, the trimmed numeric string is returned.

    Returns:
        str: The resolved Arabic label when a resolver matches, or an empty string if unresolved.

    Notes:
        - When a resolver matches, the function may invoke side-effect hooks to update auxiliary tables (e.g., add_to_new_players or add_to_Films_O_TT) depending on which resolver produced the result.
    TODO: many funcs used here
    """
    normalized_category = category.lower()

    if re.match(r"^\d+$", normalized_category.strip()):
        return normalized_category.strip()

    if normalized_category == "people":
        return "أشخاص"

    # TODO: move it to last position
    resolved_label = new_resolvers_all(normalized_category)
    if resolved_label:
        logger.info(f">>>> (te_films) new_resolvers_all, {normalized_category=}, {resolved_label=}")
        return resolved_label

    sources = {
        "resolve_films_main": lambda k: resolve_films_main(k),
    }
    for name, source in sources.items():
        resolved_label = source(normalized_category)
        if not resolved_label:
            continue
        logger.info(f">>>> (te_films) {name}, {normalized_category=}, {resolved_label=}")
        return resolved_label

    return ""
