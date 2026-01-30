#!/usr/bin/python3
""" """

import functools

import logging
from ...translations import SPORT_KEY_RECORDS
from ...translations_formats import FormatDataV2
from .pre_defined import pre_defined_results

logger = logging.getLogger(__name__)

UNIFIED_FORMATTED_DATA: dict[str, str] = {
    "mens a {en_sport}": "{sport_label} للرجال للمحليين",
    "{en_sport} olympics": "{sport_olympic}",
    "{en_sport} olympic": "{sport_olympic}",
    "olympic {en_sport}": "{sport_olympic}",
    "{en_sport} olympic champions": "أبطال {sport_olympic}",
    "{en_sport} mass media": "إعلام {sport_label}",
    # "{en_sport} teams": "فرق {sport_jobs}",
    "{en_sport} teams": "فرق {sport_label}",
    # rugby union tournaments for national teams
    "{en_sport} tournaments for national teams": "بطولات {sport_label} للمنتخبات الوطنية",
    "amateur {en_sport}": "{sport_jobs} للهواة",
    "mens {en_sport}": "{sport_jobs} رجالية",
    "womens {en_sport}": "{sport_jobs} نسائية",
    "youth {en_sport}": "{sport_jobs} شبابية",
    "mens youth {en_sport}": "{sport_jobs} للشباب",
    "womens youth {en_sport}": "{sport_jobs} للشابات",
    "{en_sport} cup playoffs": "تصفيات كأس {sport_jobs}",
    # "{en_sport} cup": "كأس {sport_jobs}",
    "{en_sport} broadcasters": "مذيعو {sport_jobs}",
    "{en_sport} commentators": "معلقو {sport_jobs}",
    "{en_sport} commissioners": "مفوضو {sport_jobs}",
    "{en_sport} trainers": "مدربو {sport_jobs}",
    "{en_sport} coaches": "مدربو {sport_jobs}",
    "{en_sport} managers": "مدربو {sport_jobs}",
    "{en_sport} manager": "مدربو {sport_jobs}",
    "{en_sport} manager history": "تاريخ مدربو {sport_jobs}",
    "{en_sport} footballers": "لاعبو {sport_jobs}",
    "{en_sport} players": "لاعبو {sport_jobs}",
    "{en_sport} fan clubs": "أندية معجبي {sport_jobs}",
    "{en_sport} owners and executives": "رؤساء تنفيذيون وملاك {sport_jobs}",
    "{en_sport} personnel": "أفراد {sport_jobs}",
    "{en_sport} owners": "ملاك {sport_jobs}",
    "{en_sport} executives": "مدراء {sport_jobs}",
    "{en_sport} equipment": "معدات {sport_jobs}",
    "{en_sport} culture": "ثقافة {sport_jobs}",
    "{en_sport} logos": "شعارات {sport_jobs}",
    "{en_sport} tactics and skills": "مهارات {sport_jobs}",
    "{en_sport} media": "إعلام {sport_jobs}",
    "{en_sport} people": "أعلام {sport_jobs}",
    "{en_sport} terminology": "مصطلحات {sport_jobs}",
    "{en_sport} variants": "أشكال {sport_jobs}",
    "{en_sport} governing bodies": "هيئات تنظيم {sport_jobs}",
    "{en_sport} bodies": "هيئات {sport_jobs}",
    "{en_sport} video games": "ألعاب فيديو {sport_jobs}",
    "{en_sport} comics": "قصص مصورة {sport_jobs}",
    "{en_sport} records and statistics": "سجلات وإحصائيات {sport_jobs}",
    "{en_sport} leagues seasons": "مواسم دوريات {sport_jobs}",
    "{en_sport} seasons": "مواسم {sport_jobs}",
    "{en_sport} competition": "منافسات {sport_jobs}",
    "{en_sport} world competitions": "منافسات {sport_jobs} عالمية",
    "{en_sport} television series": "مسلسلات تلفزيونية {sport_jobs}",
    "{en_sport} films": "أفلام {sport_jobs}",
    "{en_sport} music": "موسيقى {sport_jobs}",
    "{en_sport} clubs and teams": "أندية وفرق {sport_jobs}",
    "{en_sport} clubs": "أندية {sport_jobs}",
    "{en_sport} referees": "حكام {sport_jobs}",
    "{en_sport} organizations": "منظمات {sport_jobs}",
    "{en_sport} non-profit organizations": "منظمات غير ربحية {sport_jobs}",
    "{en_sport} non-profit publishers": "ناشرون غير ربحيون {sport_jobs}",
    "{en_sport} stadiums": "ملاعب {sport_jobs}",
    "{en_sport} lists": "قوائم {sport_jobs}",
    "{en_sport} awards": "جوائز {sport_jobs}",
    "{en_sport} songs": "أغاني {sport_jobs}",
    "{en_sport} non-playing staff": "طاقم {sport_jobs} غير اللاعبين",
    "{en_sport} umpires": "حكام {sport_jobs}",
    "{en_sport} results": "نتائج {sport_jobs}",
    "{en_sport} matches": "مباريات {sport_jobs}",
    "{en_sport} rivalries": "دربيات {sport_jobs}",
    # "{en_sport} champions": "أبطال {sport_jobs}",
    "{en_sport} chairmen and investors": "رؤساء ومسيرو {sport_jobs}",
    # "{en_sport}": "{sport_jobs}",
    "defunct indoor {en_sport} cups": "كؤوس {sport_jobs} داخل الصالات سابقة",
    "indoor {en_sport} cups": "كؤوس {sport_jobs} داخل الصالات",
    "outdoor {en_sport} cups": "كؤوس {sport_jobs} في الهواء الطلق",
    "professional {en_sport} cups": "كؤوس {sport_jobs} للمحترفين",
    # NOTE: see test_sport_cup.py
    # "{en_sport} cup": "كؤوس {sport_jobs}",
    # "defunct {en_sport} cup": "كؤوس {sport_jobs} سابقة",
    # "domestic {en_sport} cup": "كؤوس {sport_jobs} محلية",
    "{en_sport} cups": "كؤوس {sport_jobs}",
    "defunct outdoor {en_sport} cups": "كؤوس {sport_jobs} في الهواء الطلق سابقة",
    "defunct {en_sport} cups": "كؤوس {sport_jobs} سابقة",
    "domestic womens {en_sport} cups": "كؤوس {sport_jobs} محلية للسيدات",
    "domestic {en_sport} cups": "كؤوس {sport_jobs} محلية",
    "{en_sport} competitions": "منافسات {sport_jobs}",
    "grand slam ({en_sport}) tournaments": "بطولات {sport_jobs} كبرى",
    "International {en_sport} competitions": "منافسات {sport_jobs} دولية",
    "domestic womens {en_sport} leagues": "دوريات {sport_jobs} محلية للسيدات",
    "domestic {en_sport} leagues": "دوريات {sport_jobs} محلية",
    "indoor {en_sport} leagues": "دوريات {sport_jobs} داخل الصالات",
    "defunct indoor {en_sport} leagues": "دوريات {sport_jobs} داخل الصالات سابقة",
    "professional {en_sport} leagues": "دوريات {sport_jobs} للمحترفين",
    "domestic {en_sport}": "{sport_jobs} محلية",
    "professional {en_sport}": "{sport_jobs} للمحترفين",
    "indoor {en_sport}": "{sport_jobs} داخل الصالات",
    "defunct indoor {en_sport}": "{sport_jobs} داخل الصالات سابقة",
    "domestic womens {en_sport}": "{sport_jobs} محلية للسيدات",
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
    "college {en_sport}": "{sport_jobs} الكليات",
    "current {en_sport} seasons": "مواسم {sport_jobs} حالية",
    "defunct outdoor {en_sport} leagues": "دوريات {sport_jobs} في الهواء الطلق سابقة",
    "defunct outdoor {en_sport}": "{sport_jobs} في الهواء الطلق سابقة",
    "defunct {en_sport} teams": "فرق {sport_jobs} سابقة",
    "defunct {en_sport}": "{sport_jobs} سابقة",
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
    "grand slam ({en_sport})": "بطولات {sport_jobs} كبرى",
    "international mens {en_sport} players": "لاعبو {sport_jobs} دوليون",
    "international mens {en_sport}": "{sport_jobs} دولية للرجال",
    "international womens {en_sport} players": "لاعبات {sport_jobs} دوليات",
    "international womens {en_sport}": "{sport_jobs} دولية للسيدات",
    "International {en_sport} competition": "منافسات {sport_jobs} دولية",
    "international {en_sport} managers": "مدربو {sport_jobs} دوليون",
    "international {en_sport} players": "لاعبو {sport_jobs} دوليون",
    "International {en_sport} races": "سباقات {sport_jobs} دولية",
    "International {en_sport}": "{sport_jobs} دولية",
    "international youth {en_sport}": "{sport_jobs} شبابية دولية",
    "mens international {en_sport} players": "لاعبو {sport_jobs} دوليون",
    "mens international {en_sport}": "{sport_jobs} دولية للرجال",
    "mens {en_sport} teams": "فرق {sport_jobs} رجالية",
    "military {en_sport}": "{sport_jobs} عسكرية",
    "multi-national {en_sport} league": "دوريات {sport_jobs} متعددة الجنسيات",
    "national a {en_sport} teams": "منتخبات {sport_jobs} للمحليين",
    "national a. {en_sport} teams": "منتخبات {sport_jobs} للمحليين",
    "national b {en_sport} teams": "منتخبات {sport_jobs} رديفة",
    "national b. {en_sport} teams": "منتخبات {sport_jobs} رديفة",
    "national junior mens {en_sport} teams": "منتخبات {sport_jobs} وطنية للناشئين",
    "national junior {en_sport} teams": "منتخبات {sport_jobs} وطنية للناشئين",
    "national mens {en_sport} teams": "منتخبات {sport_jobs} وطنية رجالية",
    "national reserve {en_sport} teams": "منتخبات {sport_jobs} وطنية احتياطية",
    "national womens {en_sport} teams": "منتخبات {sport_jobs} وطنية نسائية",
    "national {en_sport} champions": "أبطال بطولات {sport_jobs} وطنية",
    "national {en_sport} league": "دوريات {sport_jobs} وطنية",
    "multi-national {en_sport} leagues": "دوريات {sport_jobs} متعددة الجنسيات",
    "defunct national {en_sport} leagues": "دوريات {sport_jobs} وطنية سابقة",
    "national {en_sport} leagues": "دوريات {sport_jobs} وطنية",
    "outdoor {en_sport} leagues": "دوريات {sport_jobs} في الهواء الطلق",
    "defunct national {en_sport} teams": "منتخبات {sport_jobs} وطنية سابقة",
    "national {en_sport} teams": "منتخبات {sport_jobs} وطنية",
    "national {en_sport} team results": "نتائج منتخبات {sport_jobs} وطنية",
    "national youth {en_sport} teams": "منتخبات {sport_jobs} وطنية شبابية",
    "outdoor {en_sport}": "{sport_jobs} في الهواء الطلق",
    "premier {en_sport} league": "دوريات {sport_jobs} من الدرجة الممتازة",
    "premier {en_sport} leagues": "دوريات {sport_jobs} من الدرجة الممتازة",
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
    "womens international {en_sport} players": "لاعبات {sport_jobs} دوليات",
    "womens international {en_sport}": "{sport_jobs} دولية للسيدات",
    "womens {en_sport} teams": "فرق {sport_jobs} نسائية",
    "{en_sport} league teams": "فرق دوري {sport_jobs}",
    # "{en_sport} league": "دوري {sport_jobs}",
    "{en_sport} leagues": "دوريات {sport_jobs}",
    "defunct {en_sport} leagues": "دوريات {sport_jobs} سابقة",
    "{en_sport} olympic bronze medalists": "ميداليات {sport_jobs} برونزية أولمبية",
    "{en_sport} olympic gold medalists": "ميداليات {sport_jobs} ذهبية أولمبية",
    "{en_sport} olympic silver medalists": "ميداليات {sport_jobs} فضية أولمبية",
    "{en_sport} races": "سباقات {sport_jobs}",
    "{en_sport} super leagues": "دوريات سوبر {sport_jobs}",
    "youth international {en_sport}": "{sport_jobs} دولية شبابية",
    # Category:Multi-national women's basketball leagues in Europe
    "multi-national womens {en_sport} leagues": "دوريات {sport_jobs} نسائية متعددة الجنسيات",
    # Category:National junior women's goalball teams
    "national junior womens {en_sport} teams": "منتخبات {sport_jobs} للناشئات",
    # "national mens {en_sport}": "منتخبات {sport_jobs} وطنية للرجال",
    # "national {en_sport}": "منتخبات {sport_jobs} وطنية",
    # "national womens {en_sport}": "منتخبات {sport_jobs} وطنية للسيدات",
    "national mens {en_sport}": "{sport_jobs} وطنية للرجال",
    "national {en_sport}": "{sport_jobs} وطنية",
    "national womens {en_sport}": "{sport_jobs} وطنية للسيدات",
    # "national under-13 {en_sport}": "منتخبات {sport_jobs} تحت 13 سنة",
    # "national under-14 {en_sport}": "منتخبات {sport_jobs} تحت 14 سنة",
    # "national under-15 {en_sport}": "منتخبات {sport_jobs} تحت 15 سنة",
    # "national under-16 {en_sport}": "منتخبات {sport_jobs} تحت 16 سنة",
    # "national under-17 {en_sport}": "منتخبات {sport_jobs} تحت 17 سنة",
    # "national under-18 {en_sport}": "منتخبات {sport_jobs} تحت 18 سنة",
    # "national under-19 {en_sport}": "منتخبات {sport_jobs} تحت 19 سنة",
    # "national under-20 {en_sport}": "منتخبات {sport_jobs} تحت 20 سنة",
    # "national under-21 {en_sport}": "منتخبات {sport_jobs} تحت 21 سنة",
    # "national under-23 {en_sport}": "منتخبات {sport_jobs} تحت 23 سنة",
    # "national under-24 {en_sport}": "منتخبات {sport_jobs} تحت 24 سنة",
    "national under-13 {en_sport}": "{sport_jobs} تحت 13 سنة",
    "national under-14 {en_sport}": "{sport_jobs} تحت 14 سنة",
    "national under-15 {en_sport}": "{sport_jobs} تحت 15 سنة",
    "national under-16 {en_sport}": "{sport_jobs} تحت 16 سنة",
    "national under-17 {en_sport}": "{sport_jobs} تحت 17 سنة",
    "national under-18 {en_sport}": "{sport_jobs} تحت 18 سنة",
    "national under-19 {en_sport}": "{sport_jobs} تحت 19 سنة",
    "national under-20 {en_sport}": "{sport_jobs} تحت 20 سنة",
    "national under-21 {en_sport}": "{sport_jobs} تحت 21 سنة",
    "national under-23 {en_sport}": "{sport_jobs} تحت 23 سنة",
    "national under-24 {en_sport}": "{sport_jobs} تحت 24 سنة",
    # teams_formatted_data = {
    "amateur {en_sport} world cup": "كأس العالم {sport_team} للهواة",
    "mens {en_sport} world cup": "كأس العالم {sport_team} للرجال",
    "womens {en_sport} world cup": "كأس العالم {sport_team} للسيدات",
    "{en_sport} world cup": "كأس العالم {sport_team}",
    "youth {en_sport} world cup": "كأس العالم {sport_team} للشباب",
    "international {en_sport} council": "المجلس الدولي {sport_team}",
    "mens {en_sport} championship": "بطولة {sport_team} للرجال",
    "mens {en_sport} world championship": "بطولة العالم {sport_team} للرجال",
    "outdoor world {en_sport} championship": "بطولة العالم {sport_team} في الهواء الطلق",
    "womens world {en_sport} championship": "بطولة العالم {sport_team} للسيدات",
    "womens {en_sport} championship": "بطولة {sport_team} للسيدات",
    "womens {en_sport} world championship": "بطولة العالم {sport_team} للسيدات",
    "world amateur {en_sport} championship": "بطولة العالم {sport_team} للهواة",
    "world champion national {en_sport} teams": "أبطال بطولة العالم {sport_team}",
    "world junior {en_sport} championship": "بطولة العالم {sport_team} للناشئين",
    "world outdoor {en_sport} championship": "بطولة العالم {sport_team} في الهواء الطلق",
    "world wheelchair {en_sport} championship": "بطولة العالم {sport_team} على الكراسي المتحركة",
    "world {en_sport} amateur championship": "بطولة العالم {sport_team} للهواة",
    "world {en_sport} championship": "بطولة العالم {sport_team}",
    "world {en_sport} championship competitors": "منافسو بطولة العالم {sport_team}",
    "world {en_sport} championship medalists": "فائزون بميداليات بطولة العالم {sport_team}",
    "world {en_sport} junior championship": "بطولة العالم {sport_team} للناشئين",
    "world {en_sport} youth championship": "بطولة العالم {sport_team} للشباب",
    "world youth {en_sport} championship": "بطولة العالم {sport_team} للشباب",
    "{en_sport} amateur world championship": "بطولة العالم {sport_team} للهواة",
    "{en_sport} junior world championship": "بطولة العالم {sport_team} للناشئين",
    "{en_sport} world amateur championship": "بطولة العالم {sport_team} للهواة",
    "{en_sport} world championship": "بطولة العالم {sport_team}",
    "{en_sport} world junior championship": "بطولة العالم {sport_team} للناشئين",
    "{en_sport} world youth championship": "بطولة العالم {sport_team} للشباب",
    "{en_sport} youth world championship": "بطولة العالم {sport_team} للشباب",
    # world championships in athletics
    "world championship in {en_sport}": "بطولة العالم {sport_team}",
    "world championship in {en_sport} athletes": "عداؤو بطولة العالم {sport_team}",
    # labels_formatted_data = {
    "{en_sport} finals": "نهائيات {sport_label}",
    "{en_sport}": "{sport_label}",
    "{en_sport} cup": "كأس {sport_label}",
    "olympic gold medalists in {en_sport}": "فائزون بميداليات ذهبية أولمبية في {sport_label}",
    "olympic silver medalists in {en_sport}": "فائزون بميداليات فضية أولمبية في {sport_label}",
    "olympic bronze medalists in {en_sport}": "فائزون بميداليات برونزية أولمبية في {sport_label}",
    "{en_sport} league": "دوري {sport_label}",
    "{en_sport} champions": "أبطال {sport_label}",
    "olympics {en_sport}": "{sport_label} في الألعاب الأولمبية",
    "summer olympics {en_sport}": "{sport_label} في الألعاب الأولمبية الصيفية",
    "winter olympics {en_sport}": "{sport_label} في الألعاب الأولمبية الشتوية",
    # spicial cases
    "olympics sports": "رياضات الألعاب الأولمبية",
    "summer olympics sports": "رياضات الألعاب الأولمبية الصيفية",
    "winter olympics sports": "رياضات الألعاب الأولمبية الشتوية",
    "rugby union chairmen and investors": "رؤساء ومسيرو اتحاد الرجبي",
    "rugby league chairmen and investors": "رؤساء ومسيرو دوري الرجبي",
    "multi-national {en_sport} championships": "بطولات {sport_jobs} متعددة الجنسيات",
    "national {en_sport} championships": "بطولات {sport_jobs} وطنية",
    "{en_sport} championships": "بطولات {sport_jobs}",
    "amateur {en_sport} championships": "بطولات {sport_jobs} للهواة",
}


@functools.lru_cache(maxsize=1)
def _build_unified_sport_keys() -> dict[str, dict[str, str]]:
    """
    Build a unified dictionary mapping sport names to their translation values.

    Returns:
        dict[str, dict[str, str]]: Dictionary where keys are sport names and values
        are dicts containing 'sport_jobs', 'sport_team', and 'sport_label' keys.
    """
    unified: dict[str, dict[str, str]] = {}

    for sport, record in SPORT_KEY_RECORDS.items():
        sport_lower = sport.lower()
        unified[sport_lower] = {
            "sport_jobs": record.get("jobs", ""),
            "sport_team": record.get("team", ""),
            "sport_label": record.get("label", ""),
            "sport_olympic": record.get("olympic", ""),
        }
    unified.update(
        {
            "sports": {
                "sport_jobs": "رياضية",
                "sport_team": "",
                "sport_label": "رياضات",
            }
        }
    )
    return unified


@functools.lru_cache(maxsize=1)
def _load_unified_bot() -> FormatDataV2:
    """
    Create and cache the unified FormatDataV2 instance.

    Returns:
        FormatDataV2: Configured bot for all sports translations.
    """

    UNIFIED_SPORT_KEYS: dict[str, dict[str, str]] = _build_unified_sport_keys()

    return FormatDataV2(
        formatted_data=UNIFIED_FORMATTED_DATA,
        data_list=UNIFIED_SPORT_KEYS,
        key_placeholder="{en_sport}",
    )


def fix_result_callable(result: str, category: str, key: str, value: str) -> str:
    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    if key == "teams" and "national" in category:
        result = result.replace("فرق ", "منتخبات ")

    return result


@functools.lru_cache(maxsize=10000)
def fix_keys(category: str) -> str:
    """
    Normalize a raw category string by removing quotes and prefixes, fixing common typos, and trimming whitespace.

    Parameters:
        category (str): Input category text that may contain single quotes, a "category:" prefix, inconsistent casing, or the typo "playerss".

    Returns:
        str: The cleaned category string in lowercase with the "category:" prefix and single quotes removed, "playerss" corrected to "players", and surrounding whitespace trimmed.
    """
    category = category.replace("'", "").lower().replace("category:", "")
    category = category.replace("playerss", "players")
    return category.strip()


@functools.lru_cache(maxsize=10000)
def resolve_sport_label_unified(category: str, default: str = "") -> str:
    """
    Resolve the Arabic label for a sport given a category key.

    Normalizes the provided category and attempts to find a matching Arabic sport label; returns the provided default when no match is found.


    This function combines the functionality of:
    - resolve_sport_label_unified
    - resolve_sport_label_by_teams_key
    - resolve_sport_label_by_labels_key

    Parameters:
        category (str): Category key or phrase identifying the sport to resolve.
        default (str): Value to return if no label can be found.

    Returns:
        str: The resolved Arabic sport label if found, otherwise `default`.
    """
    logger.debug(f"<<yellow>> start resolve_sport_label_unified: {category=}")
    category = fix_keys(category)

    # if pre_defined_results.get(category):
    #     logger.info(f"<<yellow>> end resolve_sport_label_unified (pre_defined): {category=}, {pre_defined_results[category]=}")
    #     return pre_defined_results[category]

    if SPORT_KEY_RECORDS.get(category):
        label = SPORT_KEY_RECORDS[category].get("label", "")
        logger.info(f"<<yellow>> end resolve_sport_label_unified (SPORT_KEY_RECORDS): {category=}, {label=}")
        return label

    unified_bot = _load_unified_bot()
    result = unified_bot.search(category)

    if not result and "world" in category:
        category2 = category.replace("championships", "championship")
        result = unified_bot.search(category2)

    logger.info_if_or_debug(f"<<yellow>> end resolve_sport_label_unified: {category=}, {result=}", result)
    return result or default


__all__ = [
    "resolve_sport_label_unified",
]
