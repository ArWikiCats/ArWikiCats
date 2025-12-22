#!/usr/bin/python3
"""
!
"""

import functools
import re

from ..fix import fixtitle
from ..helps.log import logger
from ..main_processers import event2bot
from ..translations import Ambassadors_tab, get_from_new_p17_final
from ..make_bots.countries_formats.t4_2018_jobs import te4_2018_Jobs
from ..make_bots.jobs_bots.bot_te_4 import Jobs_in_Multi_Sports
from ..make_bots.lazy_data_bots.bot_2018 import get_pop_All_18
from ..make_bots.matables_bots.bot import New_Lan
from ..make_bots.media_bots.films_bot import te_films
from ..make_bots.o_bots import univer
from ..make_bots.o_bots.peoples_resolver import work_peoples

from ..translations.sports_formats_national.sport_lab_nat import sport_lab_nat_load_new
from ..time_resolvers.time_to_arabic import convert_time_to_arabic
# from ..bots import tmp_bot
from ..new_resolvers.translations_resolvers.us_states import resolve_us_states
from ..make_bots.sports_bots import team_work
from . import ye_ts_bot

en_literes = "[abcdefghijklmnopqrstuvwxyz]"


def te_bot_3(category_key: str) -> str:
    """Return cached category labels when available in ``New_Lan``."""
    arabic_label = New_Lan.get(category_key.lower(), "")

    if arabic_label:
        logger.info("<<lightblue>>>> vvvvvvvvvvvv te_bot_3 start vvvvvvvvvvvv ")
        logger.info(f'<<lightyellow>>>>>>  {category_key}", labs :"{arabic_label}"')
        if re.sub(en_literes, "", arabic_label, flags=re.IGNORECASE) == arabic_label:
            normalized_label = f"تصنيف:{fixtitle.fixlabel(arabic_label, en=category_key)}"
            logger.info(f'>>>>>> <<lightyellow>> te_bot_3: cat:"{category_key}", labs:"{normalized_label}"')
            logger.info("<<lightblue>>>> ^^^^^^^^^ te_bot_3 end ^^^^^^^^^ ")
            return normalized_label
    return ""


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

    logger.info("<<lightblue>>>> vvvvvvvvvvvv event_label_work start vvvvvvvvvvvv ")
    logger.info(f'<<lightyellow>>>>>> {normalized_target_category=}')

    resolved_category_label = get_from_new_p17_final(normalized_target_category, "")

    if not resolved_category_label:
        resolved_category_label = Ambassadors_tab.get(normalized_target_category, "")

    if not resolved_category_label:
        resolved_category_label = team_work.Get_team_work_Club(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = event2bot.event2_new(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = get_pop_All_18(normalized_target_category, "")

    if not resolved_category_label:
        resolved_category_label = convert_time_to_arabic(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = te4_2018_Jobs(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = Jobs_in_Multi_Sports(normalized_target_category)

    # if not category_lab:
    #     category_lab = tmp_bot.Work_Templates(category3)

    if not resolved_category_label:
        resolved_category_label = univer.te_universities(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = te_films(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = sport_lab_nat_load_new(normalized_target_category)

    if not resolved_category_label:
        # print("translate_general_category 12")
        resolved_category_label = ye_ts_bot.translate_general_category(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = resolve_us_states(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = work_peoples(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = te_bot_3(normalized_target_category)

    # print(f"{resolved_category_label=}")

    return resolved_category_label


@functools.lru_cache(maxsize=None)
def event_Lab_seoo(reference_category: str, target_category: str) -> str:
    return event_label_work(target_category)
