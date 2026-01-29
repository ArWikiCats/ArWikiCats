"""

This module provides functionality to translate category titles
that follow a 'nat-year' pattern. It uses a pre-configured
bot (`yc_bot`) to handle the translation logic.
    "2000s American films": "أفلام أمريكية في عقد 2000",
"""

import functools

from ...helps import getLogger

logger = getLogger(__name__)
from ...translations import all_country_with_nat_ar
from ...translations_formats import (
    MultiDataFormatterBaseYearV2,
    format_year_country_data_v2,
)

# from ..main_processers.categories_patterns.COUNTRY_YEAR import COUNTRY_YEAR_DATA
formatted_data = {
    # "12th-century Indian books": "كتب هندية في القرن 12",
    "{year1} {en_nat} books": "كتب {female} في {year1}",
    # "20th-century Mexican literature": "أدب مكسيكي القرن 20",
    "{year1} {en_nat} literature": "أدب {male} في {year1}",
    # "coming-of-age story television programmes endings": "برامج تلفزيونية قصة تقدم في العمر انتهت في",
    "{year1} {en_nat} coming-of-age story television programmes endings": "برامج تلفزيونية قصة تقدم في العمر انتهت في {year1}",
    "{year1} {en_nat} films": "أفلام {female} في {year1}",
    "{year1} {en_nat} texts": "نصوص {female} في {year1}",
    "{en_nat} general election {year1}": "الانتخابات التشريعية {the_female} {year1}",
    "{en_nat} presidential election {year1}": "انتخابات الرئاسة {the_female} {year1}",
}


def populate_film_patterns(formatted_data):
    """
    Add Arabic translations for specific film-related category patterns into the provided formatted_data mapping.

    Updates formatted_data in-place with entries for base, year-prefixed, nat-prefixed, and "-endings"/" endings" variants for two film-related titles ("animated television series" and "children's animated adventure television series"), using both plain and gendered (`{female}`) value forms and year/placeholders (`{year1}`, `{en_nat}`).

    Parameters:
        formatted_data (dict): Mapping of pattern keys to translation strings; the function mutates this dict by inserting the generated patterns.
    """
    films_non_patterns_data = {
        "animated television series": {
            "value": "مسلسلات رسوم متحركة تلفزيونية",
            "value_nat": "مسلسلات رسوم متحركة تلفزيونية {female}",
        },
        "children's animated adventure television series": {
            "value": "مسلسلات مغامرات رسوم متحركة تلفزيونية للأطفال",
            "value_nat": "مسلسلات مغامرات رسوم متحركة تلفزيونية {female} للأطفال",
        },
    }
    for k, v in films_non_patterns_data.items():
        value_with_nat = v.get("value_nat")
        value = v.get("value")
        formatted_data.update(
            {
                f"{k}": f"{value}",
                f"{{year1}} {k}": f"{value} في {{year1}}",
                f"{{en_nat}} {k}": f"{value_with_nat}",
                f"{{year1}} {{en_nat}} {k}": f"{value_with_nat} في {{year1}}",
                f"{{year1}} {k}-endings": f"{value} انتهت في {{year1}}",
                f"{{year1}} {k} endings": f"{value} انتهت في {{year1}}",
                f"{{year1}} {{en_nat}} {k}-endings": f"{value_with_nat} انتهت في {{year1}}",
                f"{{year1}} {{en_nat}} {k} endings": f"{value_with_nat} انتهت في {{year1}}",
            }
        )


@functools.lru_cache(maxsize=1)
def _bot_new() -> MultiDataFormatterBaseYearV2:
    """
    Constructs and returns a MultiDataFormatterBaseYearV2 configured with nat-year translation patterns.

    Initializes the formatter with predefined pattern mappings and the available Arabic nationality data so it can expand category templates containing the placeholders `{en_nat}` and `{year1}` into Arabic nat-year phrases.

    Returns:
        MultiDataFormatterBaseYearV2: A formatter set up to format categories that combine nationality and year placeholders into Arabic translations.
    """
    # populate_film_patterns(formatted_data)

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
