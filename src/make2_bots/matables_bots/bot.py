#!/usr/bin/python3
"""
python3 core8/pwb.py -m cProfile -s ncalls make/make2_bots.matables_bots/bot.py

"""
from ..lazy_data_bots.bot_2018 import pop_All_2018
from ...helps import len_print
from ...translations import (
    typeTable,
    military_format_women,
    military_format_men,
    olympics,
    languages_pop,
    Films_TT,
    typeTable_7,
    ALBUMS_TYPE,
    FILM_PRODUCTION_COMPANY,
    SPORTS_KEYS_FOR_LABEL,
    By_table,
    ADD_IN_TABLE2,
    People_key,
    all_country_with_nat,
)

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

players_keys["women"] = "المرأة"

Films_O_TT.update({x.lower(): v for x, v in Films_TT.items() if v})

players_keys.update({x.lower(): v for x, v in typeTable_7.items()})

players_keys["national sports teams"] = "منتخبات رياضية وطنية"
players_keys["people"] = "أشخاص"

Add_ar_in = dict(olympics)

for olmp, olmp_lab in Add_ar_in.items():
    players_keys[olmp] = olmp_lab

# ---
Table_for_frist_word = {
    "typetable": typeTable,
    "Films_O_TT": Films_O_TT,
    "New_players": players_keys,
}

players_new_keys = players_keys


def add_to_new_players(en: str, ar: str) -> None:
    if not en or not ar:
        return
    if not isinstance(en, str) or not isinstance(ar, str):
        return
    players_new_keys[en] = ar


len_print.data_len("make2_bots.matables_bots/bot.py", {
    "players_new_keys": players_new_keys,   # 99517
    "All_P17": All_P17,
    "pop_of_in": pop_of_in,
    "pop_new": pop_new,
})

__all__ = [
    "players_new_keys",
]
