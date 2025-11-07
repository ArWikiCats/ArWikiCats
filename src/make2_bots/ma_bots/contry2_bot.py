#!/usr/bin/python3
"""
python3 core8/pwb.py make/make2_bots.ma_bots/contry2_bot

# from ..ma_bots.contry2_bot import Get_contry2


from ..ma_bots import contry2_bot # contry2_bot.Get_contry2()


lab = contry2_bot.Get_contry2()

"""

import sys
from typing import Dict, List
from . import contry2_lab

from . import ye_ts_bot
from .c2_bots.contry2_tit_bt import contry_2_tit

from ..matables_bots.bot_2018 import pop_All_2018

from ...helps.print_bot import print_def_head, print_put, output_test

from ..fromnet.wd_bot import find_wikidata

GET_COUNTRY_CACHE: Dict[str, str] = {}
USE_MAIN_COUNTRY_DONE: List[str] = []

USE_MAIN_FLAGS: Dict[int, bool] = {1: "usemains" in sys.argv or "use_main_s" in sys.argv}


def Get_contry2(country: str, orginal: str = "", With_Years: bool = True) -> str:
    """Retrieve information related to a specified country."""

    if country in GET_COUNTRY_CACHE:
        output_test(
            f'>>>> contry: "{country}" in Get_contry2_done, lab:"{GET_COUNTRY_CACHE[country]}"'
        )
        return GET_COUNTRY_CACHE[country]

    normalized_country = country.lower().strip()
    print_def_head(f'>> Get_contry2 "{normalized_country}":')

    resolved_label = ""

    if not resolved_label:
        resolved_label = contry2_lab.get_lab_for_contry2(country, with_test_ye=False)

    if not resolved_label:
        resolved_label = ye_ts_bot.translate_general_category(
            normalized_country, do_Get_contry2=False
        )
    title_separators = [
        " based in ",
        " in ",
        " by ",
        " about ",
        " to ",
        "-of ",
        " of ",
        " from ",
        " at ",
        " on ",
    ]
    for separator in title_separators:
        if separator not in normalized_country:
            continue

        resolved_label = contry_2_tit(separator, country, With_Years=With_Years)

        break

    if not resolved_label:
        if normalized_country in USE_MAIN_COUNTRY_DONE:
            if USE_MAIN_FLAGS[1]:
                USE_MAIN_COUNTRY_DONE.append(normalized_country)
                resolved_label = find_wikidata(normalized_country)

        elif pop_All_2018.get(normalized_country.lower(), "") != "":
            resolved_label = pop_All_2018.get(normalized_country.lower(), "")
    if resolved_label:
        GET_COUNTRY_CACHE[country] = resolved_label
        print_put(f'>> Get_ scontry2 "{normalized_country}": cnt_la: {resolved_label}')
        return resolved_label

    GET_COUNTRY_CACHE[country] = resolved_label
    return resolved_label
