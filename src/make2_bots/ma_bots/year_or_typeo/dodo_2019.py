#!/usr/bin/python3
"""
Usage:
from .year_or_typeo.dodo_2019 import work_2019
# cat4_lab = work_2019(category3, year, year_labe)

"""

import re

from ....helps.log import logger
from ....new.time_to_arabic import match_en_return_ar
from ...lazy_data_bots.bot_2018 import get_pop_All_18
from ...matables_bots.check_bot import check_key_new_players
from ..country_bot import get_country

# from pathlib import Path
# from ....helps.jsonl_dump import dump_data

# @dump_data(["category3", "year", "year_labe"])


def work_2019(category3: str, year: str, year_labe: str) -> str:
    """
    Process category data.
    example:
        input:
            category3: "18th century dutch explorers"
            year: "18th century
            year_labe: "القرن 18
        result:
            "مستكشفون هولنديون في القرن 18
    """
    logger.info(f'<<lightyellow>>>> ============ start work_2019 :"{category3}", year:"{year}" ============ ')
    cat_4 = re.sub(rf"{year}\s*(.*)$", r"\g<1>", category3)
    cat_4 = cat_4.strip()
    logger.info(f'<<lightgreen>>>>>> 2019: NoLab and year, cat_4="{cat_4}"')
    cat4_lab = get_pop_All_18(cat_4, "")
    if not cat4_lab:
        cat4_lab = get_country(cat_4)
    arlabel = ""
    if cat4_lab:
        logger.info(f'<<lightgreen>>>>>> cat4_lab = "{cat4_lab}"')
        in_tables = check_key_new_players(cat_4)
        if in_tables:
            arlabel = f"{cat4_lab} في {year_labe}"
        elif cat4_lab.endswith(" في"):
            arlabel = f"{cat4_lab} {year_labe}"
        else:
            arlabel = f"{year_labe} {cat4_lab}"

        logger.info(f'<<lightgreen>>>>>> 2019: New arlabel :"{arlabel}" ')
        logger.info("<<lightyellow>>>> ^^^^^^^^^ end work_2019 ^^^^^^^^^ ")
    return arlabel


def work_2019_wrap(category: str) -> str:
    """Wrap ``work_2019`` with a quick lookup of year metadata from English text."""
    year_data = match_en_return_ar(category)
    if not year_data:
        return ""

    year, year_label = "", ""

    for x, v in year_data.items():
        year = x
        year_label = v
        break

    if year == year_label and not year.isdigit():
        return ""

    return work_2019(category, year, year_label)
