#!/usr/bin/python3
"""
!
"""

import functools
import re

from ...fix import fixtitle
from ...helps.log import logger
from ...main_processers import event2bot
from ...translations import Ambassadors_tab, New_P17_Finall
from ..jobs_bots.bot_te_4 import Jobs_in_Multi_Sports
from ..jobs_bots.te4_bots.t4_2018_jobs import te4_2018_Jobs
from ..lazy_data_bots.bot_2018 import get_pop_All_18
from ..matables_bots.bot import New_Lan
from ..matables_bots.centries_bot import centries_years_dec
from ..media_bots.films_bot import te_films
from ..o_bots import univer
from ..o_bots.popl import work_peoples

# from ..bots import tmp_bot
from ..p17_bots import nats
from ..p17_bots.us_stat import Work_US_State
from ..sports_bots import team_work
from . import ye_ts_bot

en_literes = "[abcdefghijklmnopqrstuvwxyz]"


def te_bot_3(category_key: str) -> str:
    """Return cached category labels when available in ``New_Lan``."""
    arabic_label = ""

    if category_key.lower() in New_Lan:
        logger.info("<<lightblue>>>> vvvvvvvvvvvv te_bot_3 start vvvvvvvvvvvv ")
        existing_label = New_Lan[category_key.lower()]
        logger.info(f'<<lightyellow>>>>>>  {category_key}", labs :"{existing_label}"')
        if existing_label is not None:
            if re.sub(en_literes, "", existing_label, flags=re.IGNORECASE) == existing_label:
                normalized_label = f"تصنيف:{fixtitle.fixlab(existing_label, en=category_key)}"
                logger.info(f'>>>>>> <<lightyellow>> te_bot_3: cat:"{category_key}", labs:"{normalized_label}"')
                logger.info("<<lightblue>>>> ^^^^^^^^^ te_bot_3 end ^^^^^^^^^ ")
                return normalized_label
    return arabic_label


@functools.lru_cache(maxsize=None)
def event_Lab_seoo(reference_category: str, target_category: str) -> str:
    """Retrieve category lab information based on the provided category.

    This function attempts to find the corresponding category lab for a
    given category string by checking multiple sources in a specific order.
    It first normalizes the input category string and then queries various
    data sources to retrieve the relevant information. If no match is found,
    it attempts to find a wikidata entry based on the category string.

    Args:
        reference_category (str): A reference category string used in some lookups.
        target_category (str): The category string for which the lab information is sought.

    Returns:
        str: The corresponding category lab information or an empty string if not
            found.
    """

    normalized_target_category = target_category.lower().strip()

    logger.info("<<lightblue>>>>event_Lab_seoo vvvvvvvvvvvv event_Lab_seoo start vvvvvvvvvvvv ")
    logger.info(f'<<lightyellow>>>>>> event_Lab_seoo, normalized_target_category:"{normalized_target_category}"')

    resolved_category_label = New_P17_Finall.get(normalized_target_category, "")

    if not resolved_category_label:
        resolved_category_label = Ambassadors_tab.get(normalized_target_category, "")

    if not resolved_category_label:
        resolved_category_label = team_work.Get_team_work_Club(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = event2bot.event2(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = get_pop_All_18(normalized_target_category, "")

    if not resolved_category_label:
        resolved_category_label = centries_years_dec.get(normalized_target_category, "")

    if not resolved_category_label:
        resolved_category_label = te4_2018_Jobs(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = Jobs_in_Multi_Sports(normalized_target_category)

    # if not category_lab:
    #     category_lab = tmp_bot.Work_Templates(category3)

    if not resolved_category_label:
        resolved_category_label = univer.te_universities(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = te_films(normalized_target_category, reference_category=reference_category)

    if not resolved_category_label:
        resolved_category_label = nats.find_nat_others(normalized_target_category, reference_category=reference_category)

    if not resolved_category_label:
        # print("translate_general_category 12")
        resolved_category_label = ye_ts_bot.translate_general_category(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = Work_US_State(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = work_peoples(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = te_bot_3(normalized_target_category)

    # print(f"{resolved_category_label=}")

    return resolved_category_label
