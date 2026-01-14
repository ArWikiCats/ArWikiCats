#!/usr/bin/python3
"""
Comprehensive sport template dictionaries used throughout the project.
"""

from typing import Dict, Final

from ...helps import len_print
from .Sport_key import SPORTS_KEYS_FOR_LABEL, SPORTS_KEYS_FOR_TEAM

COUNTRY_PLACEHOLDER: Final[str] = "{}"

SPORT_FORMATS_MALE_NAT = {}  # الإنجليزي جنسية والعربي جنسية


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

        label_index[f"{team2.lower()} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {team2_lab}"

        label_index[f"women's {team2.lower()} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {team2_lab} للسيدات"
        label_index[f"{team2.lower()} league administrators"] = f"مدراء الدوري {COUNTRY_PLACEHOLDER} {team2_lab}"
        label_index[f"{team2.lower()} league players"] = f"لاعبو الدوري {COUNTRY_PLACEHOLDER} {team2_lab}"
        label_index[f"{team2.lower()} league playerss"] = f"لاعبو الدوري {COUNTRY_PLACEHOLDER} {team2_lab}"

        # tab[Category:American Indoor Soccer League coaches] = "تصنيف:مدربو الدوري الأمريكي لكرة القدم داخل الصالات"
        label_index[f"indoor {team2.lower()} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {team2_lab} داخل الصالات"
        label_index[f"outdoor {team2.lower()} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {team2_lab} في الهواء الطلق"

        # tab[Category:Canadian Major Indoor Soccer League seasons] = "تصنيف:مواسم الدوري الرئيسي الكندي لكرة القدم داخل الصالات"
        label_index[f"major indoor {team2.lower()} league"] = f"الدوري الرئيسي {COUNTRY_PLACEHOLDER} {team2_lab} داخل الصالات"

    return label_index


# ----------------------------------------------------------------------
# Build final dictionaries once
# ----------------------------------------------------------------------
SPORT_FORMATS_MALE_NAT = _build_male_nat()

len_print.data_len(
    "skeys.py",
    {
        "SPORT_FORMATS_MALE_NAT": SPORT_FORMATS_MALE_NAT,
    },
)

__all__ = [
    "SPORT_FORMATS_MALE_NAT",
]
