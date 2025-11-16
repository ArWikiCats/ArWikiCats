#!/usr/bin/python3
"""
This module is responsible for retrieving localized information for a specified country.
"""

import functools
from ...helps.log import logger

from ..lazy_data_bots.bot_2018 import get_pop_All_18
from ...helps.print_bot import print_def_head
from ..fromnet.wd_bot import find_wikidata
from .c2_bots.country2_tit_bt import country_2_title_work
from . import country2_lab
from . import ye_ts_bot


@functools.lru_cache(maxsize=None)
def Get_country2(country: str, With_Years: bool = True) -> str:
    """Retrieve information related to a specified country."""

    normalized_country = country.lower().strip()
    print_def_head(f'>> Get_country2 "{normalized_country}":')

    resolved_label = ""

    if not resolved_label:
        resolved_label = country2_lab.get_lab_for_country2(country, with_test_ye=False)

    if not resolved_label:
        resolved_label = ye_ts_bot.translate_general_category(
            normalized_country, start_get_country2=False
        )

    if not resolved_label:
        resolved_label = country_2_title_work(country, With_Years=With_Years)

    if not resolved_label:
        resolved_label = find_wikidata(normalized_country)

    if not resolved_label:
        resolved_label = get_pop_All_18(normalized_country.lower(), "")

    if resolved_label:
        logger.info(f'>> Get_ scountry2 "{normalized_country}": cnt_la: {resolved_label}')
        return resolved_label

    return resolved_label
