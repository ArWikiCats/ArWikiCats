#!/usr/bin/python3
"""

    arlabel = (
        ""
        or sub_general_resolver.sub_translate_general_category(category)
        or general_resolver.work_separator_names(category)
    )
"""

import functools
import re

from ...helps import logger
from ...time_formats import time_to_arabic
from ...translations import Jobs_new, jobs_mens_data
from ...utils import get_value_from_any_table
from ..legacy_resolvers_bots.bot_2018 import get_pop_All_18
from ..make_bots import Films_O_TT, players_new_keys

en_literes = "[abcdefghijklmnopqrstuvwxyz]"


@functools.lru_cache(maxsize=10000)
def sub_translate_general_category(category_r: str) -> str:
    """
    "Category:20th-century musicians by instrument from Northern Ireland": "تصنيف:موسيقيون في القرن 20 حسب الآلة من أيرلندا الشمالية",
    "Category:21st-century musicians by instrument from Northern Ireland": "تصنيف:موسيقيون في القرن 21 حسب الآلة من أيرلندا الشمالية",
    """
    category = category_r.replace("_", " ").lower()
    category = re.sub(r"category:", "", category, flags=re.IGNORECASE)

    logger.info(f"<<lightyellow>>>> ^^^^^^^^^ sub_translate_general_category start ^^^^^^^^^ ({category}) ")
    logger.debug(f"<<lightyellow>>>>>> {category_r=}")

    arlabel = (
        ""
        or get_pop_All_18(category, "")
        or Films_O_TT.get(category, "")
        or get_value_from_any_table(category, [players_new_keys, jobs_mens_data, Jobs_new])
        or time_to_arabic.convert_time_to_arabic(category)
    )

    if arlabel:
        logger.debug(f"<<lightyellow>>>> sub_translate_general_category {arlabel=}  ")

    logger.debug("<<lightyellow>>>> ^^^^^^^^^ sub_translate_general_category end ^^^^^^^^^ ")

    return arlabel
