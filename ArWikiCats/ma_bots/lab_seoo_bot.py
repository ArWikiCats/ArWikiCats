#!/usr/bin/python3
"""
!
"""

import functools
from ..helps import logger
from ..ma_bots2.year_or_typeo import bot_lab
from ..ma_bots.country_bot import event2_d2
from ..old_bots.films_and_others_bot import te_films
from ..make_bots.languages_bot.langs_w import Lang_work
from ..make_bots.languages_bot.resolve_languages_new import resolve_languages_labels
from ..make_bots.lazy_data_bots.bot_2018 import get_pop_All_18
from ..make_bots.o_bots import univer
from ..make_bots.o_bots.peoples_resolver import work_peoples
from ..make_bots.sports_bots import team_work

from ..new_resolvers.reslove_all import new_resolvers_all

from ..old_bots import with_years_bot
from ..time_resolvers.time_to_arabic import convert_time_to_arabic
from ..translations import Ambassadors_tab, People_key, get_from_new_p17_final
from . import ye_ts_bot


@functools.lru_cache(maxsize=None)
def event_label_work(target_category: str) -> str:
    """
    Resolve an Arabic label for a category key by consulting multiple resolver sources in priority order.
    
    The input is normalized (lowercased and trimmed); the special key "people" maps to "أشخاص". The function returns the first non-empty label found from a sequence of resolver modules, or an empty string when no resolver provides a label.
    
    Parameters:
        target_category (str): The category key to resolve (will be lowercased and stripped).
    
    Returns:
        str: The resolved Arabic label for the category, or an empty string if none is found.
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
        or univer.te_universities(normalized_target_category)
        or event2_d2(normalized_target_category)
        or with_years_bot.Try_With_Years2(normalized_target_category)
        or bot_lab.label_for_startwith_year_or_typeo(normalized_target_category)
        or get_pop_All_18(normalized_target_category, "")
        or convert_time_to_arabic(normalized_target_category)
        or new_resolvers_all(normalized_target_category)
        or Lang_work(normalized_target_category)
        or resolve_languages_labels(normalized_target_category)
        or People_key.get(normalized_target_category)
        or univer.te_universities(normalized_target_category)
        or te_films(normalized_target_category)
        or ye_ts_bot.translate_general_category(normalized_target_category)
        or work_peoples(normalized_target_category)
        or ""
    )

    return resolved_category_label