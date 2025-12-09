#!/usr/bin/python3
""" """
import functools
from ..translations_formats import format_multi_data_v2, MultiDataFormatterBaseV2
from ..translations.nats.Nationality import all_country_with_nat_ar
from ..translations.sports.Sport_key import SPORT_KEY_RECORDS

sports_formatted_data = {
    "{country_en} {sport_en} federation": "الاتحاد {the_male} {sport_team}",
    "{country_en} testxx": "{country_ar} اختبار!",
    "{country_en}": "{country_ar}",
    "olympic gold medalists for {country_en}": "فائزون بميداليات ذهبية أولمبية من {country_ar}",
    "olympic gold medalists for {country_en} in alpine skiing": "فائزون بميداليات ذهبية أولمبية من {country_ar} في التزلج على المنحدرات الثلجية",
    "olympic gold medalists for {country_en} in {sport_en}": "فائزون بميداليات ذهبية أولمبية من {country_ar} في {sport_ar}",
}


def remove_the(text: str) -> str:
    if text.lower().startswith("the "):
        return text[4:]
    return text


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    nats_data = {
        remove_the(v["en"]): {
            "country_ar": v["ar"],
            "the_male": v["the_male"],
        }
        for x, v in all_country_with_nat_ar.items()
        if v.get("ar") and v.get("en")
    }

    sports_data = {
        x: {
            "sport_ar": v["label"],
            "sport_team": v["team"],
        }
        for x, v in SPORT_KEY_RECORDS.items()
        if v.get("label")
    }

    both_bot = format_multi_data_v2(
        formatted_data=sports_formatted_data,
        data_list=nats_data,
        key_placeholder="{country_en}",
        data_list2=sports_data,
        key2_placeholder="{sport_en}",
        text_after="",
        text_before="the ",
        search_first_part=True,
    )
    return both_bot


def resolve_countries_names_sport(category: str) -> str:
    normalized_category = category.lower().replace("category:", "")
    both_bot = _load_bot()

    result = both_bot.search_all(normalized_category)

    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result
    return result


__all__ = [
    "resolve_countries_names_sport",
]
