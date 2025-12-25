#!/usr/bin/python3
"""
This module is responsible for retrieving localized information for a specified country.
"""

import functools

from . import country2_lab

from ..fix import fixtitle
from ..helps.log import logger
from ..make_bots.lazy_data_bots.bot_2018 import get_pop_All_18
from . import ye_ts_bot
from ..ma_bots2.country2_bots.country2_label_bot import country_2_title_work


@functools.lru_cache(maxsize=None)
def Get_country2(country: str, with_years: bool = True, fix_title=True) -> str:
    """Retrieve information related to a specified country."""

    normalized_country = country.lower().strip()
    logger.info(f'>> Get_country2 "{normalized_country}":')

    resolved_label = country2_lab.get_lab_for_country2(country)

    if not resolved_label:
        resolved_label = ye_ts_bot.translate_general_category(
            normalized_country, start_get_country2=False, fix_title=False
        )

    _label = country_2_title_work(country, with_years=with_years)
    # if not resolved_label and _label:
    if _label:
        resolved_label = _label

    if not resolved_label:
        resolved_label = get_pop_All_18(normalized_country.lower(), "")

    if resolved_label and fix_title:
        resolved_label = fixtitle.fixlabel(resolved_label, en=normalized_country)

    logger.info(f'>> Get_ scountry2 "{normalized_country}": cnt_la: {resolved_label}')

    resolved_label = " ".join(resolved_label.strip().split())

    return resolved_label
