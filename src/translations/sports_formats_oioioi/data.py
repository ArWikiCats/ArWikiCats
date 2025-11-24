#!/usr/bin/python3
"""
!
"""

from ...helps import len_print

YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]

nat_f = "{nat}"
# ---
NAT_P17_OIOI = {}  # الإنجليزي إسم البلد والعربي جنسية
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
# indoor & outdoor
NAT_P17_OIOI["domestic oioioi"] = f"oioioi {nat_f} محلية"
NAT_P17_OIOI["indoor oioioi"] = f"oioioi {nat_f} داخل الصالات"
NAT_P17_OIOI["outdoor oioioi"] = f"oioioi {nat_f} في الهواء الطلق"
# ---
len_print.data_len("sportsb/nat_p17.py", {
    "NAT_P17_OIOI": NAT_P17_OIOI,  # nat_p17.py: NAT_P17_OIOI: 98
})

__all__ = [
    "NAT_P17_OIOI",
]
