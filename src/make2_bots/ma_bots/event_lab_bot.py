"""
Usage:
from ..make2_bots.ma_bots import event_lab_bot
# category_lab = event_lab_bot.event_Lab(cate_r)

"""

import sys
import re

# from .. import printe

from . import fax2
from . import list_cat_format

from .. import malists_sport_lab as sport_lab

from ..helps.print_bot import print_put
from ..make2_bots.date_bots import year_lab
from ..make2_bots.o_bots import univer
from ..ma_lists import New_P17_Finall
from ..make2_bots.fromnet import kooora
from ..make2_bots.fromnet.wd_bot import find_wikidata
from ..make2_bots.format_bots import pp_ends_with, pp_ends_with_pase, change_cat
from ..fix import fixtitle
from ..make2_bots.matables_bots.bot_2018 import pop_All_2018
from ..make2_bots.bots import tmp_bot

from .lab_seoo_bot import event_Lab_seoo
from .contry2_bot import Get_contry2

# ImportError: cannot import name 'translate_general_category' from partially initialized module 'make2.make2_bots.ma_bots.ye_ts_bot'
#  (most likely due to a circular import) (make2_bots.ma_bots\ye_ts_bot.py)
from . import ye_ts_bot

en_literes = "[abcdefghijklmnopqrstuvwxyz]"
Find_f_wikidata = {1: "nowikidata" not in sys.argv}


def event_Lab(cate_r):
    category_lab = ""
    list_of_cat = ""
    cate_r2 = cate_r
    category = cate_r.lower()
    category = category.replace("_", " ")
    if not category.startswith("category:"):
        category = f"category:{category}"
    category = change_cat(category)

    category3_nolower = cate_r2
    if category3_nolower.startswith("Category:"):
        category3_nolower = category3_nolower.split("Category:")[1]

    category3 = category.lower()
    if category3.startswith("category:"):
        category3 = category3.split("category:")[1]

    orginal_category3 = category3
    # ---
    if not category_lab:
        category_lab = fax2.get_list_of_and_cat3_with_lab2(category3, category3_nolower)
    # ---
    foot_ballers = False
    # ---
    Find_wd, Find_ko = False, False
    # ---
    if not category_lab:
        list_of_cat, Find_wd, Find_ko, foot_ballers, category3 = fax2.get_list_of_and_cat3(category3, category3_nolower)
    # ---
    # ايجاد تسميات مثل لاعبو  كرة سلة أثيوبيون
    if category_lab == "" and list_of_cat == "لاعبو {}":
        category_lab = Get_contry2(orginal_category3)
        if category_lab:
            list_of_cat = ""

    if not category_lab:
        category_lab = univer.test_Universities(category3)

    if not category_lab:
        category_lab = year_lab.make_year_lab(category3)

    if not category_lab:
        category_lab = sport_lab.Get_New_team_xo(category3)

    if category_lab == "" and Find_wd:
        category_lab = pop_All_2018.get(category3, "")

    if list_of_cat == "" and category_lab == "":
        # print("translate_general_category 10")
        category_lab = ye_ts_bot.translate_general_category(category)

    if not category_lab:
        category_lab = Get_contry2(category3)

    if category_lab == "" and Find_ko:
        category_lab = kooora.kooora_team(category3, Local=Find_f_wikidata[1])
        if category_lab and category_lab and re.sub(en_literes, "", category_lab, flags=re.IGNORECASE) == category_lab:
            pop_All_2018.get({category3.lower(): category_lab})

    if category_lab == "" and Find_wd:
        category_lab = find_wikidata(category3)

    for pri_ff, vas in pp_ends_with_pase.items():
        if list_of_cat == "" and category_lab == "":
            if category3.endswith(pri_ff.lower()):
                print_put(f'>>>><<lightblue>> category3.endswith pri_ff("{pri_ff}")')
                list_of_cat = vas
                category3 = category3.replace(pri_ff.lower(), "", 1).strip()

    for pri_ff, vasv in pp_ends_with.items():
        if list_of_cat == "" and category_lab == "":
            if category3.endswith(pri_ff.lower()):
                print_put(f'>>>><<lightblue>> category3.endswith pri_ff("{pri_ff}")')
                list_of_cat = vasv
                category3 = category3.replace(pri_ff.lower(), "", 1).strip()

    # العمل مع list_of_cat

    # إيجاد تعريب للعمل مع list_of_cat
    if not category_lab:
        category_lab = event_Lab_seoo("", category3)

    if list_of_cat and category_lab:
        category_lab, list_of_cat = list_cat_format.list_of_cat_func(cate_r, category_lab, list_of_cat, foot_ballers)

    # ---
    # عند عدم وجود تعريب إلغاء العمل مع list_of_cat
    if list_of_cat and not category_lab:
        list_of_cat = ""
        category_lab = event_Lab_seoo(cate_r, orginal_category3)

    # ---
    if not category_lab:
        category_lab = tmp_bot.Work_Templates(orginal_category3)
    # ---
    if not category_lab:
        # print("translate_general_category 11")
        category_lab = ye_ts_bot.translate_general_category(orginal_category3)

    if not category_lab:
        category32 = ""
        list_of_cat2 = ""

        if category3.endswith(" cricketers"):
            list_of_cat2 = "لاعبو كريكت من {}"
            category32 = category3_nolower.replace(" cricketers", "", 1)
        elif category3.endswith(" cricket captains"):
            list_of_cat2 = "قادة كريكت من {}"
            category32 = category3_nolower.replace(" cricket captains", "", 1)

        if list_of_cat2 and category32:
            category3_lab = New_P17_Finall.get(category32.lower(), "")

            if category3_lab:
                category_lab = list_of_cat2.format(category3_lab)

    if category_lab:
        # category_lab = "تصنيف:" + fixlab(category_lab, en=cate_r)
        fixed = fixtitle.fixlab(category_lab, en=cate_r)
        category_lab = f"تصنيف:{fixed}"

    return category_lab
