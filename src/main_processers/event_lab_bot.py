"""
!
"""

# from ..new.end_start_bots import fax2
from ..new.end_start_bots.fax2 import get_list_of_and_cat3
from ..new.end_start_bots.fax2_temp import get_templates_fo
from ..new.end_start_bots.fax2_episodes import get_episodes

from ..make2_bots.ma_bots.squad_title_bot import get_squad_title
from ..fix import fixtitle
from ..helps.log import logger
from ..translations import New_P17_Finall, Get_New_team_xo
from ..make2_bots import tmp_bot
from ..make2_bots.date_bots import year_lab
from ..make2_bots.format_bots import change_cat, pp_ends_with, pp_ends_with_pase
from ..make2_bots.fromnet import kooora
from ..make2_bots.fromnet.wd_bot import find_wikidata
from ..make2_bots.lazy_data_bots.bot_2018 import get_pop_All_18
from ..make2_bots.o_bots import univer

# ImportError: cannot import name 'translate_general_category' from partially initialized module 'make2.make2_bots.ma_bots.ye_ts_bot'
#  (most likely due to a circular import) (make2_bots.ma_bots\ye_ts_bot.py)
from ..make2_bots.ma_bots import list_cat_format, ye_ts_bot
from ..make2_bots.ma_bots.country2_bot import Get_country2
from ..make2_bots.ma_bots.lab_seoo_bot import event_Lab_seoo
from ..config import app_settings
# from ..helps.jsonl_dump import save
# from pathlib import Path


def get_list_of_and_cat3_with_lab2(category3_o: str) -> str:
    category_lab = ""
    list_of_cat = ""
    category3 = category3_o
    category3 = category3.strip()

    if category3.endswith(" squad templates"):
        list_of_cat = "قوالب تشكيلات {}"
        category3 = category3[: -len(" squad templates")]
        cate_labs = get_squad_title(category3)
        if cate_labs:
            category_lab = f"قوالب {cate_labs}"

    elif category3.endswith(" squad navigational boxes"):
        list_of_cat = "صناديق تصفح تشكيلات {}"
        category3 = category3[: -len(" squad navigational boxes")]
        cate_labs = get_squad_title(category3)
        if cate_labs:
            category_lab = f"صناديق تصفح {cate_labs}"

    if category_lab:
        logger.debug(f'<<lightblue>>get_list_of_and_cat3_with_lab(): {list_of_cat=}, {category3=}, {category_lab=}')
        print(f"<<lightblue>>(): {category3_o=}, {category_lab=}")

    return category_lab


def event_Lab(cate_r: str) -> str:
    category_lab = ""
    category = cate_r.lower()
    category = category.replace("_", " ")
    if not category.startswith("category:"):
        category = f"category:{category}"
    category = change_cat(category)

    category3_nolower = cate_r
    if category3_nolower.startswith("Category:"):
        category3_nolower = category3_nolower.split("Category:")[1]

    category3 = category.lower()
    if category3.startswith("category:"):
        category3 = category3.split("category:")[1]

    orginal_category3 = category3
    # ---
    if not category_lab:
        category_lab = get_list_of_and_cat3_with_lab2(category3)
    # ---
    Find_wd, Find_ko, foot_ballers = False, False, False
    # ---
    list_of_cat = ""
    # ---
    if not category_lab:
        if category3.endswith(" episodes"):
            Find_wd = True
            list_of_cat, category3 = get_episodes(category3, category3_nolower)

        elif category3.endswith(" templates"):
            list_of_cat, category3 = get_templates_fo(category3)

        else:
            # list_of_cat, Find_wd, Find_ko, foot_ballers, category3 = fax2.get_list_of_and_cat3(category3, category3_nolower, app_settings.find_stubs)
            list_of_cat, Find_wd, Find_ko, foot_ballers, category3 = get_list_of_and_cat3(category3, category3_nolower, app_settings.find_stubs)
    # ---
    # ايجاد تسميات مثل لاعبو  كرة سلة أثيوبيون
    if category_lab == "" and list_of_cat == "لاعبو {}":
        category_lab = Get_country2(orginal_category3)
        if category_lab:
            list_of_cat = ""

    if not category_lab:
        category_lab = univer.te_universities(category3)

    if not category_lab:
        category_lab = year_lab.make_year_lab(category3)

    if not category_lab:
        category_lab = Get_New_team_xo(category3)

    if category_lab == "" and Find_wd:
        category_lab = get_pop_All_18(category3, "")

    if list_of_cat == "" and category_lab == "":
        # print("translate_general_category 10")
        category_lab = ye_ts_bot.translate_general_category(category)

    if not category_lab:
        category_lab = Get_country2(category3)

    if category_lab == "" and Find_ko:
        category_lab = kooora.kooora_team(category3)

    if category_lab == "" and Find_wd:
        category_lab = find_wikidata(category3)

    for pri_ff, vas in pp_ends_with_pase.items():
        if list_of_cat == "" and category_lab == "":
            if category3.endswith(pri_ff.lower()):
                logger.info(f'>>>><<lightblue>> category3.endswith pri_ff("{pri_ff}")')
                list_of_cat = vas
                category3 = category3[: -len(pri_ff)].strip()

    for pri_ff, vasv in pp_ends_with.items():
        if list_of_cat == "" and category_lab == "":
            if category3.endswith(pri_ff.lower()):
                logger.info(f'>>>><<lightblue>> category3.endswith pri_ff("{pri_ff}")')
                list_of_cat = vasv
                category3 = category3[: -len(pri_ff)].strip()

    # work with list_of_cat
    if not category_lab:
        category_lab = event_Lab_seoo("", category3)

    if list_of_cat and category_lab:
        category_lab, list_of_cat = list_cat_format.list_of_cat_func(cate_r, category_lab, list_of_cat, foot_ballers)

    # ---
    # dont work with list_of_cat
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
            category32 = category3_nolower[: -len(" cricketers")]
        elif category3.endswith(" cricket captains"):
            list_of_cat2 = "قادة كريكت من {}"
            category32 = category3_nolower[: -len(" cricket captains")]

        if list_of_cat2 and category32:
            category3_lab = New_P17_Finall.get(category32.lower(), "")

            if category3_lab:
                category_lab = list_of_cat2.format(category3_lab)

    if category_lab:
        # category_lab = "تصنيف:" + fixlab(category_lab, en=cate_r)
        fixed = fixtitle.fixlab(category_lab, en=cate_r)
        category_lab = f"تصنيف:{fixed}"
        # save(Path(__file__).parent / "event_Lab_examples.json", [{cate_r: category_lab}])

    return category_lab
