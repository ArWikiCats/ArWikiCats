"""

This module provides functionality to translate category titles
that follow a 'nat-year' pattern. It uses a pre-configured
bot (`yc_bot`) to handle the translation logic.
    "2000s American films": "أفلام أمريكية في عقد 2000",
"""

import functools

from ...helps import logger
from ...translations import all_country_with_nat_ar
from ...translations_formats import (
    MultiDataFormatterBaseYearV2,
    format_year_country_data_v2,
)

# from ..main_processers.categories_patterns.COUNTRY_YEAR import COUNTRY_YEAR_DATA


@functools.lru_cache(maxsize=1)
def _bot_new() -> MultiDataFormatterBaseYearV2:
    formatted_data = {
        # "coming-of-age story television programmes endings": "برامج تلفزيونية قصة تقدم في العمر انتهت في",
        "{year1} {en_nat} coming-of-age story television programmes endings": "برامج تلفزيونية قصة تقدم في العمر انتهت في {year1}",
        "{year1} {en_nat} films": "أفلام {female} في {year1}",
        "{en_nat} general election {year1}": "الانتخابات التشريعية {the_female} {year1}",
        "{en_nat} presidential election {year1}": "انتخابات الرئاسة {the_female} {year1}",
    }

    nats_data = {x: v for x, v in all_country_with_nat_ar.items() if v.get("ar")}

    return format_year_country_data_v2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en_nat}",
        key2_placeholder="{year1}",
        value2_placeholder="{year1}",
        text_after="",
        text_before="the ",
    )


@functools.lru_cache(maxsize=10000)
def resolve_nats_time_v2(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_nats_time_v2: {category=}")
    yc_bot = _bot_new()

    result = yc_bot.search_all_category(category)

    logger.info_if_or_debug(f"<<yellow>> end resolve_nats_time_v2: {category=}, {result=}", result)
    return result or ""


__all__ = [
    "resolve_nats_time_v2",
]
