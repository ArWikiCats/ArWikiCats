"""Utilities for gendered Arabic player labels and related helpers.

The legacy implementation of this module relied on a large, mutable script that
loaded JSON dictionaries and updated them in place.  The refactor exposes typed
constants and helper functions that retain the original Arabic content while
being easier to reason about and test.
"""

from __future__ import annotations

from typing import Dict, Mapping

from ...helps import len_print
from ..sports.Sport_key import (
    SPORTS_KEYS_FOR_JOBS,
    SPORTS_KEYS_FOR_LABEL,
    SPORTS_KEYS_FOR_TEAM,
)
from ..utils.json_dir import open_json
from .jobs_defs import GenderedLabel, GenderedLabelMap

# ---------------------------------------------------------------------------
# Static configuration

BOXING_WEIGHT_TRANSLATIONS: Mapping[str, str] = {
    "bantamweight": "وزن بانتام",
    "featherweight": "وزن الريشة",
    "lightweight": "وزن خفيف",
    "light heavyweight": "وزن ثقيل خفيف",
    "light-heavyweight": "وزن ثقيل خفيف",
    "light middleweight": "وزن خفيف متوسط",
    "middleweight": "وزن متوسط",
    "super heavyweight": "وزن ثقيل سوبر",
    "heavyweight": "وزن ثقيل",
    "welterweight": "وزن الويلتر",
    "flyweight": "وزن الذبابة",
    "super middleweight": "وزن متوسط سوبر",
    "pinweight": "وزن الذرة",
    "super flyweight": "وزن الذبابة سوبر",
    "super featherweight": "وزن الريشة سوبر",
    "super bantamweight": "وزن البانتام سوبر",
    "light flyweight": "وزن ذبابة خفيف",
    "light welterweight": "وزن والتر خفيف",
    "cruiserweight": "وزن الطراد",
    "minimumwe": "",
    "inimumweight": "",
    "atomweight": "وزن الذرة",
    "super cruiserweight": "وزن الطراد سوبر",
}

WORLD_BOXING_CHAMPION_PREFIX: GenderedLabel = {"mens": "أبطال العالم للملاكمة فئة", "females": ""}
# Prefix applied to boxing world champion descriptors.

SKATING_DISCIPLINE_LABELS: Mapping[str, GenderedLabel] = {
    "nordic combined": {"mens": "تزلج نوردي مزدوج", "females": "تزلج نوردي مزدوج"},
    "speed": {"mens": "سرعة", "females": "سرعة"},
    "roller": {"mens": "بالعجلات", "females": "بالعجلات"},
    "alpine": {"mens": "منحدرات ثلجية", "females": "منحدرات ثلجية"},
    "short track speed": {"mens": "مسار قصير", "females": "مسار قصير"},
}

TEAM_SPORT_TRANSLATIONS: Mapping[str, str] = {
    # "ice hockey players":"هوكي جليد",
    # "ice hockey playerss":"هوكي جليد",
    # "floorball players":"هوكي العشب",
    # "tennis players":"تنس",
    "croquet players": "",  # "كروكيت"
    "badminton players": "تنس الريشة",
    "chess players": "شطرنج",
    "basketball players": "كرة السلة",
    "beach volleyball players": "",
    "fifa world cup players": "كأس العالم لكرة القدم",
    "fifa futsal world cup players": "كأس العالم لكرة الصالات",
    "polo players": "بولو",
    "racquets players": "",
    "real tennis players": "",
    "roque players": "",
    "rugby players": "الرجبي",
    "softball players": "سوفتبول",
    "floorball players": "كرة الأرض",
    "table tennis players": "كرة الطاولة",
    "volleyball players": "كرة الطائرة",
    "water polo players": "كرة الماء",
    "field hockey players": "هوكي الميدان",
    "handball players": "كرة يد",
    "tennis players": "كرة مضرب",
    "football referees": "حكام كرة قدم",
    "racing drivers": "سائقو سيارات سباق",
    "snooker players": "سنوكر",
    "baseball players": "كرة القاعدة",
    "players of american football": "كرة قدم أمريكية",
    "players of canadian football": "كرة قدم كندية",
    "association football players": "كرة قدم",
    "gaelic footballers": "كرة قدم غيلية",
    "australian rules footballers": "كرة قدم أسترالية",
    "rules footballers": "كرة قدم",
    "players of australian rules football": "كرة القدم الأسترالية",
    "kabaddi players": "كابادي",
    "poker players": "بوكر",
    "rugby league players": "دوري الرغبي",
    "rugby union players": "اتحاد الرغبي",
    "lacrosse players": "لاكروس",
}

GENERAL_SPORT_ROLES: Mapping[str, GenderedLabel] = {
    "managers": {"mens": "مدربون", "females": "مدربات"},
    "competitors": {"mens": "منافسون", "females": "منافسات"},
    "coaches": {"mens": "مدربون", "females": "مدربات"},
}

SPORT_SCOPE_ROLES: Mapping[str, GenderedLabel] = {
    "paralympic": {"mens": "بارالمبيون", "females": "بارالمبيات"},
    "olympics": {"mens": "أولمبيون", "females": "أولمبيات"},
    "sports": {"mens": "رياضيون", "females": "رياضيات"},
}

# Suffix describing Olympic level participation.

# Suffix describing international level participation.

STATIC_PLAYER_LABELS: GenderedLabelMap = {
    "national team coaches": {"mens": "مدربو فرق وطنية", "females": "مدربات فرق وطنية"},
    "national team managers": {"mens": "مدربو فرق وطنية", "females": "مدربات فرق وطنية"},
    "sports agents": {"mens": "وكلاء رياضات", "females": "وكيلات رياضات"},
    "expatriate sprtspeople": {"mens": "رياضيون مغتربون", "females": "رياضيات مغتربات"},
    "expatriate sportspeople": {"mens": "رياضيون مغتربون", "females": "رياضيات مغتربات"},
}
# ---------------------------------------------------------------------------
# Builders


def _build_boxing_labels(weights: Mapping[str, str]) -> GenderedLabelMap:
    """Return gendered labels for boxing weight classes."""

    result: GenderedLabelMap = {}

    for weight_key, arabic_label in weights.items():
        if not arabic_label:
            continue
        weight_boxers_key = f"{weight_key} boxers"
        result[weight_boxers_key] = {"mens": f"ملاكمو {arabic_label}", "females": f"ملاكمات {arabic_label}"}
        result[f"world {weight_key} boxing champions"] = {
            "mens": f"أبطال العالم للملاكمة فئة {arabic_label}",
            "females": "",
        }
    return result


def _build_skating_labels(labels: Mapping[str, GenderedLabel]) -> GenderedLabelMap:
    """Create labels for skating and skiing disciplines."""

    result: GenderedLabelMap = {}
    for discipline_key, discipline_labels in labels.items():
        mens = discipline_labels["mens"]
        womens = discipline_labels["females"]
        result[f"{discipline_key} skaters"] = {
            "mens": f"متزلجو {mens}",
            "females": f"متزلجات {womens}",
        }
        result[f"{discipline_key} skiers"] = {
            "mens": f"متزحلقو {mens}",
            "females": f"متزحلقات {womens}",
        }

    return result


def _build_team_sport_labels(translations: Mapping[str, str]) -> GenderedLabelMap:
    """Translate team sport categories into gendered Arabic labels."""

    result: GenderedLabelMap = {}
    for english_key, arabic_value in translations.items():
        if not arabic_value:
            continue
        result[english_key] = {
            "mens": f"لاعبو {arabic_value}",
            "females": f"لاعبات {arabic_value}",
        }
    return result


def _build_jobs_player_variants(players: Mapping[str, GenderedLabel]) -> GenderedLabelMap:
    """Generate derivative labels for the base player dataset."""

    result: GenderedLabelMap = {}
    for english_key, labels in players.items():
        mens_label = labels.get("mens", "")
        womens_label = labels.get("females", "")

        if not (mens_label or womens_label):
            continue

        lowered_key = english_key.lower()
        result[lowered_key] = {"mens": mens_label, "females": womens_label}

        result[f"olympic {lowered_key}"] = {"mens": f"{mens_label} أولمبيون", "females": f"{womens_label} أولمبيات"}
        result[f"international {lowered_key}"] = {"mens": f"{mens_label} دوليون", "females": f"{womens_label} دوليات"}

    return result


def _build_general_scope_labels(
    roles: Mapping[str, GenderedLabel],
    scopes: Mapping[str, GenderedLabel],
) -> GenderedLabelMap:
    """Combine generic sport roles with scope modifiers (e.g. Olympic)."""

    result: GenderedLabelMap = {}
    for role_key, role_labels in roles.items():
        for scope_key, scope_labels in scopes.items():
            composite_key = f"{scope_key} {role_key}".lower()
            result[composite_key] = {
                "mens": f"{role_labels['mens']} {scope_labels['mens']}",
                "females": f"{role_labels['womens']} {scope_labels['womens']}",
            }
    return result


def _build_champion_labels(labels: Mapping[str, str]) -> GenderedLabelMap:
    """Create champion labels from the sport label mapping."""

    result: GenderedLabelMap = {}
    for sport_key, arabic_label in labels.items():
        composite_key = f"{sport_key.lower()} champions"
        result[composite_key] = {
            "mens": f"أبطال {arabic_label}",
            "females": "",
        }
    return result


def _build_world_champion_labels(labels: Mapping[str, str]) -> GenderedLabelMap:
    """Create world champion labels from team descriptors."""

    result: GenderedLabelMap = {}
    for sport_key, arabic_label in labels.items():
        composite_key = f"world {sport_key.lower()} champions"
        result[composite_key] = {
            "mens": f"أبطال العالم {arabic_label} ",
            "females": "",
        }
    return result


def _build_sports_job_variants(
    sport_jobs: Mapping[str, str],
    football_roles: Mapping[str, GenderedLabel],
) -> tuple[GenderedLabelMap, Dict[str, str]]:
    """Create commentators, announcers, and other job variants."""

    result: GenderedLabelMap = {}

    for job_key, arabic_label in sport_jobs.items():
        lowered_job_key = job_key.lower()
        result[f"{lowered_job_key} biography"] = {
            "mens": f"أعلام {arabic_label}",
            "females": "",
        }
        result[f"{lowered_job_key} commentators_"] = {  # TODO: remove this
            "mens": f"معلقو {arabic_label}",
            "females": f"معلقات {arabic_label}",
        }
        result[f"{lowered_job_key} announcers"] = {
            "mens": f"مذيعو {arabic_label}",
            "females": f"مذيعات {arabic_label}",
        }
        result[f"{lowered_job_key} stage winners"] = {
            "mens": f"فائزون في مراحل {arabic_label}",
            "females": f"فائزات في مراحل {arabic_label}",
        }
        result[f"{lowered_job_key} coaches"] = {
            "mens": f"مدربو {arabic_label}",
            "females": f"مدربات {arabic_label}",
        }
        result[f"{lowered_job_key} executives"] = {
            "mens": f"مسيرو {arabic_label}",
            "females": f"مسيرات {arabic_label}",
        }
        result[f"{lowered_job_key} sprtspeople"] = {
            "mens": f"رياضيو {arabic_label}",
            "females": f"رياضيات {arabic_label}",
        }
        result[f"{lowered_job_key} sportspeople"] = {
            "mens": f"رياضيو {arabic_label}",
            "females": f"رياضيات {arabic_label}",
        }
        for football_key, football_labels in football_roles.items():
            lowered_football_key = football_key.lower()
            olympic_key = f"olympic {lowered_job_key} {lowered_football_key}"
            result[olympic_key] = {
                "mens": f"{football_labels['mens']} {arabic_label} أولمبيون",
                "females": f"{football_labels['womens']} {arabic_label} أولمبيات",
            }
            mens_key = f"men's {lowered_job_key} {lowered_football_key}"
            result[mens_key] = {
                "mens": f"{football_labels['mens']} {arabic_label} رجالية",
                "females": "",
            }
            composite_key = f"{lowered_job_key} {lowered_football_key}"
            result[composite_key] = {
                "mens": f"{football_labels['mens']} {arabic_label}",
                "females": f"{football_labels['womens']} {arabic_label}",
            }

    return result


def _merge_maps(*maps: Mapping[str, GenderedLabel]) -> GenderedLabelMap:
    """Merge multiple :class:`GenderedLabelMap` instances."""

    merged: GenderedLabelMap = {}
    for source in maps:
        merged.update(source)
    return merged


# ---------------------------------------------------------------------------
# Data assembly

FOOTBALL_KEYS_PLAYERS: GenderedLabelMap = open_json("jobs/jobs_Football_Keys_players.json") or {}

JOBS_PLAYERS: GenderedLabelMap = open_json("jobs/Jobs_players.json") or {}

JOBS_PLAYERS.setdefault("freestyle swimmers", {"mens": "سباحو تزلج حر", "females": "سباحات تزلج حر"})

TEAM_SPORT_LABELS = _build_team_sport_labels(TEAM_SPORT_TRANSLATIONS)
BOXING_LABELS = _build_boxing_labels(BOXING_WEIGHT_TRANSLATIONS)
# ---
JOBS_PLAYERS.update(BOXING_LABELS)
# ---
BASE_PLAYER_VARIANTS = _build_jobs_player_variants(JOBS_PLAYERS)

SKATING_LABELS = _build_skating_labels(SKATING_DISCIPLINE_LABELS)

SKATING_LABELS = {x: v for x, v in SKATING_LABELS.items() if x not in BASE_PLAYER_VARIANTS}

GENERAL_SCOPE_LABELS = _build_general_scope_labels(GENERAL_SPORT_ROLES, SPORT_SCOPE_ROLES)
CHAMPION_LABELS = _build_champion_labels(SPORTS_KEYS_FOR_LABEL)
WORLD_CHAMPION_LABELS = _build_world_champion_labels(SPORTS_KEYS_FOR_TEAM)
SPORT_JOB_VARIANTS = _build_sports_job_variants(
    SPORTS_KEYS_FOR_JOBS,
    FOOTBALL_KEYS_PLAYERS,
)

PLAYERS_TO_MEN_WOMENS_JOBS = _merge_maps(
    STATIC_PLAYER_LABELS,
    TEAM_SPORT_LABELS,
    SKATING_LABELS,
    BOXING_LABELS,
    GENERAL_SCOPE_LABELS,
    CHAMPION_LABELS,
    WORLD_CHAMPION_LABELS,
    SPORT_JOB_VARIANTS,
    BASE_PLAYER_VARIANTS,
)

# ---------------------------------------------------------------------------
# Backwards compatible exports

Football_Keys_players: GenderedLabelMap = FOOTBALL_KEYS_PLAYERS

__all__ = [
    "FOOTBALL_KEYS_PLAYERS",
    "JOBS_PLAYERS",
    "PLAYERS_TO_MEN_WOMENS_JOBS",
]

len_print.data_len(
    "jobs_players_list.py",
    {
        "FOOTBALL_KEYS_PLAYERS": FOOTBALL_KEYS_PLAYERS,
        "JOBS_PLAYERS": JOBS_PLAYERS,
        "PLAYERS_TO_MEN_WOMENS_JOBS": PLAYERS_TO_MEN_WOMENS_JOBS,
    },
)
