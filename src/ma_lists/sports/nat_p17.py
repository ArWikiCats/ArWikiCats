#!/usr/bin/python3
"""
from .nat_p17 import sport_formts_for_p17, nat_p17_oioi
"""


import sys

# ---
from ...helps import len_print
from .Sport_key import Sports_Keys_For_Team
from ... import app_settings
nat_p17_oioi = {}  # الإنجليزي إسم البلد والعربي جنسية
# ---
Years_List = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
sport_formts_for_p17 = {}


# ---
# فرق دول وطنية
# ---
def make_tab() -> dict[str, str]:
    SP17 = {}
    for team2, team2_lab in Sports_Keys_For_Team.items():
        # ---
        nat_f = "{nat}"
        # ---
        for ioi in ["championships", "championship"]:
            SP17[f"{team2} {ioi}"] = f"بطولة {nat_f} {team2_lab}"
            SP17[f"youth {team2} {ioi}"] = f"بطولة {nat_f} {team2_lab} للشباب"
            SP17[f"men's {team2} {ioi}"] = f"بطولة {nat_f} {team2_lab} للرجال"
            SP17[f"women's {team2} {ioi}"] = f"بطولة {nat_f} {team2_lab} للسيدات"
            SP17[f"amateur {team2} {ioi}"] = f"بطولة {nat_f} {team2_lab} للهواة"
            SP17[f"outdoor {team2} {ioi}"] = f"بطولة {nat_f} {team2_lab} في الهواء الطلق"
            SP17[f"{team2} indoor {ioi}"] = f"بطولة {nat_f} {team2_lab} داخل الصالات"
        # ---
        for yearr in Years_List:
            kk1 = f"{team2} u{str(yearr)} championships"
            kk2 = f"{team2} u-{yearr} championships"
            SP17[kk1] = f"بطولة {nat_f} {team2_lab} تحت {yearr} سنة"
            SP17[kk2] = f"بطولة {nat_f} {team2_lab} تحت {yearr} سنة"
        # ---
        SP17[f"{team2} junior championships"] = f"بطولة {nat_f} {team2_lab} للناشئين"
        SP17[f"championships ({team2})"] = f"بطولة {nat_f} {team2_lab}"
        SP17[f"championships {team2}"] = f"بطولة {nat_f} {team2_lab}"
        SP17[f"open ({team2})"] = f"{nat_f} المفتوحة {team2_lab}"
        SP17[f"open {team2}"] = f"{nat_f} المفتوحة {team2_lab}"
        # ---
        # Middle East Rally Championship بطولة الشرق الأوسط للراليات
        # ---
        # Category:Polish men's volleyball national team
        SP17[f"{team2} national team"] = f"منتخب {nat_f} {team2_lab}"
        SP17[f"men's {team2} national team"] = f"منتخب {nat_f} {team2_lab} للرجال"
        SP17[f"men's u23 national {team2} team"] = f"منتخب {nat_f} {team2_lab} تحت 23 سنة للرجال"
        # ---
        """


        new way to make keys 2024


        && indoor & outdoor &&
        """
        # ---
        SP17[f"women's {team2}"] = f"{team2_lab} {nat_f} نسائية"
        SP17[f"{team2} chairmen and investors"] = f"رؤساء ومسيرو {team2_lab} {nat_f}"
        SP17[f"defunct {team2} cup competitions"] = f"منافسات كؤوس {team2_lab} {nat_f} سابقة"
        SP17[f"{team2} cup competitions"] = f"منافسات كؤوس {team2_lab} {nat_f}"

        # ---
        SP17[f"domestic {team2} cup"] = f"كؤوس {team2_lab} {nat_f} محلية"
        SP17[f"current {team2} seasons"] = f"مواسم {team2_lab} {nat_f} حالية"
        # ---

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
        # ---
        # ---
        # indoor & outdoor
        SP17[f"domestic {team2}"] = f"{team2_lab} {nat_f} محلية"
        SP17[f"indoor {team2}"] = f"{team2_lab} {nat_f} داخل الصالات"
        SP17[f"outdoor {team2}"] = f"{team2_lab} {nat_f} في الهواء الطلق"
    # ---
    return SP17


if app_settings.load_p17nat:
    sport_formts_for_p17 = make_tab()

# ---
sport_formts_for_p17["sports templates"] = "قوالب رياضة {nat}"
# ---
nat_f = "{nat}"
# ---
for ioi in ["championships", "championship"]:
    nat_p17_oioi[f"oioioi {ioi}"] = f"بطولة {nat_f} oioioi"
    nat_p17_oioi[f"youth oioioi {ioi}"] = f"بطولة {nat_f} oioioi للشباب"
    nat_p17_oioi[f"men's oioioi {ioi}"] = f"بطولة {nat_f} oioioi للرجال"
    nat_p17_oioi[f"women's oioioi {ioi}"] = f"بطولة {nat_f} oioioi للسيدات"
    nat_p17_oioi[f"amateur oioioi {ioi}"] = f"بطولة {nat_f} oioioi للهواة"
    nat_p17_oioi[f"outdoor oioioi {ioi}"] = f"بطولة {nat_f} oioioi في الهواء الطلق"
    nat_p17_oioi[f"oioioi indoor {ioi}"] = f"بطولة {nat_f} oioioi داخل الصالات"
# ---
for yearr in Years_List:
    kk1 = f"oioioi u{str(yearr)} championships"
    kk2 = f"oioioi u-{yearr} championships"
    nat_p17_oioi[kk1] = f"بطولة {nat_f} oioioi تحت {yearr} سنة"
    nat_p17_oioi[kk2] = f"بطولة {nat_f} oioioi تحت {yearr} سنة"
# ---
nat_p17_oioi["oioioi junior championships"] = f"بطولة {nat_f} oioioi للناشئين"
nat_p17_oioi["championships (oioioi)"] = f"بطولة {nat_f} oioioi"
nat_p17_oioi["championships oioioi"] = f"بطولة {nat_f} oioioi"
nat_p17_oioi["open (oioioi)"] = f"{nat_f} المفتوحة oioioi"
nat_p17_oioi["open oioioi"] = f"{nat_f} المفتوحة oioioi"
# ---
# Middle East Rally Championship بطولة الشرق الأوسط للراليات
# ---
# Category:Polish men's volleyball national team
nat_p17_oioi["oioioi national team"] = f"منتخب {nat_f} oioioi"
nat_p17_oioi["men's oioioi national team"] = f"منتخب {nat_f} oioioi للرجال"
nat_p17_oioi["men's u23 national oioioi team"] = f"منتخب {nat_f} oioioi تحت 23 سنة للرجال"
# ---
"""


new way to make keys 2024


&& indoor & outdoor &&
"""
# ---
nat_p17_oioi["women's oioioi"] = f"oioioi {nat_f} نسائية"
nat_p17_oioi["oioioi chairmen and investors"] = f"رؤساء ومسيرو oioioi {nat_f}"
nat_p17_oioi["defunct oioioi cup competitions"] = f"منافسات كؤوس oioioi {nat_f} سابقة"
nat_p17_oioi["oioioi cup competitions"] = f"منافسات كؤوس oioioi {nat_f}"

# ---
nat_p17_oioi["domestic oioioi cup"] = f"كؤوس oioioi {nat_f} محلية"
nat_p17_oioi["current oioioi seasons"] = f"مواسم oioioi {nat_f} حالية"
# ---

typies = {
    "cups": "كؤوس",
    "clubs": "أندية",
    "competitions": "منافسات",
    "leagues": "دوريات",
    "coaches": "مدربو",  # Category:Indoor soccer coaches in the United States by club
}

for en, ar in typies.items():
    nat_p17_oioi[f"oioioi {en}"] = f"{ar} oioioi {nat_f}"
    nat_p17_oioi[f"professional oioioi {en}"] = f"{ar} oioioi {nat_f} للمحترفين"
    nat_p17_oioi[f"defunct oioioi {en}"] = f"{ar} oioioi {nat_f} سابقة"
    nat_p17_oioi[f"domestic oioioi {en}"] = f"{ar} oioioi محلية {nat_f}"
    nat_p17_oioi[f"domestic women's oioioi {en}"] = f"{ar} oioioi محلية {nat_f} للسيدات"

    nat_p17_oioi[f"domestic oioioi {en}"] = f"{ar} oioioi {nat_f} محلية"
    nat_p17_oioi[f"indoor oioioi {en}"] = f"{ar} oioioi {nat_f} داخل الصالات"
    nat_p17_oioi[f"outdoor oioioi {en}"] = f"{ar} oioioi {nat_f} في الهواء الطلق"
    nat_p17_oioi[f"defunct indoor oioioi {en}"] = f"{ar} oioioi {nat_f} داخل الصالات سابقة"
    nat_p17_oioi[f"defunct outdoor oioioi {en}"] = f"{ar} oioioi {nat_f} في الهواء الطلق سابقة"
# ---
# ---
# indoor & outdoor
nat_p17_oioi["domestic oioioi"] = f"oioioi {nat_f} محلية"
nat_p17_oioi["indoor oioioi"] = f"oioioi {nat_f} داخل الصالات"
nat_p17_oioi["outdoor oioioi"] = f"oioioi {nat_f} في الهواء الطلق"
# ---
Lenth1 = {
    "sport_formts_for_p17": sport_formts_for_p17,  #
    "nat_p17_oioi": nat_p17_oioi,  # nat_p17.py: nat_p17_oioi: 98
}
# ---
len_print.data_len("sportsb/nat_p17.py", Lenth1)

__all__ = [
    "sport_formts_for_p17",
    "nat_p17_oioi",
]
