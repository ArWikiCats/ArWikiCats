#!/usr/bin/python3
"""
Arabic label translation for general categories.

This module provides functionality to translate English category names
into Arabic labels by applying various resolution strategies.
"""

import functools
import re

from ...format_bots.relation_mapping import translation_category_relations
from ...helps import logger
from ...time_formats import time_to_arabic
from ...translations import Jobs_new, jobs_mens_data
from ...utils import get_relation_word, get_value_from_any_table
from ..legacy_resolvers_bots.bot_2018 import get_pop_All_18
from ..make_bots import Films_O_TT, players_new_keys
from .ar_lab_bot import find_ar_label

en_literes = "[abcdefghijklmnopqrstuvwxyz]"


@functools.lru_cache(maxsize=10000)
def work_separator_names(
    category: str,
    cate_test: str = "",
    start_get_country2: bool = False,
) -> str:
    """Process categories that contain relational words (separator).

    This function extracts relational words from categories and uses them
    to find appropriate Arabic labels.

    Args:
        category: The category string to process
        cate_test: Optional test category string
        start_get_country2: Whether to start country lookup

    Returns:
        The associated Arabic label if found, otherwise an empty string.
    """
    separator, separator_name = get_relation_word(category, translation_category_relations)

    if not separator:
        return ""

    logger.info(f'<<lightblue>>>>>> work_separator_names: separator:"{separator_name}":"{separator}" in category ')
    arlabel = find_ar_label(category, separator, cate_test=cate_test, start_get_country2=start_get_country2)

    if not arlabel:
        return ""

    # Check if the result contains Arabic characters
    if re.sub(en_literes, "", arlabel, flags=re.IGNORECASE) != arlabel:
        arlabel = ""

    logger.info(f">>>> <<lightyellow>> {arlabel=}")

    return arlabel


@functools.lru_cache(maxsize=10000)
def translate_general_category(category_r: str, start_get_country2: bool = True, fix_title: bool = True) -> str:
    """
    "Category:20th-century musicians by instrument from Northern Ireland": "تصنيف:موسيقيون في القرن 20 حسب الآلة من أيرلندا الشمالية",
    "Category:21st-century musicians by instrument from Northern Ireland": "تصنيف:موسيقيون في القرن 21 حسب الآلة من أيرلندا الشمالية",
    """
    category = category_r.replace("_", " ").lower()
    category = re.sub(r"category:", "", category, flags=re.IGNORECASE)

    logger.info(f"<<lightyellow>>>> ^^^^^^^^^ translate_general_category start ^^^^^^^^^ ({category}) ")
    logger.debug(f"<<lightyellow>>>>>> {category_r=}, {start_get_country2=}, {fix_title=}")

    arlabel = (
        ""
        or get_pop_All_18(category, "")
        or Films_O_TT.get(category, "")
        or get_value_from_any_table(category, [players_new_keys, jobs_mens_data, Jobs_new])
        or time_to_arabic.convert_time_to_arabic(category)
    )

    if not arlabel:
        arlabel = work_separator_names(category, category, start_get_country2=start_get_country2)

    if arlabel and fix_title:
        logger.info(f'>>>>>> <<green>>test: cat "{category_r}", {arlabel=}')

    if arlabel:
        logger.debug(f"<<lightyellow>>>> translate_general_category {arlabel=}  ")

    logger.debug("<<lightyellow>>>> ^^^^^^^^^ translate_general_category end ^^^^^^^^^ ")

    return arlabel
