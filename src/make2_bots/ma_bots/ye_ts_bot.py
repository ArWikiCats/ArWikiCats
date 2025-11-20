#!/usr/bin/python3
"""
from  make.make2_bots.ma_bots.ye_ts_bot import translate_general_category

from ..ma_bots import ye_ts_bot


lab = ye_ts_bot.translate_general_category()

"""

import functools
import re

from ...helps.log import logger
from ...translations import Jobs_new  # to be removed from players_new_keys
from ...translations import jobs_mens_data  # to be  removed from players_new_keys
from ...utils import get_value_from_any_table
from ..date_bots import year_lab
from ..format_bots import category_relation_mapping

from ..lazy_data_bots.bot_2018 import get_pop_All_18
from ..matables_bots.bot import Films_O_TT, players_new_keys
from .ar_lab import find_ar_label

en_literes = "[abcdefghijklmnopqrstuvwxyz]"


def find_lab(category: str, category_r: str) -> str:
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


def work_titose_names(
    category_r: str,
    category: str,
    Cate_test: str="",
    start_get_country2: bool=False,
) -> str:
    """Work with titose names based on the provided category.

    This function iterates through a predefined dictionary of titose names
    and checks if the given category contains any of these names. If a match
    is found, it calls the `find_ar_label` function to retrieve an
    associated label. The function will print the label if it is found and
    return it. The iteration stops after the first match.

    Args:
        category_r (type): Description of category_r parameter.
        start_get_country2 (type): Description of start_get_country2 parameter.
        category (str): The category string to search for titose names.
        Cate_test (type): Description of Cate_test parameter.

    Returns:
        str: The associated arlabel if found, otherwise an empty string.
    """

    arlabel = ""

    for tito, tito_name in category_relation_mapping.items():
        tito = f" {tito} "
        # if Keep_Work and tito in category:
        if tito not in category:
            continue
        # ---
        logger.info(f'<<lightblue>>>>>> yementest: tito:"{tito_name}":"{tito}" in category ')
        arlabel = find_ar_label(category, tito, Cate_test, category_r=category_r, start_get_country2=start_get_country2)
        if arlabel:
            logger.info(f'>>>> <<lightyellow>>arlabel "{arlabel}"')
        # ---
        break
    return arlabel


@functools.lru_cache(maxsize=None)
def translate_general_category(category_r: str, start_get_country2: bool = True) -> str:
    """Retrieve and process category names for the Yementest application.

    This function takes a category string, processes it to standardize the
    format, and attempts to retrieve associated labels from predefined data
    structures. If the category is not found, it will invoke additional
    functions to derive the necessary labels based on the input. The
    function also handles logging for debugging purposes.

    Args:
        category_r (str): The input category string that needs to be processed.
        start_get_country2 (bool): A flag indicating whether to retrieve country-related data.
            Defaults to True.

    Returns:
        str: The processed label associated with the input category.
    """

    category = category_r.replace("_", " ")
    category = re.sub(r"category:", "", category, flags=re.IGNORECASE)

    logger.info(f"<<lightyellow>>>> ^^^^^^^^^ yementest start ^^^^^^^^^ ({category}) ")

    # if category == "women's universities and colleges":
    #     print(dadas)

    logger.info(f'<<lightyellow>>>>>> yementest, category_r:"{category_r}", category:"{category}"')
    Cate_test = category.lower()

    # Keep_Work = True

    arlabel = get_pop_All_18(category, "")

    if not arlabel:
        arlabel = find_lab(category, category_r)

    if not arlabel:
        arlabel = work_titose_names(category_r, start_get_country2, category, Cate_test)

    if arlabel:
        logger.info(f'xxxxx <<green>>Cate_test: "{Cate_test}" ')
        logger.info(f'>>>>>> <<green>>test: cat "{category_r}", arlabel:"{arlabel}"')

    logger.info("<<lightyellow>>>> ^^^^^^^^^ yementest end ^^^^^^^^^ ")

    return arlabel
