#!/usr/bin/python3
"""
NOTE: this file has alot of formatted_data

TODO: merge with sports_resolvers/nationalities_and_sports.py

"""

import functools
import re

from ...helps import getLogger, len_print
from ...new.handle_suffixes import resolve_sport_category_suffix_with_mapping
from ...translations import SPORT_KEY_RECORDS, Nat_women
from ...translations_formats import MultiDataFormatterBase, format_multi_data_v2
from ..nats_as_country_names import nats_keys_as_country_names

logger = getLogger(__name__)

# TODO: add data from new_for_nat_female_xo_team_additional
new_for_nat_female_xo_team_2 = {
    # "yemeni football": "كرة قدم يمنية",
    # "{en} {en_sport}": "{sport_jobs} {female}",  # Category:American_basketball
    "{en} {en_sport} leagues": "دوريات {sport_jobs} {female}",
    "{en} {en_sport} competitions": "منافسات {sport_jobs} {female}",
    "{en_sport} competitions": "منافسات {sport_jobs}",
    # "{en} {en_sport}": "{sport_label} {the_female}",  # Category:American_basketball
    # "yemeni national football": "كرة قدم وطنية يمنية",
    "{en} national {en_sport}": "{sport_jobs} وطنية {female}",
    "{en} womens {en_sport}": "{sport_jobs} {female} نسائية",
    "amateur {en_sport} world cup": "كأس العالم {sport_team} للهواة",
    "mens {en_sport} world cup": "كأس العالم {sport_team} للرجال",
    "womens {en_sport} world cup": "كأس العالم {sport_team} للسيدات",
    "{en_sport} world cup": "كأس العالم {sport_team}",
    "youth {en_sport} world cup": "كأس العالم {sport_team} للشباب",
    "{en} amateur {en_sport} cup": "كأس {female} {sport_jobs} للهواة",
    "{en} youth {en_sport} cup": "كأس {female} {sport_jobs} للشباب",
    "{en} mens {en_sport} cup": "كأس {female} {sport_jobs} للرجال",
    "{en} womens {en_sport} cup": "كأس {female} {sport_jobs} للسيدات",
    # "{en} defunct {en_sport} cups": "كؤوس {sport_jobs} {female} سابقة",
    # "{en} {en_sport} cups": "كؤوس {sport_jobs} {female}",
    # "{en} domestic {en_sport} cups": "كؤوس {sport_jobs} {female} محلية",
    "{en} defunct {en_sport} cup": "كؤوس {sport_jobs} {female} سابقة",
    "{en} {en_sport} cup": "كؤوس {sport_jobs} {female}",
    "{en} domestic {en_sport} cup": "كؤوس {sport_jobs} {female} محلية",
    "{en} {en_sport} teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national teams": "منتخبات {sport_jobs} {female}",
    # tab[Category:Canadian domestic Soccer: "تصنيف:كرة قدم كندية محلية"
    "{en} domestic {en_sport}": "{sport_jobs} {female} محلية",
    "{en} domestic womens {en_sport}": "{sport_jobs} {female} محلية للسيدات",
    "{en} {en_sport} championships": "بطولات {sport_jobs} {female}",
    "{en} national {en_sport} championships": "بطولات {sport_jobs} وطنية {female}",
    # "{en} national {en_sport} champions": "أبطال بطولات {sport_jobs} وطنية {female}",
    "{en} national {en_sport} champions": "أبطال {sport_jobs} وطنية {female}",
    "{en} {en_sport} super leagues": "دوريات سوبر {sport_jobs} {female}",
    "{en} current {en_sport} seasons": "مواسم {sport_jobs} {female} حالية",
    # ---
    "{en} professional {en_sport}": "{sport_jobs} {female} للمحترفين",
    "{en} indoor {en_sport}": "{sport_jobs} {female} داخل الصالات",
    "{en} outdoor {en_sport}": "{sport_jobs} {female} في الهواء الطلق",
    "{en} defunct indoor {en_sport}": "{sport_jobs} {female} داخل الصالات سابقة",
    "{en} defunct outdoor {en_sport}": "{sport_jobs} {female} في الهواء الطلق سابقة",
    "{en} reserve {en_sport}": "{sport_jobs} {female} احتياطية",
    "{en} defunct {en_sport}": "{sport_jobs} {female} سابقة",
    # [european national womens volleyball teams] = "منتخبات كرة طائرة وطنية أوروبية للسيدات"
    "{en} national womens {en_sport} teams": "منتخبات {sport_jobs} وطنية {female} للسيدات",
    "{en} national {en_sport} teams": "منتخبات {sport_jobs} وطنية {female}",
    "{en} national a {en_sport} teams": "منتخبات {sport_jobs} محليين {female}",
    "{en} national b {en_sport} teams": "منتخبات {sport_jobs} رديفة {female}",
    "{en} national reserve {en_sport} teams": "منتخبات {sport_jobs} وطنية احتياطية {female}",
    "{en} national {en_sport} teams premier": "منتخبات {sport_jobs} وطنية {female} من الدرجة الممتازة",
    "{en} {en_sport} teams premier": "فرق {sport_jobs} {female} من الدرجة الممتازة",
}

new_for_nat_female_xo_team_additional = {
    "{en} national amateur under-13 {en_sport}": "{sport_jobs} وطنية {female} تحت 13 سنة للهواة",
    "{en} national amateur under-14 {en_sport}": "{sport_jobs} وطنية {female} تحت 14 سنة للهواة",
    "{en} national amateur under-15 {en_sport}": "{sport_jobs} وطنية {female} تحت 15 سنة للهواة",
    "{en} national amateur under-16 {en_sport}": "{sport_jobs} وطنية {female} تحت 16 سنة للهواة",
    "{en} national amateur under-17 {en_sport}": "{sport_jobs} وطنية {female} تحت 17 سنة للهواة",
    "{en} national amateur under-18 {en_sport}": "{sport_jobs} وطنية {female} تحت 18 سنة للهواة",
    "{en} national amateur under-19 {en_sport}": "{sport_jobs} وطنية {female} تحت 19 سنة للهواة",
    "{en} national amateur under-20 {en_sport}": "{sport_jobs} وطنية {female} تحت 20 سنة للهواة",
    "{en} national amateur under-21 {en_sport}": "{sport_jobs} وطنية {female} تحت 21 سنة للهواة",
    "{en} national amateur under-23 {en_sport}": "{sport_jobs} وطنية {female} تحت 23 سنة للهواة",
    "{en} national amateur under-24 {en_sport}": "{sport_jobs} وطنية {female} تحت 24 سنة للهواة",
    "{en} national amateur {en_sport}": "{sport_jobs} وطنية {female} للهواة",
    "{en} national junior mens under-13 {en_sport}": "{sport_jobs} وطنية {female} تحت 13 سنة للناشئين",
    "{en} national junior mens under-14 {en_sport}": "{sport_jobs} وطنية {female} تحت 14 سنة للناشئين",
    "{en} national junior mens under-15 {en_sport}": "{sport_jobs} وطنية {female} تحت 15 سنة للناشئين",
    "{en} national junior mens under-16 {en_sport}": "{sport_jobs} وطنية {female} تحت 16 سنة للناشئين",
    "{en} national junior mens under-17 {en_sport}": "{sport_jobs} وطنية {female} تحت 17 سنة للناشئين",
    "{en} national junior mens under-18 {en_sport}": "{sport_jobs} وطنية {female} تحت 18 سنة للناشئين",
    "{en} national junior mens under-19 {en_sport}": "{sport_jobs} وطنية {female} تحت 19 سنة للناشئين",
    "{en} national junior mens under-20 {en_sport}": "{sport_jobs} وطنية {female} تحت 20 سنة للناشئين",
    "{en} national junior mens under-21 {en_sport}": "{sport_jobs} وطنية {female} تحت 21 سنة للناشئين",
    "{en} national junior mens under-23 {en_sport}": "{sport_jobs} وطنية {female} تحت 23 سنة للناشئين",
    "{en} national junior mens under-24 {en_sport}": "{sport_jobs} وطنية {female} تحت 24 سنة للناشئين",
    "{en} national junior mens {en_sport}": "{sport_jobs} وطنية {female} للناشئين",
    "{en} national junior womens under-13 {en_sport}": "{sport_jobs} وطنية {female} تحت 13 سنة للناشئات",
    "{en} national junior womens under-14 {en_sport}": "{sport_jobs} وطنية {female} تحت 14 سنة للناشئات",
    "{en} national junior womens under-15 {en_sport}": "{sport_jobs} وطنية {female} تحت 15 سنة للناشئات",
    "{en} national junior womens under-16 {en_sport}": "{sport_jobs} وطنية {female} تحت 16 سنة للناشئات",
    "{en} national junior womens under-17 {en_sport}": "{sport_jobs} وطنية {female} تحت 17 سنة للناشئات",
    "{en} national junior womens under-18 {en_sport}": "{sport_jobs} وطنية {female} تحت 18 سنة للناشئات",
    "{en} national junior womens under-19 {en_sport}": "{sport_jobs} وطنية {female} تحت 19 سنة للناشئات",
    "{en} national junior womens under-20 {en_sport}": "{sport_jobs} وطنية {female} تحت 20 سنة للناشئات",
    "{en} national junior womens under-21 {en_sport}": "{sport_jobs} وطنية {female} تحت 21 سنة للناشئات",
    "{en} national junior womens under-23 {en_sport}": "{sport_jobs} وطنية {female} تحت 23 سنة للناشئات",
    "{en} national junior womens under-24 {en_sport}": "{sport_jobs} وطنية {female} تحت 24 سنة للناشئات",
    "{en} national junior womens {en_sport}": "{sport_jobs} وطنية {female} للناشئات",
    "{en} national mens under-13 {en_sport}": "{sport_jobs} وطنية {female} تحت 13 سنة للرجال",
    "{en} national mens under-14 {en_sport}": "{sport_jobs} وطنية {female} تحت 14 سنة للرجال",
    "{en} national mens under-15 {en_sport}": "{sport_jobs} وطنية {female} تحت 15 سنة للرجال",
    "{en} national mens under-16 {en_sport}": "{sport_jobs} وطنية {female} تحت 16 سنة للرجال",
    "{en} national mens under-17 {en_sport}": "{sport_jobs} وطنية {female} تحت 17 سنة للرجال",
    "{en} national mens under-18 {en_sport}": "{sport_jobs} وطنية {female} تحت 18 سنة للرجال",
    "{en} national mens under-19 {en_sport}": "{sport_jobs} وطنية {female} تحت 19 سنة للرجال",
    "{en} national mens under-20 {en_sport}": "{sport_jobs} وطنية {female} تحت 20 سنة للرجال",
    "{en} national mens under-21 {en_sport}": "{sport_jobs} وطنية {female} تحت 21 سنة للرجال",
    "{en} national mens under-23 {en_sport}": "{sport_jobs} وطنية {female} تحت 23 سنة للرجال",
    "{en} national mens under-24 {en_sport}": "{sport_jobs} وطنية {female} تحت 24 سنة للرجال",
    "{en} national mens {en_sport}": "{sport_jobs} وطنية {female} للرجال",
    "{en} national under-13 {en_sport}": "{sport_jobs} وطنية {female} تحت 13 سنة",
    "{en} national under-14 {en_sport}": "{sport_jobs} وطنية {female} تحت 14 سنة",
    "{en} national under-15 {en_sport}": "{sport_jobs} وطنية {female} تحت 15 سنة",
    "{en} national under-16 {en_sport}": "{sport_jobs} وطنية {female} تحت 16 سنة",
    "{en} national under-17 {en_sport}": "{sport_jobs} وطنية {female} تحت 17 سنة",
    "{en} national under-18 {en_sport}": "{sport_jobs} وطنية {female} تحت 18 سنة",
    "{en} national under-19 {en_sport}": "{sport_jobs} وطنية {female} تحت 19 سنة",
    "{en} national under-20 {en_sport}": "{sport_jobs} وطنية {female} تحت 20 سنة",
    "{en} national under-21 {en_sport}": "{sport_jobs} وطنية {female} تحت 21 سنة",
    "{en} national under-23 {en_sport}": "{sport_jobs} وطنية {female} تحت 23 سنة",
    "{en} national under-24 {en_sport}": "{sport_jobs} وطنية {female} تحت 24 سنة",
    "{en} national womens under-13 {en_sport}": "{sport_jobs} وطنية {female} تحت 13 سنة للسيدات",
    "{en} national womens under-14 {en_sport}": "{sport_jobs} وطنية {female} تحت 14 سنة للسيدات",
    "{en} national womens under-15 {en_sport}": "{sport_jobs} وطنية {female} تحت 15 سنة للسيدات",
    "{en} national womens under-16 {en_sport}": "{sport_jobs} وطنية {female} تحت 16 سنة للسيدات",
    "{en} national womens under-17 {en_sport}": "{sport_jobs} وطنية {female} تحت 17 سنة للسيدات",
    "{en} national womens under-18 {en_sport}": "{sport_jobs} وطنية {female} تحت 18 سنة للسيدات",
    "{en} national womens under-19 {en_sport}": "{sport_jobs} وطنية {female} تحت 19 سنة للسيدات",
    "{en} national womens under-20 {en_sport}": "{sport_jobs} وطنية {female} تحت 20 سنة للسيدات",
    "{en} national womens under-21 {en_sport}": "{sport_jobs} وطنية {female} تحت 21 سنة للسيدات",
    "{en} national womens under-23 {en_sport}": "{sport_jobs} وطنية {female} تحت 23 سنة للسيدات",
    "{en} national womens under-24 {en_sport}": "{sport_jobs} وطنية {female} تحت 24 سنة للسيدات",
    "{en} national womens {en_sport}": "{sport_jobs} وطنية {female} للسيدات",
    "{en} national youth under-13 {en_sport}": "{sport_jobs} وطنية {female} تحت 13 سنة للشباب",
    "{en} national youth under-14 {en_sport}": "{sport_jobs} وطنية {female} تحت 14 سنة للشباب",
    "{en} national youth under-15 {en_sport}": "{sport_jobs} وطنية {female} تحت 15 سنة للشباب",
    "{en} national youth under-16 {en_sport}": "{sport_jobs} وطنية {female} تحت 16 سنة للشباب",
    "{en} national youth under-17 {en_sport}": "{sport_jobs} وطنية {female} تحت 17 سنة للشباب",
    "{en} national youth under-18 {en_sport}": "{sport_jobs} وطنية {female} تحت 18 سنة للشباب",
    "{en} national youth under-19 {en_sport}": "{sport_jobs} وطنية {female} تحت 19 سنة للشباب",
    "{en} national youth under-20 {en_sport}": "{sport_jobs} وطنية {female} تحت 20 سنة للشباب",
    "{en} national youth under-21 {en_sport}": "{sport_jobs} وطنية {female} تحت 21 سنة للشباب",
    "{en} national youth under-23 {en_sport}": "{sport_jobs} وطنية {female} تحت 23 سنة للشباب",
    "{en} national youth under-24 {en_sport}": "{sport_jobs} وطنية {female} تحت 24 سنة للشباب",
    "{en} national youth womens under-13 {en_sport}": "{sport_jobs} وطنية {female} تحت 13 سنة للشابات",
    "{en} national youth womens under-14 {en_sport}": "{sport_jobs} وطنية {female} تحت 14 سنة للشابات",
    "{en} national youth womens under-15 {en_sport}": "{sport_jobs} وطنية {female} تحت 15 سنة للشابات",
    "{en} national youth womens under-16 {en_sport}": "{sport_jobs} وطنية {female} تحت 16 سنة للشابات",
    "{en} national youth womens under-17 {en_sport}": "{sport_jobs} وطنية {female} تحت 17 سنة للشابات",
    "{en} national youth womens under-18 {en_sport}": "{sport_jobs} وطنية {female} تحت 18 سنة للشابات",
    "{en} national youth womens under-19 {en_sport}": "{sport_jobs} وطنية {female} تحت 19 سنة للشابات",
    "{en} national youth womens under-20 {en_sport}": "{sport_jobs} وطنية {female} تحت 20 سنة للشابات",
    "{en} national youth womens under-21 {en_sport}": "{sport_jobs} وطنية {female} تحت 21 سنة للشابات",
    "{en} national youth womens under-23 {en_sport}": "{sport_jobs} وطنية {female} تحت 23 سنة للشابات",
    "{en} national youth womens under-24 {en_sport}": "{sport_jobs} وطنية {female} تحت 24 سنة للشابات",
    "{en} national youth womens {en_sport}": "{sport_jobs} وطنية {female} للشابات",
    "{en} national youth {en_sport}": "{sport_jobs} وطنية {female} للشباب",
    "{en} under-13 {en_sport}": "{sport_jobs} {female} تحت 13 سنة",
    "{en} under-14 {en_sport}": "{sport_jobs} {female} تحت 14 سنة",
    "{en} under-15 {en_sport}": "{sport_jobs} {female} تحت 15 سنة",
    "{en} under-16 {en_sport}": "{sport_jobs} {female} تحت 16 سنة",
    "{en} under-17 {en_sport}": "{sport_jobs} {female} تحت 17 سنة",
    "{en} under-18 {en_sport}": "{sport_jobs} {female} تحت 18 سنة",
    "{en} under-19 {en_sport}": "{sport_jobs} {female} تحت 19 سنة",
    "{en} under-20 {en_sport}": "{sport_jobs} {female} تحت 20 سنة",
    "{en} under-21 {en_sport}": "{sport_jobs} {female} تحت 21 سنة",
    "{en} under-23 {en_sport}": "{sport_jobs} {female} تحت 23 سنة",
    "{en} under-24 {en_sport}": "{sport_jobs} {female} تحت 24 سنة",
}

new_for_nat_female_xo_team_2.update(new_for_nat_female_xo_team_additional)


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBase:
    nats_data = {x: {"female": v} for x, v in Nat_women.items()}
    sport_key_records = dict(SPORT_KEY_RECORDS)
    sport_key_records.get("sports", {}).update(
        {
            "jobs": "رياضية",
        }
    )
    nats_data.update({x: {"female": v.get("female")} for x, v in nats_keys_as_country_names.items() if v.get("female")})

    sports_data = {
        x: {
            "sport_label": v.get("label", ""),
            "sport_team": v.get("team", ""),
            "sport_jobs": v.get("jobs", ""),
        }
        for x, v in SPORT_KEY_RECORDS.items()
        if v.get("jobs")
    }

    return format_multi_data_v2(
        formatted_data=new_for_nat_female_xo_team_2,
        data_list=nats_data,
        key_placeholder="{en}",
        data_list2=sports_data,
        key2_placeholder="{en_sport}",
        text_after=" people",
        text_before="the ",
        search_first_part=True,
        use_other_formatted_data=True,
    )


@functools.lru_cache(maxsize=1)
def _load_end_key_mappings() -> dict[str, str]:
    """
    Provide a mapping of English end-key phrases to Arabic templates for label substitution.

    The returned mapping uses the `{lab}` placeholder where a category label will be inserted.
    Keys are ordered so that phrases with more words and longer length appear first, which helps
    matching routines prefer longer/multi-word endings before shorter ones.

    Returns:
        dict[str, str]: Mapping from English end-key phrase to Arabic template containing `{lab}`.
    """
    keys_ending = {
        "teams": "فرق {lab}",
        "premier": "{lab} من الدرجة الممتازة",
        "first tier": "{lab} من الدرجة الأولى",
        "top tier": "{lab} من الدرجة الأولى",
        "second tier": "{lab} من الدرجة الثانية",
        "third tier": "{lab} من الدرجة الثالثة",
        "fourth tier": "{lab} من الدرجة الرابعة",
        "fifth tier": "{lab} من الدرجة الخامسة",
        "sixth tier": "{lab} من الدرجة السادسة",
        "seventh tier": "{lab} من الدرجة السابعة",
        "chairmen and investors": "رؤساء ومسيرو {lab}",
        "cups": "كؤوس {lab}",
        "champions": "أبطال {lab}",
        "clubs": "أندية {lab}",
        "clubs and teams": "أندية وفرق {lab}",
        "coaches": "مدربو {lab}",  # Category:Indoor soccer coaches in the United States by club
        "competitions": "منافسات {lab}",
        "events": "أحداث {lab}",
        "films": "أفلام {lab}",
        "finals": "نهائيات {lab}",
        "home stadiums": "ملاعب {lab}",
        "leagues": "دوريات {lab}",
        "lists": "قوائم {lab}",
        "manager history": "تاريخ مدربو {lab}",
        "managers": "مدربو {lab}",
        "matches": "مباريات {lab}",
        "navigational boxes": "صناديق تصفح {lab}",
        "non-profit organizations": "منظمات غير ربحية {lab}",
        "non-profit publishers": "ناشرون غير ربحيون {lab}",
        "organisations": "منظمات {lab}",
        "organizations": "منظمات {lab}",
        "players": "لاعبو {lab}",
        "positions": "مراكز {lab}",
        "records": "سجلات {lab}",
        "records and statistics": "سجلات وإحصائيات {lab}",
        "results": "نتائج {lab}",
        "rivalries": "دربيات {lab}",
        "scouts": "كشافة {lab}",
        "squads": "تشكيلات {lab}",
        "statistics": "إحصائيات {lab}",
        "templates": "قوالب {lab}",
        "tournaments": "بطولات {lab}",
        "trainers": "مدربو {lab}",
        "umpires": "حكام {lab}",
        "venues": "ملاعب {lab}",
    }

    keys_ending = dict(
        sorted(
            keys_ending.items(),
            key=lambda k: (-k[0].count(" "), -len(k[0])),
        )
    )
    return keys_ending


@functools.lru_cache(maxsize=10000)
def _sport_lab_nat_load_new(category) -> str:
    """
    Format and return the localized label for a sport-related category.

    Parameters:
        category (str): The category string to look up and format (e.g., "national teams", "premier league").

    Returns:
        str: The localized/formatted label corresponding to the provided category.
    """
    logger.debug(f"<<yellow>> start _sport_lab_nat_load_new: {category=}")
    both_bot = _load_bot()
    result = both_bot.search_all_category(category)
    logger.info_if_or_debug(f"<<yellow>> end _sport_lab_nat_load_new: {category=}, {result=}", result)
    return result


def fix_keys(category: str) -> str:
    category = category.replace("'", "").lower()

    replacements = {
        "level": "tier",
        "canadian football": "canadian-football",
    }

    for old, new in replacements.items():
        category = re.sub(rf"\b{re.escape(old)}\b", new, category)

    return category


def fix_result_callable(result: str, category: str, key: str, value: str) -> str:
    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    if key == "teams" and "national" in category:
        result = result.replace("فرق ", "منتخبات ")

    return result


@functools.lru_cache(maxsize=10000)
def sport_lab_nat_load_new(category: str) -> str:
    category = fix_keys(category)

    logger.debug(f"<<yellow>> start sport_lab_nat_load_new: {category=}")
    keys_ending = _load_end_key_mappings()

    result = resolve_sport_category_suffix_with_mapping(
        category=category,
        data=keys_ending,
        callback=_sport_lab_nat_load_new,
        fix_result_callable=fix_result_callable,
        format_key="lab",
    )

    logger.info_if_or_debug(f"<<yellow>> end sport_lab_nat_load_new: {category=}, {result=}", result)
    return result


len_print.data_len(
    "sports_formats_teams/sport_lab_nat.py",
    {
        "new_for_nat_female_xo_team_2": new_for_nat_female_xo_team_2,
        "new_for_nat_female_xo_team_additional": new_for_nat_female_xo_team_additional,
    },
)

__all__ = [
    "sport_lab_nat_load_new",
]
