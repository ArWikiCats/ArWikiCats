"""
from  make.make2_bots.fromnet.wd_bot import find_wikidata
"""

import sys
from typing import Dict
from .wd import find_name_from_wikidata
from ...helps.print_bot import print_put
from ...ma_lists import New_P17_Finall
from ...ma_lists import Ambassadors_tab
from ..matables_bots.centries_bot import centries_years_dec
from ..matables_bots.bot_2018 import pop_All_2018
from ..matables_bots.bot_2018 import Add_to_pop_All_18  # Add_to_pop_All_18(tab)

WIKIDATA_CACHE: Dict[str, str] = {}
Find_f_wikidata: Dict[int, bool] = {1: "nowikidata" not in sys.argv}


def find_wikidata(country: str) -> str:
    normalized_country = country.lower().strip()
    if WIKIDATA_CACHE.get(normalized_country, False):
        return WIKIDATA_CACHE.get(normalized_country, "")

    resolved_label = ""
    if not resolved_label:
        resolved_label = New_P17_Finall.get(normalized_country, "")
    if not resolved_label:
        resolved_label = Ambassadors_tab.get(normalized_country, "")
    if not resolved_label:
        resolved_label = pop_All_2018.get(normalized_country, "")
    if not resolved_label:
        resolved_label = centries_years_dec.get(normalized_country, "")

    if resolved_label == "" and Find_f_wikidata[1]:
        wikidata_matches = find_name_from_wikidata(
            country, "en", Local=Find_f_wikidata[1]
        )

        for match_key, match_label in wikidata_matches.items():
            if match_key.lower() != normalized_country:
                continue
            if match_label:
                resolved_label = match_label
                Add_to_pop_All_18({normalized_country: match_label})
                break

        if not resolved_label:
            print_put(
                f"<<lightpurple>> >no lab in wikidata len({len(wikidata_matches)}):> "
            )

    WIKIDATA_CACHE[normalized_country] = resolved_label

    return resolved_label
