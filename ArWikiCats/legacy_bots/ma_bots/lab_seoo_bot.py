#!/usr/bin/python3
"""
Event label processing bot.

This module provides functionality for processing event-related categories
and translating them to Arabic labels.
"""

import functools

from ...new_resolvers.sports_resolvers.legacy_sports_bots import team_work

from ...helps import logger
from ...new_resolvers import all_new_resolvers
from ...new_resolvers.languages_resolves import resolve_languages_labels_with_time
from ...time_formats.time_to_arabic import convert_time_to_arabic
from ...translations import Ambassadors_tab, People_key, get_from_new_p17_final
from .. import with_years_bot
from ..ma_bots2 import year_or_typeo
from ..make_bots.bot_2018 import get_pop_All_18
from ..o_bots import university_resolver
from ...new_resolvers.other_resolvers.peoples_resolver import work_peoples
from . import general_resolver
from .country_bot import event2_d2


@functools.lru_cache(maxsize=None)
def event_label_work(target_category: str) -> str:
    """Retrieve category lab information based on the provided category.

    This function attempts to find the corresponding category lab for a
    given category string by checking multiple sources in a specific order.
    It first normalizes the input category string and then queries various
    data sources to retrieve the relevant information. If no match is found,
    it attempts to find a wikidata entry based on the category string.

    Args:
        target_category (str): The category string for which the lab information is sought.

    Returns:
        str: The corresponding category lab information or an empty string if not
            found.
    """

    normalized_target_category = target_category.lower().strip()

    if normalized_target_category == "people":
        return "أشخاص"

    logger.info("<<lightblue>>>> vvvvvvvvvvvv event_label_work start vvvvvvvvvvvv ")
    logger.info(f"<<lightyellow>>>>>> {normalized_target_category=}")

    resolved_category_label = (
        get_from_new_p17_final(normalized_target_category, "")
        or Ambassadors_tab.get(normalized_target_category, "")
        or team_work.Get_team_work_Club(normalized_target_category)
        or university_resolver.resolve_university_category(normalized_target_category)
        or event2_d2(normalized_target_category)
        or with_years_bot.wrap_try_with_years(normalized_target_category)
        or year_or_typeo.label_for_startwith_year_or_typeo(normalized_target_category)
        or get_pop_All_18(normalized_target_category, "")
        or convert_time_to_arabic(normalized_target_category)
        or all_new_resolvers(normalized_target_category)
        or resolve_languages_labels_with_time(normalized_target_category)
        or People_key.get(normalized_target_category)
        or general_resolver.translate_general_category(normalized_target_category)
        or work_peoples(normalized_target_category)
        or ""
    )

    return resolved_category_label
