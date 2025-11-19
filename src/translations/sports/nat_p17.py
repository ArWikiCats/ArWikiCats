#!/usr/bin/python3
"""
!
"""


import sys

from ...config import app_settings
from ...helps import len_print
from .Sport_key import SPORTS_KEYS_FOR_TEAM

NAT_P17_OIOI = {}  # الإنجليزي إسم البلد والعربي جنسية
# ---
YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
SPORT_FORMATS_FOR_P17 = {}
# فرق دول وطنية
# ---


def make_tab() -> dict[str, str]:
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


if app_settings.load_p17nat:
    SPORT_FORMATS_FOR_P17 = make_tab()
SPORT_FORMATS_FOR_P17["sports templates"] = "قوالب رياضة {nat}"
# ---
nat_f = "{nat}"
# ---
for ioi in ["championships", "championship"]:
    NAT_P17_OIOI[f"oioioi {ioi}"] = f"بطولة {nat_f} oioioi"
    NAT_P17_OIOI[f"youth oioioi {ioi}"] = f"بطولة {nat_f} oioioi للشباب"
    NAT_P17_OIOI[f"men's oioioi {ioi}"] = f"بطولة {nat_f} oioioi للرجال"
    NAT_P17_OIOI[f"women's oioioi {ioi}"] = f"بطولة {nat_f} oioioi للسيدات"
    NAT_P17_OIOI[f"amateur oioioi {ioi}"] = f"بطولة {nat_f} oioioi للهواة"
    NAT_P17_OIOI[f"outdoor oioioi {ioi}"] = f"بطولة {nat_f} oioioi في الهواء الطلق"
    NAT_P17_OIOI[f"oioioi indoor {ioi}"] = f"بطولة {nat_f} oioioi داخل الصالات"
# ---
for yearr in YEARS_LIST:
    kk1 = f"oioioi u{str(yearr)} championships"
    kk2 = f"oioioi u-{yearr} championships"
    NAT_P17_OIOI[kk1] = f"بطولة {nat_f} oioioi تحت {yearr} سنة"
    NAT_P17_OIOI[kk2] = f"بطولة {nat_f} oioioi تحت {yearr} سنة"
# ---
NAT_P17_OIOI["oioioi junior championships"] = f"بطولة {nat_f} oioioi للناشئين"
NAT_P17_OIOI["championships (oioioi)"] = f"بطولة {nat_f} oioioi"
NAT_P17_OIOI["championships oioioi"] = f"بطولة {nat_f} oioioi"
NAT_P17_OIOI["open (oioioi)"] = f"{nat_f} المفتوحة oioioi"
NAT_P17_OIOI["open oioioi"] = f"{nat_f} المفتوحة oioioi"
# ---
# Middle East Rally Championship بطولة الشرق الأوسط للراليات
# ---
# Category:Polish men's volleyball national team
NAT_P17_OIOI["oioioi national team"] = f"منتخب {nat_f} oioioi"
NAT_P17_OIOI["men's oioioi national team"] = f"منتخب {nat_f} oioioi للرجال"
NAT_P17_OIOI["men's u23 national oioioi team"] = f"منتخب {nat_f} oioioi تحت 23 سنة للرجال"
# ---
"""


new way to make keys 2024


&& indoor & outdoor &&
"""
# ---
NAT_P17_OIOI["women's oioioi"] = f"oioioi {nat_f} نسائية"
NAT_P17_OIOI["oioioi chairmen and investors"] = f"رؤساء ومسيرو oioioi {nat_f}"
NAT_P17_OIOI["defunct oioioi cup competitions"] = f"منافسات كؤوس oioioi {nat_f} سابقة"
NAT_P17_OIOI["oioioi cup competitions"] = f"منافسات كؤوس oioioi {nat_f}"
NAT_P17_OIOI["domestic oioioi cup"] = f"كؤوس oioioi {nat_f} محلية"
NAT_P17_OIOI["current oioioi seasons"] = f"مواسم oioioi {nat_f} حالية"
# ---

typies = {
    "cups": "كؤوس",
    "clubs": "أندية",
    "competitions": "منافسات",
    "leagues": "دوريات",
    "coaches": "مدربو",  # Category:Indoor soccer coaches in the United States by club
}

for en, ar in typies.items():
    NAT_P17_OIOI[f"oioioi {en}"] = f"{ar} oioioi {nat_f}"
    NAT_P17_OIOI[f"professional oioioi {en}"] = f"{ar} oioioi {nat_f} للمحترفين"
    NAT_P17_OIOI[f"defunct oioioi {en}"] = f"{ar} oioioi {nat_f} سابقة"
    NAT_P17_OIOI[f"domestic oioioi {en}"] = f"{ar} oioioi محلية {nat_f}"
    NAT_P17_OIOI[f"domestic women's oioioi {en}"] = f"{ar} oioioi محلية {nat_f} للسيدات"

    NAT_P17_OIOI[f"domestic oioioi {en}"] = f"{ar} oioioi {nat_f} محلية"
    NAT_P17_OIOI[f"indoor oioioi {en}"] = f"{ar} oioioi {nat_f} داخل الصالات"
    NAT_P17_OIOI[f"outdoor oioioi {en}"] = f"{ar} oioioi {nat_f} في الهواء الطلق"
    NAT_P17_OIOI[f"defunct indoor oioioi {en}"] = f"{ar} oioioi {nat_f} داخل الصالات سابقة"
    NAT_P17_OIOI[f"defunct outdoor oioioi {en}"] = f"{ar} oioioi {nat_f} في الهواء الطلق سابقة"
# ---
# ---
# indoor & outdoor
NAT_P17_OIOI["domestic oioioi"] = f"oioioi {nat_f} محلية"
NAT_P17_OIOI["indoor oioioi"] = f"oioioi {nat_f} داخل الصالات"
NAT_P17_OIOI["outdoor oioioi"] = f"oioioi {nat_f} في الهواء الطلق"
# ---
Lenth1 = {
    "SPORT_FORMATS_FOR_P17": SPORT_FORMATS_FOR_P17,  #
    "NAT_P17_OIOI": NAT_P17_OIOI,  # nat_p17.py: NAT_P17_OIOI: 98
}
# ---
len_print.data_len("sportsb/nat_p17.py", Lenth1)

__all__ = [
    "SPORT_FORMATS_FOR_P17",
    "NAT_P17_OIOI",
]
