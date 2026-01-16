#!/usr/bin/python3
"""Resolve media-related categories to their Arabic labels."""

import functools
import re

from ..helps import logger
from ..new.resolve_films_bots import get_films_key_tyty_new, get_films_key_tyty_new_and_time
from ..new.resolve_films_bots.film_keys_bot import Films, get_Films_key_CAO
from ..new_resolvers.reslove_all import new_resolvers_all
from ..new_resolvers.resolve_languages import resolve_languages_labels
from ..translations import People_key
from .matables_bots.bot import add_to_Films_O_TT, add_to_new_players

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
        "get_Films_key_CAO": lambda k: get_Films_key_CAO(k),
        "get_films_key_tyty_new_and_time": lambda k: get_films_key_tyty_new_and_time(k),
        "get_films_key_tyty_new": lambda k: get_films_key_tyty_new(k),
        "Films": lambda k: Films(k),
        # TODO: get_pop_All_18 make some issues, see: tests/test_bug/test_bug_bad_data.py
        # "get_pop_All_18": lambda k: get_pop_All_18(k),
        "resolve_languages_labels": lambda k: resolve_languages_labels(k),
        "People_key": lambda k: People_key.get(k),
    }
    _add_to_new_players_tables = [
        "resolve_languages_labels",
        # "get_pop_All_18",
    ]

    _add_to_films_o_tt_tables = [
        "ethnic_label_main",
        "Films",
    ]

    for name, source in sources.items():
        resolved_label = source(normalized_category)
        if not resolved_label:
            continue
        if name in _add_to_new_players_tables:
            add_to_new_players(normalized_category, resolved_label)

        if name in _add_to_films_o_tt_tables:
            add_to_Films_O_TT(normalized_category, resolved_label)

        logger.info(f">>>> (te_films) {name}, {normalized_category=}, {resolved_label=}")
        return resolved_label

    return ""
