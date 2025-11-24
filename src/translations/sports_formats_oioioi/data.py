#!/usr/bin/python3
"""
!
"""

from ...helps import len_print

YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]

nat_f = "{nat}"
# ---
NAT_P17_DATA = {}  # الإنجليزي إسم البلد والعربي جنسية
# ---
for ioi in ["championships", "championship"]:
    NAT_P17_DATA[f"oioioi {ioi}"] = f"بطولة {nat_f} ixix"
    NAT_P17_DATA[f"youth oioioi {ioi}"] = f"بطولة {nat_f} ixix للشباب"
    NAT_P17_DATA[f"men's oioioi {ioi}"] = f"بطولة {nat_f} ixix للرجال"
    NAT_P17_DATA[f"women's oioioi {ioi}"] = f"بطولة {nat_f} ixix للسيدات"
    NAT_P17_DATA[f"amateur oioioi {ioi}"] = f"بطولة {nat_f} ixix للهواة"
    NAT_P17_DATA[f"outdoor oioioi {ioi}"] = f"بطولة {nat_f} ixix في الهواء الطلق"
    NAT_P17_DATA[f"oioioi indoor {ioi}"] = f"بطولة {nat_f} ixix داخل الصالات"
# ---
for yearr in YEARS_LIST:
    kk1 = f"oioioi u{str(yearr)} championships"
    kk2 = f"oioioi u-{yearr} championships"
    NAT_P17_DATA[kk1] = f"بطولة {nat_f} ixix تحت {yearr} سنة"
    NAT_P17_DATA[kk2] = f"بطولة {nat_f} ixix تحت {yearr} سنة"
# ---
NAT_P17_DATA["oioioi junior championships"] = f"بطولة {nat_f} ixix للناشئين"
NAT_P17_DATA["championships (oioioi)"] = f"بطولة {nat_f} ixix"
NAT_P17_DATA["championships oioioi"] = f"بطولة {nat_f} ixix"
NAT_P17_DATA["open (oioioi)"] = f"{nat_f} المفتوحة ixix"
NAT_P17_DATA["open oioioi"] = f"{nat_f} المفتوحة ixix"
# ---
# Middle East Rally Championship بطولة الشرق الأوسط للراليات
# ---
# Category:Polish men's volleyball national team
NAT_P17_DATA["oioioi national team"] = f"منتخب {nat_f} ixix"
NAT_P17_DATA["men's oioioi national team"] = f"منتخب {nat_f} ixix للرجال"
NAT_P17_DATA["men's u23 national oioioi team"] = f"منتخب {nat_f} ixix تحت 23 سنة للرجال"
# ---
NAT_P17_DATA["women's oioioi"] = f"ixix {nat_f} نسائية"
NAT_P17_DATA["oioioi chairmen and investors"] = f"رؤساء ومسيرو ixix {nat_f}"
NAT_P17_DATA["defunct oioioi cup competitions"] = f"منافسات كؤوس ixix {nat_f} سابقة"
NAT_P17_DATA["oioioi cup competitions"] = f"منافسات كؤوس ixix {nat_f}"
NAT_P17_DATA["domestic oioioi cup"] = f"كؤوس ixix {nat_f} محلية"
NAT_P17_DATA["current oioioi seasons"] = f"مواسم ixix {nat_f} حالية"
# ---

typies = {
    "cups": "كؤوس",
    "clubs": "أندية",
    "competitions": "منافسات",
    "leagues": "دوريات",
    "coaches": "مدربو",  # Category:Indoor soccer coaches in the United States by club
}

for en, ar in typies.items():
    NAT_P17_DATA[f"oioioi {en}"] = f"{ar} ixix {nat_f}"
    NAT_P17_DATA[f"professional oioioi {en}"] = f"{ar} ixix {nat_f} للمحترفين"
    NAT_P17_DATA[f"defunct oioioi {en}"] = f"{ar} ixix {nat_f} سابقة"
    NAT_P17_DATA[f"domestic oioioi {en}"] = f"{ar} ixix محلية {nat_f}"
    NAT_P17_DATA[f"domestic women's oioioi {en}"] = f"{ar} ixix محلية {nat_f} للسيدات"

    NAT_P17_DATA[f"domestic oioioi {en}"] = f"{ar} ixix {nat_f} محلية"
    NAT_P17_DATA[f"indoor oioioi {en}"] = f"{ar} ixix {nat_f} داخل الصالات"
    NAT_P17_DATA[f"outdoor oioioi {en}"] = f"{ar} ixix {nat_f} في الهواء الطلق"
    NAT_P17_DATA[f"defunct indoor oioioi {en}"] = f"{ar} ixix {nat_f} داخل الصالات سابقة"
    NAT_P17_DATA[f"defunct outdoor oioioi {en}"] = f"{ar} ixix {nat_f} في الهواء الطلق سابقة"
# ---
# indoor & outdoor
NAT_P17_DATA["domestic oioioi"] = f"ixix {nat_f} محلية"
NAT_P17_DATA["indoor oioioi"] = f"ixix {nat_f} داخل الصالات"
NAT_P17_DATA["outdoor oioioi"] = f"ixix {nat_f} في الهواء الطلق"
# ---
NAT_P17_OIOI = {f"{{nat}} {x}": v for x, v in NAT_P17_DATA.items()}
# ---
len_print.data_len("sportsb/nat_p17.py", {
    "NAT_P17_OIOI": NAT_P17_OIOI,  # nat_p17.py: NAT_P17_OIOI: 98
})

__all__ = [
    "NAT_P17_OIOI",
]
