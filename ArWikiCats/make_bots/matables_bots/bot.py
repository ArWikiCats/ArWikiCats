#!/usr/bin/python3
"""
python3 core8/pwb.py -m cProfile -s ncalls make/make_bots.matables_bots/bot.py

"""

from ...helps import len_print
from ...translations import (
    ALBUMS_TYPE,
    Jobs_new,
)

typeTable_7: dict[str, str] = {
    "air force": "قوات جوية",
    "airlines accidents": "حوادث طيران",
    "aviation accident": "حوادث طيران",
    "aviation accidents": "حوادث طيران",
    "design institutions": "مؤسسات تصميم",
    "distance education institutions": "مؤسسات تعليم عن بعد",
    "executed-burning": "أعدموا شنقاً",
    "executed-decapitation": "أعدموا بقطع الرأس",
    "executed-firearm": "أعدموا بسلاح ناري",
    "executed-hanging": "أعدموا حرقاً",
    "executions": "إعدامات",
    "people executed by": "أشخاص أعدموا من قبل",
    "people executed-by-burning": "أشخاص أعدموا شنقاً",
    "people executed-by-decapitation": "أشخاص أعدموا بقطع الرأس",
    "people executed-by-firearm": "أشخاص أعدموا بسلاح ناري",
    "people executed-by-hanging": "أشخاص أعدموا حرقاً",
    "railway accident": "حوادث سكك حديد",
    "railway accidents": "حوادث سكك حديد",
    "road accidents": "حوادث طرق",
    "transport accident": "حوادث نقل",
    "transport accidents": "حوادث نقل",
    "transport disasters": "كوارث نقل",
}


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


def _make_players_keys() -> dict:
    players_keys = {}
    players_keys["women"] = "المرأة"

    players_keys.update({x.lower(): v for x, v in Jobs_new.items() if v})

    players_keys.update({x.lower(): v for x, v in typeTable_7.items()})

    players_keys["national sports teams"] = "منتخبات رياضية وطنية"
    players_keys["people"] = "أشخاص"

    return players_keys


players_new_keys = _make_players_keys()

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
    "cash_2022",
    "Films_O_TT",
    "players_new_keys",
    "add_to_new_players",
    "add_to_Films_O_TT",
    "All_P17",
    "Pp_Priffix",
]
