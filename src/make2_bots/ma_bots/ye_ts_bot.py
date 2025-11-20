#!/usr/bin/python3
"""
Arabic label translation for general categories.

This module provides functionality to translate English category names
into Arabic labels by applying various resolution strategies.
"""

import functools
import re
from typing import Optional

from ...fix import fixtitle
from ...helps.log import logger
from ...translations import Jobs_new
from ...translations import jobs_mens_data
from ...utils import get_value_from_any_table, get_relation_word
from ..date_bots import year_lab
from ..format_bots import category_relation_mapping

from ..lazy_data_bots.bot_2018 import get_pop_All_18
from ..matables_bots.bot import Films_O_TT, players_new_keys
from .ar_lab import find_ar_label

en_literes = "[abcdefghijklmnopqrstuvwxyz]"


@functools.lru_cache(maxsize=10000)
def find_lab(category: str, category_r: str) -> str:
    """Find a label for the given category using multiple data sources.

    Args:
        category: The normalized category string to look up
        category_r: The original category string for logging

    Returns:
        The found Arabic label or empty string if not found
    """
    cate_low = category.lower()

    _lab = Films_O_TT.get(cate_low, "")

    if not _lab:
        _lab = get_pop_All_18(cate_low, "")

    if not _lab:
        _lab = get_value_from_any_table(cate_low, [players_new_keys, jobs_mens_data, Jobs_new])

    if not _lab:
        _lab = year_lab.make_year_lab(cate_low)

    if _lab:
        logger.info(f'>>>> <<lightyellow>>test: cat "{category_r}", _lab:"{_lab}"')
        logger.info(f'>>>> <<lightyellow>> cat:"{category_r}", _lab "{_lab}"')

    return _lab


@functools.lru_cache(maxsize=10000)
def work_titose_names(
    category: str,
    cate_test: str = "",
    start_get_country2: bool = False,
) -> str:
    """Process categories that contain relational words (tito).

    This function extracts relational words from categories and uses them
    to find appropriate Arabic labels.

    Args:
        category: The category string to process
        cate_test: Optional test category string
        start_get_country2: Whether to start country lookup

    Returns:
        The associated Arabic label if found, otherwise an empty string.
    """
    tito, tito_name = get_relation_word(category, category_relation_mapping)

    if not tito:
        return ""

    logger.info(f'<<lightblue>>>>>> yementest: tito:"{tito_name}":"{tito}" in category ')
    arlabel = find_ar_label(category, tito, cate_test=cate_test, start_get_country2=start_get_country2)

    if not arlabel:
        return ""

    # Check if the result contains Arabic characters
    if re.sub(en_literes, "", arlabel, flags=re.IGNORECASE) != arlabel:
        arlabel = ""

    logger.info(f'>>>> <<lightyellow>>arlabel "{arlabel}"')

    return arlabel


@functools.lru_cache(maxsize=10000)
def translate_general_category(category_r: str, start_get_country2: bool = True) -> str:
    """Translate an English category to Arabic label.

    This function processes a category string by normalizing the format
    and applying various strategies to find an appropriate Arabic label.

    Args:
        category_r: The input category string that needs to be processed
        start_get_country2: A flag indicating whether to retrieve country-related data.
            Defaults to True.

    Returns:
        The processed Arabic label associated with the input category.
    """
    category = category_r.replace("_", " ")
    category = re.sub(r"category:", "", category, flags=re.IGNORECASE)

    logger.info(f"<<lightyellow>>>> ^^^^^^^^^ yementest start ^^^^^^^^^ ({category}) ")

    logger.info(f'<<lightyellow>>>>>> yementest, category_r:"{category_r}", category:"{category}"')
    cate_test = category.lower()

    arlabel = get_pop_All_18(category, "")

    if not arlabel:
        arlabel = find_lab(category, category_r)

    if not arlabel:
        arlabel = work_titose_names(category, cate_test, start_get_country2=start_get_country2)

    if arlabel:
        arlabel = fixtitle.fixlab(arlabel, en=category_r)
        logger.info(f'xxxxx <<green>>cate_test: "{cate_test}" ')
        logger.info(f'>>>>>> <<green>>test: cat "{category_r}", arlabel:"{arlabel}"')

    logger.info("<<lightyellow>>>> ^^^^^^^^^ yementest end ^^^^^^^^^ ")

    return arlabel
