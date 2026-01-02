#!/usr/bin/python3
"""Resolve media-related categories to their Arabic labels."""

import functools
import re


# from ...helps.jsonl_dump import dump_data
from ..helps.log import logger
from .countries_formats import resolved_countries_formats_labels
from .countries_formats.t4_2018_jobs import te4_2018_Jobs
from .jobs_bots.bot_te_4 import Jobs_in_Multi_Sports, nat_match, te_2018_with_nat
from .matables_bots.bot import add_to_Films_O_TT, add_to_new_players

from ..new_resolvers.nationalities_resolvers.ministers_resolver import resolve_secretaries_labels
from ..new_resolvers.nationalities_resolvers import resolve_nationalities_main
from ..new_resolvers.sports_resolvers import resolve_sports_main

from ..new_resolvers.countries_names_resolvers import resolve_countries_names_main
from ..new_resolvers.jobs_resolvers import resolve_jobs_main
from ..new_resolvers.translations_resolvers_v3i import resolve_v3i_main
from .languages_bot.languages_resolvers import te_language
from .lazy_data_bots.bot_2018 import get_pop_All_18

from ..new.resolve_films_bots.film_keys_bot import get_Films_key_CAO, resolve_films
from ..new.resolve_films_bots.resolve_films_labels import get_films_key_tyty_new


@functools.lru_cache(maxsize=None)
def te_films(category: str) -> str:
    """
    Resolve a media category into an Arabic label using layered fallbacks.

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
        "get_films_key_tyty_new": lambda k: get_films_key_tyty_new(k),
        "Jobs_in_Multi_Sports": lambda k: Jobs_in_Multi_Sports(k),
        "te_2018_with_nat": lambda k: te_2018_with_nat(k),
        "resolve_films": lambda k: resolve_films(k),
        # TODO: get_pop_All_18 make some issues, see: tests/test_bug/test_bug_bad_data.py
        # "get_pop_All_18": lambda k: get_pop_All_18(k),
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
        "Jobs_in_Multi_Sports",
        "te4_2018_Jobs",
        # "get_pop_All_18",
    ]

    _add_to_films_o_tt_tables = [
        "te_2018_with_nat",
        "resolve_films",
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
