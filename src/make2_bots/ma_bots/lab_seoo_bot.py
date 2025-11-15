#!/usr/bin/python3
"""
from  make.make2_bots.ma_bots.lab_seoo_bot import event_Lab_seoo

"""
import re

from ...fix import fixtitle
from ...helps.print_bot import print_put
from ...ma_lists import Ambassadors_tab, New_P17_Finall
from ..fromnet.wd_bot import find_wikidata
from ..jobs_bots.test4_bots.t4_2018_jobs import te4_2018_Jobs
from ..jobs_bots.bot_te_4 import Jobs_in_Multi_Sports
from ..matables_bots.bot import New_Lan
from ..lazy_data_bots.bot_2018 import get_pop_All_18
from ..matables_bots.centries_bot import centries_years_dec
from ..media_bots.films_bot import te_films
from ..o_bots import univer
from ..o_bots.popl import work_peoples

# from ..bots import tmp_bot
from ..p17_bots import nats
from ..p17_bots.us_stat import Work_US_State
from ..sports_bots import team_work

# ---
from . import event2bot, ye_ts_bot

en_literes = "[abcdefghijklmnopqrstuvwxyz]"


def te_bot_3(category_key: str) -> str:
    arabic_label = ""

    if category_key in New_Lan:
        print_put("<<lightblue>>>> vvvvvvvvvvvv te_bot_3 start vvvvvvvvvvvv ")
        existing_label = New_Lan[category_key]
        print_put(f'<<lightyellow>>>>>>  {category_key}", labs :"{existing_label}"')
        if existing_label is not None:
            if re.sub(en_literes, "", existing_label, flags=re.IGNORECASE) == existing_label:
                normalized_label = f"تصنيف:{fixtitle.fixlab(existing_label, en=category_key)}"
                print_put(f'>>>>>> <<lightyellow>> te_bot_3: cat:"{category_key}", labs:"{normalized_label}"')
                print_put("<<lightblue>>>> ^^^^^^^^^ te_bot_3 end ^^^^^^^^^ ")
                return normalized_label
    return arabic_label


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

    target_category_original_case = target_category.strip()
    normalized_target_category = target_category.lower().strip()

    print_put("<<lightblue>>>>event_Lab_seoo vvvvvvvvvvvv event_Lab_seoo start vvvvvvvvvvvv ")
    print_put(f'<<lightyellow>>>>>> event_Lab_seoo, normalized_target_category:"{normalized_target_category}"')

    resolved_category_label = ""

    if not resolved_category_label:
        resolved_category_label = New_P17_Finall.get(normalized_target_category, "")

    if not resolved_category_label:
        resolved_category_label = Ambassadors_tab.get(normalized_target_category, "")

    if not resolved_category_label:
        resolved_category_label = team_work.Get_team_work_Club(target_category_original_case)

    if not resolved_category_label:
        resolved_category_label = event2bot.event2(normalized_target_category)
    if not resolved_category_label:
        resolved_category_label = get_pop_All_18(normalized_target_category, "")

    if not resolved_category_label:
        resolved_category_label = centries_years_dec.get(normalized_target_category, "")

    if not resolved_category_label:
        resolved_category_label = te4_2018_Jobs(normalized_target_category)

    if not resolved_category_label:
        resolved_category_label = Jobs_in_Multi_Sports(target_category_original_case)

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

    if resolved_category_label == "" and " " not in normalized_target_category.strip():
        resolved_category_label = find_wikidata(normalized_target_category)

    return resolved_category_label
