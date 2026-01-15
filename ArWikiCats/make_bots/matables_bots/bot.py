#!/usr/bin/python3
"""
python3 core8/pwb.py -m cProfile -s ncalls make/make_bots.matables_bots/bot.py

"""

from ...helps import len_print
from ...translations import (
    ALBUMS_TYPE,
    Jobs_new,
    olympic_event_translations,
    typeTable,
    typeTable_7,
)


def _create_pp_prefix(albums_typies: dict[str, str]) -> dict[str, str]:
    Pp_Priffix = {
        " memorials": "نصب {} التذكارية",
        " video albums": "ألبومات فيديو {}",
        " albums": "ألبومات {}",
        " cabinet": "مجلس وزراء {}",
        " administration cabinet members": "أعضاء مجلس وزراء إدارة {}",
        " administration personnel": "موظفو إدارة {}",
        " executive office": "مكتب {} التنفيذي",
    }

    for io in albums_typies:
        Pp_Priffix[f"{io} albums"] = "ألبومات %s {}" % albums_typies[io]

    return Pp_Priffix


def _make_players_keys(Add_ar_in: dict[str, str]) -> dict:
    players_keys = {}
    players_keys["women"] = "المرأة"

    players_keys.update({x.lower(): v for x, v in Jobs_new.items() if v})

    players_keys.update({x.lower(): v for x, v in typeTable_7.items()})

    players_keys["national sports teams"] = "منتخبات رياضية وطنية"
    players_keys["people"] = "أشخاص"

    players_keys.update(Add_ar_in)
    return players_keys


Add_ar_in = dict(olympic_event_translations)
players_new_keys = _make_players_keys(Add_ar_in)
Pp_Priffix = _create_pp_prefix(ALBUMS_TYPE)


cash_2022 = {
    "category:japan golf tour golfers": "تصنيف:لاعبو بطولة اليابان للغولف",
    "category:asian tour golfers": "تصنيف:لاعبو بطولة آسيا للغولف",
    "category:european tour golfers": "تصنيف:لاعبو بطولة أوروبا للغولف",
    "category:ladies european tour golfers": "تصنيف:لاعبات بطولة أوروبا للغولف للسيدات",
}
# ---
All_P17 = {}
Films_O_TT = {}

Table_for_frist_word = {
    "typetable": typeTable,
    "Films_O_TT": Films_O_TT,
    "New_players": players_new_keys,
}


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
    },
)

__all__ = [
    "Table_for_frist_word",
    "cash_2022",
    "Films_O_TT",
    "Add_ar_in",
    "players_new_keys",
    "add_to_new_players",
    "add_to_Films_O_TT",
    "All_P17",
    "Pp_Priffix",
]
