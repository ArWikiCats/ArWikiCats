"""

Usage:
from ...matables_bots.table1_bot import table1get, get_KAKO

"""
from typing import Dict, Any
from ... import printe
from .bot_2018 import pop_All_2018
from ...helps.print_bot import output_test
from .bot import Add_to_main2_tab
from .bot import Films_O_TT, New_players
from .centries_bot import centries_years_dec

fasop: Dict[str, str] = {}
table1get_tab: Dict[str, str] = {}
# ---
Fgos2: Dict[str, Dict[str, str]] = {
    "Films_O_TT": Films_O_TT,
    "pop_All_2018": pop_All_2018,
}

Fgos1: Dict[str, Dict[str, str]] = {
    "centries_years_dec": centries_years_dec,
    "pop_All_2018": pop_All_2018,
    "New_players": New_players,
    "Films_O_TT": Films_O_TT,
}

papa = False
if papa == 4:
    for tabd, tab_data in Fgos1.items():
        for ta, value in tab_data.items():
            ta2 = ta.lower()
            if "ف" in value and "f" not in ta2 and "ph" not in ta2:
                fasop[ta2] = value
            if ta2 in table1get_tab and table1get_tab[ta2] != value:
                printe.output(f"<<lightblue>>{tabd}: {ta2}: {table1get_tab[ta2]} != {value}")
            table1get_tab[ta2] = value
            if "," in value:
                printe.output(value)
    printe.output(f'<<lightblue>> len "<<lightpurple>>table1get_tab"<<default>>:\t{len(table1get_tab)}. ')
    printe.output(f"<<lightblue>>len fasop: {len(fasop)}")

Fgo_done: Dict[str, Dict[str, str]] = {}

for tabd in list(Fgos1):
    Fgo_done[tabd] = {}
for tabd in list(Fgos2):
    Fgo_done[tabd] = {}

FgosLi: Dict[int, Dict[str, Dict[str, str]]] = {1: Fgos1, 2: Fgos2}

from ...ma_lists import pf_keys2
from ...ma_lists import Music_By_table
from ...ma_lists import Films_key_man
from .bot import All_P17
from ...ma_lists import By_table

KAKO: Dict[str, Dict[str, str]] = {
    "pf_keys2": pf_keys2,
    "pop_All_2018": pop_All_2018,
    "Music_By_table": Music_By_table,
    "Films_key_man": Films_key_man,
    "All_P17": All_P17,
    "By_table": By_table,
    "Films_O_TT": Films_O_TT,
    "New_players": New_players,
}


def get_KAKO(cont: str) -> str:
    resolved_label = ""
    for table_name, table_data in KAKO.items():
        if not resolved_label:
            resolved_label = table_data.get(cont, "")
            if resolved_label:
                output_test(
                    f'>> get_KAKO_({table_name}) for ["{cont}"] = "{resolved_label}"'
                )
                return resolved_label
    return resolved_label


def table1get(category3: str, tt: int) -> str:
    Fgos = FgosLi.get(tt, {})

    resolved_label = ""
    for table1 in list(Fgos):
        if not resolved_label:
            if category3 not in Fgo_done[table1]:
                output_test(f'a<<lightblue>>>>>> table1get find in "{len(Fgos[table1])}" keys in table1 "{table1}"')
                resolved_label = Fgos[table1].get(category3, "")
                Fgo_done[table1][category3] = resolved_label
                break
            else:
                cached_label = Fgo_done[table1][category3]
                output_test(f'a<<lightblue>>>>>> category3:"{category3}" in table1 "{table1}", lab:"{cached_label}"')
                if cached_label:
                    Add_to_main2_tab(category3, cached_label)
                    output_test(f'a<<lightgreen>>>>>> category3:"{category3}" in table1 "{table1}", lab:"{cached_label}"')
                    resolved_label = cached_label
                    break
    return resolved_label
