#!/usr/bin/python3
"""
from  make.make2_bots.ma_bots.lab_seoo_bot import event_Lab_seoo

"""
import re
from ...fix import fixtitle

from ..p17_bots.us_stat import Work_US_State
from ..o_bots.popl import Work_peoples

# from ..bots import tmp_bot
from ..p17_bots import nats
from ..o_bots import univer
from ..sports_bots import team_work
from ..jobs_bots.test_4 import Jobs_in_Multi_Sports
from ..jobs_bots.test4_bots.t4_2018_jobs import test4_2018_Jobs

# ---
from . import ye_ts_bot
from ..media_bots.films_bot import test_films
from . import event2bot
from ...ma_lists import New_P17_Finall
from ...ma_lists import Ambassadors_tab
from ..fromnet.wd_bot import find_wikidata
from ..matables_bots.bot_2018 import pop_All_2018
from ..matables_bots.centries_bot import centries_years_dec
from ..matables_bots.bot import New_Lan
from ...helps.print_bot import print_put, main_output_enabled

en_literes = "[abcdefghijklmnopqrstuvwxyz]"


def test3(category_r):
    arlabs = ""

    if category_r in New_Lan:
        print_put("<<lightblue>>>> vvvvvvvvvvvv test3 start vvvvvvvvvvvv ")
        labs = New_Lan[category_r]
        print_put(f'<<lightyellow>>>>>>  {category_r}", labs :"{labs}"')
        if labs is not None:
            if re.sub(en_literes, "", labs, flags=re.IGNORECASE) == labs:
                labs = f"تصنيف:{fixtitle.fixlab(labs, en=category_r)}"
                print_put(f'>>>>>> <<lightyellow>> test3: cat:"{category_r}", labs:"{labs}"')
                print_put("<<lightblue>>>> ^^^^^^^^^ test3 end ^^^^^^^^^ ")
                return labs
    return arlabs


def event_Lab_seoo(category_r, category3):
    """Retrieve category lab information based on the provided category.

    This function attempts to find the corresponding category lab for a
    given category string by checking multiple sources in a specific order.
    It first normalizes the input category string and then queries various
    data sources to retrieve the relevant information. If no match is found,
    it attempts to find a wikidata entry based on the category string.

    Args:
        category_r (str): A reference category string used in some lookups.
        category3 (str): The category string for which the lab information is sought.

    Returns:
        str: The corresponding category lab information or an empty string if not
            found.
    """

    category3_no_lower = category3.strip()
    category3 = category3.lower().strip()

    print_put("<<lightblue>>>>event_Lab_seoo vvvvvvvvvvvv event_Lab_seoo start vvvvvvvvvvvv ")
    print_put(f'<<lightyellow>>>>>> event_Lab_seoo, category3:"{category3}"')

    category_lab = ""

    if not category_lab:
        category_lab = New_P17_Finall.get(category3, "")

    if not category_lab:
        category_lab = Ambassadors_tab.get(category3, "")

    if not category_lab:
        category_lab = team_work.Get_team_work_Club(category3_no_lower)

    if not category_lab:
        category_lab = event2bot.event2(category3)
    if not category_lab:
        category_lab = pop_All_2018.get(category3.lower(), "")

    if not category_lab:
        category_lab = centries_years_dec.get(category3, "")

    if not category_lab:
        category_lab = test4_2018_Jobs(category3, out=main_output_enabled[1])

    if not category_lab:
        category_lab = Jobs_in_Multi_Sports(category3_no_lower, out=main_output_enabled[1])

    # if not category_lab:
    #     category_lab = tmp_bot.Work_Templates(category3)

    if not category_lab:
        category_lab = univer.test_Universities(category3)

    if not category_lab:
        category_lab = test_films(category3, fa=category_r)

    if not category_lab:
        category_lab = nats.find_nat_others(category3, fa=category_r)

    if not category_lab:
        # print("translate_general_category 12")
        category_lab = ye_ts_bot.translate_general_category(category3)

    if not category_lab:
        category_lab = Work_US_State(category3)

    if not category_lab:
        category_lab = Work_peoples(category3)

    if not category_lab:
        category_lab = test3(category3)

    if category_lab == "" and category3.strip().find(" ") == -1:
        category_lab = find_wikidata(category3)

    return category_lab
