#!/usr/bin/python3
"""Resolve media-related categories to their Arabic labels."""

import functools
import re


# from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ..countries_formats import resolved_countries_formats_labels
from ..countries_formats.t4_2018_jobs import te4_2018_Jobs
from ..jobs_bots.bot_te_4 import Jobs_in_Multi_Sports, nat_match, te_2018_with_nat
from ..matables_bots.bot import add_to_Films_O_TT, add_to_new_players

from ...new_resolvers.nationalities_resolvers.ministers_resolver import resolve_secretaries_labels
from ...new_resolvers.nationalities_resolvers import resolve_nationalities_main

from ...new_resolvers.countries_names_resolvers import resolve_countries_names_main
from ...new_resolvers.jobs_resolvers import resolve_jobs_main
from ...new_resolvers.translations_resolvers_v3i import resolve_v3i_main
from .film_keys_bot import resolve_films

from ..media_bots.film_keys_bot import get_Films_key_CAO
from ..media_bots.tyty_new_format import get_films_key_tyty_new
from ...make_bots.languages_bot.languages_resolvers import te_language
from ...make_bots.lazy_data_bots.bot_2018 import get_pop_All_18


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
        logger.info(f'>>>> (te_films) resolve_secretaries_labels, {normalized_category=}, {resolved_label=}')
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

        # NOTE: resolved_translations_resolvers_v2 must be before resolved_translations_resolvers to avoid conflicts like:
        # resolved_translations_resolvers> [Italy political leader]:  "قادة إيطاليا السياسيون"
        # resolved_translations_resolvers_v2> [Italy political leader]:  "قادة سياسيون إيطاليون"

        "resolved_translations_resolvers_v2": lambda k: resolve_nationalities_main(k),
        "resolved_countries_formats_labels": lambda k: resolved_countries_formats_labels(k),
        "resolved_translations_resolvers": lambda k: resolve_countries_names_main(k),
        "new_jobs_resolver_label": lambda k: resolve_jobs_main(k),
        # "resolved_translations_resolvers_v3i": lambda k: resolved_translations_resolvers_v3i(k),
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

        logger.info(f'>>>> (te_films) {name}, {normalized_category=}, {resolved_label=}')
        return resolved_label

    # most likely due to a circular import
    # resolved_label = resolved_translations_resolvers_v3i(normalized_category)
    # if resolved_label:
    #     logger.info(f'>>>> (te_films) resolved_translations_resolvers_v3i, {normalized_category=}, {resolved_label=}')
    #     return resolved_label

    return ""
