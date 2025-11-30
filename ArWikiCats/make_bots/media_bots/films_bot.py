#!/usr/bin/python3
"""Resolve media-related categories to their Arabic labels."""

import functools
import re

# from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ..countries_formats import resolved_countries_formats_labels  # , p17_bot, p17_bot_2, p17_bot_sport
from ..countries_formats.t4_2018_jobs import te4_2018_Jobs
from ..jobs_bots.bot_te_4 import Jobs_in_Multi_Sports, nat_match, te_2018_with_nat
from ..matables_bots.bot import add_to_Films_O_TT, add_to_new_players
from ..media_bots.film_keys_bot import get_Films_key_CAO
from ..o_bots import fax
from ..o_bots.army import te_army
from ...translations_resolvers import resolved_sports_formats_labels


@functools.lru_cache(maxsize=None)
def te_films(category: str) -> str:
    """
    Resolve a media category into an Arabic label using layered fallbacks.

    TODO: many funcs used here
    """
    normalized_category = category.lower()
    logger.info(f"<<lightblue>>>> xxxxxxxxxx te_films normalized_category:{normalized_category} xxxxxxxxxxx ")
    resolved_label = ""

    if re.match(r"^\d+$", normalized_category.strip()):
        resolved_label = normalized_category.strip()

    if not resolved_label:
        resolved_label = get_Films_key_CAO(normalized_category)

    if not resolved_label:
        resolved_label = Jobs_in_Multi_Sports(normalized_category)
        if resolved_label:
            add_to_new_players(normalized_category, resolved_label)
            logger.debug(f'>>>> Jobs_in_Multi Sports: add_to_new_players[{normalized_category}] ="{resolved_label}"')

    if not resolved_label:
        resolved_label = te_2018_with_nat(normalized_category)
        if resolved_label:
            add_to_Films_O_TT(normalized_category, resolved_label)

    if not resolved_label:
        resolved_label = te4_2018_Jobs(normalized_category)
        if resolved_label:
            add_to_new_players(normalized_category, resolved_label)
            logger.debug(f'>>>> bot_te_4 2018 Jobs: add_to_new_players[{normalized_category}] ="{resolved_label}"')

    if not resolved_label:
        resolved_label = nat_match(normalized_category)
        if resolved_label:
            logger.debug(f'>>>> nat_match: [{normalized_category}] ="{resolved_label}"')

    if not resolved_label:
        resolved_label = resolved_countries_formats_labels(normalized_category)

    if not resolved_label:
        resolved_label = resolved_sports_formats_labels(normalized_category)

    if not resolved_label:
        resolved_label = fax.te_language(normalized_category)

    if not resolved_label:
        resolved_label = te_army(normalized_category)

    if not resolved_label:
        resolved_label = te4_2018_Jobs(normalized_category)

    logger.info(f"<<lightblue>>>> xxxxxxxxx te_films end xxxxxxxxxxx resolved_label:{resolved_label}")
    return resolved_label
