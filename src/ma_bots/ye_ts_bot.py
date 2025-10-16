#!/usr/bin/python3
"""
from  make.ma_bots.ye_ts_bot import translate_general_category

from ..ma_bots import ye_ts_bot


lab = ye_ts_bot.translate_general_category()

"""

import re
import sys
from ..fix import fixtitle
from ..matables_bots.bot_2018 import pop_All_2018
from ..helps.print_bot import print_def_head, print_put
from ..format_bots import Tit_ose_Nmaes
from ..date_bots import year_lab

from ..ma_bots.ar_label_bot import find_ar_label

Find_f_wikidata = {1: "nowikidata" not in sys.argv}

YTN_cash = {}
from ..matables_bots.bot import Films_O_TT, New_players


def find_lab(category, category_r):
    cate_low = category.lower()

    _lab = Films_O_TT.get(cate_low, "")

    if not _lab:
        _lab = pop_All_2018.get(cate_low, "")

    if not _lab:
        _lab = New_players.get(cate_low, "")
    if not _lab:
        _lab = year_lab.make_year_lab(cate_low)

    if _lab:
        _lab = fixtitle.fixlab(_lab, en=category_r)

        print_put(f'>>>> <<lightyellow>>test: cat "{category_r}", _lab:"{_lab}"')
        # NoLabb = False
        print_put(f'>>>> <<lightyellow>> cat:"{category_r}", _lab "{_lab}"')
    return _lab


def work_titose_nmaes(category_r, do_Get_contry2, category, Cate_test):
    """Work with titose names based on the provided category.

    This function iterates through a predefined dictionary of titose names
    and checks if the given category contains any of these names. If a match
    is found, it calls the `find_ar_label` function to retrieve an
    associated label. The function will print the label if it is found and
    return it. The iteration stops after the first match.

    Args:
        category_r (type): Description of category_r parameter.
        do_Get_contry2 (type): Description of do_Get_contry2 parameter.
        category (str): The category string to search for titose names.
        Cate_test (type): Description of Cate_test parameter.

    Returns:
        str: The associated arlabel if found, otherwise an empty string.
    """

    arlabel = ""

    for tito, tito_name in Tit_ose_Nmaes.items():
        tito = f" {tito} "
        # if Keep_Work and category.find(tito) != -1:
        if category.find(tito) == -1:
            continue
        # ---
        arlabel = find_ar_label(category, tito, tito_name, Cate_test, category_r, do_Get_contry2=do_Get_contry2)
        # ---
        if arlabel:
            print_put(f'>>>> <<lightyellow>>arlabel "{arlabel}"')
        # ---
        break
    return arlabel


def translate_general_category(category_r, do_Get_contry2=True):
    """Retrieve and process category names for the Yementest application.

    This function takes a category string, processes it to standardize the
    format, and attempts to retrieve associated labels from predefined data
    structures. If the category is not found, it will invoke additional
    functions to derive the necessary labels based on the input. The
    function also handles logging for debugging purposes.

    Args:
        category_r (str): The input category string that needs to be processed.
        do_Get_contry2 (bool): A flag indicating whether to retrieve country-related data.
            Defaults to True.

    Returns:
        str: The processed label associated with the input category.
    """

    category = re.sub(r"_", " ", category_r)
    category = re.sub(r"category:", "", category, flags=re.IGNORECASE)

    cash_key = category.lower().strip()

    if cash_key in YTN_cash:
        return YTN_cash[cash_key]

    print_def_head(f"<<lightyellow>>>> ^^^^^^^^^ yementest start ^^^^^^^^^ ({category}) ")

    # if category == "women's universities and colleges":
    #     print(dadas)

    print_def_head(f'<<lightyellow>>>>>> yementest, category_r:"{category_r}", category:"{category}"')
    Cate_test = category.lower()

    # Keep_Work = True

    arlabel = pop_All_2018.get(category, "")

    if not arlabel:
        arlabel = find_lab(category, category_r)

    if not arlabel:
        arlabel = work_titose_nmaes(category_r, do_Get_contry2, category, Cate_test)

    if arlabel:
        arlabel = fixtitle.fixlab(arlabel, en=category_r)
        print_put(f'xxxxx <<lightyellow>>Cate_test: "{Cate_test}" ')
        print_put(f'>>>>>> <<lightyellow>>test: cat "{category_r}", arlabel:"{arlabel}"')

    print_def_head("<<lightyellow>>>> ^^^^^^^^^ yementest end ^^^^^^^^^ ")

    YTN_cash[cash_key] = arlabel

    return arlabel
