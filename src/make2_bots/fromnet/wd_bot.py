"""
from  make.make2_bots.fromnet.wd_bot import find_wikidata
"""

import functools
from typing import Dict

from .wd import find_name_from_wikidata
from ... import app_settings
from ...helps.print_bot import print_put
from ...translations import New_P17_Finall
from ...translations import Ambassadors_tab
from ..matables_bots.centries_bot import centries_years_dec
from ..lazy_data_bots.bot_2018 import Add_to_pop_All_18, get_pop_All_18


@functools.lru_cache(maxsize=None)
def find_wikidata(country: str) -> str:
    normalized_country = country.lower().strip()

    resolved_label = ""

    if not resolved_label:
        resolved_label = New_P17_Finall.get(normalized_country, "")

    if not resolved_label:
        resolved_label = Ambassadors_tab.get(normalized_country, "")

    if not resolved_label:
        resolved_label = get_pop_All_18(normalized_country, "")

    if not resolved_label:
        resolved_label = centries_years_dec.get(normalized_country, "")

    if resolved_label:
        return resolved_label

    if not app_settings.enable_wikidata:
        return ""

    wikidata_matches = find_name_from_wikidata(country, "en")

    for match_key, match_label in wikidata_matches.items():
        if match_key.lower() != normalized_country:
            continue
        if match_label:
            resolved_label = match_label
            Add_to_pop_All_18({normalized_country: match_label})
            break

    if not resolved_label:
        print_put(f"<<lightpurple>> >no lab in wikidata len({len(wikidata_matches)}):> ")

    return resolved_label
