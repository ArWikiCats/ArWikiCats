#!/usr/bin/python3
"""
python3 core8/pwb.py -m cProfile -s ncalls make/make2_bots.matables_bots/bot.py

"""
import copy
from typing import Callable, Optional
from ..lazy_data_bots.bot_2018 import pop_All_2018
from ...helps import len_print
from ...ma_lists import (
    military_format_women,
    military_format_men,
    olympics,
    languages_pop,
    Films_TT,
    typeTable_4,
    typeTable_7,
    ALBUMS_TYPE,
    FILM_PRODUCTION_COMPANY,
    Jobs_new,
    jobs_mens_data,
    SPORTS_KEYS_FOR_LABEL,
    By_table,
    ADD_IN_TABLE2,
    People_key,
    all_country_with_nat,
)

from ..format_bots import Tit_ose_Nmaes

# ---
MONTH_table = {
    "january": "يناير",
    "february": "فبراير",
    "march": "مارس",
    "april": "أبريل",
    "may": "مايو",
    "june": "يونيو",
    "july": "يوليو",
    "august": "أغسطس",
    "september": "سبتمبر",
    "october": "أكتوبر",
    "november": "نوفمبر",
    "december": "ديسمبر",
}
# ---
cash_2022 = {
    "category:japan golf tour golfers": "تصنيف:لاعبو بطولة اليابان للغولف",
    "category:asian tour golfers": "تصنيف:لاعبو بطولة آسيا للغولف",
    "category:european tour golfers": "تصنيف:لاعبو بطولة أوروبا للغولف",
    "category:ladies european tour golfers": "تصنيف:لاعبات بطولة أوروبا للغولف للسيدات",
}
# ---
Work_With_Change_key = {1: False}

# ---
New_Lan = {}
all_country_with_nat_lower = {}
Kingdom = {}
# KAKO4 = {}

years_Baco = {}
Baco_decades = {}
# Baco_centries = {}
pop_of_in = {}
pop_new = {}
pop_type = {}

All_P17 = {}
Films_O_TT = {}

players_keys = {}
# ---
typeTable = {
    "youth sport": {"ar": "رياضة شبابية"},
    "works by": {"ar": "أعمال بواسطة"},
    "warm springs of": {"ar": "ينابيع دائفة في"},
    "video games": {"ar": "ألعاب فيديو", "priff": "ألعاب فيديو"},
    "uci road world cup": {"ar": "كأس العالم لسباق الدراجات على الطريق"},
    "television series": {"ar": "مسلسلات تلفزيونية"},
    "television seasons": {"ar": "مواسم تلفزيونية"},
    "television news": {"ar": "أخبار تلفزيونية"},
    "television miniseries": {"ar": "مسلسلات قصيرة"},
    "television films": {"ar": "أفلام تلفزيونية"},
    "television commercials": {"ar": "إعلانات تجارية تلفزيونية"},
    "sports events": {"ar": "أحداث", "Q": ["Q1190554", "Q349"], "s": "الرياضية"},
    "sorts-events": {"ar": "أحداث", "s": "الرياضية"},
    "road cycling": {"ar": "سباق الدراجات على الطريق", "Q": "Q1190554"},
    "qualification for": {"ar": "تصفيات مؤهلة إلى"},
    "produced": {"ar": "أنتجت"},
    "politics": {"ar": "سياسة", "priff": "سياسة"},
    "paralympic competitors for": {"ar": "منافسون بارالمبيون من"},
    "olympic medalists for": {"ar": "فائزون بميداليات أولمبية من"},
    "olympic competitors for": {"ar": "منافسون أولمبيون من"},
    "members of parliament for": {"ar": "أعضاء البرلمان عن"},
    "lists of": {"ar": "قوائم"},
    "interactive fiction": {"ar": "الخيال التفاعلي"},
    "installations": {"ar": "منشآت", "priff": "منشآت"},
    "fortifications": {"ar": "تحصينات", "priff": "تحصينات"},
    "fish described": {"ar": "أسماك وصفت"},
    "finales": {"ar": "نهايات", "priff": "نهايات"},
    "festivals": {"ar": "مهرجانات", "priff": "مهرجانات"},
    "events": {"ar": "أحداث", "Q": "Q1190554"},
    "establishments": {"ar": "تأسيسات", "Q": "Q3406134", "priff": "تأسيسات"},
    "endings": {"ar": "نهايات"},
    "elections": {"ar": "انتخابات", "priff": "انتخابات"},
    "disestablishments": {"ar": "انحلالات", "Q": "Q37621071", "priff": "انحلالات"},
    "disasters": {"ar": "كوارث"},
    "deaths": {"ar": "وفيات"},
    "deaths by": {"ar": "وفيات بواسطة"},
    "crimes": {"ar": "جرائم", "Q": "Q83267"},
    "counties": {"ar": "مقاطعات", "priff": "مقاطعات"},
    "conflicts": {"ar": "نزاعات"},
    "characters": {"ar": "شخصيات"},
    "births": {"ar": "مواليد"},
    "beginnings": {"ar": "بدايات"},
    "awards": {"ar": "جوائز", "priff": "جوائز"},
    "attacks": {"ar": "هجمات", "Q": "Q81672"},
    "architecture": {"ar": "عمارة"},
    "UCI Oceania Tour": {"ar": "طواف أوقيانوسيا للدراجات"},
    "UCI Europe Tour": {"ar": "طواف أوروبا للدراجات"},
    "UCI Asia Tour": {"ar": "طواف آسيا للدراجات"},
    "UCI America Tour": {"ar": "طواف أمريكا للدراجات"},
    "UCI Africa Tour": {"ar": "طواف إفريقيا للدراجات"},
    "Hot springs of": {"ar": "ينابيع حارة في"},
    "FIFA World Cup players": {"ar": "لاعبو كأس العالم لكرة القدم"},
    "FIFA futsal World Cup players": {"ar": "لاعبو كأس العالم لكرة الصالات"},
    "-related timelines": {"ar": "جداول زمنية متعلقة"},
    "-related professional associations": {"ar": "جمعيات تخصصية متعلقة"},
    "-related lists": {"ar": "قوائم متعلقة"},
    "commonwealth games competitors for": {
        "ar": "منافسون في ألعاب الكومنولث من",
    },
    "winter olympics competitors for": {
        "ar": "منافسون في الألعاب الأولمبية الشتوية من",
    },
    "civil aviation in": {
        "ar": "الطيران المدني في",
        "priff": "الطيران المدني في",
    },
    "national football team managers": {
        "priff": "مدربو منتخب",
        "s": "الوطني لكرة القدم",
        "ar": "",
    },
    "uci women's road world cup": {
        "ar": "كأس العالم لسباق الدراجات على الطريق للنساء",
    },
    # 'olympic gold medalists for' : {"ar":"حائزون على ميداليات ذهبية أولمبية من"},
    # 'sports ' : {"ar":"ألعاب رياضية", "s":""},
}

# safo = "|".join(typeTable.keys())
# ---
LOG = {1: False}
# ---
# split form start country[len("fasa "):])
# split form end  country[:-len("fm")])
# ---
Pp_Priffix = {
    " memorials": "نصب {} التذكارية",
    " video albums": "ألبومات فيديو {}",
    " albums": "ألبومات {}",
    " cabinet": "مجلس وزراء {}",
    " administration cabinet members": "أعضاء مجلس وزراء إدارة {}",
    " administration personnel": "موظفو إدارة {}",
    " executive office": "مكتب {} التنفيذي",
}
for io in ALBUMS_TYPE:
    Pp_Priffix[f"{io} albums"] = "ألبومات %s {}" % ALBUMS_TYPE[io]

# ---
# titttto = "disestablished in |hosted by |established in |produced in |based in |based on |set in |in |at |to "
titttto = ""
for titf in Tit_ose_Nmaes.keys():
    titttto += f"{titf.strip()} |"

# ---
Keep_it_last = ["remakes of"]
# ---
Keep_it_frist = [
    "spaceflight",
    "lists of",
    # "people associated with" ,
    "actors in",
    "male actors in",
    "centuries in",
    "centuries",
    "qualification for",
    "participants",
    "seasons in",
    "seasons",
    "works by",
]

Keep_it_frist2 = ["lists of", "works by", "qualification for", "seasons"]

Add_in_table = [
    "historical documents",
    "road incidents",
    "racehorse deaths",
    "animal deaths",
    "documents",
    "sports awards",
    "military alliances",
    "illuminated manuscripts",
    "biblical manuscripts",
]
# ---
Add_in_table += ADD_IN_TABLE2
# ---
# P17_keys = [x for x in pop_new]
P17_keys = [x for x in list(pop_All_2018)]
P17_new_keys = " |".join(P17_keys)

# t_tits = r'(' + pop_new_keys + ')\s*(of \w+|in \w+|by \w+|)(by \w+|)'
# t_tits = '(' + pop_new_keys + '|)(\s*\w+)'
# pop_new_ke = pop_new_keys
pop_new_ke = "decades in |valleys of |the spanish empire |events |water resource management in |landmarks in "
t_start = r"Category\:(" + pop_new_ke + ").*"
t_tits = r"Category\:(" + pop_new_ke + "|)(" + P17_new_keys + "|)"
t_other = f"({P17_new_keys}|)"
# ---
add_in_to_country = ["solar eclipses"]
# ---
army_line = "|".join(military_format_women.keys())
army_line = f"{army_line}|{'|'.join(military_format_men.keys())}"
# ---
for x in all_country_with_nat:
    all_country_with_nat_lower[x.lower()] = all_country_with_nat[x]
# ---
Lang_line = f"{'|'.join(languages_pop.keys())}|"

# ---
for ss in SPORTS_KEYS_FOR_LABEL:  #
    cd = f"by {ss.lower()} team"
    By_table[cd] = f"حسب فريق {SPORTS_KEYS_FOR_LABEL[ss]}"

for uh in People_key:  #
    By_table[f"by {uh.lower()}"] = f"بواسطة {People_key[uh]}"

for uh in FILM_PRODUCTION_COMPANY:  #
    By_table[f"by {uh.lower()}"] = f"بواسطة {FILM_PRODUCTION_COMPANY[uh]}"

len_Kingdom = {1: 0}

players_keys["women"] = "المرأة"

safo = "|".join(list(typeTable))

Films_O_TT.update({x.lower(): v for x, v in Films_TT.items() if v})

players_keys.update({x.lower(): {"ar": v} for x, v in typeTable_7.items()})

typeTable.update({x.lower(): v for x, v in typeTable_4.items() if v})
# ---
players_keys["national sports teams"] = "منتخبات رياضية وطنية"
players_keys["people"] = "أشخاص"

Add_ar_in = copy.deepcopy(olympics)

for olmp, olmp_lab in Add_ar_in.items():
    typeTable[f"{olmp} for"] = {"ar": f"{olmp_lab} من"}
    players_keys[olmp] = olmp_lab

type_Table_oo = {
    "prisoners sentenced to life imprisonment by": "سجناء حكم عليهم بالحبس المؤبد من قبل",
    "categories by province of": "تصنيفات حسب المقاطعة في",
    "invasions of": "غزو",
    "invasions by": "غزوات",
    "casualties": "خسائر",
    "prisoners of war held by": "أسرى أعتقلوا من قبل",
    "amnesty international prisoners-of-conscience held by": "سجناء حرية التعبير في",
    # "people executed by hanging by" : "أشخاص أعدموا شنقاً من قبل",
}
for tt_ype in list(type_Table_oo):
    typeTable[tt_ype.lower()] = {"ar": type_Table_oo[tt_ype]}

# typeTable["multi-sport events"] = {"ar":"أحداث رياضية متعددة"}
# safo = 'crimes|attacks|events|sports events|sports|establishments|disestablishments'

# ---
Table_for_frist_word = {
    "typetable": typeTable,
    "Films_O_TT": Films_O_TT,
    "New_players": players_keys,
}
# Table_for_frist_word_o = {
#     "typetable": set(typeTable.keys()),
#     "Films_O_TT": set(Films_O_TT.keys()),
#     "players_keys": set(players_keys.keys()),
# }
players_new_keys = players_keys


def add_to_new_players(en: str, ar: str) -> None:
    if not en or not ar:
        return
    players_new_keys[en] = ar


len_print.data_len("make2_bots.matables_bots/bot.py", {
    "players_new_keys": players_new_keys,   # 99517
    "All_P17": All_P17,
    "pop_of_in": pop_of_in,
    "pop_new": pop_new,
    "typeTable": typeTable,
})

__all__ = [
    "players_new_keys",
]
