#!/usr/bin/python3
"""

"""
import functools
from ..translations_formats import format_multi_data_v2, MultiDataFormatterBaseV2
from ..translations.nats.Nationality import all_country_with_nat_ar
from ..translations.sports.Sport_key import SPORT_KEY_RECORDS

sports_formatted_data = {
    "{en} {en_sport} federation": "الاتحاد {the_male} {sport_team}",
    "{en} testxx": "{ar} اختبار!",
    "{en}": "{ar}",
    "olympic gold medalists for {en}": "فائزون بميداليات ذهبية أولمبية من {ar}",
    "olympic gold medalists for {en} in alpine skiing": "فائزون بميداليات ذهبية أولمبية من {ar} في التزلج على المنحدرات الثلجية",
    "olympic gold medalists for {en} in {en_sport}": "فائزون بميداليات ذهبية أولمبية من {ar} في {sport_ar}",

    "{en} women's {en_sport} playerss": "لاعبات {sport_jobs} {females}",
    "women's {en_sport} playerss": "لاعبات {sport_jobs}",

    "{en} women's national {en_sport} team" : "منتخب {ar} {sport_team} للسيدات",
    "{en} women's national {en_sport} team players" : "لاعبات منتخب {ar} {sport_team} للسيدات",

    "{en} national {en_sport} team" : "منتخب {ar} {sport_team}",
    "{en} national {en_sport} team players" : "لاعبو منتخب {ar} {sport_team}",

    "{en} women's international footballers": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's youth international footballers": "لاعبات منتخب {ar} لكرة القدم للشابات",
    "{en} women's international {en_sport} players": "لاعبات {sport_jobs} دوليات من {ar}",

    "{en} international footballers": "لاعبو منتخب {ar} لكرة القدم",
    "{en} international {en_sport} players": "لاعبو {sport_jobs} دوليون من {ar}",
}

WOMENS_NATIONAL_DATA = {
    x.replace("women's national", "national women's"): v
    for x, v in sports_formatted_data.items()
    if "women's national" in x
}

sports_formatted_data.update(WOMENS_NATIONAL_DATA)


def remove_the(text: str) -> str:
    if text.lower().startswith("the "):
        return text[4:]
    return text


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    nats_data = {
        remove_the(v["en"]): {
            "ar": v["ar"],
            "the_male": v["the_male"],
        }
        for x, v in all_country_with_nat_ar.items()
        if v.get("ar") and v.get("en")
    }

    sports_data = {
        x: {
            "sport_ar": v["label"],
            "sport_team": v["team"],
            "sport_jobs": v["jobs"],
        }
        for x, v in SPORT_KEY_RECORDS.items()
        if v.get("label")
    }

    both_bot = format_multi_data_v2(
        formatted_data=sports_formatted_data,
        data_list=nats_data,
        key_placeholder="{en}",
        data_list2=sports_data,
        key2_placeholder="{en_sport}",
        text_after="",
        text_before="the ",
        search_first_part=True,
        use_other_formatted_data=True,
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
