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

new_team_xo_jobs = {
    "{en_sport}": "{sport_label}",
    "under-13 {en_sport}": "{sport_label} تحت 13 سنة",
    "under-14 {en_sport}": "{sport_label} تحت 14 سنة",
    "under-15 {en_sport}": "{sport_label} تحت 15 سنة",
    "under-16 {en_sport}": "{sport_label} تحت 16 سنة",
    "under-17 {en_sport}": "{sport_label} تحت 17 سنة",
    "under-18 {en_sport}": "{sport_label} تحت 18 سنة",
    "under-19 {en_sport}": "{sport_label} تحت 19 سنة",
    "under-20 {en_sport}": "{sport_label} تحت 20 سنة",
    "under-21 {en_sport}": "{sport_label} تحت 21 سنة",
    "under-23 {en_sport}": "{sport_label} تحت 23 سنة",
    "under-24 {en_sport}": "{sport_label} تحت 24 سنة",
    "amateur {en_sport} championships": "بطولات {sport_label} للهواة",
    "amateur {en_sport}": "{sport_label} للهواة",
    "college {en_sport}": "{sport_label} الكليات",
    "current {en_sport} seasons": "مواسم {sport_label} حالية",
    "defunct indoor {en_sport} cups": "كؤوس {sport_label} داخل الصالات سابقة",
    "defunct indoor {en_sport} leagues": "دوريات {sport_label} داخل الصالات سابقة",
    "defunct indoor {en_sport}": "{sport_label} داخل الصالات سابقة",
    "defunct outdoor {en_sport} cups": "كؤوس {sport_label} في الهواء الطلق سابقة",
    "defunct outdoor {en_sport} leagues": "دوريات {sport_label} في الهواء الطلق سابقة",
    "defunct outdoor {en_sport}": "{sport_label} في الهواء الطلق سابقة",
    "defunct {en_sport} cup": "كؤوس {sport_label} سابقة",
    "defunct {en_sport} cups": "كؤوس {sport_label} سابقة",
    "defunct {en_sport} leagues": "دوريات {sport_label} سابقة",
    "defunct {en_sport} teams": "فرق {sport_label} سابقة",
    "defunct {en_sport}": "{sport_label} سابقة",
    "domestic women's {en_sport} cups": "كؤوس {sport_label} محلية للسيدات",
    "domestic women's {en_sport} leagues": "دوريات {sport_label} محلية للسيدات",
    "domestic women's {en_sport}": "{sport_label} محلية للسيدات",
    "domestic {en_sport} cup": "كؤوس {sport_label} محلية",
    "domestic {en_sport} cups": "كؤوس {sport_label} محلية",
    "domestic {en_sport} leagues": "دوريات {sport_label} محلية",
    "domestic {en_sport}": "{sport_label} محلية",
    "fictional {en_sport}": "{sport_label} خيالية",
    "fifth level {en_sport} league": "دوريات {sport_label} من الدرجة الخامسة",
    "fifth level {en_sport} leagues": "دوريات {sport_label} من الدرجة الخامسة",
    "fifth tier {en_sport} league": "دوريات {sport_label} من الدرجة الخامسة",
    "fifth tier {en_sport} leagues": "دوريات {sport_label} من الدرجة الخامسة",
    "first level {en_sport} league": "دوريات {sport_label} من الدرجة الأولى",
    "first level {en_sport} leagues": "دوريات {sport_label} من الدرجة الأولى",
    "first tier {en_sport} league": "دوريات {sport_label} من الدرجة الأولى",
    "first tier {en_sport} leagues": "دوريات {sport_label} من الدرجة الأولى",
    "first-class {en_sport}": "{sport_label} من الدرجة الأولى",
    "first-class {en_sport} teams": "فرق {sport_label} من الدرجة الأولى",
    "fourth level {en_sport} league": "دوريات {sport_label} من الدرجة الرابعة",
    "fourth level {en_sport} leagues": "دوريات {sport_label} من الدرجة الرابعة",
    "fourth tier {en_sport} league": "دوريات {sport_label} من الدرجة الرابعة",
    "fourth tier {en_sport} leagues": "دوريات {sport_label} من الدرجة الرابعة",
    "grand slam ({en_sport}) tournament champions": "أبطال بطولات {sport_label} كبرى",
    "grand slam ({en_sport}) tournaments": "بطولات {sport_label} كبرى",
    "grand slam ({en_sport})": "بطولات {sport_label} كبرى",
    "indoor {en_sport} cups": "كؤوس {sport_label} داخل الصالات",
    "indoor {en_sport} leagues": "دوريات {sport_label} داخل الصالات",
    "indoor {en_sport}": "{sport_label} داخل الصالات",
    "international men's {en_sport} players": "لاعبو {sport_label} دوليون",
    "international men's {en_sport} playerss": "لاعبو {sport_label} دوليون",
    "international men's {en_sport}": "{sport_label} دولية للرجال",
    "international women's {en_sport} players": "لاعبات {sport_label} دوليات",
    "international women's {en_sport} playerss": "لاعبات {sport_label} دوليات",
    "international women's {en_sport}": "{sport_label} دولية للسيدات",
    "International {en_sport} competition": "منافسات {sport_label} دولية",
    "international {en_sport} managers": "مدربو {sport_label} دوليون",
    "international {en_sport} players": "لاعبو {sport_label} دوليون",
    "international {en_sport} playerss": "لاعبو {sport_label} دوليون",
    "International {en_sport} races": "سباقات {sport_label} دولية",
    "International {en_sport}": "{sport_label} دولية",
    "international youth {en_sport}": "{sport_label} شبابية دولية",
    "men's international {en_sport} players": "لاعبو {sport_label} دوليون",
    "men's international {en_sport} playerss": "لاعبو {sport_label} دوليون",
    "men's international {en_sport}": "{sport_label} دولية للرجال",
    "men's {en_sport} teams": "فرق {sport_label} رجالية",
    "men's {en_sport}": "{sport_label} رجالية",
    "military {en_sport}": "{sport_label} عسكرية",
    "multi-national {en_sport} championships": "بطولات {sport_label} متعددة الجنسيات",
    "multi-national {en_sport} league": "دوريات {sport_label} متعددة الجنسيات",
    "multi-national {en_sport} leagues": "دوريات {sport_label} متعددة الجنسيات",
    "national a' {en_sport} teams": "منتخبات {sport_label} للمحليين",
    "national a. {en_sport} teams": "منتخبات {sport_label} للمحليين",
    "national b {en_sport} teams": "منتخبات {sport_label} رديفة",
    "national b. {en_sport} teams": "منتخبات {sport_label} رديفة",
    "national junior men's {en_sport} teams": "منتخبات {sport_label} وطنية للناشئين",
    "national junior {en_sport} teams": "منتخبات {sport_label} وطنية للناشئين",
    "national men's {en_sport} teams": "منتخبات {sport_label} وطنية رجالية",
    "national men's {en_sport}": "منتخبات {sport_label} وطنية للرجال",
    "national reserve {en_sport} teams": "منتخبات {sport_label} وطنية احتياطية",
    "national under-13 {en_sport}": "منتخبات {sport_label} تحت 13 سنة",
    "national under-14 {en_sport}": "منتخبات {sport_label} تحت 14 سنة",
    "national under-15 {en_sport}": "منتخبات {sport_label} تحت 15 سنة",
    "national under-16 {en_sport}": "منتخبات {sport_label} تحت 16 سنة",
    "national under-17 {en_sport}": "منتخبات {sport_label} تحت 17 سنة",
    "national under-18 {en_sport}": "منتخبات {sport_label} تحت 18 سنة",
    "national under-19 {en_sport}": "منتخبات {sport_label} تحت 19 سنة",
    "national under-20 {en_sport}": "منتخبات {sport_label} تحت 20 سنة",
    "national under-21 {en_sport}": "منتخبات {sport_label} تحت 21 سنة",
    "national under-23 {en_sport}": "منتخبات {sport_label} تحت 23 سنة",
    "national under-24 {en_sport}": "منتخبات {sport_label} تحت 24 سنة",
    "national women's {en_sport} teams": "منتخبات {sport_label} وطنية نسائية",
    "national women's {en_sport}": "منتخبات {sport_label} وطنية للسيدات",
    "national {en_sport} champions": "أبطال بطولات {sport_label} وطنية",
    "national {en_sport} championships": "بطولات {sport_label} وطنية",
    "national {en_sport} league": "دوريات {sport_label} وطنية",
    "national {en_sport} leagues": "دوريات {sport_label} وطنية",
    "national {en_sport} team results": "نتائج منتخبات {sport_label} وطنية",
    "national {en_sport} teams": "منتخبات {sport_label} وطنية",
    "national {en_sport}": "منتخبات {sport_label} وطنية",
    "national youth {en_sport} teams": "منتخبات {sport_label} وطنية شبابية",
    "outdoor {en_sport} cups": "كؤوس {sport_label} في الهواء الطلق",
    "outdoor {en_sport} leagues": "دوريات {sport_label} في الهواء الطلق",
    "outdoor {en_sport}": "{sport_label} في الهواء الطلق",
    "premier {en_sport} league": "دوريات {sport_label} من الدرجة الممتازة",
    "premier {en_sport} leagues": "دوريات {sport_label} من الدرجة الممتازة",
    "professional {en_sport} cups": "كؤوس {sport_label} للمحترفين",
    "professional {en_sport} leagues": "دوريات {sport_label} للمحترفين",
    "professional {en_sport}": "{sport_label} للمحترفين",
    "reserve {en_sport} teams": "فرق {sport_label} احتياطية",
    "second level {en_sport} league": "دوريات {sport_label} من الدرجة الثانية",
    "second level {en_sport} leagues": "دوريات {sport_label} من الدرجة الثانية",
    "second tier {en_sport} league": "دوريات {sport_label} من الدرجة الثانية",
    "second tier {en_sport} leagues": "دوريات {sport_label} من الدرجة الثانية",
    "seventh level {en_sport} league": "دوريات {sport_label} من الدرجة السابعة",
    "seventh level {en_sport} leagues": "دوريات {sport_label} من الدرجة السابعة",
    "seventh tier {en_sport} league": "دوريات {sport_label} من الدرجة السابعة",
    "seventh tier {en_sport} leagues": "دوريات {sport_label} من الدرجة السابعة",
    "sixth level {en_sport} league": "دوريات {sport_label} من الدرجة السادسة",
    "sixth level {en_sport} leagues": "دوريات {sport_label} من الدرجة السادسة",
    "sixth tier {en_sport} league": "دوريات {sport_label} من الدرجة السادسة",
    "sixth tier {en_sport} leagues": "دوريات {sport_label} من الدرجة السادسة",
    "third level {en_sport} league": "دوريات {sport_label} من الدرجة الثالثة",
    "third level {en_sport} leagues": "دوريات {sport_label} من الدرجة الثالثة",
    "third tier {en_sport} league": "دوريات {sport_label} من الدرجة الثالثة",
    "third tier {en_sport} leagues": "دوريات {sport_label} من الدرجة الثالثة",
    "top level {en_sport} league": "دوريات {sport_label} من الدرجة الأولى",
    "top level {en_sport} leagues": "دوريات {sport_label} من الدرجة الأولى",
    "women's international {en_sport} players": "لاعبات {sport_label} دوليات",
    "women's international {en_sport} playerss": "لاعبات {sport_label} دوليات",
    "women's international {en_sport}": "{sport_label} دولية للسيدات",
    "women's {en_sport} teams": "فرق {sport_label} نسائية",
    "women's {en_sport}": "{sport_label} نسائية",
    "{en_sport} chairmen and investors": "رؤساء ومسيرو {sport_label}",
    "{en_sport} cup": "كؤوس {sport_label}",
    "{en_sport} cups": "كؤوس {sport_label}",
    "{en_sport} league teams": "فرق دوري {sport_label}",
    "{en_sport} league": "دوري {sport_label}",
    "{en_sport} leagues": "دوريات {sport_label}",
    "{en_sport} olympic bronze medalists": "ميداليات {sport_label} برونزية أولمبية",
    "{en_sport} olympic gold medalists": "ميداليات {sport_label} ذهبية أولمبية",
    "{en_sport} olympic silver medalists": "ميداليات {sport_label} فضية أولمبية",
    "{en_sport} races": "سباقات {sport_label}",
    "{en_sport} super leagues": "دوريات سوبر {sport_label}",
    "youth international {en_sport}": "{sport_label} دولية شبابية",
    "youth {en_sport}": "{sport_label} شبابية",
}

new_team_xo_labels = {
    "olympic gold medalists in {en_sport}": "فائزون بميداليات ذهبية أولمبية في {sport_label}",
    "olympic silver medalists in {en_sport}": "فائزون بميداليات فضية أولمبية في {sport_label}",
    "olympic bronze medalists in {en_sport}": "فائزون بميداليات برونزية أولمبية في {sport_label}",
    "{en_sport}": "{sport_label}",
    "{en_sport} league": "دوري {sport_label}",
    "{en_sport} champions": "أبطال {sport_label}",
    "olympics {en_sport}": "{sport_label} في الألعاب الأولمبية",
    "summer olympics {en_sport}": "{sport_label} في الألعاب الأولمبية الصيفية",
    "winter olympics {en_sport}": "{sport_label} في الألعاب الأولمبية الشتوية",
}

new_team_xo_team_labels = {
    "amateur xoxo world cup": "كأس العالم xoxo للهواة",
    "international xoxo council": "المجلس الدولي xoxo",
    "men's xoxo championship": "بطولة xoxo للرجال",
    "men's xoxo world championship": "بطولة العالم xoxo للرجال",
    "men's xoxo world cup": "كأس العالم xoxo للرجال",
    "outdoor world xoxo championship": "بطولة العالم xoxo في الهواء الطلق",
    "women's world xoxo championship": "بطولة العالم xoxo للسيدات",
    "women's xoxo championship": "بطولة xoxo للسيدات",
    "women's xoxo world championship": "بطولة العالم xoxo للسيدات",
    "women's xoxo world cup": "كأس العالم xoxo للسيدات",
    "world amateur xoxo championship": "بطولة العالم xoxo للهواة",
    "world champion national xoxo teams": "أبطال بطولة العالم xoxo",
    "world junior xoxo championship": "بطولة العالم xoxo للناشئين",
    "world outdoor xoxo championship": "بطولة العالم xoxo في الهواء الطلق",
    "world wheelchair xoxo championship": "بطولة العالم xoxo على الكراسي المتحركة",
    "world xoxo amateur championship": "بطولة العالم xoxo للهواة",
    "world xoxo championship": "بطولة العالم xoxo",
    "world xoxo championship competitors": "منافسو بطولة العالم xoxo",
    "world xoxo championship medalists": "فائزون بميداليات بطولة العالم xoxo",
    "world xoxo junior championship": "بطولة العالم xoxo للناشئين",
    "world xoxo youth championship": "بطولة العالم xoxo للشباب",
    "world youth xoxo championship": "بطولة العالم xoxo للشباب",
    "xoxo amateur world championship": "بطولة العالم xoxo للهواة",
    "xoxo junior world championship": "بطولة العالم xoxo للناشئين",
    "xoxo world amateur championship": "بطولة العالم xoxo للهواة",
    "xoxo world championship": "بطولة العالم xoxo",
    "xoxo world cup": "كأس العالم xoxo",
    "xoxo world junior championship": "بطولة العالم xoxo للناشئين",
    "xoxo world youth championship": "بطولة العالم xoxo للشباب",
    "xoxo youth world championship": "بطولة العالم xoxo للشباب",
    "youth xoxo world cup": "كأس العالم xoxo للشباب",
}

new_team_jobs = dict(new_team_xo_jobs)

new_team_jobs.update(
    {
        # Category:Multi-national women's basketball leagues in Europe
        "multi-national women's {en_sport} leagues": "دوريات {sport_label} نسائية متعددة الجنسيات",
        # Category:National junior women's goalball teams
        "national junior women's {en_sport} teams": "منتخبات {sport_label} للناشئات",
    }
)

labels_bot = FormatData(
    new_team_xo_labels,
    SPORTS_KEYS_FOR_LABEL,
    key_placeholder="{en_sport}",
    value_placeholder="{sport_label}",
)
teams_bot = FormatData(
    new_team_xo_team_labels,
    SPORTS_KEYS_FOR_TEAM,
    key_placeholder="{en_sport}",
    value_placeholder="{sport_teams}",
)
jobs_bot = FormatData(
    new_team_jobs,
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
