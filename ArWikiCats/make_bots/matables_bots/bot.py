#!/usr/bin/python3
"""
python3 core8/pwb.py -m cProfile -s ncalls make/make_bots.matables_bots/bot.py

"""

from ...helps import len_print
from ...translations import (
    ALBUMS_TYPE,
    FILM_PRODUCTION_COMPANY,
    SPORTS_KEYS_FOR_LABEL,
    By_table,
    Films_TT,
    Jobs_new,
    People_key,
    all_country_with_nat,
    olympics,
    typeTable,
    typeTable_7,
)

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
for x in all_country_with_nat:
    all_country_with_nat_lower[x.lower()] = all_country_with_nat[x]
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

players_keys.update({x.lower(): v for x, v in Jobs_new.items() if v})

players_keys.update({x.lower(): v for x, v in typeTable_7.items()})

players_keys["national sports teams"] = "منتخبات رياضية وطنية"
players_keys["people"] = "أشخاص"

Add_ar_in = dict(olympics)

players_keys.update({x: v for x, v in Add_ar_in.items()})

Table_for_frist_word = {
    "typetable": typeTable,
    "Films_O_TT": Films_O_TT,
    "New_players": players_keys,
}

players_new_keys = players_keys


def add_to_new_players(en: str, ar: str) -> None:
    """Add a new English/Arabic player label pair to the cache."""
    if not en or not ar:
        return

    if not isinstance(en, str) or not isinstance(ar, str):
        return

    players_new_keys[en] = ar


def add_to_Films_O_TT(en: str, ar: str) -> None:
    """Add a new English/Arabic player label pair to the cache."""
    if not en or not ar:
        return

    if not isinstance(en, str) or not isinstance(ar, str):
        return

    Films_O_TT[en] = ar


len_print.data_len(
    "make_bots.matables_bots/bot.py",
    {
        "players_new_keys": players_new_keys,  # 99517
        "All_P17": All_P17,
        "pop_of_in": pop_of_in,
        "pop_new": pop_new,
    },
)

__all__ = [
    "Add_ar_in",
    "players_new_keys",
    "add_to_new_players",
    "add_to_Films_O_TT",
    "All_P17",
    "pop_of_in",
    "pop_new",
]
