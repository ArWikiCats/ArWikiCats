#!/usr/bin/python3
"""
Resolve country names categories translations
"""
from typing import Dict
import functools
from ...helps import logger
from ...translations_formats import FormatData, MultiDataFormatterBase
from ...translations import countries_from_nat, COUNTRY_LABEL_OVERRIDES

# TODO: add data from ArWikiCats/translations/sports/olympics_data.py
medalists_data = {
    "central-american-and-caribbean-games": "ألعاب أمريكا الوسطى والكاريبي",
    # "central american and caribbean games": "ألعاب أمريكا الوسطى والكاريبي",
    "african games": "الألعاب الإفريقية",
    "all-africa games": "ألعاب عموم إفريقيا",
    "asian games": "الألعاب الآسيوية",
    "central american games": "ألعاب أمريكا الوسطى",
    "commonwealth games": "ألعاب الكومنولث",
    "deaflympic games": "ألعاب ديفلمبياد",
    "european youth olympic winter": "الألعاب الأولمبية الشبابية الأوروبية الشتوية",
    "european youth olympic": "الألعاب الأولمبية الشبابية الأوروبية",
    "islamic solidarity games": "ألعاب التضامن الإسلامي",
    "jeux de la francophonie": "الألعاب الفرانكوفونية",
    "military world games" : "دورة الألعاب العسكرية",
    "olympic games": "الألعاب الأولمبية",
    "olympics": "الألعاب الأولمبية",
    "pan american games": "دورة الألعاب الأمريكية",
    "paralympics games": "الألعاب البارالمبية",
    "south american games": "ألعاب أمريكا الجنوبية",
    "universiade": "الألعاب الجامعية",
    "world games" : "دورة الألعاب العالمية",
    "youth olympic games": "الألعاب الأولمبية الشبابية",
    "youth olympics": "الألعاب الأولمبية الشبابية",
}

# NOTE: formatted_data used in other resolver
formatted_data: Dict[str, str] = {
    "olympic gold medalists for {en}": "فائزون بميداليات ذهبية أولمبية من {ar}",
    "olympic gold medalists for {en} in alpine skiing": "فائزون بميداليات ذهبية أولمبية من {ar} في التزلج على المنحدرات الثلجية",
}

for key, value in medalists_data.items():
    formatted_data.update({
        f"{key} medalists for {{en}}" : f"فائزون بميداليات {value} من {{ar}}",
        f"{key} bronze medalists for {{en}}" : f"فائزون بميداليات برونزية في {value} من {{ar}}",
        f"{key} gold medalists for {{en}}" : f"فائزون بميداليات ذهبية في {value} من {{ar}}",
        f"{key} silver medalists for {{en}}" : f"فائزون بميداليات فضية في {value} من {{ar}}",
    })

countries_from_nat_data: Dict[str, str] = dict(countries_from_nat)

# TODO: update countries_from_nat_data with COUNTRY_LABEL_OVERRIDES after check any issues!
# countries_from_nat_data.update(COUNTRY_LABEL_OVERRIDES)


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBase:

    return FormatData(
        formatted_data,
        countries_from_nat_data,
        key_placeholder="{en}",
        value_placeholder="{ar}",
        text_before="the ",
        regex_filter=r"[\w-]",
    )


@functools.lru_cache(maxsize=10000)
def resolve_countries_names_medalists(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_countries_names_medalists: {category=}")

    nat_bot = _load_bot()
    result = nat_bot.search_all_category(category)

    logger.debug(f"<<yellow>> end resolve_countries_names_medalists: {category=}, {result=}")
    return result


__all__ = [
    "resolve_countries_names_medalists",
]
