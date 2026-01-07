#!/usr/bin/python3
"""Resolve media-related categories to their Arabic labels."""

import functools
import re

# from ...helps.jsonl_dump import dump_data
from ..helps import logger
from ..make_bots.languages_bot.langs_w import Lang_work
from ..new.resolve_films_bots.film_keys_bot import get_Films_key_CAO, Films
from ..new.resolve_films_bots import get_films_key_tyty_new, get_films_key_tyty_new_and_time
from ..new_resolvers.countries_names_resolvers import resolve_countries_names_main
from ..new_resolvers.jobs_resolvers import resolve_jobs_main
from ..new_resolvers.nationalities_resolvers import resolve_nationalities_main
from ..new_resolvers.nationalities_resolvers.ministers_resolver import resolve_secretaries_labels
from ..new_resolvers.sports_resolvers import resolve_sports_main
# from ..new_resolvers.translations_resolvers_v3i import resolve_v3i_main
from .countries_formats import resolved_countries_formats_labels
from ..old_bots.t4_2018_jobs import te4_2018_Jobs
from ..old_bots.bot_te_4 import jobs_in_multi_sports
from ..old_bots.bot_te_4_nat import nat_match
from .languages_bot.languages_resolvers import te_language
# from .lazy_data_bots.bot_2018 import get_pop_All_18
from .matables_bots.bot import add_to_Films_O_TT, add_to_new_players
from ..make_bots.languages_bot.resolve_languages_new import resolve_languages_labels


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

    # TODO: move it to last position
    resolved_label = resolve_secretaries_labels(normalized_category)
    if resolved_label:
        logger.info(f">>>> (te_films) resolve_secretaries_labels, {normalized_category=}, {resolved_label=}")
        return resolved_label

    sources = {
        "get_Films_key_CAO": lambda k: get_Films_key_CAO(k),
        "get_films_key_tyty_new_and_time": lambda k: get_films_key_tyty_new_and_time(k),
        "get_films_key_tyty_new": lambda k: get_films_key_tyty_new(k),
        "jobs_in_multi_sports": lambda k: jobs_in_multi_sports(k),
        "Films": lambda k: Films(k),
        # TODO: get_pop_All_18 make some issues, see: tests/test_bug/test_bug_bad_data.py
        # "get_pop_All_18": lambda k: get_pop_All_18(k),
        "Lang_work": lambda k: Lang_work(k),
        "resolve_languages_labels": lambda k: resolve_languages_labels(k),
        "te4_2018_Jobs": lambda k: te4_2018_Jobs(k),
        "nat_match": lambda k: nat_match(k),
        # NOTE: resolve_nationalities_main must be before resolve_countries_names_main to avoid conflicts like:
        # resolve_countries_names_main> [Italy political leader]:  "قادة إيطاليا السياسيون"
        # resolve_nationalities_main> [Italy political leader]:  "قادة سياسيون إيطاليون"
        "resolve_sports_main": lambda k: resolve_sports_main(k),
        "resolve_nationalities_main": lambda k: resolve_nationalities_main(k),
        "resolved_countries_formats_labels": lambda k: resolved_countries_formats_labels(k),
        "resolve_countries_names_main": lambda k: resolve_countries_names_main(k),
        "resolve_jobs_main": lambda k: resolve_jobs_main(k),
        # "resolve_v3i_main": lambda k: resolve_v3i_main(k),
        "te_language": lambda k: te_language(k),
    }
    _add_to_new_players_tables = [
        "jobs_in_multi_sports",
        "resolve_languages_labels",
        "te4_2018_Jobs",
        # "get_pop_All_18",
    ]

    _add_to_films_o_tt_tables = [
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

    # most likely due to a circular import
    # resolved_label = resolve_v3i_main(normalized_category)
    # if resolved_label:
    #     logger.info(f'>>>> (te_films) resolve_v3i_main, {normalized_category=}, {resolved_label=}')
    #     return resolved_label

    return ""
