#!/usr/bin/python3
"""
Usage:
from .dodo_bots.dodo_2019 import work_2019
# cat4_lab = work_2019(category3, year, year_labe)

"""

import re
from ...matables_bots.bot import New_players, Table_for_frist_word

from ...matables_bots.bot_2018 import pop_All_2018
from ...helps.print_bot import print_put
from ..contry_bot import Get_contry


def work_2019(category3: str, year: str, year_labe: str) -> str:
    """Process category data for the year 2019."""

    print_put(f'<<lightyellow>>>> ============ start work_2019 :"{category3}", year:"{year}" ============ ')
    cat_4 = re.sub(rf"{year}\s*(.*)$", r"\g<1>", category3)
    cat_4 = cat_4.strip()
    print_put(f'<<lightgreen>>>>>> 2019: NoLab and year, cat_4="{cat_4}"')
    cat4_lab = pop_All_2018.get(cat_4, "")
    if not cat4_lab:
        cat4_lab = Get_contry(cat_4)

    arlabel = ""
    if cat4_lab:
        print_put(f'<<lightgreen>>>>>> cat4_lab = "{cat4_lab}"')
        # cat_4_in_Table = False
        for table, ta_t in Table_for_frist_word.items():
            if cat_4 in ta_t:
                # cat_4_in_Table = True
                print_put(f'X:<<lightpurple>>>>>> cat_4 "{cat_4}" in {table}.')

        if cat_4 in New_players:
            arlabel = f"{cat4_lab} في {year_labe}"
        elif cat4_lab.endswith(" في"):
            arlabel = f"{cat4_lab} {year_labe}"
        else:
            arlabel = f"{year_labe} {cat4_lab}"

        print_put(f'<<lightgreen>>>>>> 2019: New arlabel :"{arlabel}" ')
        print_put("<<lightyellow>>>> ^^^^^^^^^ end work_2019 ^^^^^^^^^ ")
    # ---
    return arlabel
