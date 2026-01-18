#!/usr/bin/python3
"""
Event label processing bot.

This module provides functionality for processing event-related categories
and translating them to Arabic labels.
"""

import functools

from ...helps import logger
from ...new_resolvers import all_new_resolvers
from ...new_resolvers.languages_resolves import resolve_languages_labels_with_time
from ...time_formats.time_to_arabic import convert_time_to_arabic
from ...translations import Ambassadors_tab, People_key, get_from_new_p17_final
from .. import team_work, with_years_bot
from ..ma_bots2 import year_or_typeo
from ..make_bots.bot_2018 import get_pop_All_18
from ..o_bots import university_resolver
from ..o_bots.peoples_resolver import work_peoples
from . import general_resolver
from .country_bot import event2_d2


@functools.lru_cache(maxsize=None)
def event_label_work(target_category: str) -> str:
    """
    Resolve an Arabic label for an event-related category.
    
    The function normalizes the input and consults a fixed sequence of resolvers, returning the first non-empty label found. If the normalized category is "people", returns "أشخاص". If no resolver produces a label, returns an empty string.
    
    Parameters:
        target_category (str): Category string to resolve.
    
    Returns:
        str: The resolved Arabic label for the category, or an empty string if unresolved.
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