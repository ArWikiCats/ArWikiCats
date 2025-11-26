#!/usr/bin/python3
"""
Comprehensive sport template dictionaries used throughout the project.
"""

from typing import Final, Dict

from ...helps import len_print
from .Sport_key import SPORTS_KEYS_FOR_LABEL, SPORTS_KEYS_FOR_TEAM

COUNTRY_PLACEHOLDER: Final[str] = "{}"
NAT_PLACEHOLDER: Final[str] = "{nat}"

SPORT_FORMTS_MALE_NAT = {}  # الإنجليزي جنسية والعربي جنسية
SPORT_FORMTS_FEMALE_NAT = {}  # الإنجليزي جنسية والعربي جنسية
SPORT_FORMTS_EN_P17_AR_NAT = {}  # الإنجليزي إسم البلد والعربي جنسية
SPORT_FORMTS_EN_AR_IS_P17 = {}  # الإنجليزي إسم البلد والعربي يكون اسم البلد
SPORT_FORMTS_NEW_KKK = {}  # الإنجليزي جنسية والعربي اسم البلد

Teams = {
    "national sports teams": "منتخبات رياضية وطنية",
    "national teams": "منتخبات وطنية",
    "teams": "فرق",
    "sports teams": "فرق رياضية",
    "football clubs": "أندية كرة قدم",
    "clubs": "أندية",
}

sport_starts = {
    "": "",
    "men's a' ": "للرجال للمحليين",
    "men's b ": "الرديف للرجال",
    "men's ": "للرجال",
    "women's ": "للسيدات",
    "men's youth ": "للشباب",
    "women's youth ": "للشابات",
    "amateur ": "للهواة",
    "youth ": "للشباب",
}


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------

def _build_male_nat() -> Dict[str, str]:
    """English nationality → Arabic nationality (male formats)."""
    label_index: Dict[str, str] = {}

    for sport, label in SPORTS_KEYS_FOR_LABEL.items():
        label_index[f"{sport.lower()} super league"] = f"دوري السوبر {label} {COUNTRY_PLACEHOLDER}"

        # tab[Category:yemeni professional Soccer League] = "تصنيف:دوري كرة القدم اليمني للمحترفين"
        label_index[f"professional {sport.lower()} league"] = f"دوري {label} {COUNTRY_PLACEHOLDER} للمحترفين"

    # فرق دول وطنية

    for team2, team2_lab in SPORTS_KEYS_FOR_TEAM.items():
        # Middle East Rally Championship بطولة الشرق الأوسط للراليات

        label_index[f"{team2.lower()} federation"] = f"الاتحاد {COUNTRY_PLACEHOLDER} {team2_lab}"

        label_index[f"{team2.lower()} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {team2_lab}"

        label_index[f"women's {team2.lower()} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {team2_lab} للسيدات"
        label_index[f"{team2.lower()} league administrators"] = f"مدراء الدوري {COUNTRY_PLACEHOLDER} {team2_lab}"
        label_index[f"{team2.lower()} league players"] = f"لاعبو الدوري {COUNTRY_PLACEHOLDER} {team2_lab}"
        label_index[f"{team2.lower()} league playerss"] = f"لاعبو الدوري {COUNTRY_PLACEHOLDER} {team2_lab}"

        # tab[Category:American Indoor Soccer League coaches] = "تصنيف:مدربو الدوري الأمريكي لكرة القدم داخل الصالات"
        label_index[f"indoor {team2.lower()} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {team2_lab} داخل الصالات"
        label_index[f"outdoor {team2.lower()} league"] = (
            f"الدوري {COUNTRY_PLACEHOLDER} {team2_lab} في الهواء الطلق"
        )

        # tab[Category:Canadian Major Indoor Soccer League seasons] = "تصنيف:مواسم الدوري الرئيسي الكندي لكرة القدم داخل الصالات"
        label_index[f"major indoor {team2.lower()} league"] = (
            f"الدوري الرئيسي {COUNTRY_PLACEHOLDER} {team2_lab} داخل الصالات"
        )

    return label_index


def _build_female_nat() -> Dict[str, str]:
    """English nationality → Arabic nationality (female formats)."""
    label_index: Dict[str, str] = {}

    for sport, label in SPORTS_KEYS_FOR_LABEL.items():
        # tab[Category:American Indoor Soccer] = "تصنيف:كرة القدم الأمريكية داخل الصالات"
        label_index[f"outdoor {sport.lower()}"] = f"{label} {COUNTRY_PLACEHOLDER} في الهواء الطلق"
        label_index[f"indoor {sport.lower()}"] = f"{label} {COUNTRY_PLACEHOLDER} داخل الصالات"

    return label_index


def _build_en_p17_ar_nat() -> Dict[str, str]:
    """
    English country-name → Arabic nationality
    Example: “{team2} federation” = "الاتحاد {nat} ..."
    """
    label_index: Dict[str, str] = {}

    for team2, team2_lab in SPORTS_KEYS_FOR_TEAM.items():
        label_index[f"{team2} federation"] = f"الاتحاد {NAT_PLACEHOLDER} {team2_lab}"

    return label_index


def _build_new_kkk() -> Dict[str, str]:
    """
    English nationality → Arabic country-name
    Example: “men's hockey cup” → “كأس {} الهوكي للرجال”
    """
    label_index: Dict[str, str] = {}

    for team2, team2_lab in SPORTS_KEYS_FOR_TEAM.items():
        # Category:National junior women's goalball teams
        label_index[f"men's {team2} cup"] = f"كأس {COUNTRY_PLACEHOLDER} {team2_lab} للرجال"
        label_index[f"women's {team2} cup"] = f"كأس {COUNTRY_PLACEHOLDER} {team2_lab} للسيدات"
        label_index[f"{team2} cup"] = f"كأس {COUNTRY_PLACEHOLDER} {team2_lab}"
        label_index[f"national junior men's {team2} team"] = f"منتخب {COUNTRY_PLACEHOLDER} {team2_lab} للناشئين"
        label_index[f"national junior {team2} team"] = f"منتخب {COUNTRY_PLACEHOLDER} {team2_lab} للناشئين"
        label_index[f"national {team2} team"] = f"منتخب {COUNTRY_PLACEHOLDER} {team2_lab}"
        label_index[f"national women's {team2} team"] = f"منتخب {COUNTRY_PLACEHOLDER} {team2_lab} للسيدات"
        label_index[f"national men's {team2} team"] = f"منتخب {COUNTRY_PLACEHOLDER} {team2_lab} للرجال"

    return label_index


def _build_en_ar_is_p17() -> Dict[str, str]:
    """
    English country-name → Arabic country-name.
    This is the biggest dictionary (footballers, under-18, etc.).
    """
    YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
    # years make 330 key

    label_index: Dict[str, str] = {}

    # Static entries
    label_index["international rules football team"] = "منتخب {} لكرة القدم الدولية"

    label_index["cup"] = "كأس {}"
    label_index["presidents"] = "رؤساء {}"
    label_index["territorial officials"] = "مسؤولو أقاليم {}"
    label_index["territorial judges"] = "قضاة أقاليم {}"
    label_index["war"] = "حرب {}"

    # Under-year managers/players
    for year in YEARS_LIST:
        label_index[f"under-{year} international managers"] = (
            f"مدربو تحت {year} سنة دوليون من {COUNTRY_PLACEHOLDER}"
        )
        label_index[f"under-{year} international players"] = (
            f"لاعبو تحت {year} سنة دوليون من {COUNTRY_PLACEHOLDER}"
        )
        label_index[f"under-{year} international playerss"] = (
            f"لاعبو تحت {year} سنة دوليون من {COUNTRY_PLACEHOLDER}"
        )

    # Footballers base groups
    for modifier, mod_label in sport_starts.items():
        # label_index["international footballers"] = f"لاعبو منتخب {COUNTRY_PLACEHOLDER} لكرة القدم"

        start_word = "لاعبات منتخب" if "women's" in modifier else "لاعبو منتخب"

        base = f"{start_word} {COUNTRY_PLACEHOLDER} لكرة القدم {mod_label}"

        label_index[f"{modifier}international footballers"] = base
        label_index[f"{modifier}international soccer players"] = base
        label_index[f"{modifier}international soccer playerss"] = base

        # Category:Australia under-18 international soccer players
        # تصنيف:لاعبو منتخب أستراليا تحت 18 سنة لكرة القدم

        # Category:Zimbabwe men's A' international footballers
        # Category:Belgian men's international footballers

        for year in YEARS_LIST:
            youth = f"{start_word} {COUNTRY_PLACEHOLDER} تحت {year} سنة لكرة القدم {mod_label}"
            label_index[f"{modifier}under-{year} international footballers"] = youth
            label_index[f"{modifier}under-{year} international soccer players"] = youth
            label_index[f"{modifier}under-{year} international soccer playerss"] = youth

    label_index["rally championship"] = f"بطولة {COUNTRY_PLACEHOLDER} للراليات"
    label_index["war and conflict"] = f"حروب ونزاعات {COUNTRY_PLACEHOLDER}"
    label_index["governorate"] = f"حكومة {COUNTRY_PLACEHOLDER}"

    label_index["sports templates"] = f"قوالب {COUNTRY_PLACEHOLDER} الرياضية"
    label_index["national team"] = f"منتخبات {COUNTRY_PLACEHOLDER} الوطنية"
    label_index["national teams"] = f"منتخبات {COUNTRY_PLACEHOLDER} الوطنية"
    label_index["national football team managers"] = f"مدربو منتخب {COUNTRY_PLACEHOLDER} لكرة القدم"

    label_index["international rally"] = f"رالي {COUNTRY_PLACEHOLDER} الدولي"

    return label_index


# ----------------------------------------------------------------------
# Build final dictionaries once
# ----------------------------------------------------------------------
SPORT_FORMTS_MALE_NAT = _build_male_nat()
SPORT_FORMTS_FEMALE_NAT = _build_female_nat()
SPORT_FORMTS_EN_P17_AR_NAT = _build_en_p17_ar_nat()
SPORT_FORMTS_EN_AR_IS_P17 = _build_en_ar_is_p17()
SPORT_FORMTS_NEW_KKK = _build_new_kkk()

len_print.data_len(
    "skeys.py",
    {
        "SPORT_FORMTS_EN_AR_IS_P17": SPORT_FORMTS_EN_AR_IS_P17,
        "SPORT_FORMTS_EN_P17_AR_NAT": SPORT_FORMTS_EN_P17_AR_NAT,
        "SPORT_FORMTS_FEMALE_NAT": SPORT_FORMTS_FEMALE_NAT,
        "SPORT_FORMTS_MALE_NAT": SPORT_FORMTS_MALE_NAT,
        "SPORT_FORMTS_NEW_KKK": SPORT_FORMTS_NEW_KKK,
    },
)

__all__ = [
    "SPORT_FORMTS_EN_AR_IS_P17",
    "SPORT_FORMTS_EN_P17_AR_NAT",
    "SPORT_FORMTS_FEMALE_NAT",
    "SPORT_FORMTS_MALE_NAT",
    "SPORT_FORMTS_NEW_KKK",
]
