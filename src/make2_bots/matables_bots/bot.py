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
    Sports_Keys_For_Label,
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
make_tab = {1: False}
main2_tab = {1: {"title": "", "lab": {}, "nolab": {}}}
_current_table_sink: Optional[Callable[[str, str], None]] = None

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
    # 'winter' : {"ar":"الشتاء", "Q":""},
    # 'winter sports' : {"ar":"الرياضة الشتوية", "Q":""},
    # 'united states senate elections' : {"ar":"انتخابات مجلس الشيوخ الأمريكي", "Q":""},
    # 'sports events' : {"ar":"أحداث رياضية", "Q":"Q16510064", "s":"الرياضية"},
    # 'professional wrestling' : {"ar":"مصارعة المحترفين", "Q":"", "priff":"مصارعة المحترفين"},
    # 'prehistory of' : {"ar":"ما قبل التاريخ", "Q":"", "priff":"ما قبل التاريخ"},
    # 'peer reviews' : {"ar":"مراجعة الأقران", "Q":"Q215028"},
    # 'non-combat' : {"ar":"", "Q":"", "s":"غير قتالية"},
    # 'military history' : {"ar":"التاريخ العسكري", "Q":""},
    # 'in sports' : {"ar":"أحداث", "Q":"Q16510064", "s":"الرياضية"},
    # 'elections in' : {"ar":"انتخابات", "Q":"", "priff":"انتخابات"},
    # 'categories named after' : {"ar":"أعمال بواسطة", "Q":""},
    # 'Summer sports' : {"ar":"الرياضة الصيفية", "Q":""},
    # '-related media' : {"ar":"إعلام متعلق", "Q":""},
    # "paintings-by" : {"ar":"لوحات بواسطة", "Q":""},
    # "business":{"ar":"أعمال تجارية", "Q":""},
    # "american motorsport":{"ar":"رياضة محركات في الولايات المتحدة", "Q":""},
    # 'spring' : {"ar":"الربيع", "Q":""},
    "youth sport": {"ar": "رياضة شبابية", "Q": ""},
    "works by": {"ar": "أعمال بواسطة", "Q": ""},
    "warm springs of": {"ar": "ينابيع دائفة في", "Q": ""},
    "video games": {"ar": "ألعاب فيديو", "Q": "", "priff": "ألعاب فيديو"},
    "uci road world cup": {"ar": "كأس العالم لسباق الدراجات على الطريق", "Q": ""},
    "television series": {"ar": "مسلسلات تلفزيونية", "Q": ""},
    "television seasons": {"ar": "مواسم تلفزيونية", "Q": ""},
    "television news": {"ar": "أخبار تلفزيونية", "Q": ""},
    "television miniseries": {"ar": "مسلسلات قصيرة", "Q": ""},
    "television films": {"ar": "أفلام تلفزيونية", "Q": ""},
    "television commercials": {"ar": "إعلانات تجارية تلفزيونية", "Q": ""},
    "sports events": {"ar": "أحداث", "Q": ["Q1190554", "Q349"], "s": "الرياضية"},
    "sorts-events": {"ar": "أحداث", "Q": "", "s": "الرياضية"},
    "road cycling": {"ar": "سباق الدراجات على الطريق", "Q": "Q1190554"},
    "qualification for": {"ar": "تصفيات مؤهلة إلى", "Q": ""},
    "produced": {"ar": "أنتجت", "Q": ""},
    "politics": {"ar": "سياسة", "Q": "", "priff": "سياسة"},
    "paralympic competitors for": {"ar": "منافسون بارالمبيون من", "Q": ""},
    "olympic medalists for": {"ar": "فائزون بميداليات أولمبية من", "Q": ""},
    "olympic competitors for": {"ar": "منافسون أولمبيون من", "Q": ""},
    "members of parliament for": {"ar": "أعضاء البرلمان عن", "Q": ""},
    "lists of": {"ar": "قوائم", "Q": ""},
    "interactive fiction": {"ar": "الخيال التفاعلي", "Q": ""},
    "installations": {"ar": "منشآت", "Q": "", "priff": "منشآت"},
    "fortifications": {"ar": "تحصينات", "Q": "", "priff": "تحصينات"},
    "fish described": {"ar": "أسماك وصفت", "Q": ""},
    "finales": {"ar": "نهايات", "Q": "", "priff": "نهايات"},
    "festivals": {"ar": "مهرجانات", "Q": "", "priff": "مهرجانات"},
    "events": {"ar": "أحداث", "Q": "Q1190554"},
    "establishments": {"ar": "تأسيسات", "Q": "Q3406134", "priff": "تأسيسات"},
    "endings": {"ar": "نهايات", "Q": ""},
    "elections": {"ar": "انتخابات", "Q": "", "priff": "انتخابات"},
    "disestablishments": {"ar": "انحلالات", "Q": "Q37621071", "priff": "انحلالات"},
    "disasters": {"ar": "كوارث", "Q": ""},
    "deaths": {"ar": "وفيات", "Q": ""},
    "deaths by": {"ar": "وفيات بواسطة", "Q": ""},
    "crimes": {"ar": "جرائم", "Q": "Q83267"},
    "counties": {"ar": "مقاطعات", "Q": "", "priff": "مقاطعات"},
    "conflicts": {"ar": "نزاعات", "Q": ""},
    "characters": {"ar": "شخصيات", "Q": ""},
    "births": {"ar": "مواليد", "Q": ""},
    "beginnings": {"ar": "بدايات", "Q": ""},
    "awards": {"ar": "جوائز", "Q": "", "priff": "جوائز"},
    "attacks": {"ar": "هجمات", "Q": "Q81672"},
    "architecture": {"ar": "عمارة", "Q": ""},
    "UCI Oceania Tour": {"ar": "طواف أوقيانوسيا للدراجات", "Q": ""},
    "UCI Europe Tour": {"ar": "طواف أوروبا للدراجات", "Q": ""},
    "UCI Asia Tour": {"ar": "طواف آسيا للدراجات", "Q": ""},
    "UCI America Tour": {"ar": "طواف أمريكا للدراجات", "Q": ""},
    "UCI Africa Tour": {"ar": "طواف إفريقيا للدراجات", "Q": ""},
    "Hot springs of": {"ar": "ينابيع حارة في", "Q": ""},
    "FIFA World Cup players": {"ar": "لاعبو كأس العالم لكرة القدم", "Q": ""},
    "FIFA futsal World Cup players": {"ar": "لاعبو كأس العالم لكرة الصالات", "Q": ""},
    "-related timelines": {"ar": "جداول زمنية متعلقة", "Q": ""},
    "-related professional associations": {"ar": "جمعيات تخصصية متعلقة", "Q": ""},
    "-related lists": {"ar": "قوائم متعلقة", "Q": ""},
    "commonwealth games competitors for": {
        "ar": "منافسون في ألعاب الكومنولث من",
        "Q": "",
    },
    "winter olympics competitors for": {
        "ar": "منافسون في الألعاب الأولمبية الشتوية من",
        "Q": "",
    },
    "civil aviation in": {
        "ar": "الطيران المدني في",
        "Q": "",
        "priff": "الطيران المدني في",
    },
    "national football team managers": {
        "priff": "مدربو منتخب",
        "Q": "",
        "s": "الوطني لكرة القدم",
        "ar": "",
    },
    "uci women's road world cup": {
        "ar": "كأس العالم لسباق الدراجات على الطريق للنساء",
        "Q": "",
    },
    # 'olympic gold medalists for' : {"ar":"حائزون على ميداليات ذهبية أولمبية من", "Q":""},
    # 'sports ' : {"ar":"ألعاب رياضية", "Q":"", "s":""},
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
for ss in Sports_Keys_For_Label:  #
    cd = f"by {ss.lower()} team"
    By_table[cd] = f"حسب فريق {Sports_Keys_For_Label[ss]}"

for uh in People_key:  #
    By_table[f"by {uh.lower()}"] = f"بواسطة {People_key[uh]}"

for uh in FILM_PRODUCTION_COMPANY:  #
    By_table[f"by {uh.lower()}"] = f"بواسطة {FILM_PRODUCTION_COMPANY[uh]}"

len_Kingdom = {1: 0}

players_keys["women"] = "المرأة"

# for le in Lenth:

safo = "|".join(list(typeTable))

# ---

Films_O_TT.update({x.lower(): v for x, v in Films_TT.items() if v})
# ---
# with jobs_mens_data Jobs_new, len of players_keys = 99517
# without, len = 415
# players_keys.update({x.lower(): v for x, v in jobs_mens_data.items() if v})
# players_keys.update({x.lower(): v for x, v in Jobs_new.items() if v})
# ---

# all_keys3
players_keys.update({x.lower(): {"ar": v, "Q": ""} for x, v in typeTable_7.items()})

typeTable.update({x.lower(): v for x, v in typeTable_4.items() if v})
# ---
# KAKO3 = [All_P17 ]#Films_key_man , Music_By_table , By_table , pop_new , players_keys , Films_O_TT , pop_of_in]

Log_Work = {1: True}

# ---
tita_Q = {
    "disestablishments": {"Q": "Q37621071", "priff": "انحلالات"},
    "establishments": {"Q": "Q3406134", "priff": "تأسيسات"},
}

players_keys["national sports teams"] = "منتخبات رياضية وطنية"
players_keys["people"] = "أشخاص"

# MONTHSTR = '(January|February|March|April|May|June|July|August|September|October|November|December)'
MONTHSTR = "(January|February|March|April|May|June|July|August|September|October|November|December|)"

type_after_country = ["non-combat"]

# Add_ar_in = [ "mediterranean games medalists",]
Add_ar_in = copy.deepcopy(olympics)

for olmp, olmp_lab in Add_ar_in.items():
    typeTable[f"{olmp} for"] = {"ar": f"{olmp_lab} من", "Q": ""}
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
    typeTable[tt_ype.lower()] = {"ar": type_Table_oo[tt_ype], "Q": ""}

# typeTable["multi-sport events"] = {"ar":"أحداث رياضية متعددة", "Q":""}
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


def set_table_sink(sink: Optional[Callable[[str, str], None]]) -> None:
    """Register a table sink used by the new event processor."""

    global _current_table_sink
    _current_table_sink = sink
    make_tab[1] = sink is not None
    main2_tab[1] = {"title": "", "lab": {}, "nolab": {}}


def Add_to_main2_tab(en: str, ar: str) -> None:
    if not en or not ar:
        return
    if _current_table_sink is not None:
        _current_table_sink(en, ar)


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
