#!/usr/bin/python3
"""

Resolves category labels for sports federations based on nationality.
This module constructs a formatter that combines nationality data with sports data
to translate category titles like "{nationality} {sport} federation" into Arabic.

NOTE: compare it with ArWikiCats/new_resolvers/sports_formats_teams/sport_lab_nat.py

"""

import functools

from ...helps import getLogger
from ...new.handle_suffixes import resolve_sport_category_suffix_with_mapping
from ...translations import SPORT_KEY_RECORDS, all_country_with_nat_ar
from ...translations_formats import MultiDataFormatterBaseV2, format_multi_data_v2
from ..nationalities_resolvers.data import sports_formatted_data_for_jobs
from .utils import fix_keys
from .utils.formated_data import SPORTS_FORMATTED_DATA_NATS_AND_NAMES

logger = getLogger(__name__)


@functools.lru_cache(maxsize=1)
def _get_sorted_teams_labels() -> dict[str, str]:
    teams_label_mappings_ends_old = {
        "champions": "أبطال",
        "events": "أحداث",
        "films": "أفلام",
        "finals": "نهائيات",
        "home stadiums": "ملاعب",
        "lists": "قوائم",
        "manager history": "تاريخ مدربو",
        "managers": "مدربو",
        "matches": "مباريات",
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

    mappings_data = {
        "tournaments": "بطولات",
        "leagues": "دوريات",
        "coaches": "مدربو",
        "clubs": "أندية",
        "clubs and teams": "أندية وفرق",
        "competitions": "منافسات",
        # "chairmen and investors": "رؤساء ومسيرو",
        "cups": "كؤوس",
    }

    mappings_data = dict(
        sorted(
            mappings_data.items(),
            key=lambda k: (-k[0].count(" "), -len(k[0])),
        )
    )
    return mappings_data


def _levels_data() -> dict[str, str]:
    data = {
        "{en} league of {en_sport}": "الدوري {the_male} {sport_team}",
        "{en} {en_sport} premier league": "الدوري {the_male} الممتاز {sport_team}",
        "{en} premier {en_sport} league": "الدوري {the_male} الممتاز {sport_team}",
        # "bangladesh football premier leagues": "تصنيف:دوريات كرة قدم بنغلاديشية من الدرجة الممتازة",
        "{en} {en_sport} premier": "{sport_jobs} {female} من الدرجة الممتازة",
        "{en_sport} premier": "{sport_jobs} من الدرجة الممتازة",
        "{en} premier {en_sport}": "{sport_jobs} {female} من الدرجة الممتازة",
        "premier {en_sport}": "{sport_jobs} من الدرجة الممتازة",
    }
    LEVELS: dict[str, str] = {
        "premier": "الدرجة الممتازة",
        "top level": "الدرجة الأولى",
        "first level": "الدرجة الأولى",
        "first tier": "الدرجة الأولى",
        "second level": "الدرجة الثانية",
        "second tier": "الدرجة الثانية",
        "third level": "الدرجة الثالثة",
        "third tier": "الدرجة الثالثة",
        "fourth level": "الدرجة الرابعة",
        "fourth tier": "الدرجة الرابعة",
        "fifth level": "الدرجة الخامسة",
        "fifth tier": "الدرجة الخامسة",
        "sixth level": "الدرجة السادسة",
        "sixth tier": "الدرجة السادسة",
        "seventh level": "الدرجة السابعة",
        "seventh tier": "الدرجة السابعة",
    }
    for level, lvl_lab in LEVELS.items():
        data.update(
            {
                f"{{en}} {{en_sport}} {level} leagues": f"دوريات {{sport_jobs}} {{female}} من {lvl_lab}",
                f"{{en}} {level} {{en_sport}} leagues": f"دوريات {{sport_jobs}} {{female}} من {lvl_lab}",
                f"national {{en_sport}} {level} leagues": f"دوريات {{sport_jobs}} وطنية من {lvl_lab}",
                f"{{en_sport}} {level} leagues": f"دوريات {{sport_jobs}} من {lvl_lab}",
                f"{level} {{en_sport}} leagues": f"دوريات {{sport_jobs}} من {lvl_lab}",
            }
        )

    return data


@functools.lru_cache(maxsize=1)
def _load_sports_formatted_data() -> dict[str, str]:
    sports_formatted_data = {
        "{en} league cup": "كأس الدوري {the_male}",
        "{en} independence cup": "كأس الاستقلال {the_male}",
        "amateur {en_sport} world cup": "كأس العالم {sport_team} للهواة",
        "mens {en_sport} world cup": "كأس العالم {sport_team} للرجال",
        "womens {en_sport} world cup": "كأس العالم {sport_team} للسيدات",
        "{en_sport} world cup": "كأس العالم {sport_team}",
        "youth {en_sport} world cup": "كأس العالم {sport_team} للشباب",
        "{en} mens {en_sport} cup": "كأس {ar} {sport_team} للرجال",
        "{en} womens {en_sport} cup": "كأس {ar} {sport_team} للسيدات",
        "{en} {en_sport} cup": "كأس {ar} {sport_team}",
        # NAT_P17_OIOI_TO_CHECK data
        # "yemeni defunct basketball cup": "كؤوس كرة سلة يمنية سابقة",
        "{en} defunct {en_sport} cup": "كؤوس {sport_jobs} {female} سابقة",
        "{en} domestic {en_sport} cup": "كؤوس {sport_jobs} {female} محلية",
        "{en} federation cup": "كأس الاتحاد {the_male}",
        "olympic gold medalists in {en_sport}": "فائزون بميداليات ذهبية أولمبية في {sport_label}",
        "olympic silver medalists in {en_sport}": "فائزون بميداليات فضية أولمبية في {sport_label}",
        "olympic bronze medalists in {en_sport}": "فائزون بميداليات برونزية أولمبية في {sport_label}",
        "{en} mens {en_sport} national team": "منتخب {ar} {sport_team} للرجال",
        "{en} mens u23 national {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة للرجال",
        "{en} {en_sport} national team": "منتخب {ar} {sport_team}",
        "first league of {en}": "دوري {ar} الممتاز",
        "{en}-american coaches of canadian-football": "مدربو كرة قدم كندية أمريكيون {males}",
        # "yemeni men's basketball players" : "لاعبو كرة سلة رجالية يمنيون",
        "{en} mens {en_sport} players": "لاعبو {sport_jobs} {males}",
        # american coaches of basketball
        "{en} coaches of {en_sport}": "مدربو {sport_jobs} {males}",
        "{en}-american coaches of {en_sport}": "مدربو {sport_jobs} أمريكيون {males}",
        # coaches of basketball
        "coaches of {en_sport}": "مدربو {sport_jobs}",
        "players of {en_sport}": "لاعبو {sport_jobs}",
        # lithuanian expatriate basketball people "أعلام كرة سلة ليتوانيون مغتربون"
        "{en} expatriate {en_sport} peoplee": "أعلام {sport_jobs} {males} مغتربون",
        "{en} expatriate {en_sport} people": "أعلام {sport_jobs} {males} مغتربون",
        # expatriate basketball people
        "expatriate {en_sport} peoplee": "أعلام {sport_jobs} مغتربون",
        "expatriate {en_sport} people": "أعلام {sport_jobs} مغتربون",
        "{en} {en_sport} people": "أعلام {sport_label} {the_female}",
        # _build_new_kkk() -> dict[str, str]:
        # Category:National junior womens goalball teams
        "{en} national junior mens {en_sport} team": "منتخب {ar} {sport_team} للناشئين",
        "{en} national junior {en_sport} team": "منتخب {ar} {sport_team} للناشئين",
        "{en} national womens {en_sport} team": "منتخب {ar} {sport_team} للسيدات",
        "{en} national mens {en_sport} team": "منتخب {ar} {sport_team} للرجال",
        # _build_male_nat()
        "{en} league": "الدوري {the_male}",
        "{en} fa cup": "كأس الاتحاد {the_male}",
        "{en} {en_sport} super league": "دوري السوبر {sport_label} {the_male}",
        "{en} professional {en_sport} league": "دوري {sport_label} {the_male} للمحترفين",
        # Middle East Rally Championship بطولة الشرق الأوسط للراليات
        "{en} {en_sport} league": "الدوري {the_male} {sport_team}",
        "{en} {en_sport} league administrators": "مدراء الدوري {the_male} {sport_team}",
        "{en} {en_sport} league players": "لاعبو الدوري {the_male} {sport_team}",
        "{en} {en_sport} league playerss": "لاعبو الدوري {the_male} {sport_team}",
        # tab[Category:American Indoor Soccer League coaches] = "تصنيف:مدربو الدوري الأمريكي لكرة القدم داخل الصالات"
        "{en} indoor {en_sport} league": "الدوري {the_male} {sport_team} داخل الصالات",
        "{en} outdoor {en_sport} league": "الدوري {the_male} {sport_team} في الهواء الطلق",
        # tab[Category:Canadian Major Indoor Soccer League seasons] = "تصنيف:مواسم الدوري الرئيسي الكندي لكرة القدم داخل الصالات"
        "{en} major indoor {en_sport} league": "الدوري الرئيسي {the_male} {sport_team} داخل الصالات",
        # "yemeni major indoor wheelchair football league": "الدوري الرئيسي اليمني لكرة القدم على الكراسي المتحركة داخل الصالات",
        "{en} major indoor wheelchair {en_sport} league": "الدوري الرئيسي {the_male} {sport_team} على الكراسي المتحركة داخل الصالات",
        # ---
        # SPORT_FORMATS_FEMALE_NAT
        # [chinese outdoor boxing] : "تصنيف:بوكسينغ صينية في الهواء الطلق",
        "{en} outdoor {en_sport}": "{sport_jobs} {female} في الهواء الطلق",
        # [Category:American Indoor Soccer] : "تصنيف:كرة قدم أمريكية داخل الصالات",
        "{en} indoor {en_sport}": "{sport_jobs} {female} داخل الصالات",
        # data
        # "Category:zaïrean wheelchair sports federation": "تصنيف:الاتحاد الزائيري للرياضة على الكراسي المتحركة",
        # "Category:surinamese sports federation": "تصنيف:الاتحاد السورينامي للرياضة",
        "{en} sports federation": "الاتحاد {the_male} للرياضة",
        "{en} wheelchair sports federation": "الاتحاد {the_male} للرياضة على الكراسي المتحركة",
        "{en} wheelchair racers": "متسابقو كراسي متحركة {males}",
        "{en} mens wheelchair racers": "متسابقو كراسي متحركة {males}",
        "{en} {en_sport} federation": "الاتحاد {the_male} {sport_team}",
        "ladies {en} {en_sport} championships": "بطولة {ar} {sport_team} للسيدات",
        "ladies {en} {en_sport} tour": "بطولة {ar} {sport_team} للسيدات",
        "womens {en} {en_sport} tour": "بطولة {ar} {sport_team} للسيدات",
        "{en} {en_sport} championships": "بطولة {ar} {sport_team}",
        "{en} {en_sport} championshipszz": "بطولة {ar} {sport_team}",
        "{en} {en_sport} tour": "بطولة {ar} {sport_team}",
        # Category:yemeni Women's Football League
        "womens {en} {en_sport} league": "الدوري {the_male} {sport_team} للسيدات",
        "womens {en} {en_sport} league players": "لاعبات الدوري {the_male} {sport_team} للسيدات",
        "{en} womens {en_sport} league": "الدوري {the_male} {sport_team} للسيدات",
        "{en} womens {en_sport} league players": "لاعبات الدوري {the_male} {sport_team} للسيدات",
        "womens national {en_sport} league": "الدوري الوطني {sport_team} للسيدات",
        "{en} national {en_sport} teams": "منتخبات {sport_jobs} وطنية {female}",
        "{en} womens {en_sport} players": "لاعبات {sport_jobs} {females}",
        "womens {en_sport} players": "لاعبات {sport_jobs}",
        "{en} womens {en_sport} playerss": "لاعبات {sport_jobs} {females}",
        "womens {en_sport} playerss": "لاعبات {sport_jobs}",
        "{en} womens national {en_sport} team": "منتخب {ar} {sport_team} للسيدات",
        "{en} womens national {en_sport} team players": "لاعبات منتخب {ar} {sport_team} للسيدات",
        "{en} national {en_sport} team": "منتخب {ar} {sport_team}",
        "{en} national {en_sport} team players": "لاعبو منتخب {ar} {sport_team}",
        "{en} womens international footballers": "لاعبات منتخب {ar} لكرة القدم للسيدات",
        "{en} womens youth international footballers": "لاعبات منتخب {ar} لكرة القدم للشابات",
        "{en} womens international {en_sport} players": "لاعبات {sport_jobs} دوليات من {ar}",
        "{en} international footballers": "لاعبو منتخب {ar} لكرة القدم",
        "{en} international {en_sport} players": "لاعبو {sport_jobs} دوليون من {ar}",
        "{en} {en_sport} association": "الرابطة {the_female} {sport_team}",
        "womens {en} {en_sport} association": "الرابطة {the_female} {sport_team} للسيدات",
        # Category:African women's national association football teams
        "womens national {en_sport} teams": "منتخبات {sport_jobs} وطنية للسيدات",
        "{en} womens national {en_sport} teams": "منتخبات {sport_jobs} وطنية {female} للسيدات",
        "{en} womens {en_sport}": "{sport_jobs} {female} للسيدات",
        # northern ireland national men's football teams
        "national mens {en_sport} teams": "منتخبات {sport_jobs} وطنية للرجال",
        "{en} national mens {en_sport} teams": "منتخبات {sport_jobs} وطنية {female} للرجال",
        # NAT_P17_OIOI data
        "{en} amateur {en_sport} championship": "بطولة {ar} {sport_team} للهواة",
        "{en} amateur {en_sport} championships": "بطولة {ar} {sport_team} للهواة",
        "{en} championships ({en_sport})": "بطولة {ar} {sport_team}",
        "{en} championships {en_sport}": "بطولة {ar} {sport_team}",
        "{en} mens {en_sport} championship": "بطولة {ar} {sport_team} للرجال",
        "{en} mens {en_sport} championships": "بطولة {ar} {sport_team} للرجال",
        "{en} {en_sport} championship": "بطولة {ar} {sport_team}",
        "{en} {en_sport} indoor championship": "بطولة {ar} {sport_team} داخل الصالات",
        "{en} {en_sport} indoor championships": "بطولة {ar} {sport_team} داخل الصالات",
        "{en} {en_sport} junior championships": "بطولة {ar} {sport_team} للناشئين",
        "{en} {en_sport} u-13 championships": "بطولة {ar} {sport_team} تحت 13 سنة",
        "{en} {en_sport} u-14 championships": "بطولة {ar} {sport_team} تحت 14 سنة",
        "{en} {en_sport} u-15 championships": "بطولة {ar} {sport_team} تحت 15 سنة",
        "{en} {en_sport} u-16 championships": "بطولة {ar} {sport_team} تحت 16 سنة",
        "{en} {en_sport} u-17 championships": "بطولة {ar} {sport_team} تحت 17 سنة",
        "{en} {en_sport} u-18 championships": "بطولة {ar} {sport_team} تحت 18 سنة",
        "{en} {en_sport} u-19 championships": "بطولة {ar} {sport_team} تحت 19 سنة",
        "{en} {en_sport} u-20 championships": "بطولة {ar} {sport_team} تحت 20 سنة",
        "{en} {en_sport} u-21 championships": "بطولة {ar} {sport_team} تحت 21 سنة",
        "{en} {en_sport} u-23 championships": "بطولة {ar} {sport_team} تحت 23 سنة",
        "{en} {en_sport} u-24 championships": "بطولة {ar} {sport_team} تحت 24 سنة",
        "{en} {en_sport} u13 championships": "بطولة {ar} {sport_team} تحت 13 سنة",
        "{en} {en_sport} u14 championships": "بطولة {ar} {sport_team} تحت 14 سنة",
        "{en} {en_sport} u15 championships": "بطولة {ar} {sport_team} تحت 15 سنة",
        "{en} {en_sport} u16 championships": "بطولة {ar} {sport_team} تحت 16 سنة",
        "{en} {en_sport} u17 championships": "بطولة {ar} {sport_team} تحت 17 سنة",
        "{en} {en_sport} u18 championships": "بطولة {ar} {sport_team} تحت 18 سنة",
        "{en} {en_sport} u19 championships": "بطولة {ar} {sport_team} تحت 19 سنة",
        "{en} {en_sport} u20 championships": "بطولة {ar} {sport_team} تحت 20 سنة",
        "{en} {en_sport} u21 championships": "بطولة {ar} {sport_team} تحت 21 سنة",
        "{en} {en_sport} u23 championships": "بطولة {ar} {sport_team} تحت 23 سنة",
        "{en} {en_sport} u24 championships": "بطولة {ar} {sport_team} تحت 24 سنة",
        "{en} outdoor {en_sport} championship": "بطولة {ar} {sport_team} في الهواء الطلق",
        "{en} outdoor {en_sport} championships": "بطولة {ar} {sport_team} في الهواء الطلق",
        "{en} womens {en_sport} championship": "بطولة {ar} {sport_team} للسيدات",
        "{en} womens {en_sport} championships": "بطولة {ar} {sport_team} للسيدات",
        "{en} youth {en_sport} championship": "بطولة {ar} {sport_team} للشباب",
        "{en} youth {en_sport} championships": "بطولة {ar} {sport_team} للشباب",
        # "yemeni domestic basketball": "كرة سلة يمنية محلية",
        "{en} domestic {en_sport}": "{sport_jobs} {female} محلية",
        "{en} domestic womens {en_sport}": "{sport_jobs} {female} محلية للسيدات",
        # "yemeni football": "كرة قدم يمنية",
        # "{en} {en_sport}": "{sport_jobs} {female}",
        # Category:American_basketball
        "{en} {en_sport}": "{sport_label} {the_female}",
        # german football chairmen and investors
        "{en} {en_sport} chairmen and investors": "رؤساء ومسيرو {sport_label} {the_female}",
        "{en} current {en_sport} seasons": "مواسم {sport_jobs} {female} حالية",
        "{en} reserve {en_sport}": "{sport_jobs} {female} احتياطية",
        "{en} defunct indoor {en_sport}": "{sport_jobs} {female} داخل الصالات سابقة",
        "{en} defunct {en_sport}": "{sport_jobs} {female} سابقة",
        "{en} defunct outdoor {en_sport}": "{sport_jobs} {female} في الهواء الطلق سابقة",
        "{en} professional {en_sport}": "{sport_jobs} {female} للمحترفين",
        "{en} rugby union": "اتحاد الرجبي {the_male}",
        "{en} rugby league": "الدوري {the_male} للرجبي",
        # spicial cases
        "{en} rugby union chairmen and investors": "رؤساء ومسيرو اتحاد الرجبي {the_male}",
        "{en} rugby league chairmen and investors": "رؤساء ومسيرو الدوري {the_male} للرجبي",
    }
    sports_formatted_data.update(SPORTS_FORMATTED_DATA_NATS_AND_NAMES)
    sports_formatted_data.update(_levels_data())
    sports_formatted_data.update(sports_formatted_data_for_jobs)

    WOMENS_NATIONAL_DATA = {
        x.replace("womens national", "national womens"): v
        for x, v in sports_formatted_data.items()
        if "womens national" in x
    }

    sports_formatted_data.update(WOMENS_NATIONAL_DATA)

    return sports_formatted_data


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    nats_data = {x: v for x, v in all_country_with_nat_ar.items() if v.get("ar")}  # and v.get("en")

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
def _resolve_nats_sport_multi_v2(category: str) -> str:
    logger.debug(f"<<yellow>> start _resolve_nats_sport_multi_v2: {category=}")

    both_bot = _load_bot()
    category = fix_keys(category)
    result = both_bot.search_all_category(category)

    logger.info_if_or_debug(f"<<yellow>> end _resolve_nats_sport_multi_v2: {category=}, {result=}", result)
    return result


def fix_result_callable(result: str, category: str, key: str, value: str) -> str:
    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    if key == "teams" and "national" in category:
        result = result.replace("فرق ", "منتخبات ")

    return result


@functools.lru_cache(maxsize=10000)
def resolve_nats_sport_multi_v2(category: str) -> str:
    category = fix_keys(category)

    logger.debug(f"<<yellow>> start resolve_nats_sport_multi_v2: {category=}")
    teams_label_mappings_ends = _get_sorted_teams_labels()

    result = resolve_sport_category_suffix_with_mapping(
        category=category,
        data=teams_label_mappings_ends,
        callback=_resolve_nats_sport_multi_v2,
        fix_result_callable=fix_result_callable,
    )

    logger.info_if_or_debug(f"<<yellow>> end resolve_nats_sport_multi_v2: {category=}, {result=}", result)
    return result


__all__ = [
    "resolve_nats_sport_multi_v2",
]
