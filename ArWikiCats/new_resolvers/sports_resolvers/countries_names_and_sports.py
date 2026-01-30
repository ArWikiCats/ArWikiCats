#!/usr/bin/python3
""" """

import functools
import logging

from ...new.handle_suffixes import resolve_sport_category_suffix_with_mapping
from ...translations import SPORT_KEY_RECORDS, all_country_with_nat_ar
from ...translations_formats import MultiDataFormatterBaseV2, format_multi_data_v2
from ..countries_names_resolvers.countries_names_data import formatted_data_en_ar_only
from ..nats_as_country_names import nats_keys_as_country_names
from ..teams_mappings_ends import teams_label_mappings_ends
from .utils import fix_keys
from .utils.formated_data import SPORTS_FORMATTED_DATA_NATS_AND_NAMES

logger = logging.getLogger(__name__)

# NOTE: patterns with only en-ar should be in formatted_data_en_ar_only countries_names.py to handle countries without gender details
# NOTE: patterns with only en-ar-time should be in COUNTRY_YEAR_DATA to handle countries-time without gender details


@functools.lru_cache(maxsize=1)
def _load_sports_formatted_data() -> dict[str, str]:
    sports_formatted_data = {
        # Category:yemeni Women's Football League
        "womens {en} {en_sport} league": "الدوري {the_male} {sport_team} للسيدات",
        "womens {en} {en_sport} league players": "لاعبات الدوري {the_male} {sport_team} للسيدات",
        "{en} womens {en_sport} league": "الدوري {the_male} {sport_team} للسيدات",
        "{en} womens {en_sport} league players": "لاعبات الدوري {the_male} {sport_team} للسيدات",
        "amateur {en_sport} world cup": "كأس العالم {sport_team} للهواة",
        "mens {en_sport} world cup": "كأس العالم {sport_team} للرجال",
        "womens {en_sport} world cup": "كأس العالم {sport_team} للسيدات",
        "{en_sport} world cup": "كأس العالم {sport_team}",
        "youth {en_sport} world cup": "كأس العالم {sport_team} للشباب",
        # sports_formatted_data data:
        # "Category:zaïrean wheelchair sports federation": "تصنيف:الاتحاد الزائيري للرياضة على الكراسي المتحركة",
        # "Category:surinamese sports federation": "تصنيف:الاتحاد السورينامي للرياضة",
        "{en} sports federation": "الاتحاد {the_male} للرياضة",
        "{en} wheelchair sports federation": "الاتحاد {the_male} للرياضة على الكراسي المتحركة",
        "{en} {en_sport} federation": "الاتحاد {the_male} {sport_team}",
        "olympic gold medalists for {en}": "فائزون بميداليات ذهبية أولمبية من {ar}",
        "olympic silver medalists for {en}": "فائزون بميداليات فضية أولمبية من {ar}",
        "olympic bronze medalists for {en}": "فائزون بميداليات برونزية أولمبية من {ar}",
        "olympic gold medalists for {en} in {en_sport}": "فائزون بميداليات ذهبية أولمبية من {ar} في {sport_label}",
        "olympic silver medalists for {en} in {en_sport}": "فائزون بميداليات فضية أولمبية من {ar} في {sport_label}",
        "olympic bronze medalists for {en} in {en_sport}": "فائزون بميداليات برونزية أولمبية من {ar} في {sport_label}",
        "{en} womens {en_sport} playerss": "لاعبات {sport_jobs} {females}",
        "womens {en_sport} playerss": "لاعبات {sport_jobs}",
        "{en} womens national {en_sport} team": "منتخب {ar} {sport_team} للسيدات",
        "{en} womens national {en_sport} team players": "لاعبات منتخب {ar} {sport_team} للسيدات",
        "{en} national {en_sport} team": "منتخب {ar} {sport_team}",
        "{en} national {en_sport} team players": "لاعبو منتخب {ar} {sport_team}",
        "{en} {en_sport} association": "الرابطة {the_female} {sport_team}",
        "womens {en} {en_sport} association": "الرابطة {the_female} {sport_team} للسيدات",
        "{en} womens international {en_sport} players": "لاعبات {sport_jobs} دوليات من {ar}",
        "{en} international {en_sport} players": "لاعبو {sport_jobs} دوليون من {ar}",
        "{en} international mens {en_sport} players": "لاعبو {sport_jobs} دوليون من {ar}",
        "{en} mens international {en_sport} players": "لاعبو {sport_jobs} دوليون من {ar}",
        "{en} international womens {en_sport} players": "لاعبات {sport_jobs} دوليات من {ar}",
        # data from p17_bot_sport_for_job.py
        # "national men's under-17 {en_sport} teams": "منتخبات {sport_jobs} تحت 17 سنة للرجال",
        "{en} under-13 international {en_sport} players": "لاعبو {sport_jobs} تحت 13 سنة دوليون من {ar}",
        "{en} under-14 international {en_sport} players": "لاعبو {sport_jobs} تحت 14 سنة دوليون من {ar}",
        "{en} under-15 international {en_sport} players": "لاعبو {sport_jobs} تحت 15 سنة دوليون من {ar}",
        "{en} under-16 international {en_sport} players": "لاعبو {sport_jobs} تحت 16 سنة دوليون من {ar}",
        "{en} under-17 international {en_sport} players": "لاعبو {sport_jobs} تحت 17 سنة دوليون من {ar}",
        "{en} under-18 international {en_sport} players": "لاعبو {sport_jobs} تحت 18 سنة دوليون من {ar}",
        "{en} under-19 international {en_sport} players": "لاعبو {sport_jobs} تحت 19 سنة دوليون من {ar}",
        "{en} under-20 international {en_sport} players": "لاعبو {sport_jobs} تحت 20 سنة دوليون من {ar}",
        "{en} under-21 international {en_sport} players": "لاعبو {sport_jobs} تحت 21 سنة دوليون من {ar}",
        "{en} under-23 international {en_sport} players": "لاعبو {sport_jobs} تحت 23 سنة دوليون من {ar}",
        "{en} under-24 international {en_sport} players": "لاعبو {sport_jobs} تحت 24 سنة دوليون من {ar}",
        "{en} under-13 international {en_sport} managers": "مدربو {sport_jobs} تحت 13 سنة دوليون من {ar}",
        "{en} under-14 international {en_sport} managers": "مدربو {sport_jobs} تحت 14 سنة دوليون من {ar}",
        "{en} under-15 international {en_sport} managers": "مدربو {sport_jobs} تحت 15 سنة دوليون من {ar}",
        "{en} under-16 international {en_sport} managers": "مدربو {sport_jobs} تحت 16 سنة دوليون من {ar}",
        "{en} under-17 international {en_sport} managers": "مدربو {sport_jobs} تحت 17 سنة دوليون من {ar}",
        "{en} under-18 international {en_sport} managers": "مدربو {sport_jobs} تحت 18 سنة دوليون من {ar}",
        "{en} under-19 international {en_sport} managers": "مدربو {sport_jobs} تحت 19 سنة دوليون من {ar}",
        "{en} under-20 international {en_sport} managers": "مدربو {sport_jobs} تحت 20 سنة دوليون من {ar}",
        "{en} under-21 international {en_sport} managers": "مدربو {sport_jobs} تحت 21 سنة دوليون من {ar}",
        "{en} under-23 international {en_sport} managers": "مدربو {sport_jobs} تحت 23 سنة دوليون من {ar}",
        "{en} under-24 international {en_sport} managers": "مدربو {sport_jobs} تحت 24 سنة دوليون من {ar}",
        "{en} olympics {en_sport}": "{sport_jobs} {ar} في الألعاب الأولمبية",
        "{en} summer olympics {en_sport}": "{sport_jobs} {ar} في الألعاب الأولمبية الصيفية",
        "{en} winter olympics {en_sport}": "{sport_jobs} {ar} في الألعاب الأولمبية الشتوية",
        "{en} {en_sport} manager history": "تاريخ مدربو {sport_jobs} {ar}",
        # data from SPORT_FORMATS_ENAR_P17_TEAM
        "{en} {en_sport} league": "دوري {ar} {sport_team}",
        "{en} professional {en_sport} league": "دوري {ar} {sport_team} للمحترفين",
        "{en} amateur {en_sport} cup": "كأس {ar} {sport_team} للهواة",
        "{en} youth {en_sport} cup": "كأس {ar} {sport_team} للشباب",
        "{en} mens {en_sport} cup": "كأس {ar} {sport_team} للرجال",
        "{en} womens {en_sport} cup": "كأس {ar} {sport_team} للسيدات",
        "{en} {en_sport} cup": "كأس {ar} {sport_team}",
        "{en} amateur {en_sport} championships": "بطولة {ar} {sport_team} للهواة",
        "{en} youth {en_sport} championships": "بطولة {ar} {sport_team} للشباب",
        "{en} mens {en_sport} championships": "بطولة {ar} {sport_team} للرجال",
        "{en} womens {en_sport} championships": "بطولة {ar} {sport_team} للسيدات",
        "{en} amateur {en_sport} championship": "بطولة {ar} {sport_team} للهواة",
        "{en} youth {en_sport} championship": "بطولة {ar} {sport_team} للشباب",
        "{en} mens {en_sport} championship": "بطولة {ar} {sport_team} للرجال",
        "{en} womens {en_sport} championship": "بطولة {ar} {sport_team} للسيدات",
        # ---national youth handball team
        "{en} {en_sport} national team": "منتخب {ar} {sport_team}",
        # Category:Denmark national football team staff
        "{en} {en_sport} national team staff": "طاقم منتخب {ar} {sport_team}",
        # Category:Denmark national football team non-playing staff
        "{en} {en_sport} national team non-playing staff": "طاقم منتخب {ar} {sport_team} غير اللاعبين",
        # Polish men's volleyball national team national junior men's
        "{en} national junior mens {en_sport} team": "منتخب {ar} {sport_team} للناشئين",
        "{en} national junior {en_sport} team": "منتخب {ar} {sport_team} للناشئين",
        "{en} national womens {en_sport} team": "منتخب {ar} {sport_team} للسيدات",
        "{en} mens national {en_sport} team": "منتخب {ar} {sport_team} للرجال",
        "{en} mens {en_sport} national team": "منتخب {ar} {sport_team} للرجال",
        "{en} national mens {en_sport} team": "منتخب {ar} {sport_team} للرجال",
        # Australian men's U23 national road cycling team
        "{en} mens u23 national {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة للرجال",
        "{en} national youth {en_sport} team": "منتخب {ar} {sport_team} للشباب",
        "{en} national womens {en_sport} team managers": "مدربو منتخب {ar} {sport_team} للسيدات",
        "{en} national {en_sport} team managers": "مدربو منتخب {ar} {sport_team}",
        "{en} national womens {en_sport} team coaches": "مدربو منتخب {ar} {sport_team} للسيدات",
        "{en} national {en_sport} team coaches": "مدربو منتخب {ar} {sport_team}",
        "{en} national womens {en_sport} team trainers": "مدربو منتخب {ar} {sport_team} للسيدات",
        "{en} national {en_sport} team trainers": "مدربو منتخب {ar} {sport_team}",
        "{en} national youth womens {en_sport} team": "منتخب {ar} {sport_team} للشابات",
        "{en} national junior womens {en_sport} team": "منتخب {ar} {sport_team} للناشئات",
        "{en} national amateur {en_sport} team": "منتخب {ar} {sport_team} للهواة",
        "{en} multi-national womens {en_sport} team": "منتخب {ar} {sport_team} متعددة الجنسيات للسيدات",
    }

    WOMENS_NATIONAL_DATA = {
        x.replace("womens national", "national womens"): v
        for x, v in sports_formatted_data.items()
        if "womens national" in x
    }

    sports_formatted_data.update(SPORTS_FORMATTED_DATA_NATS_AND_NAMES)
    sports_formatted_data.update(WOMENS_NATIONAL_DATA)
    sports_formatted_data.update(formatted_data_en_ar_only)  # NOTE: should not be here!
    return sports_formatted_data


@functools.lru_cache(maxsize=1)
def _load_nats_data() -> dict[str, dict[str, str]]:
    nats_data = {v["en"]: v for x, v in all_country_with_nat_ar.items() if v.get("ar") and v.get("en")}

    # nats_data.update(nats_keys_as_country_names)

    nats_data.update({x: v for x, v in nats_keys_as_country_names.items() if v.get("ar") and v.get("en")})
    return nats_data


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    nats_data = _load_nats_data()

    sports_data = {
        x: {
            "sport_label": v.get("label", ""),
            "sport_team": v.get("team", ""),
            "sport_jobs": v.get("jobs", ""),
        }
        for x, v in SPORT_KEY_RECORDS.items()
        if v.get("label")
    }
    sports_formatted_data = _load_sports_formatted_data()
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
    nats_data = _load_nats_data()

    category = fix_keys(category)
    if nats_data.get(category):
        return ""

    logger.debug(f"<<yellow>> start {category=}")

    both_bot = _load_bot()
    result = both_bot.search_all_category(category)

    logger.info(f"<<yellow>> end {category=}, {result=}")
    return result


def fix_result_callable(result: str, category: str, key: str, value: str) -> str:
    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    if key == "teams" and "national" in category:
        result = result.replace("فرق ", "منتخبات ")

    return result


def resolve_countries_names_sport_with_ends(category) -> str:
    category = fix_keys(category)
    logger.debug(f"<<yellow>> start {category=}")

    result = resolve_sport_category_suffix_with_mapping(
        category=category,
        data=teams_label_mappings_ends,
        callback=resolve_countries_names_sport,
        fix_result_callable=fix_result_callable,
    )
    logger.info(f"<<yellow>> end {category=}, {result=}")
    return result


__all__ = [
    "resolve_countries_names_sport",
    "resolve_countries_names_sport_with_ends",
]
