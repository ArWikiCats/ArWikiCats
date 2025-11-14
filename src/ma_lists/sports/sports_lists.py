#!/usr/bin/python3
"""
!
"""

# ---
YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
# ---
menstt333 = {
    "": "{}",
    "national": "{}",
    # "youth national" : "{} للشباب",
    "national youth": "{} للشباب",
    # "amateur national" : "{} للهواة",
    "national amateur": "{} للهواة",
    "national junior men's": "{} للناشئين",
    # "national men's junior" : "{} للناشئين",
    # "men's junior national" : "{} للناشئين",
    # "men's national junior" : "{} للناشئين",
    "national junior women's": "{} للناشئات",
    # "national women's junior" : "{} للناشئات",
    # "women's junior national" : "{} للناشئات",
    # "women's national junior" : "{} للناشئات",
    "national men's": "{} للرجال",
    # "men's national" : "{} للرجال",
    "national women's": "{} للسيدات",
    "multi-national women's": "{} متعددة الجنسيات للسيدات",
    # "women's national" : "{} للسيدات",
    # "national women's youth" : "{} للشابات",
    # "women's youth national" : "{} للشابات",
    # "women's national youth" : "{} للشابات",
    "national youth women's": "{} للشابات",
}
NAT_MENSTT33 = {fafo: menstt333[fafo].replace("{}", "{nat}") for fafo in menstt333}
# ---
# =================
# ---
NEW_TATO_NAT = {}
# ---
# Category:National junior women's goalball teams
# tab[Category:Women's national under-20 association football teams] = "تصنيف:منتخبات كرة قدم وطنية نسائية تحت 20 سنة"
# ---
for template_key, template_label in NAT_MENSTT33.items():
    NEW_TATO_NAT[template_key] = template_label
    # printe.output(lightred % (mr_nat , mr_nat_a) )
    for year in YEARS_LIST:
        # for ye# ---a in [23]:
        # ---
        # Category:Women's national under-20 association football teams
        # تصنيف:منتخبات كرة قدم وطنية تحت 20 سنة للسيدات
        # ---
        arabic_label = template_label.replace("{nat}", "{nat} تحت %d سنة" % year)
        english_key = f"{template_key} under-{year}"
        # printe.output(english_key)
        # printe.output(arabic_label)
        NEW_TATO_NAT[english_key] = arabic_label
# ---
# =================
# ---
levels = {
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
# ---
AFTER_KEYS = {
    "squads": "تشكيلات",
    "finals": "نهائيات",
    "positions": "مراكز",
    "tournaments": "بطولات",
    "films": "أفلام",
    "teams": "فرق",
    "venues": "ملاعب",
    "clubs": "أندية",
    "organizations": "منظمات",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "organisations": "منظمات",
    "events": "أحداث",
    "umpires": "حكام",
    "trainers": "مدربو",
    "scouts": "كشافة",
    # "people" : "أعلام",
    "coaches": "مدربو",
    "leagues": "دوريات",
    "managers": "مدربو",
    # "managers" : "مدراء",
    # "captains" : "مدربو",
    "playerss": "لاعبو",
    "players": "لاعبو",
    "results": "نتائج",
    "matches": "مباريات",
    "navigational boxes": "صناديق تصفح",
    "lists": "قوائم",
    "home stadiums": "ملاعب",
    "templates": "قوالب",
    "rivalries": "دربيات",
    "champions": "أبطال",
    "competitions": "منافسات",
    "statistics": "إحصائيات",
    "records": "سجلات",
    "records and statistics": "سجلات وإحصائيات",
    "manager history": "تاريخ مدربو",
}
# ---
AFTER_KEYS_TEAM = {
    "team": "{}",
    "team umpires": "حكام {}",
    "team trainers": "مدربو {}",
    "team scouts": "كشافة {}",
}
# ---
AFTER_KEYS_NAT = {
    "": "{lab}",
    "second level leagues": "دوريات {lab} من الدرجة الثانية",
    "second tier leagues": "دوريات {lab} من الدرجة الثانية",
}
# ---
# نسخ AFTER_KEYS إلى AFTER_KEYS_TEAM وإلى AFTER_KEYS
for suffix_key, suffix_label in AFTER_KEYS.items():
    # ---
    AFTER_KEYS_TEAM[f"team {suffix_key}"] = suffix_label + " {}"
    # ---
    AFTER_KEYS_NAT[f"{suffix_key}"] = suffix_label + " {lab}"
# ---
for level_key, level_label in levels.items():
    AFTER_KEYS_NAT[f"{level_key} league"] = "دوريات {lab} من %s" % level_label
    AFTER_KEYS_NAT[f"{level_key} leagues"] = "دوريات {lab} من %s" % level_label
# ---
