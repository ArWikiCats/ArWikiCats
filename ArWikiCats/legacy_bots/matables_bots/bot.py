#!/usr/bin/python3
"""
python3 core8/pwb.py -m cProfile -s ncalls make/make_bots.matables_bots/bot.py

"""

from ...helps import len_print
from ...translations import Jobs_new

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


def _make_players_keys() -> dict:
    """
    Build a mapping of player-related English terms (lowercased) to their Arabic labels for category mapping.

    Returns:
        dict: Mapping where keys are lowercase English player-related terms and values are Arabic equivalents.
    """
    players_keys = {}
    players_keys["women"] = "المرأة"

    players_keys.update({x.lower(): v for x, v in Jobs_new.items() if v})

    players_keys.update({x.lower(): v for x, v in typeTable_7.items()})

    players_keys["national sports teams"] = "منتخبات رياضية وطنية"
    players_keys["people"] = "أشخاص"

    return players_keys


players_new_keys = _make_players_keys()

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
    },
)

__all__ = [
    "Films_O_TT",
    "players_new_keys",
    "add_to_new_players",
    "add_to_Films_O_TT",
]
