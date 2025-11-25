#!/usr/bin/python3
"""
!
"""

import re

from ...helps import len_print
from ..sports.sports_lists import AFTER_KEYS_NAT, LEVELS, NEW_TATO_NAT

New_team_xo_labels = {
    "xoxo": "xoxo",
    "xoxo league": "دوري xoxo",
    "xoxo finals": "نهائيات xoxo",
    "xoxo champions": "أبطال xoxo",
    "olympics xoxo": "xoxo في الألعاب الأولمبية",
    "summer olympics xoxo": "xoxo في الألعاب الأولمبية الصيفية",
    "winter olympics xoxo": "xoxo في الألعاب الأولمبية الشتوية",
}
# ---
New_team_xo_jobs = {}
sport_formts_enar_p17_jobs = {}
# ---
YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
# السنة الواحدة تساوي 1343 مدخلة
# ---
team = "xoxo"
job_label = "xoxo"
# ---

New_team_xo_jobs["xoxo olympic gold medalists"] = "ميداليات xoxo ذهبية أولمبية"
New_team_xo_jobs["xoxo olympic silver medalists"] = "ميداليات xoxo فضية أولمبية"
New_team_xo_jobs["xoxo olympic bronze medalists"] = "ميداليات xoxo برونزية أولمبية"
New_team_xo_jobs["national a' xoxo teams"] = "منتخبات xoxo للمحليين"
New_team_xo_jobs["national a. xoxo teams"] = "منتخبات xoxo للمحليين"
New_team_xo_jobs["national b. xoxo teams"] = "منتخبات xoxo رديفة"
New_team_xo_jobs["national b xoxo teams"] = "منتخبات xoxo رديفة"
New_team_xo_jobs["national reserve xoxo teams"] = "منتخبات xoxo وطنية احتياطية"
New_team_xo_jobs["reserve xoxo teams"] = "فرق xoxo احتياطية"
New_team_xo_jobs["defunct xoxo teams"] = "فرق xoxo سابقة"
New_team_xo_jobs["defunct xoxo clubs"] = "أندية xoxo سابقة"
# New_team_xo_jobs[ "xoxo olympic champions"] = "تاريخ مدربو منتخبات xoxo وطنية للسيدات"
sport_formts_enar_p17_jobs["olympics xoxo"] = "xoxo {} في الألعاب الأولمبية"
sport_formts_enar_p17_jobs["summer olympics xoxo"] = "xoxo {} في الألعاب الأولمبية الصيفية"
sport_formts_enar_p17_jobs["winter olympics xoxo"] = "xoxo {} في الألعاب الأولمبية الشتوية"
sport_formts_enar_p17_jobs["xoxo manager history"] = "تاريخ مدربو xoxo {}"
# tab[Category:Women's national football manager history navigational boxes] = "تصنيف:صناديق تصفح تاريخ مدربو منتخبات كرة قدم وطنية للسيدات"
New_team_xo_jobs["national women's xoxo manager history"] = "تاريخ مدربو منتخبات xoxo وطنية للسيدات"
# tab[Category:national football manager history navigational boxes] = "تصنيف:صناديق تصفح تاريخ مدربو منتخبات كرة قدم وطنية"
New_team_xo_jobs["national men's xoxo manager history"] = "تاريخ مدربو منتخبات xoxo وطنية للرجال"
New_team_xo_jobs["national xoxo manager history"] = "تاريخ مدربو منتخبات xoxo وطنية"
for year in YEARS_LIST:
    New_team_xo_jobs[f"under-{year} xoxo"] = f"xoxo تحت {year} سنة"
    # Category:National under-17 football manager history navigational boxes
    New_team_xo_jobs[f"national under-{year} xoxo manager history"] = f"تاريخ مدربو منتخبات xoxo تحت {year} سنة"
    New_team_xo_jobs[f"under-{year} xoxo manager history"] = f"تاريخ مدربو فرق xoxo تحت {year} سنة"
    sport_formts_enar_p17_jobs[f"under-{year} international xoxo managers"] = (
        f"مدربو xoxo تحت {year} سنة دوليون من {{}}"
    )
    sport_formts_enar_p17_jobs[f"under-{year} international xoxo players"] = (
        f"لاعبو xoxo تحت {year} سنة دوليون من {{}}"
    )
sport_formts_enar_p17_jobs["international women's xoxo players"] = "لاعبات xoxo دوليات من {}"
sport_formts_enar_p17_jobs["women's international xoxo players"] = "لاعبات xoxo دوليات من {}"
sport_formts_enar_p17_jobs["international men's xoxo players"] = "لاعبو xoxo دوليون من {}"
sport_formts_enar_p17_jobs["men's international xoxo players"] = "لاعبو xoxo دوليون من {}"
sport_formts_enar_p17_jobs["international xoxo players"] = "لاعبو xoxo دوليون من {}"
New_team_xo_jobs["grand slam (xoxo) tournaments"] = "بطولات xoxo كبرى"
New_team_xo_jobs["grand slam (xoxo) tournament champions"] = "أبطال بطولات xoxo كبرى"

New_team_xo_jobs["grand slam (xoxo)"] = "بطولات xoxo كبرى"
New_team_xo_jobs["multi-national xoxo league"] = "دوريات xoxo متعددة الجنسيات"
New_team_xo_jobs["multi-national xoxo leagues"] = "دوريات xoxo متعددة الجنسيات"
New_team_xo_jobs["national xoxo league"] = "دوريات xoxo وطنية"
New_team_xo_jobs["national xoxo leagues"] = "دوريات xoxo وطنية"
New_team_xo_jobs["xoxo super leagues"] = "دوريات سوبر xoxo"
New_team_xo_jobs["first-class xoxo"] = "xoxo من الدرجة الأولى"
New_team_xo_jobs["first-class xoxo competitions"] = "منافسات xoxo من الدرجة الأولى"
New_team_xo_jobs["first-class xoxo matches"] = "مباريات xoxo من الدرجة الأولى"
New_team_xo_jobs["first-class xoxo records"] = "سجلات xoxo من الدرجة الأولى"
New_team_xo_jobs["first-class xoxo teams"] = "فرق xoxo من الدرجة الأولى"
New_team_xo_jobs["amateur xoxo"] = "xoxo للهواة"
New_team_xo_jobs["fictional xoxo"] = "xoxo خيالية"
New_team_xo_jobs["military xoxo"] = "xoxo عسكرية"
New_team_xo_jobs["college xoxo"] = "xoxo الكليات"
New_team_xo_jobs["military xoxo"] = "xoxo عسكرية"

New_team_xo_jobs["multi-national xoxo championships"] = "بطولات xoxo متعددة الجنسيات"
New_team_xo_jobs["amateur xoxo championships"] = "بطولات xoxo للهواة"
New_team_xo_jobs["international xoxo"] = "xoxo دولية"
New_team_xo_jobs["xoxo league competitions"] = "منافسات دوري xoxo"
New_team_xo_jobs["xoxo league teams"] = "فرق دوري xoxo"
New_team_xo_jobs["International xoxo competition tournaments"] = "بطولات منافسات xoxo دولية"
New_team_xo_jobs["International xoxo competitions"] = "منافسات xoxo دولية"
New_team_xo_jobs["International xoxo races"] = "سباقات xoxo دولية"
New_team_xo_jobs["International xoxo records and statistics"] = "سجلات وإحصائيات xoxo دولية"
New_team_xo_jobs["International xoxo tournaments"] = "بطولات xoxo دولية"
New_team_xo_jobs["international xoxo managers"] = "مدربو xoxo دوليون"
New_team_xo_jobs["international xoxo players"] = "لاعبو xoxo دوليون"
New_team_xo_jobs["international xoxo playerss"] = "لاعبو xoxo دوليون"
New_team_xo_jobs["military xoxo competitions"] = "منافسات xoxo عسكرية"
New_team_xo_jobs["xoxo races"] = "سباقات xoxo"
New_team_xo_jobs["national xoxo champions"] = "أبطال بطولات xoxo وطنية"
New_team_xo_jobs["national xoxo championships"] = "بطولات xoxo وطنية"
New_team_xo_jobs["national xoxo team results"] = "نتائج منتخبات xoxo وطنية"
New_team_xo_jobs["national xoxo teams"] = "منتخبات xoxo وطنية"
New_team_xo_jobs["national junior xoxo teams"] = "منتخبات xoxo وطنية للناشئين"
New_team_xo_jobs["national junior men's xoxo teams"] = "منتخبات xoxo وطنية للناشئين"
New_team_xo_jobs["men's xoxo"] = "xoxo رجالية"
New_team_xo_jobs["women's xoxo"] = "xoxo نسائية"
mens_womens = {
    "men's": "للرجال",
    "women's": "للسيدات",
    "men's youth": "للشباب",
    "women's youth": "للشابات",
    "youth": "للشباب",
}
New_team_xo_jobs["international men's xoxo competitions"] = "منافسات xoxo رجالية دولية"
New_team_xo_jobs["international men's xoxo players"] = "لاعبو xoxo دوليون"
New_team_xo_jobs["international men's xoxo playerss"] = "لاعبو xoxo دوليون"
New_team_xo_jobs["international men's xoxo"] = "xoxo دولية للرجال"
# --
New_team_xo_jobs["international women's xoxo competitions"] = "منافسات xoxo نسائية دولية"
New_team_xo_jobs["international women's xoxo players"] = "لاعبات xoxo دوليات"
New_team_xo_jobs["international women's xoxo playerss"] = "لاعبات xoxo دوليات"
New_team_xo_jobs["international women's xoxo"] = "xoxo دولية للسيدات"
New_team_xo_jobs["national women's xoxo teams"] = "منتخبات xoxo وطنية نسائية"
New_team_xo_jobs["women's international xoxo players"] = "لاعبات xoxo دوليات"
New_team_xo_jobs["women's international xoxo playerss"] = "لاعبات xoxo دوليات"
New_team_xo_jobs["women's international xoxo"] = "xoxo دولية للسيدات"
New_team_xo_jobs["women's xoxo teams"] = "فرق xoxo نسائية"
New_team_xo_jobs["international youth xoxo competitions"] = "منافسات xoxo شبابية دولية"
New_team_xo_jobs["national youth xoxo teams"] = "منتخبات xoxo وطنية شبابية"
New_team_xo_jobs["youth international xoxo"] = "xoxo دولية شبابية"
New_team_xo_jobs["youth xoxo competitions"] = "منافسات xoxo شبابية"
New_team_xo_jobs["youth xoxo"] = "xoxo شبابية"
New_team_xo_jobs["men's international xoxo players"] = "لاعبو xoxo دوليون"
New_team_xo_jobs["men's international xoxo playerss"] = "لاعبو xoxo دوليون"
New_team_xo_jobs["men's international xoxo"] = "xoxo دولية للرجال"
New_team_xo_jobs["men's xoxo teams"] = "فرق xoxo رجالية"
New_team_xo_jobs["national men's xoxo teams"] = "منتخبات xoxo وطنية رجالية"
for ty_nat, tas in NEW_TATO_NAT.items():
    tas = tas.strip()
    Ar_labs_3 = f"منتخبات xoxo وطنية {tas.format(nat='').strip()}"
    Ar_labs_league = f"دوريات xoxo وطنية {tas.format(nat='').strip()}"
    if "national" not in ty_nat:
        Ar_labs_3 = f"فرق xoxo {tas.format(nat='').strip()}"
        Ar_labs_league = f"دوريات xoxo {tas.format(nat='').strip()}"
    elif "multi-national" in ty_nat:
        Ar_labs_3 = Ar_labs_3.replace(" وطنية", "")
        Ar_labs_league = Ar_labs_league.replace(" وطنية", "")
    # Ar_labs = K_at_p.format(nat = "{nat}" , d = job_label)
    for pr_e, pr_e_Lab in AFTER_KEYS_NAT.items():
        if (pr_e == "players" or pr_e == "playerss") and "women's" in ty_nat:
            pr_e_Lab = "لاعبات {lab}"
        elif "لاعبو" in pr_e_Lab and "women's" in ty_nat:
            pr_e_Lab = re.sub(r"لاعبو ", "لاعبات ", pr_e_Lab)
        New_team_xo_jobs[f"{ty_nat} xoxo teams {pr_e}".strip()] = pr_e_Lab.format(lab=Ar_labs_3)
        New_team_xo_jobs[f"{ty_nat} xoxo leagues {pr_e}".strip()] = pr_e_Lab.format(lab=Ar_labs_league)
        if "national" not in ty_nat:
            New_team_xo_jobs[f"{ty_nat.strip()} xoxo teams"] = "فرق xoxo " + tas.format(nat="").strip()
for level, lvl_lab in LEVELS.items():
    New_team_xo_jobs[f"national xoxo {level} league"] = f"دوريات xoxo وطنية من {lvl_lab}"
    New_team_xo_jobs[f"national xoxo {level} leagues"] = f"دوريات xoxo وطنية من {lvl_lab}"

    New_team_xo_jobs[f"defunct xoxo {level} leagues"] = f"دوريات xoxo سابقة من {lvl_lab}"
    New_team_xo_jobs[f"defunct xoxo {level} league"] = f"دوريات xoxo سابقة من {lvl_lab}"

    New_team_xo_jobs[f"{level} xoxo league"] = f"دوريات xoxo من {lvl_lab}"
    New_team_xo_jobs[f"{level} xoxo leagues"] = f"دوريات xoxo من {lvl_lab}"

    New_team_xo_jobs[f"xoxo {level} league"] = f"دوريات xoxo من {lvl_lab}"
    New_team_xo_jobs[f"xoxo {level} leagues"] = f"دوريات xoxo من {lvl_lab}"
"""


new way to make keys 2024


&& indoor & outdoor &&
"""
# ---
New_team_xo_jobs["women's xoxo"] = "xoxo نسائية"
New_team_xo_jobs["xoxo chairmen and investors"] = "رؤساء ومسيرو xoxo"
New_team_xo_jobs["defunct xoxo cup competitions"] = "منافسات كؤوس xoxo سابقة"
New_team_xo_jobs["xoxo cup competitions"] = "منافسات كؤوس xoxo"
New_team_xo_jobs["domestic xoxo cup"] = "كؤوس xoxo محلية"
New_team_xo_jobs["current xoxo seasons"] = "مواسم xoxo حالية"

typies = {
    "cups": "كؤوس",
    "clubs": "أندية",
    "competitions": "منافسات",
    "leagues": "دوريات",
    "coaches": "مدربو",  # Category:Indoor soccer coaches in the United States by club
}

for en, ar in typies.items():
    New_team_xo_jobs[f"xoxo {en}"] = f"{ar} xoxo"
    New_team_xo_jobs[f"professional xoxo {en}"] = f"{ar} xoxo للمحترفين"
    New_team_xo_jobs[f"defunct xoxo {en}"] = f"{ar} xoxo سابقة"
    New_team_xo_jobs[f"domestic xoxo {en}"] = f"{ar} xoxo محلية"
    New_team_xo_jobs[f"domestic women's xoxo {en}"] = f"{ar} xoxo محلية للسيدات"

    New_team_xo_jobs[f"domestic xoxo {en}"] = f"{ar} xoxo محلية"
    New_team_xo_jobs[f"indoor xoxo {en}"] = f"{ar} xoxo داخل الصالات"
    New_team_xo_jobs[f"outdoor xoxo {en}"] = f"{ar} xoxo في الهواء الطلق"
    New_team_xo_jobs[f"defunct indoor xoxo {en}"] = f"{ar} xoxo داخل الصالات سابقة"
    New_team_xo_jobs[f"defunct outdoor xoxo {en}"] = f"{ar} xoxo في الهواء الطلق سابقة"
# indoor & outdoor
# tab[Category:domestic Soccer] = "تصنيف:كرة قدم محلية"
New_team_xo_jobs["domestic xoxo"] = "xoxo محلية"
New_team_xo_jobs["indoor xoxo"] = "xoxo داخل الصالات"
New_team_xo_jobs["outdoor xoxo"] = "xoxo في الهواء الطلق"
# sport_formts_enar_p17_jobs["international rally"] =  "رالي {} الدولي"
# ---
len_print.data_len(
    "sports_formats_teams/team_job.py",
    {
        "sport_formts_enar_p17_jobs": sport_formts_enar_p17_jobs,
        "New_team_xo_labels": New_team_xo_labels,
        "New_team_xo_jobs": New_team_xo_jobs,
    },
)
