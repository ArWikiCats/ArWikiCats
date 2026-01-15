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
from ..utils.json_dir import open_json_file
from .jobs_defs import GenderedLabel, GenderedLabelMap, combine_gender_labels

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

WORLD_BOXING_CHAMPION_PREFIX: GenderedLabel = {"males": "أبطال العالم للملاكمة فئة", "females": ""}
# Prefix applied to boxing world champion descriptors.

SKATING_DISCIPLINE_LABELS: Mapping[str, GenderedLabel] = {
    "nordic combined": {"males": "تزلج نوردي مزدوج", "females": "تزلج نوردي مزدوج"},
    "speed": {"males": "سرعة", "females": "سرعة"},
    "roller": {"males": "بالعجلات", "females": "بالعجلات"},
    "alpine": {"males": "منحدرات ثلجية", "females": "منحدرات ثلجية"},
    "short track speed": {"males": "مسار قصير", "females": "مسار قصير"},
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
    "rugby league players": "دوري الرجبي",
    "rugby union players": "اتحاد الرجبي",
    "lacrosse players": "لاكروس",
}

GENERAL_SPORT_ROLES: Mapping[str, GenderedLabel] = {
    "managers": {"males": "مدربون", "females": "مدربات"},
    "competitors": {"males": "منافسون", "females": "منافسات"},
    "coaches": {"males": "مدربون", "females": "مدربات"},
}

SPORT_SCOPE_ROLES: Mapping[str, GenderedLabel] = {
    "paralympic": {"males": "بارالمبيون", "females": "بارالمبيات"},
    "olympics": {"males": "أولمبيون", "females": "أولمبيات"},
    "sports": {"males": "رياضيون", "females": "رياضيات"},
}

# Suffix describing Olympic level participation.

# Suffix describing international level participation.

STATIC_PLAYER_LABELS: GenderedLabelMap = {
    "national team coaches": {"males": "مدربو فرق وطنية", "females": "مدربات فرق وطنية"},
    "national team managers": {"males": "مدربو فرق وطنية", "females": "مدربات فرق وطنية"},
    "sports agents": {"males": "وكلاء رياضات", "females": "وكيلات رياضات"},
    "expatriate sports-people": {"males": "رياضيون مغتربون", "females": "رياضيات مغتربات"},
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
        result[weight_boxers_key] = {"males": f"ملاكمو {arabic_label}", "females": f"ملاكمات {arabic_label}"}
        result[f"world {weight_key} boxing champions"] = {
            "males": f"أبطال العالم للملاكمة فئة {arabic_label}",
            "females": "",
        }
    return result


def _build_skating_labels(labels: Mapping[str, GenderedLabel]) -> GenderedLabelMap:
    """Create labels for skating and skiing disciplines."""

    result: GenderedLabelMap = {}
    for discipline_key, discipline_labels in labels.items():
        males = discipline_labels["males"]
        females = discipline_labels["females"]
        result[f"{discipline_key} skaters"] = {
            "males": f"متزلجو {males}",
            "females": f"متزلجات {females}",
        }
        result[f"{discipline_key} skiers"] = {
            "males": f"متزحلقو {males}",
            "females": f"متزحلقات {females}",
        }

    return result


def _build_team_sport_labels(translations: Mapping[str, str]) -> GenderedLabelMap:
    """Translate team sport categories into gendered Arabic labels."""

    result: GenderedLabelMap = {}
    for english_key, arabic_value in translations.items():
        if not arabic_value:
            continue
        result[english_key] = {
            "males": f"لاعبو {arabic_value}",
            "females": f"لاعبات {arabic_value}",
        }
    return result


def _build_jobs_player_variants(players: Mapping[str, GenderedLabel]) -> GenderedLabelMap:
    """Generate derivative labels for the base player dataset."""

    result: GenderedLabelMap = {}
    for english_key, labels in players.items():
        mens_label = labels.get("males", "")
        womens_label = labels.get("females", "")

        if not (mens_label or womens_label):
            continue

        lowered_key = english_key.lower()
        result[lowered_key] = {"males": mens_label, "females": womens_label}

        result[f"olympic {lowered_key}"] = {"males": f"{mens_label} أولمبيون", "females": f"{womens_label} أولمبيات"}
        result[f"international {lowered_key}"] = {"males": f"{mens_label} دوليون", "females": f"{womens_label} دوليات"}

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
            males_label = combine_gender_labels(role_labels["males"], scope_labels["males"])
            females_label = combine_gender_labels(role_labels["females"], scope_labels["females"])
            result[composite_key] = {
                "males": males_label,
                "females": females_label,
            }
    return result


def _build_champion_labels(labels: Mapping[str, str]) -> GenderedLabelMap:
    """Create champion labels from the sport label mapping."""

    result: GenderedLabelMap = {}
    for sport_key, arabic_label in labels.items():
        if not arabic_label:
            continue
        composite_key = f"{sport_key.lower()} champions"
        result[composite_key] = {
            "males": f"أبطال {arabic_label}",
            "females": "",
        }
    return result


def _build_world_champion_labels(labels: Mapping[str, str]) -> GenderedLabelMap:
    """Create world champion labels from team descriptors."""

    result: GenderedLabelMap = {}
    for sport_key, arabic_label in labels.items():
        if not arabic_label:
            continue
        composite_key = f"world {sport_key.lower()} champions"
        result[composite_key] = {
            "males": f"أبطال العالم {arabic_label} ",
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
        if not arabic_label:
            continue
        result[f"{lowered_job_key} biography"] = {
            "males": f"أعلام {arabic_label}",
            "females": "",
        }
        result[f"{lowered_job_key} announcers"] = {
            "males": f"مذيعو {arabic_label}",
            "females": f"مذيعات {arabic_label}",
        }
        result[f"{lowered_job_key} stage winners"] = {
            "males": f"فائزون في مراحل {arabic_label}",
            "females": f"فائزات في مراحل {arabic_label}",
        }
        result[f"{lowered_job_key} coaches"] = {
            "males": f"مدربو {arabic_label}",
            "females": f"مدربات {arabic_label}",
        }
        result[f"{lowered_job_key} executives"] = {
            "males": f"مسيرو {arabic_label}",
            "females": f"مسيرات {arabic_label}",
        }
        result[f"{lowered_job_key} sports-people"] = {
            "males": f"رياضيو {arabic_label}",
            "females": f"رياضيات {arabic_label}",
        }
        for football_key, football_labels in football_roles.items():
            lowered_football_key = football_key.lower()

            olympic_key = f"olympic {lowered_job_key} {lowered_football_key}"
            result[olympic_key] = {
                "males": combine_gender_labels(football_labels["males"], f"{arabic_label} أولمبيون"),
                "females": combine_gender_labels(football_labels["females"], f"{arabic_label} أولمبيات"),
            }

            mens_key = f"men's {lowered_job_key} {lowered_football_key}"
            result[mens_key] = {
                "males": combine_gender_labels(football_labels["males"], f"{arabic_label} رجالية"),
                "females": "",
            }

            composite_key = f"{lowered_job_key} {lowered_football_key}"
            result[composite_key] = {
                "males": combine_gender_labels(football_labels["males"], arabic_label),
                "females": combine_gender_labels(football_labels["females"], arabic_label),
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

FOOTBALL_KEYS_PLAYERS: GenderedLabelMap = open_json_file("jobs/jobs_Football_Keys_players.json") or {}

JOBS_PLAYERS: GenderedLabelMap = open_json_file("jobs/Jobs_players.json") or {}

JOBS_PLAYERS.setdefault("freestyle swimmers", {"males": "سباحو تزلج حر", "females": "سباحات تزلج حر"})

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

# SPORT_JOB_VARIANTS = _build_sports_job_variants(SPORTS_KEYS_FOR_JOBS, FOOTBALL_KEYS_PLAYERS)
SPORT_JOB_VARIANTS = open_json_file("SPORT_JOB_VARIANTS_found.json") or {}

SPORT_JOB_VARIANTS.update(
    {
        "sports executives": {"males": "مسيرو رياضية", "females": "مسيرات رياضية"},
        "sports coaches": {"males": "مدربو رياضية", "females": "مدربات رياضية"},
        "sports journalists": {"males": "صحفيو رياضية", "females": "صحفيات رياضية"},
        "sports biography": {"males": "أعلام رياضة", "females": ""},
        "sports players": {"males": "لاعبو رياضية", "females": "لاعبات رياضية"},
        "sports managers": {"males": "مدربو رياضية", "females": "مدربات رياضية"},
        "sports announcers": {"males": "مذيعو رياضية", "females": "مذيعات رياضية"},
        "sports referees": {"males": "حكام رياضية", "females": "حكمات رياضية"},
        "sports scouts": {"males": "كشافة رياضية", "females": "كشافة رياضية"},
    }
)

SPORT_JOB_VARIANTS_additional = {
    "canadian football players": {"males": "لاعبو كرة قدم كندية", "females": "لاعبات كرة قدم كندية"},
    "canadian football biography": {"males": "أعلام كرة قدم كندية", "females": ""},
    "canadian football centres": {"males": "لاعبو وسط كرة قدم كندية", "females": "لاعبات وسط كرة قدم كندية"},
    "canadian football defensive backs": {
        "males": "مدافعون خلفيون كرة قدم كندية",
        "females": "مدافعات خلفيات كرة قدم كندية",
    },
    "canadian football defensive linemen": {"males": "مدافعو خط كرة قدم كندية", "females": "مدافعات خط كرة قدم كندية"},
    "canadian football fullbacks": {"males": "مدافعو كرة قدم كندية", "females": "مدافعات كرة قدم كندية"},
    "canadian football guards": {"males": "حراس كرة قدم كندية", "females": "حراس كرة قدم كندية"},
    "canadian football linebackers": {"males": "أظهرة كرة قدم كندية", "females": "ظهيرات كرة قدم كندية"},
    "canadian football offensive linemen": {"males": "مهاجمو خط كرة قدم كندية", "females": "مهاجمات خط كرة قدم كندية"},
    "canadian football placekickers": {"males": "مسددو كرة قدم كندية", "females": "مسددات كرة قدم كندية"},
    "canadian football quarterbacks": {
        "males": "أظهرة رباعيون كرة قدم كندية",
        "females": "ظهيرات رباعيات كرة قدم كندية",
    },
    "canadian football running backs": {"males": "راكضون للخلف كرة قدم كندية", "females": "راكضات للخلف كرة قدم كندية"},
    "canadian football scouts": {"males": "كشافة كرة قدم كندية", "females": "كشافة كرة قدم كندية"},
    "canadian football tackles": {"males": "مصطدمو كرة قدم كندية", "females": "مصطدمات كرة قدم كندية"},
    "canadian football wide receivers": {
        "males": "مستقبلون واسعون كرة قدم كندية",
        "females": "مستقبلات واسعات كرة قدم كندية",
    },
}

SPORT_JOB_VARIANTS.update(SPORT_JOB_VARIANTS_additional)

PLAYERS_TO_MEN_WOMENS_JOBS = _merge_maps(
    STATIC_PLAYER_LABELS,
    TEAM_SPORT_LABELS,
    SKATING_LABELS,
    BOXING_LABELS,
    GENERAL_SCOPE_LABELS,
    CHAMPION_LABELS,
    WORLD_CHAMPION_LABELS,
    # SPORT_JOB_VARIANTS,
    BASE_PLAYER_VARIANTS,
)

__all__ = [
    "FOOTBALL_KEYS_PLAYERS",
    "JOBS_PLAYERS",
    "PLAYERS_TO_MEN_WOMENS_JOBS",
]

len_print.data_len(
    "jobs_players_list.py",
    {
        "PLAYERS_TO_MEN_WOMENS_JOBS": PLAYERS_TO_MEN_WOMENS_JOBS,  # 1,345
        "SPORT_JOB_VARIANTS": SPORT_JOB_VARIANTS,  # 61,919
        "BASE_PLAYER_VARIANTS": BASE_PLAYER_VARIANTS,  # 435
        "WORLD_CHAMPION_LABELS": WORLD_CHAMPION_LABELS,  # 431
        "CHAMPION_LABELS": CHAMPION_LABELS,  # 434
        "GENERAL_SCOPE_LABELS": GENERAL_SCOPE_LABELS,  # 9
        "STATIC_PLAYER_LABELS": STATIC_PLAYER_LABELS,  # 4
        "BOXING_LABELS": BOXING_LABELS,  # 42
        "TEAM_SPORT_LABELS": TEAM_SPORT_LABELS,  # 31
        "SKATING_LABELS": SKATING_LABELS,  # 4
        "FOOTBALL_KEYS_PLAYERS": FOOTBALL_KEYS_PLAYERS,  # 46
        "JOBS_PLAYERS": JOBS_PLAYERS,  # 145
    },
)
