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
from ..o_bots import fax
from ...new_resolvers.translations_resolvers_v2.ministers_resolver import resolve_secretaries_labels
from ...new_resolvers.translations_resolvers import resolved_translations_resolvers
from ...new_resolvers.new_jobs_resolver import new_jobs_resolver_label
# from ...translations_resolvers_v3i import resolved_translations_resolvers_v3i
from ...new_resolvers.translations_resolvers_v2 import resolved_translations_resolvers_v2
from .film_keys_bot import resolve_films

from ..media_bots.film_keys_bot import get_Films_key_CAO
from ..media_bots.tyty_new_format import get_films_key_tyty_new


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

    resolved_label = get_Films_key_CAO(normalized_category)
    if resolved_label:
        logger.info(f'>>>> (te_films) get_Films_key_CAO, {normalized_category=}, {resolved_label=}')
        return resolved_label

    resolved_label = get_films_key_tyty_new(normalized_category)
    if resolved_label:
        logger.info(f'>>>> (te_films) get_films_key_tyty_new, {normalized_category=}, {resolved_label=}')
        return resolved_label

    resolved_label = Jobs_in_Multi_Sports(normalized_category)
    if resolved_label:
        add_to_new_players(normalized_category, resolved_label)
        logger.info(f'>>>> (te_films) Jobs_in_Multi_Sports, {normalized_category=}, {resolved_label=}')
        return resolved_label

    resolved_label = te_2018_with_nat(normalized_category)
    if resolved_label:
        add_to_Films_O_TT(normalized_category, resolved_label)
        logger.info(f'>>>> (te_films) te_2018_with_nat, {normalized_category=}, {resolved_label=}')
        return resolved_label

    resolved_label = resolve_films(normalized_category)
    if resolved_label:
        add_to_Films_O_TT(normalized_category, resolved_label)
        logger.info(f'>>>> (te_films) resolve_films, {normalized_category=}, {resolved_label=}')
        return resolved_label

    resolved_label = te4_2018_Jobs(normalized_category)
    if resolved_label:
        add_to_new_players(normalized_category, resolved_label)
        logger.info(f'>>>> (te_films) te4_2018_Jobs, {normalized_category=}, {resolved_label=}')
        return resolved_label

    resolved_label = nat_match(normalized_category)
    if resolved_label:
        logger.info(f'>>>> (te_films) nat_match, {normalized_category=}, {resolved_label=}')
        return resolved_label

    resolved_label = resolved_countries_formats_labels(normalized_category)
    if resolved_label:
        logger.info(f'>>>> (te_films) resolved_countries_formats_labels, {normalized_category=}, {resolved_label=}')
        return resolved_label

    resolved_label = resolved_translations_resolvers(normalized_category)
    if resolved_label:
        logger.info(f'>>>> (te_films) resolved_sports_formats_labels, {normalized_category=}, {resolved_label=}')
        return resolved_label

    resolved_label = new_jobs_resolver_label(normalized_category)
    if resolved_label:
        logger.info(f'>>>> (te_films) new_jobs_resolver_label, {normalized_category=}, {resolved_label=}')
        return resolved_label

    # most likely due to a circular import
    # resolved_label = resolved_translations_resolvers_v3i(normalized_category)
    # if resolved_label:
    #     logger.info(f'>>>> (te_films) resolved_translations_resolvers_v3i, {normalized_category=}, {resolved_label=}')
    #     return resolved_label

    resolved_label = resolved_translations_resolvers_v2(normalized_category)
    if resolved_label:
        logger.info(f'>>>> (te_films) resolved_translations_resolvers_v2, {normalized_category=}, {resolved_label=}')
        return resolved_label

    resolved_label = fax.te_language(normalized_category)
    if resolved_label:
        logger.info(f'>>>> (te_films) te_language, {normalized_category=}, {resolved_label=}')
        return resolved_label

    return ""
