#!/usr/bin/python3
"""
Usage:
from .dodo_bots.dodo_2019 import work_2019
# cat4_lab = work_2019(category3, year, year_labe)

"""
import re
from ...date_bots import year_lab
from ...matables_bots.check_bot import check_key_new_players
from ...lazy_data_bots.bot_2018 import get_pop_All_18
from ....helps.print_bot import print_put
from ..country_bot import get_country


def work_2019(category3: str, year: str, year_labe: str) -> str:
    """
    Process category data.
    example:
        input:
            category3: "18th century dutch explorers
            year: "18th century
            year_labe: "القرن 18
        result:
            "مستكشفون هولنديون في القرن 18
    """
    # ---
    print_put(f'<<lightyellow>>>> ============ start work_2019 :"{category3}", year:"{year}" ============ ')
    # ---
    cat_4 = re.sub(rf"{year}\s*(.*)$", r"\g<1>", category3)
    # ---
    cat_4 = cat_4.strip()
    # ---
    print_put(f'<<lightgreen>>>>>> 2019: NoLab and year, cat_4="{cat_4}"')
    cat4_lab = get_pop_All_18(cat_4, "")
    # ---
    if not cat4_lab:
        cat4_lab = get_country(cat_4)
    # ---
    arlabel = ""
    # ---
    if cat4_lab:
        print_put(f'<<lightgreen>>>>>> cat4_lab = "{cat4_lab}"')
        # ---
        in_tables = check_key_new_players(cat_4)
        # ---
        if in_tables:
            arlabel = f"{cat4_lab} في {year_labe}"
        elif cat4_lab.endswith(" في"):
            arlabel = f"{cat4_lab} {year_labe}"
        else:
            arlabel = f"{year_labe} {cat4_lab}"

        print_put(f'<<lightgreen>>>>>> 2019: New arlabel :"{arlabel}" ')
        print_put("<<lightyellow>>>> ^^^^^^^^^ end work_2019 ^^^^^^^^^ ")
    # ---
    return arlabel


def match_year(category):
    ...


def work_2019_wrap(category):
    year = match_year(category)
    year_label = year_lab.make_year_lab(year)
    return work_2019(category, year, year_label)
