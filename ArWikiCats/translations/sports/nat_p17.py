#!/usr/bin/python3
"""
!
"""

import sys

from ...config import app_settings
from ...helps import len_print
from .Sport_key import SPORTS_KEYS_FOR_TEAM

YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]


def make_tab() -> dict[str, str]:
    """Generate nationality-sensitive sports templates for P17 mappings."""
    SP17 = {}
    for team2, team2_lab in SPORTS_KEYS_FOR_TEAM.items():
        nat_f = "{nat}"

        for ioi in ["championships", "championship"]:
            SP17[f"{team2} {ioi}"] = f"بطولة {nat_f} {team2_lab}"
            SP17[f"youth {team2} {ioi}"] = f"بطولة {nat_f} {team2_lab} للشباب"
            SP17[f"men's {team2} {ioi}"] = f"بطولة {nat_f} {team2_lab} للرجال"
            SP17[f"women's {team2} {ioi}"] = f"بطولة {nat_f} {team2_lab} للسيدات"
            SP17[f"amateur {team2} {ioi}"] = f"بطولة {nat_f} {team2_lab} للهواة"
            SP17[f"outdoor {team2} {ioi}"] = f"بطولة {nat_f} {team2_lab} في الهواء الطلق"
            SP17[f"{team2} indoor {ioi}"] = f"بطولة {nat_f} {team2_lab} داخل الصالات"

        for yearr in YEARS_LIST:
            kk1 = f"{team2} u{str(yearr)} championships"
            kk2 = f"{team2} u-{yearr} championships"
            SP17[kk1] = f"بطولة {nat_f} {team2_lab} تحت {yearr} سنة"
            SP17[kk2] = f"بطولة {nat_f} {team2_lab} تحت {yearr} سنة"

        SP17[f"{team2} junior championships"] = f"بطولة {nat_f} {team2_lab} للناشئين"
        SP17[f"championships ({team2})"] = f"بطولة {nat_f} {team2_lab}"
        SP17[f"championships {team2}"] = f"بطولة {nat_f} {team2_lab}"
        SP17[f"open ({team2})"] = f"{nat_f} المفتوحة {team2_lab}"
        SP17[f"open {team2}"] = f"{nat_f} المفتوحة {team2_lab}"
        # Middle East Rally Championship بطولة الشرق الأوسط للراليات
        # Category:Polish men's volleyball national team
        SP17[f"{team2} national team"] = f"منتخب {nat_f} {team2_lab}"
        SP17[f"men's {team2} national team"] = f"منتخب {nat_f} {team2_lab} للرجال"
        SP17[f"men's u23 national {team2} team"] = f"منتخب {nat_f} {team2_lab} تحت 23 سنة للرجال"
        """


        new way to make keys 2024


        && indoor & outdoor &&
        """
        SP17[f"women's {team2}"] = f"{team2_lab} {nat_f} نسائية"
        SP17[f"{team2} chairmen and investors"] = f"رؤساء ومسيرو {team2_lab} {nat_f}"
        SP17[f"defunct {team2} cup competitions"] = f"منافسات كؤوس {team2_lab} {nat_f} سابقة"
        SP17[f"{team2} cup competitions"] = f"منافسات كؤوس {team2_lab} {nat_f}"
        SP17[f"domestic {team2} cup"] = f"كؤوس {team2_lab} {nat_f} محلية"
        SP17[f"current {team2} seasons"] = f"مواسم {team2_lab} {nat_f} حالية"

        typies = {
            "cups": "كؤوس",
            "clubs": "أندية",
            "competitions": "منافسات",
            "leagues": "دوريات",
            "coaches": "مدربو",  # Category:Indoor soccer coaches in the United States by club
        }

        for en, ar in typies.items():
            SP17[f"{team2} {en}"] = f"{ar} {team2_lab} {nat_f}"
            SP17[f"professional {team2} {en}"] = f"{ar} {team2_lab} {nat_f} للمحترفين"
            SP17[f"defunct {team2} {en}"] = f"{ar} {team2_lab} {nat_f} سابقة"
            SP17[f"domestic {team2} {en}"] = f"{ar} {team2_lab} محلية {nat_f}"
            SP17[f"domestic women's {team2} {en}"] = f"{ar} {team2_lab} محلية {nat_f} للسيدات"

            SP17[f"domestic {team2} {en}"] = f"{ar} {team2_lab} {nat_f} محلية"
            SP17[f"indoor {team2} {en}"] = f"{ar} {team2_lab} {nat_f} داخل الصالات"
            SP17[f"outdoor {team2} {en}"] = f"{ar} {team2_lab} {nat_f} في الهواء الطلق"
            SP17[f"defunct indoor {team2} {en}"] = f"{ar} {team2_lab} {nat_f} داخل الصالات سابقة"
            SP17[f"defunct outdoor {team2} {en}"] = f"{ar} {team2_lab} {nat_f} في الهواء الطلق سابقة"
        # indoor & outdoor
        SP17[f"domestic {team2}"] = f"{team2_lab} {nat_f} محلية"
        SP17[f"indoor {team2}"] = f"{team2_lab} {nat_f} داخل الصالات"
        SP17[f"outdoor {team2}"] = f"{team2_lab} {nat_f} في الهواء الطلق"
    return SP17


SPORT_FORMATS_FOR_P17 = make_tab() if app_settings.load_p17nat else {}

SPORT_FORMATS_FOR_P17["sports templates"] = "قوالب رياضة {nat}"

__all__ = [
    "SPORT_FORMATS_FOR_P17",
]

len_print.data_len(
    "nat_p17.py",
    {
        "SPORT_FORMATS_FOR_P17": SPORT_FORMATS_FOR_P17,
    },
)
