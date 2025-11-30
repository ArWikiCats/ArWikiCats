#!/usr/bin/python3
"""
Comprehensive sport template dictionaries used throughout the project.
"""

from typing import Final, Dict

from ...helps import len_print
from .Sport_key import SPORTS_KEYS_FOR_LABEL, SPORTS_KEYS_FOR_TEAM

COUNTRY_PLACEHOLDER: Final[str] = "{}"

SPORT_FORMTS_MALE_NAT = {}  # الإنجليزي جنسية والعربي جنسية
SPORT_FORMTS_FEMALE_NAT = {}  # الإنجليزي جنسية والعربي جنسية
SPORT_FORMTS_NEW_KKK = {}  # الإنجليزي جنسية والعربي اسم البلد

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


# ----------------------------------------------------------------------
# Build final dictionaries once
# ----------------------------------------------------------------------
SPORT_FORMTS_MALE_NAT = _build_male_nat()
SPORT_FORMTS_FEMALE_NAT = _build_female_nat()
SPORT_FORMTS_NEW_KKK = _build_new_kkk()

len_print.data_len(
    "skeys.py",
    {
        "SPORT_FORMTS_FEMALE_NAT": SPORT_FORMTS_FEMALE_NAT,
        "SPORT_FORMTS_MALE_NAT": SPORT_FORMTS_MALE_NAT,
        "SPORT_FORMTS_NEW_KKK": SPORT_FORMTS_NEW_KKK,
    },
)

__all__ = [
    "SPORT_FORMTS_FEMALE_NAT",
    "SPORT_FORMTS_MALE_NAT",
    "SPORT_FORMTS_NEW_KKK",
]
