#!/usr/bin/python3
"""
NOTE: this file has alot of formatted_data

TODO: merge with ArWikiCats/new_resolvers/translations_resolvers_v2/nats_sport_multi_v2.py

"""

import functools
import re

from ...translations_formats.DataModel.model_multi_data import MultiDataFormatterBase
from ...helps import logger, len_print
from ...translations import Nat_women
from ...translations_formats import format_multi_data
from ...translations.sports.Sport_key import SPORTS_KEYS_FOR_JOBS
from ...new.handle_suffixes import resolve_sport_category_suffix_with_mapping

# TODO: add data from new_for_nat_female_xo_team_additional
new_for_nat_female_xo_team_2 = {
    # "yemeni football": "كرة قدم يمنية",
    "{en} {sport_en}": "xzxz {female}",  # Category:American_basketball
    # "yemeni national football": "كرة قدم وطنية يمنية",
    "{en} national {sport_en}": "xzxz وطنية {female}",

    "{en} {sport_en} teams": "فرق xzxz {female}",
    "{en} {sport_en} national teams": "منتخبات xzxz {female}",
    "{en} domestic {sport_en}": "xzxz {female} محلية",
    "{en} {sport_en} championships": "بطولات xzxz {female}",
    "{en} national {sport_en} championships": "بطولات xzxz وطنية {female}",
    "{en} national {sport_en} champions": "أبطال بطولات xzxz وطنية {female}",
    "{en} amateur {sport_en} cup": "كأس {female} xzxz للهواة",
    "{en} youth {sport_en} cup": "كأس {female} xzxz للشباب",
    "{en} mens {sport_en} cup": "كأس {female} xzxz للرجال",
    "{en} womens {sport_en} cup": "كأس {female} xzxz للسيدات",
    "{en} {sport_en} super leagues": "دوريات سوبر xzxz {female}",
    "{en} womens {sport_en}": "xzxz {female} نسائية",
    "{en} defunct {sport_en} cup": "كؤوس xzxz {female} سابقة",
    "{en} {sport_en} cup": "كؤوس xzxz {female}",
    "{en} domestic {sport_en} cup": "كؤوس xzxz {female} محلية",
    "{en} current {sport_en} seasons": "مواسم xzxz {female} حالية",
    # ---
    "{en} professional {sport_en}": "xzxz {female} للمحترفين",
    "{en} defunct {sport_en}": "xzxz {female} سابقة",
    "{en} domestic womens {sport_en}": "xzxz محلية {female} للسيدات",
    "{en} indoor {sport_en}": "xzxz {female} داخل الصالات",
    "{en} outdoor {sport_en}": "xzxz {female} في الهواء الطلق",
    "{en} defunct indoor {sport_en}": "xzxz {female} داخل الصالات سابقة",
    "{en} defunct outdoor {sport_en}": "xzxz {female} في الهواء الطلق سابقة",
    # tab[Category:Canadian domestic Soccer: "تصنيف:كرة قدم كندية محلية"
    # european national womens volleyball teams
    "{en} national womens {sport_en} teams": "منتخبات xzxz وطنية {female} للسيدات",
    "{en} national {sport_en} teams": "منتخبات xzxz وطنية {female}",
    "{en} reserve {sport_en} teams": "فرق xzxz احتياطية {female}",
    "{en} defunct {sport_en} teams": "فرق xzxz سابقة {female}",
    "{en} national a {sport_en} teams": "منتخبات xzxz محليين {female}",
    "{en} national b {sport_en} teams": "منتخبات xzxz رديفة {female}",
    "{en} national reserve {sport_en} teams": "منتخبات xzxz وطنية احتياطية {female}",
    "deaths by {en} airstrikes": "وفيات بضربات جوية {female}",
    "{en} airstrikes": "ضربات جوية {female}",
}

new_for_nat_female_xo_team_additional = {
    "{en} national amateur under-13 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 13 سنة للهواة",
    "{en} national amateur under-14 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 14 سنة للهواة",
    "{en} national amateur under-15 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 15 سنة للهواة",
    "{en} national amateur under-16 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 16 سنة للهواة",
    "{en} national amateur under-17 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 17 سنة للهواة",
    "{en} national amateur under-18 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 18 سنة للهواة",
    "{en} national amateur under-19 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 19 سنة للهواة",
    "{en} national amateur under-20 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 20 سنة للهواة",
    "{en} national amateur under-21 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 21 سنة للهواة",
    "{en} national amateur under-23 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 23 سنة للهواة",
    "{en} national amateur under-24 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 24 سنة للهواة",
    "{en} national amateur {sport_en} teams": "منتخبات xzxz وطنية {female} للهواة",
    "{en} national junior mens under-13 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 13 سنة للناشئين",
    "{en} national junior mens under-14 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 14 سنة للناشئين",
    "{en} national junior mens under-15 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 15 سنة للناشئين",
    "{en} national junior mens under-16 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 16 سنة للناشئين",
    "{en} national junior mens under-17 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 17 سنة للناشئين",
    "{en} national junior mens under-18 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 18 سنة للناشئين",
    "{en} national junior mens under-19 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 19 سنة للناشئين",
    "{en} national junior mens under-20 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 20 سنة للناشئين",
    "{en} national junior mens under-21 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 21 سنة للناشئين",
    "{en} national junior mens under-23 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 23 سنة للناشئين",
    "{en} national junior mens under-24 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 24 سنة للناشئين",
    "{en} national junior mens {sport_en} teams": "منتخبات xzxz وطنية {female} للناشئين",
    "{en} national junior womens under-13 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 13 سنة للناشئات",
    "{en} national junior womens under-14 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 14 سنة للناشئات",
    "{en} national junior womens under-15 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 15 سنة للناشئات",
    "{en} national junior womens under-16 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 16 سنة للناشئات",
    "{en} national junior womens under-17 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 17 سنة للناشئات",
    "{en} national junior womens under-18 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 18 سنة للناشئات",
    "{en} national junior womens under-19 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 19 سنة للناشئات",
    "{en} national junior womens under-20 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 20 سنة للناشئات",
    "{en} national junior womens under-21 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 21 سنة للناشئات",
    "{en} national junior womens under-23 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 23 سنة للناشئات",
    "{en} national junior womens under-24 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 24 سنة للناشئات",
    "{en} national junior womens {sport_en} teams": "منتخبات xzxz وطنية {female} للناشئات",
    "{en} national mens under-13 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 13 سنة للرجال",
    "{en} national mens under-14 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 14 سنة للرجال",
    "{en} national mens under-15 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 15 سنة للرجال",
    "{en} national mens under-16 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 16 سنة للرجال",
    "{en} national mens under-17 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 17 سنة للرجال",
    "{en} national mens under-18 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 18 سنة للرجال",
    "{en} national mens under-19 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 19 سنة للرجال",
    "{en} national mens under-20 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 20 سنة للرجال",
    "{en} national mens under-21 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 21 سنة للرجال",
    "{en} national mens under-23 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 23 سنة للرجال",
    "{en} national mens under-24 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 24 سنة للرجال",
    "{en} national mens {sport_en} teams": "منتخبات xzxz وطنية {female} للرجال",
    "{en} national under-13 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 13 سنة",
    "{en} national under-14 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 14 سنة",
    "{en} national under-15 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 15 سنة",
    "{en} national under-16 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 16 سنة",
    "{en} national under-17 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 17 سنة",
    "{en} national under-18 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 18 سنة",
    "{en} national under-19 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 19 سنة",
    "{en} national under-20 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 20 سنة",
    "{en} national under-21 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 21 سنة",
    "{en} national under-23 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 23 سنة",
    "{en} national under-24 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 24 سنة",
    "{en} national womens under-13 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 13 سنة للسيدات",
    "{en} national womens under-14 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 14 سنة للسيدات",
    "{en} national womens under-15 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 15 سنة للسيدات",
    "{en} national womens under-16 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 16 سنة للسيدات",
    "{en} national womens under-17 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 17 سنة للسيدات",
    "{en} national womens under-18 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 18 سنة للسيدات",
    "{en} national womens under-19 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 19 سنة للسيدات",
    "{en} national womens under-20 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 20 سنة للسيدات",
    "{en} national womens under-21 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 21 سنة للسيدات",
    "{en} national womens under-23 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 23 سنة للسيدات",
    "{en} national womens under-24 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 24 سنة للسيدات",
    "{en} national womens {sport_en} teams": "منتخبات xzxz وطنية {female} للسيدات",
    "{en} national youth under-13 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 13 سنة للشباب",
    "{en} national youth under-14 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 14 سنة للشباب",
    "{en} national youth under-15 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 15 سنة للشباب",
    "{en} national youth under-16 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 16 سنة للشباب",
    "{en} national youth under-17 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 17 سنة للشباب",
    "{en} national youth under-18 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 18 سنة للشباب",
    "{en} national youth under-19 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 19 سنة للشباب",
    "{en} national youth under-20 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 20 سنة للشباب",
    "{en} national youth under-21 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 21 سنة للشباب",
    "{en} national youth under-23 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 23 سنة للشباب",
    "{en} national youth under-24 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 24 سنة للشباب",
    "{en} national youth womens under-13 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 13 سنة للشابات",
    "{en} national youth womens under-14 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 14 سنة للشابات",
    "{en} national youth womens under-15 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 15 سنة للشابات",
    "{en} national youth womens under-16 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 16 سنة للشابات",
    "{en} national youth womens under-17 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 17 سنة للشابات",
    "{en} national youth womens under-18 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 18 سنة للشابات",
    "{en} national youth womens under-19 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 19 سنة للشابات",
    "{en} national youth womens under-20 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 20 سنة للشابات",
    "{en} national youth womens under-21 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 21 سنة للشابات",
    "{en} national youth womens under-23 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 23 سنة للشابات",
    "{en} national youth womens under-24 {sport_en} teams": "منتخبات xzxz وطنية {female} تحت 24 سنة للشابات",
    "{en} national youth womens {sport_en} teams": "منتخبات xzxz وطنية {female} للشابات",
    "{en} national youth {sport_en} teams": "منتخبات xzxz وطنية {female} للشباب",
    "{en} under-13 {sport_en} teams": "فرق xzxz {female} تحت 13 سنة",
    "{en} under-14 {sport_en} teams": "فرق xzxz {female} تحت 14 سنة",
    "{en} under-15 {sport_en} teams": "فرق xzxz {female} تحت 15 سنة",
    "{en} under-16 {sport_en} teams": "فرق xzxz {female} تحت 16 سنة",
    "{en} under-17 {sport_en} teams": "فرق xzxz {female} تحت 17 سنة",
    "{en} under-18 {sport_en} teams": "فرق xzxz {female} تحت 18 سنة",
    "{en} under-19 {sport_en} teams": "فرق xzxz {female} تحت 19 سنة",
    "{en} under-20 {sport_en} teams": "فرق xzxz {female} تحت 20 سنة",
    "{en} under-21 {sport_en} teams": "فرق xzxz {female} تحت 21 سنة",
    "{en} under-23 {sport_en} teams": "فرق xzxz {female} تحت 23 سنة",
    "{en} under-24 {sport_en} teams": "فرق xzxz {female} تحت 24 سنة"
}

new_for_nat_female_xo_team_2.update(new_for_nat_female_xo_team_additional)

new_for_nat_female_xo_team_2.update({
    "{en} national {sport_en} teams premier": "منتخبات xzxz وطنية {female} من الدرجة الممتازة",
    "{en} {sport_en} teams premier": "فرق xzxz {female} من الدرجة الممتازة",
})


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBase:
    return format_multi_data(
        new_for_nat_female_xo_team_2,
        Nat_women,
        key_placeholder="{en}",
        value_placeholder="{female}",
        data_list2=SPORTS_KEYS_FOR_JOBS,
        key2_placeholder="{sport_en}",
        value2_placeholder="xzxz",
        text_after=" people",
        text_before="the ",
    )


@functools.lru_cache(maxsize=1)
def _load_end_key_mappings() -> dict[str, str]:
    keys_ending = {
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
        "teams": "فرق {lab}",
        "templates": "قوالب {lab}",
        "tournaments": "بطولات {lab}",
        "trainers": "مدربو {lab}",
        "umpires": "حكام {lab}",
        "venues": "ملاعب {lab}"
    }

    keys_ending = dict(sorted(
        keys_ending.items(),
        key=lambda k: (-k[0].count(" "), -len(k[0])),
    ))
    return keys_ending


@functools.lru_cache(maxsize=None)
def _sport_lab_nat_load_new(category) -> str:
    logger.debug(f"<<yellow>> start _sport_lab_nat_load_new: {category=}")
    both_bot = _load_bot()
    result = both_bot.create_label(category)
    logger.debug(f"<<yellow>> end _sport_lab_nat_load_new: {category=}, {result=}")
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


@functools.lru_cache(maxsize=10000)
def sport_lab_nat_load_new(category: str) -> str:
    category = fix_keys(category)

    logger.debug(f"<<yellow>> start sport_lab_nat_load_new: {category=}")
    keys_ending = _load_end_key_mappings()

    result = resolve_sport_category_suffix_with_mapping(category, keys_ending, _sport_lab_nat_load_new, format_key="lab")

    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    logger.debug(f"<<yellow>> end sport_lab_nat_load_new: {category=}, {result=}")
    return result


len_print.data_len(
    "sports_formats_national/te2.py",
    {
        "new_for_nat_female_xo_team_2": new_for_nat_female_xo_team_2,
        "new_for_nat_female_xo_team_additional": new_for_nat_female_xo_team_additional,
    },
)

__all__ = [
    "sport_lab_nat_load_new",
]
