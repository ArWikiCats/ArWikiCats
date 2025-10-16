"""
from  make.fromnet.wd_bot import find_wikidata
"""

import sys
from typing import Dict
from .wd import find_name_from_wikidata
from ..helps.print_bot import print_put
from ..ma_lists import New_P17_Finall
from ..ma_lists import Ambassadors_tab
from ..matables_bots.centries_bot import centries_years_dec
from ..matables_bots.bot_2018 import pop_All_2018
from ..matables_bots.bot_2018 import Add_to_pop_All_18  # Add_to_pop_All_18(tab)

wikidata_cash_oo: Dict[str, str] = {}
Find_f_wikidata: Dict[int, bool] = {1: "nowikidata" not in sys.argv}


def find_wikidata(contry: str) -> str:
    contry2 = contry.lower().strip()
    if wikidata_cash_oo.get(contry2, False):
        return wikidata_cash_oo.get(contry2, "")

    cnt_la = ""
    if not cnt_la:
        cnt_la = New_P17_Finall.get(contry2, "")
    if not cnt_la:
        cnt_la = Ambassadors_tab.get(contry2, "")
    if not cnt_la:
        cnt_la = pop_All_2018.get(contry2, "")
    if not cnt_la:
        cnt_la = centries_years_dec.get(contry2, "")

    if cnt_la == "" and Find_f_wikidata[1]:
        oi = find_name_from_wikidata(contry, "en", Local=Find_f_wikidata[1])

        for tf, tf_lab in oi.items():
            if tf.lower() != contry2:
                continue
            if tf_lab:
                cnt_la = tf_lab
                Add_to_pop_All_18({contry2: tf_lab})
                break

        if not cnt_la:
            print_put(f"<<lightpurple>> >no lab in wikidata len({len(oi)}):> ")

    wikidata_cash_oo[contry2] = cnt_la

    return cnt_la
