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

Get_contry2_done: Dict[str, str] = {}
use_main_s_done: List[str] = []

use_main_s: Dict[int, bool] = {1: "usemains" in sys.argv or "use_main_s" in sys.argv}


def Get_contry2(contry: str, orginal: str = "", With_Years: bool = True) -> str:
    """Retrieve information related to a specified country."""

    if contry in Get_contry2_done:
        output_test(f'>>>> contry: "{contry}" in Get_contry2_done, lab:"{Get_contry2_done[contry]}"')
        return Get_contry2_done[contry]

    contry2 = contry.lower().strip()
    print_def_head(f'>> Get_contry2 "{contry2}":')

    resolved_label = ""

    if not resolved_label:
        resolved_label = contry2_lab.get_lab_for_contry2(contry, with_test_ye=False)

    if not resolved_label:
        resolved_label = ye_ts_bot.translate_general_category(
            contry2, do_Get_contry2=False
        )
    ti_toseslist = [
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
    for separator in ti_toseslist:
        if separator not in contry2:
            continue

        resolved_label = contry_2_tit(separator, contry, With_Years=With_Years)

        break

    if not resolved_label:
        if contry2 in use_main_s_done:
            if use_main_s[1]:
                use_main_s_done.append(contry2)
                resolved_label = find_wikidata(contry2)

        elif pop_All_2018.get(contry2.lower(), "") != "":
            resolved_label = pop_All_2018.get(contry2.lower(), "")
    if resolved_label:
        Get_contry2_done[contry] = resolved_label
        print_put(f'>> Get_ scontry2 "{contry2}": cnt_la: {resolved_label}')
        return resolved_label

    Get_contry2_done[contry] = resolved_label
    return resolved_label
