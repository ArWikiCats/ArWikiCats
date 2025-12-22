#!/usr/bin/python3
"""

"""
import functools
from ...helps import logger
from ...translations_formats import format_multi_data_v2, MultiDataFormatterBaseV2
from ...translations.nats.Nationality import all_country_with_nat_ar
from ...translations.sports.Sport_key import SPORT_KEY_RECORDS
from ..translations_resolvers.countries_names_data import formatted_data_en_ar_only
from .nats_as_country_names import nats_keys_as_country_names

# NOTE: patterns with only en-ar should be in formatted_data_en_ar_only countries_names.py to handle countries without gender details


sports_formatted_data = {
    "{en} {en_sport} federation": "الاتحاد {the_male} {sport_team}",

    "olympic gold medalists for {en}": "فائزون بميداليات ذهبية أولمبية من {ar}",
    "olympic gold medalists for {en} in {en_sport}": "فائزون بميداليات ذهبية أولمبية من {ar} في {sport_ar}",
    "olympic silver medalists for {en} in {en_sport}": "فائزون بميداليات فضية أولمبية من {ar} في {sport_ar}",
    "olympic bronze medalists for {en} in {en_sport}": "فائزون بميداليات برونزية أولمبية من {ar} في {sport_ar}",

    "{en} women's {en_sport} playerss": "لاعبات {sport_jobs} {females}",
    "women's {en_sport} playerss": "لاعبات {sport_jobs}",
    "{en} women's national {en_sport} team" : "منتخب {ar} {sport_team} للسيدات",
    "{en} women's national {en_sport} team players" : "لاعبات منتخب {ar} {sport_team} للسيدات",
    "{en} national {en_sport} team" : "منتخب {ar} {sport_team}",
    "{en} national {en_sport} team players" : "لاعبو منتخب {ar} {sport_team}",
    "{en} {en_sport} association": "الرابطة {the_female} {sport_team}",
    "women's {en} {en_sport} association": "الرابطة {the_female} {sport_team} للسيدات",


    "{en} women's international {en_sport} players": "لاعبات {sport_jobs} دوليات من {ar}",
    "{en} international {en_sport} players": "لاعبو {sport_jobs} دوليون من {ar}",

    "{en} international men's {en_sport} players": "لاعبو {sport_jobs} دوليون من {ar}",
    "{en} men's international {en_sport} players": "لاعبو {sport_jobs} دوليون من {ar}",
    "{en} international women's {en_sport} players": "لاعبات {sport_jobs} دوليات من {ar}",


    # data from p17_bot_sport_for_job.py
    "{en} under-13 international {en_sport} managers": "مدربو {sport_jobs} تحت 13 سنة دوليون من {ar}",
    "{en} under-13 international {en_sport} players": "لاعبو {sport_jobs} تحت 13 سنة دوليون من {ar}",
    "{en} under-14 international {en_sport} managers": "مدربو {sport_jobs} تحت 14 سنة دوليون من {ar}",
    "{en} under-14 international {en_sport} players": "لاعبو {sport_jobs} تحت 14 سنة دوليون من {ar}",
    "{en} under-15 international {en_sport} managers": "مدربو {sport_jobs} تحت 15 سنة دوليون من {ar}",
    "{en} under-15 international {en_sport} players": "لاعبو {sport_jobs} تحت 15 سنة دوليون من {ar}",
    "{en} under-16 international {en_sport} managers": "مدربو {sport_jobs} تحت 16 سنة دوليون من {ar}",
    "{en} under-16 international {en_sport} players": "لاعبو {sport_jobs} تحت 16 سنة دوليون من {ar}",
    "{en} under-17 international {en_sport} managers": "مدربو {sport_jobs} تحت 17 سنة دوليون من {ar}",
    "{en} under-17 international {en_sport} players": "لاعبو {sport_jobs} تحت 17 سنة دوليون من {ar}",
    "{en} under-18 international {en_sport} managers": "مدربو {sport_jobs} تحت 18 سنة دوليون من {ar}",
    "{en} under-18 international {en_sport} players": "لاعبو {sport_jobs} تحت 18 سنة دوليون من {ar}",
    "{en} under-19 international {en_sport} managers": "مدربو {sport_jobs} تحت 19 سنة دوليون من {ar}",
    "{en} under-19 international {en_sport} players": "لاعبو {sport_jobs} تحت 19 سنة دوليون من {ar}",
    "{en} under-20 international {en_sport} managers": "مدربو {sport_jobs} تحت 20 سنة دوليون من {ar}",
    "{en} under-20 international {en_sport} players": "لاعبو {sport_jobs} تحت 20 سنة دوليون من {ar}",
    "{en} under-21 international {en_sport} managers": "مدربو {sport_jobs} تحت 21 سنة دوليون من {ar}",
    "{en} under-21 international {en_sport} players": "لاعبو {sport_jobs} تحت 21 سنة دوليون من {ar}",
    "{en} under-23 international {en_sport} managers": "مدربو {sport_jobs} تحت 23 سنة دوليون من {ar}",
    "{en} under-23 international {en_sport} players": "لاعبو {sport_jobs} تحت 23 سنة دوليون من {ar}",
    "{en} under-24 international {en_sport} managers": "مدربو {sport_jobs} تحت 24 سنة دوليون من {ar}",
    "{en} under-24 international {en_sport} players": "لاعبو {sport_jobs} تحت 24 سنة دوليون من {ar}",

    "{en} olympics {en_sport}": "{sport_jobs} {ar} في الألعاب الأولمبية",
    "{en} summer olympics {en_sport}": "{sport_jobs} {ar} في الألعاب الأولمبية الصيفية",

    "{en} winter olympics {en_sport}": "{sport_jobs} {ar} في الألعاب الأولمبية الشتوية",
    "{en} {en_sport} manager history": "تاريخ مدربو {sport_jobs} {ar}",
}

WOMENS_NATIONAL_DATA = {
    x.replace("women's national", "national women's"): v
    for x, v in sports_formatted_data.items()
    if "women's national" in x
}

sports_formatted_data.update(WOMENS_NATIONAL_DATA)
sports_formatted_data.update(formatted_data_en_ar_only)


def remove_the(text: str) -> str:
    if text.lower().startswith("the "):
        return text[4:]
    return text


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    nats_data = {
        remove_the(v["en"]): v
        for x, v in all_country_with_nat_ar.items()
        if v.get("ar") and v.get("en")
    }

    nats_data.update(nats_keys_as_country_names)

    nats_data.update({
        x: v for x, v in nats_keys_as_country_names.items()
        if v.get("ar") and v.get("en")
    })

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


@functools.lru_cache(maxsize=10000)
def resolve_countries_names_sport(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_countries_names_sport: {category=}")

    both_bot = _load_bot()
    result = both_bot.search_all_category(category)

    logger.debug(f"<<yellow>> end resolve_countries_names_sport: {category=}, {result=}")
    return result


__all__ = [
    "resolve_countries_names_sport",
]
