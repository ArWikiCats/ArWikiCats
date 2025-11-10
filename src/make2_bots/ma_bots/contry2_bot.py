#!/usr/bin/python3
"""
python3 core8/pwb.py make/make2_bots.ma_bots/contry2_bot

# from ..ma_bots.contry2_bot import Get_contry2


from ..ma_bots import contry2_bot # contry2_bot.Get_contry2()


lab = contry2_bot.Get_contry2()

"""

from typing import Dict
from . import contry2_lab

from . import ye_ts_bot
from .c2_bots.contry2_tit_bt import contry_2_tit

from ..lazy_data_bots.bot_2018 import get_pop_All_18

from ...helps.print_bot import print_def_head, print_put, output_test

from ..fromnet.wd_bot import find_wikidata

GET_COUNTRY_CACHE: Dict[str, str] = {}


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
        resolved_label = find_wikidata(normalized_country)

    if not resolved_label:
        resolved_label = get_pop_All_18(normalized_country.lower(), "")

    if resolved_label:
        GET_COUNTRY_CACHE[country] = resolved_label
        print_put(f'>> Get_ scontry2 "{normalized_country}": cnt_la: {resolved_label}')
        return resolved_label

    GET_COUNTRY_CACHE[country] = resolved_label
    return resolved_label
