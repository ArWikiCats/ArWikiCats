#!/usr/bin/python3
"""
"""

import functools

from ...helps import logger, len_print

# from ...helps.jsonl_dump import dump_data
from ...new.handle_suffixes import resolve_sport_category_suffix_with_mapping
from ...translations_formats import FormatData
from ...translations.sports.Sport_key import (
    SPORTS_KEYS_FOR_JOBS,
    SPORTS_KEYS_FOR_LABEL,
    SPORTS_KEYS_FOR_TEAM,
)

jobs_formatted_data = {
    "{en_sport}": "{sport_jobs}",
    "under-13 {en_sport}": "{sport_jobs} تحت 13 سنة",
    "under-14 {en_sport}": "{sport_jobs} تحت 14 سنة",
    "under-15 {en_sport}": "{sport_jobs} تحت 15 سنة",
    "under-16 {en_sport}": "{sport_jobs} تحت 16 سنة",
    "under-17 {en_sport}": "{sport_jobs} تحت 17 سنة",
    "under-18 {en_sport}": "{sport_jobs} تحت 18 سنة",
    "under-19 {en_sport}": "{sport_jobs} تحت 19 سنة",
    "under-20 {en_sport}": "{sport_jobs} تحت 20 سنة",
    "under-21 {en_sport}": "{sport_jobs} تحت 21 سنة",
    "under-23 {en_sport}": "{sport_jobs} تحت 23 سنة",
    "under-24 {en_sport}": "{sport_jobs} تحت 24 سنة",
    "amateur {en_sport} championships": "بطولات {sport_jobs} للهواة",
    "amateur {en_sport}": "{sport_jobs} للهواة",
    "college {en_sport}": "{sport_jobs} الكليات",
    "current {en_sport} seasons": "مواسم {sport_jobs} حالية",
    "defunct indoor {en_sport} cups": "كؤوس {sport_jobs} داخل الصالات سابقة",
    "defunct indoor {en_sport} leagues": "دوريات {sport_jobs} داخل الصالات سابقة",
    "defunct indoor {en_sport}": "{sport_jobs} داخل الصالات سابقة",
    "defunct outdoor {en_sport} cups": "كؤوس {sport_jobs} في الهواء الطلق سابقة",
    "defunct outdoor {en_sport} leagues": "دوريات {sport_jobs} في الهواء الطلق سابقة",
    "defunct outdoor {en_sport}": "{sport_jobs} في الهواء الطلق سابقة",
    "defunct {en_sport} cup": "كؤوس {sport_jobs} سابقة",
    "defunct {en_sport} cups": "كؤوس {sport_jobs} سابقة",
    "defunct {en_sport} leagues": "دوريات {sport_jobs} سابقة",
    "defunct {en_sport} teams": "فرق {sport_jobs} سابقة",
    "defunct {en_sport}": "{sport_jobs} سابقة",
    "domestic women's {en_sport} cups": "كؤوس {sport_jobs} محلية للسيدات",
    "domestic women's {en_sport} leagues": "دوريات {sport_jobs} محلية للسيدات",
    "domestic women's {en_sport}": "{sport_jobs} محلية للسيدات",
    "domestic {en_sport} cup": "كؤوس {sport_jobs} محلية",
    "domestic {en_sport} cups": "كؤوس {sport_jobs} محلية",
    "domestic {en_sport} leagues": "دوريات {sport_jobs} محلية",
    "domestic {en_sport}": "{sport_jobs} محلية",
    "fictional {en_sport}": "{sport_jobs} خيالية",
    "fifth level {en_sport} league": "دوريات {sport_jobs} من الدرجة الخامسة",
    "fifth level {en_sport} leagues": "دوريات {sport_jobs} من الدرجة الخامسة",
    "fifth tier {en_sport} league": "دوريات {sport_jobs} من الدرجة الخامسة",
    "fifth tier {en_sport} leagues": "دوريات {sport_jobs} من الدرجة الخامسة",
    "first level {en_sport} league": "دوريات {sport_jobs} من الدرجة الأولى",
    "first level {en_sport} leagues": "دوريات {sport_jobs} من الدرجة الأولى",
    "first tier {en_sport} league": "دوريات {sport_jobs} من الدرجة الأولى",
    "first tier {en_sport} leagues": "دوريات {sport_jobs} من الدرجة الأولى",
    "first-class {en_sport}": "{sport_jobs} من الدرجة الأولى",
    "first-class {en_sport} teams": "فرق {sport_jobs} من الدرجة الأولى",
    "fourth level {en_sport} league": "دوريات {sport_jobs} من الدرجة الرابعة",
    "fourth level {en_sport} leagues": "دوريات {sport_jobs} من الدرجة الرابعة",
    "fourth tier {en_sport} league": "دوريات {sport_jobs} من الدرجة الرابعة",
    "fourth tier {en_sport} leagues": "دوريات {sport_jobs} من الدرجة الرابعة",
    "grand slam ({en_sport}) tournament champions": "أبطال بطولات {sport_jobs} كبرى",
    "grand slam ({en_sport}) tournaments": "بطولات {sport_jobs} كبرى",
    "grand slam ({en_sport})": "بطولات {sport_jobs} كبرى",
    "indoor {en_sport} cups": "كؤوس {sport_jobs} داخل الصالات",
    "indoor {en_sport} leagues": "دوريات {sport_jobs} داخل الصالات",
    "indoor {en_sport}": "{sport_jobs} داخل الصالات",
    "international men's {en_sport} players": "لاعبو {sport_jobs} دوليون",
    "international men's {en_sport} playerss": "لاعبو {sport_jobs} دوليون",
    "international men's {en_sport}": "{sport_jobs} دولية للرجال",
    "international women's {en_sport} players": "لاعبات {sport_jobs} دوليات",
    "international women's {en_sport} playerss": "لاعبات {sport_jobs} دوليات",
    "international women's {en_sport}": "{sport_jobs} دولية للسيدات",
    "International {en_sport} competition": "منافسات {sport_jobs} دولية",
    "International {en_sport} competitions": "منافسات {sport_jobs} دولية",
    "international {en_sport} managers": "مدربو {sport_jobs} دوليون",
    "international {en_sport} players": "لاعبو {sport_jobs} دوليون",
    "international {en_sport} playerss": "لاعبو {sport_jobs} دوليون",
    "International {en_sport} races": "سباقات {sport_jobs} دولية",
    "International {en_sport}": "{sport_jobs} دولية",
    "international youth {en_sport}": "{sport_jobs} شبابية دولية",
    "men's international {en_sport} players": "لاعبو {sport_jobs} دوليون",
    "men's international {en_sport} playerss": "لاعبو {sport_jobs} دوليون",
    "men's international {en_sport}": "{sport_jobs} دولية للرجال",
    "men's {en_sport} teams": "فرق {sport_jobs} رجالية",
    "men's {en_sport}": "{sport_jobs} رجالية",
    "military {en_sport}": "{sport_jobs} عسكرية",
    "multi-national {en_sport} championships": "بطولات {sport_jobs} متعددة الجنسيات",
    "multi-national {en_sport} league": "دوريات {sport_jobs} متعددة الجنسيات",
    "multi-national {en_sport} leagues": "دوريات {sport_jobs} متعددة الجنسيات",
    "national a' {en_sport} teams": "منتخبات {sport_jobs} للمحليين",
    "national a. {en_sport} teams": "منتخبات {sport_jobs} للمحليين",
    "national b {en_sport} teams": "منتخبات {sport_jobs} رديفة",
    "national b. {en_sport} teams": "منتخبات {sport_jobs} رديفة",
    "national junior men's {en_sport} teams": "منتخبات {sport_jobs} وطنية للناشئين",
    "national junior {en_sport} teams": "منتخبات {sport_jobs} وطنية للناشئين",
    "national men's {en_sport} teams": "منتخبات {sport_jobs} وطنية رجالية",
    "national men's {en_sport}": "منتخبات {sport_jobs} وطنية للرجال",
    "national reserve {en_sport} teams": "منتخبات {sport_jobs} وطنية احتياطية",
    "national under-13 {en_sport}": "منتخبات {sport_jobs} تحت 13 سنة",
    "national under-14 {en_sport}": "منتخبات {sport_jobs} تحت 14 سنة",
    "national under-15 {en_sport}": "منتخبات {sport_jobs} تحت 15 سنة",
    "national under-16 {en_sport}": "منتخبات {sport_jobs} تحت 16 سنة",
    "national under-17 {en_sport}": "منتخبات {sport_jobs} تحت 17 سنة",
    "national under-18 {en_sport}": "منتخبات {sport_jobs} تحت 18 سنة",
    "national under-19 {en_sport}": "منتخبات {sport_jobs} تحت 19 سنة",
    "national under-20 {en_sport}": "منتخبات {sport_jobs} تحت 20 سنة",
    "national under-21 {en_sport}": "منتخبات {sport_jobs} تحت 21 سنة",
    "national under-23 {en_sport}": "منتخبات {sport_jobs} تحت 23 سنة",
    "national under-24 {en_sport}": "منتخبات {sport_jobs} تحت 24 سنة",
    "national women's {en_sport} teams": "منتخبات {sport_jobs} وطنية نسائية",
    "national women's {en_sport}": "منتخبات {sport_jobs} وطنية للسيدات",
    "national {en_sport} champions": "أبطال بطولات {sport_jobs} وطنية",
    "national {en_sport} championships": "بطولات {sport_jobs} وطنية",
    "national {en_sport} league": "دوريات {sport_jobs} وطنية",
    "national {en_sport} leagues": "دوريات {sport_jobs} وطنية",
    "national {en_sport} team results": "نتائج منتخبات {sport_jobs} وطنية",
    "national {en_sport} teams": "منتخبات {sport_jobs} وطنية",
    "national {en_sport}": "منتخبات {sport_jobs} وطنية",
    "national youth {en_sport} teams": "منتخبات {sport_jobs} وطنية شبابية",
    "outdoor {en_sport} cups": "كؤوس {sport_jobs} في الهواء الطلق",
    "outdoor {en_sport} leagues": "دوريات {sport_jobs} في الهواء الطلق",
    "outdoor {en_sport}": "{sport_jobs} في الهواء الطلق",
    "premier {en_sport} league": "دوريات {sport_jobs} من الدرجة الممتازة",
    "premier {en_sport} leagues": "دوريات {sport_jobs} من الدرجة الممتازة",
    "professional {en_sport} cups": "كؤوس {sport_jobs} للمحترفين",
    "professional {en_sport} leagues": "دوريات {sport_jobs} للمحترفين",
    "professional {en_sport}": "{sport_jobs} للمحترفين",
    "reserve {en_sport} teams": "فرق {sport_jobs} احتياطية",
    "second level {en_sport} league": "دوريات {sport_jobs} من الدرجة الثانية",
    "second level {en_sport} leagues": "دوريات {sport_jobs} من الدرجة الثانية",
    "second tier {en_sport} league": "دوريات {sport_jobs} من الدرجة الثانية",
    "second tier {en_sport} leagues": "دوريات {sport_jobs} من الدرجة الثانية",
    "seventh level {en_sport} league": "دوريات {sport_jobs} من الدرجة السابعة",
    "seventh level {en_sport} leagues": "دوريات {sport_jobs} من الدرجة السابعة",
    "seventh tier {en_sport} league": "دوريات {sport_jobs} من الدرجة السابعة",
    "seventh tier {en_sport} leagues": "دوريات {sport_jobs} من الدرجة السابعة",
    "sixth level {en_sport} league": "دوريات {sport_jobs} من الدرجة السادسة",
    "sixth level {en_sport} leagues": "دوريات {sport_jobs} من الدرجة السادسة",
    "sixth tier {en_sport} league": "دوريات {sport_jobs} من الدرجة السادسة",
    "sixth tier {en_sport} leagues": "دوريات {sport_jobs} من الدرجة السادسة",
    "third level {en_sport} league": "دوريات {sport_jobs} من الدرجة الثالثة",
    "third level {en_sport} leagues": "دوريات {sport_jobs} من الدرجة الثالثة",
    "third tier {en_sport} league": "دوريات {sport_jobs} من الدرجة الثالثة",
    "third tier {en_sport} leagues": "دوريات {sport_jobs} من الدرجة الثالثة",
    "top level {en_sport} league": "دوريات {sport_jobs} من الدرجة الأولى",
    "top level {en_sport} leagues": "دوريات {sport_jobs} من الدرجة الأولى",
    "women's international {en_sport} players": "لاعبات {sport_jobs} دوليات",
    "women's international {en_sport} playerss": "لاعبات {sport_jobs} دوليات",
    "women's international {en_sport}": "{sport_jobs} دولية للسيدات",
    "women's {en_sport} teams": "فرق {sport_jobs} نسائية",
    "women's {en_sport}": "{sport_jobs} نسائية",
    "{en_sport} chairmen and investors": "رؤساء ومسيرو {sport_jobs}",
    "{en_sport} cup": "كؤوس {sport_jobs}",
    "{en_sport} cups": "كؤوس {sport_jobs}",
    "{en_sport} league teams": "فرق دوري {sport_jobs}",
    "{en_sport} league": "دوري {sport_jobs}",
    "{en_sport} leagues": "دوريات {sport_jobs}",
    "{en_sport} olympic bronze medalists": "ميداليات {sport_jobs} برونزية أولمبية",
    "{en_sport} olympic gold medalists": "ميداليات {sport_jobs} ذهبية أولمبية",
    "{en_sport} olympic silver medalists": "ميداليات {sport_jobs} فضية أولمبية",
    "{en_sport} races": "سباقات {sport_jobs}",
    "{en_sport} super leagues": "دوريات سوبر {sport_jobs}",
    "youth international {en_sport}": "{sport_jobs} دولية شبابية",
    "youth {en_sport}": "{sport_jobs} شبابية",

    # Category:Multi-national women's basketball leagues in Europe
    "multi-national women's {en_sport} leagues": "دوريات {sport_label} نسائية متعددة الجنسيات",
    # Category:National junior women's goalball teams
    "national junior women's {en_sport} teams": "منتخبات {sport_label} للناشئات",
}

# NOTE: used in countries_names_sport_multi_v2.py
labels_formatted_data = {
    # "{en_sport}": "{sport_label}",
    "olympic gold medalists in {en_sport}": "فائزون بميداليات ذهبية أولمبية في {sport_label}",
    "olympic silver medalists in {en_sport}": "فائزون بميداليات فضية أولمبية في {sport_label}",
    "olympic bronze medalists in {en_sport}": "فائزون بميداليات برونزية أولمبية في {sport_label}",
    "{en_sport} league": "دوري {sport_label}",
    "{en_sport} champions": "أبطال {sport_label}",
    "olympics {en_sport}": "{sport_label} في الألعاب الأولمبية",
    "summer olympics {en_sport}": "{sport_label} في الألعاب الأولمبية الصيفية",
    "winter olympics {en_sport}": "{sport_label} في الألعاب الأولمبية الشتوية",
}


teams_formatted_data = {
    "amateur {en_sport} world cup": "كأس العالم {sport_teams} للهواة",
    "international {en_sport} council": "المجلس الدولي {sport_teams}",
    "men's {en_sport} championship": "بطولة {sport_teams} للرجال",
    "men's {en_sport} world championship": "بطولة العالم {sport_teams} للرجال",
    "men's {en_sport} world cup": "كأس العالم {sport_teams} للرجال",
    "outdoor world {en_sport} championship": "بطولة العالم {sport_teams} في الهواء الطلق",
    "women's world {en_sport} championship": "بطولة العالم {sport_teams} للسيدات",
    "women's {en_sport} championship": "بطولة {sport_teams} للسيدات",
    "women's {en_sport} world championship": "بطولة العالم {sport_teams} للسيدات",
    "women's {en_sport} world cup": "كأس العالم {sport_teams} للسيدات",
    "world amateur {en_sport} championship": "بطولة العالم {sport_teams} للهواة",
    "world champion national {en_sport} teams": "أبطال بطولة العالم {sport_teams}",
    "world junior {en_sport} championship": "بطولة العالم {sport_teams} للناشئين",
    "world outdoor {en_sport} championship": "بطولة العالم {sport_teams} في الهواء الطلق",
    "world wheelchair {en_sport} championship": "بطولة العالم {sport_teams} على الكراسي المتحركة",
    "world {en_sport} amateur championship": "بطولة العالم {sport_teams} للهواة",
    "world {en_sport} championship": "بطولة العالم {sport_teams}",
    "world {en_sport} championship competitors": "منافسو بطولة العالم {sport_teams}",
    "world {en_sport} championship medalists": "فائزون بميداليات بطولة العالم {sport_teams}",
    "world {en_sport} junior championship": "بطولة العالم {sport_teams} للناشئين",
    "world {en_sport} youth championship": "بطولة العالم {sport_teams} للشباب",
    "world youth {en_sport} championship": "بطولة العالم {sport_teams} للشباب",
    "{en_sport} amateur world championship": "بطولة العالم {sport_teams} للهواة",
    "{en_sport} junior world championship": "بطولة العالم {sport_teams} للناشئين",
    "{en_sport} world amateur championship": "بطولة العالم {sport_teams} للهواة",
    "{en_sport} world championship": "بطولة العالم {sport_teams}",
    "{en_sport} world cup": "كأس العالم {sport_teams}",
    "{en_sport} world junior championship": "بطولة العالم {sport_teams} للناشئين",
    "{en_sport} world youth championship": "بطولة العالم {sport_teams} للشباب",
    "{en_sport} youth world championship": "بطولة العالم {sport_teams} للشباب",
    "youth {en_sport} world cup": "كأس العالم {sport_teams} للشباب",
}


labels_bot = FormatData(
    labels_formatted_data,
    SPORTS_KEYS_FOR_LABEL,
    key_placeholder="{en_sport}",
    value_placeholder="{sport_label}",
)
teams_bot = FormatData(
    teams_formatted_data,
    SPORTS_KEYS_FOR_TEAM,
    key_placeholder="{en_sport}",
    value_placeholder="{sport_teams}",
)
jobs_bot = FormatData(
    jobs_formatted_data,
    SPORTS_KEYS_FOR_JOBS,
    key_placeholder="{en_sport}",
    value_placeholder="{sport_jobs}",
)


@functools.lru_cache(maxsize=1)
def _get_sorted_teams_labels() -> dict[str, str]:
    teams_label_mappings_ends_old = {
        "champions": "أبطال",
        "events": "أحداث",
        "films": "أفلام",
        "home stadiums": "ملاعب",
        "lists": "قوائم",
        "managers": "مدربو",
        "navigational boxes": "صناديق تصفح",
        "non-profit organizations": "منظمات غير ربحية",
        "non-profit publishers": "ناشرون غير ربحيون",
        "organisations": "منظمات",
        "organizations": "منظمات",
        "players": "لاعبو",
        "positions": "مراكز",
        "records and statistics": "سجلات وإحصائيات",
        "records": "سجلات",
        "results": "نتائج",
        "rivalries": "دربيات",
        "scouts": "كشافة",
        "squads": "تشكيلات",
        "statistics": "إحصائيات",
        "templates": "قوالب",
        "trainers": "مدربو",
        "umpires": "حكام",
        "venues": "ملاعب",
    }

    teams_label_mappings_ends = {
        "finals": "نهائيات",
        "matches": "مباريات",
        "manager history": "تاريخ مدربو",
        "tournaments": "بطولات",
        "leagues": "دوريات",
        "coaches": "مدربو",
        "clubs": "أندية",
        "competitions": "منافسات",
        "chairmen and investors": "رؤساء ومسيرو",
        "cups": "كؤوس",
    }

    teams_label_mappings_ends = dict(
        sorted(
            teams_label_mappings_ends.items(),
            key=lambda k: (-k[0].count(" "), -len(k[0])),
        )
    )
    return teams_label_mappings_ends


def fix_result_callable(result, category, key, value):
    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    if key == "teams" and "national" in category:
        result = result.replace("فرق ", "منتخبات ")

    return result


@functools.lru_cache(maxsize=None)
def find_labels_bot(category: str, default: str = "") -> str:
    """Search for a generic sports label, returning ``default`` when missing."""
    return labels_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def find_teams_bot(category: str, default: str = "") -> str:
    """Search for a team-related label, returning ``default`` when missing."""
    category = category.replace("championships", "championship")
    return teams_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def find_jobs_bot(category: str, default: str = "") -> str:
    """Search for a job-related sports label, returning ``default`` when missing."""
    return jobs_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def wrap_team_xo_normal_2025(team: str) -> str:
    """Normalize a team string and resolve it via the available sports bots."""
    team = team.lower().replace("category:", "")
    result = find_labels_bot(team) or find_teams_bot(team) or find_jobs_bot(team) or ""
    return result.strip()


def wrap_team_xo_normal_2025_with_ends(category, callback=wrap_team_xo_normal_2025) -> str:
    # category = fix_keys(category)
    teams_label_mappings_ends = _get_sorted_teams_labels()

    label2 = callback(category)

    if not label2:
        label2 = resolve_sport_category_suffix_with_mapping(
            category=category,
            data=teams_label_mappings_ends,
            callback=callback,
            fix_result_callable=fix_result_callable,
        )

    return label2


__all__ = [
    "wrap_team_xo_normal_2025",
    "find_labels_bot",
    "find_teams_bot",
    "find_jobs_bot",
    "wrap_team_xo_normal_2025_with_ends",
]
