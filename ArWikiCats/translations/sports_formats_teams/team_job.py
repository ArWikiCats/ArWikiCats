#!/usr/bin/python3
"""
NOTE: this is has alot of common code with ArWikiCats/translations/sports_formats_national/sport_lab_nat.py
"""

import re

from ...helps import len_print

# ---
# New_team_xo_jobs[ "xoxo olympic champions"] = "تاريخ مدربو منتخبات xoxo وطنية للسيدات"
# tab[Category:Women's national football manager history navigational boxes] = "تصنيف:صناديق تصفح تاريخ مدربو منتخبات كرة قدم وطنية للسيدات"
# tab[Category:national football manager history navigational boxes] = "تصنيف:صناديق تصفح تاريخ مدربو منتخبات كرة قدم وطنية"
# ---
New_team_xo_jobs = {
    "amateur xoxo championships": "بطولات xoxo للهواة",
    "amateur xoxo": "xoxo للهواة",
    "college xoxo": "xoxo الكليات",
    "defunct xoxo clubs": "أندية xoxo سابقة",
    "defunct xoxo teams": "فرق xoxo سابقة",
    "fictional xoxo": "xoxo خيالية",
    "first-class xoxo competitions": "منافسات xoxo من الدرجة الأولى",
    "first-class xoxo matches": "مباريات xoxo من الدرجة الأولى",
    "first-class xoxo records": "سجلات xoxo من الدرجة الأولى",
    "first-class xoxo teams": "فرق xoxo من الدرجة الأولى",
    "first-class xoxo": "xoxo من الدرجة الأولى",
    "grand slam (xoxo) tournament champions": "أبطال بطولات xoxo كبرى",
    "grand slam (xoxo) tournaments": "بطولات xoxo كبرى",
    "grand slam (xoxo)": "بطولات xoxo كبرى",
    "international men's xoxo competitions": "منافسات xoxo رجالية دولية",
    "international men's xoxo players": "لاعبو xoxo دوليون",
    "international men's xoxo playerss": "لاعبو xoxo دوليون",
    "international men's xoxo": "xoxo دولية للرجال",
    "international women's xoxo competitions": "منافسات xoxo نسائية دولية",
    "international women's xoxo players": "لاعبات xoxo دوليات",
    "international women's xoxo playerss": "لاعبات xoxo دوليات",
    "international women's xoxo": "xoxo دولية للسيدات",
    "International xoxo competition tournaments": "بطولات منافسات xoxo دولية",
    "International xoxo competitions": "منافسات xoxo دولية",
    "international xoxo managers": "مدربو xoxo دوليون",
    "international xoxo players": "لاعبو xoxo دوليون",
    "international xoxo playerss": "لاعبو xoxo دوليون",
    "International xoxo races": "سباقات xoxo دولية",
    "International xoxo records and statistics": "سجلات وإحصائيات xoxo دولية",
    "International xoxo tournaments": "بطولات xoxo دولية",
    "international xoxo": "xoxo دولية",
    "international youth xoxo competitions": "منافسات xoxo شبابية دولية",
    "men's international xoxo players": "لاعبو xoxo دوليون",
    "men's international xoxo playerss": "لاعبو xoxo دوليون",
    "men's international xoxo": "xoxo دولية للرجال",
    "men's xoxo teams": "فرق xoxo رجالية",
    "men's xoxo": "xoxo رجالية",
    "military xoxo competitions": "منافسات xoxo عسكرية",
    "military xoxo": "xoxo عسكرية",
    "multi-national xoxo championships": "بطولات xoxo متعددة الجنسيات",
    "multi-national xoxo league": "دوريات xoxo متعددة الجنسيات",
    "multi-national xoxo leagues": "دوريات xoxo متعددة الجنسيات",
    "national a' xoxo teams": "منتخبات xoxo للمحليين",
    "national a. xoxo teams": "منتخبات xoxo للمحليين",
    "national b xoxo teams": "منتخبات xoxo رديفة",
    "national b. xoxo teams": "منتخبات xoxo رديفة",
    "national junior men's xoxo teams": "منتخبات xoxo وطنية للناشئين",
    "national junior xoxo teams": "منتخبات xoxo وطنية للناشئين",
    "national men's xoxo manager history": "تاريخ مدربو منتخبات xoxo وطنية للرجال",
    "national men's xoxo teams": "منتخبات xoxo وطنية رجالية",
    "national reserve xoxo teams": "منتخبات xoxo وطنية احتياطية",
    "national women's xoxo manager history": "تاريخ مدربو منتخبات xoxo وطنية للسيدات",
    "national women's xoxo teams": "منتخبات xoxo وطنية نسائية",
    "national xoxo champions": "أبطال بطولات xoxo وطنية",
    "national xoxo championships": "بطولات xoxo وطنية",
    "national xoxo league": "دوريات xoxo وطنية",
    "national xoxo leagues": "دوريات xoxo وطنية",
    "national xoxo manager history": "تاريخ مدربو منتخبات xoxo وطنية",
    "national xoxo team results": "نتائج منتخبات xoxo وطنية",
    "national xoxo teams": "منتخبات xoxo وطنية",
    "national youth xoxo teams": "منتخبات xoxo وطنية شبابية",
    "reserve xoxo teams": "فرق xoxo احتياطية",
    "women's international xoxo players": "لاعبات xoxo دوليات",
    "women's international xoxo playerss": "لاعبات xoxo دوليات",
    "women's international xoxo": "xoxo دولية للسيدات",
    "women's xoxo teams": "فرق xoxo نسائية",
    "xoxo league competitions": "منافسات دوري xoxo",
    "xoxo league teams": "فرق دوري xoxo",
    "xoxo olympic bronze medalists": "ميداليات xoxo برونزية أولمبية",
    "xoxo olympic gold medalists": "ميداليات xoxo ذهبية أولمبية",
    "xoxo olympic silver medalists": "ميداليات xoxo فضية أولمبية",
    "xoxo races": "سباقات xoxo",
    "xoxo super leagues": "دوريات سوبر xoxo",
    "youth international xoxo": "xoxo دولية شبابية",
    "youth xoxo competitions": "منافسات xoxo شبابية",
    "youth xoxo": "xoxo شبابية",
}
YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]

for year in YEARS_LIST:
    New_team_xo_jobs[f"under-{year} xoxo"] = f"xoxo تحت {year} سنة"
    # Category:National under-17 football manager history navigational boxes
    New_team_xo_jobs[f"national under-{year} xoxo manager history"] = f"تاريخ مدربو منتخبات xoxo تحت {year} سنة"
    New_team_xo_jobs[f"under-{year} xoxo manager history"] = f"تاريخ مدربو فرق xoxo تحت {year} سنة"

# (fifth|first|fourth|second|seventh|sixth|third|top)[ -](level|tier)
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
"""
Category:National association football second-tier league champions
Category:Association football third-tier league seasons
Category:Association football second-tier league seasons
Category:Association football fourth-tier league seasons
Category:National association football third-tier leagues
Category:National association football fifth-tier leagues
Category:National association football fourth-tier leagues
Category:National association football second-tier leagues
Category:National association football seventh-tier leagues
Category:National association football sixth-tier leagues
Category:Seasons in European third-tier association football leagues
"""
for level, lvl_lab in LEVELS.items():
    New_team_xo_jobs[f"{level} xoxo league"] = f"دوريات xoxo من {lvl_lab}"
    New_team_xo_jobs[f"{level} xoxo leagues"] = f"دوريات xoxo من {lvl_lab}"

New_team_xo_jobs["women's xoxo"] = "xoxo نسائية"
New_team_xo_jobs["xoxo chairmen and investors"] = "رؤساء ومسيرو xoxo"
New_team_xo_jobs["defunct xoxo cup competitions"] = "منافسات كؤوس xoxo سابقة"
New_team_xo_jobs["xoxo cup competitions"] = "منافسات كؤوس xoxo"
New_team_xo_jobs["domestic xoxo cup"] = "كؤوس xoxo محلية"
New_team_xo_jobs["current xoxo seasons"] = "مواسم xoxo حالية"
New_team_xo_jobs["domestic xoxo"] = "xoxo محلية"
New_team_xo_jobs["indoor xoxo"] = "xoxo داخل الصالات"
New_team_xo_jobs["outdoor xoxo"] = "xoxo في الهواء الطلق"

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

len_print.data_len(
    "sports_formats_teams/team_job.py",
    {
        "New_team_xo_jobs": New_team_xo_jobs,
    },
)


__all__ = [
    "New_team_xo_jobs",
]
