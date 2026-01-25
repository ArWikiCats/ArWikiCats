"""Utilities for gendered Arabic player labels and related helpers.

The legacy implementation of this module relied on a large, mutable script that
loaded JSON dictionaries and updated them in place.  The refactor exposes typed
constants and helper functions that retain the original Arabic content while
being easier to reason about and test.
"""

from __future__ import annotations

from typing import Mapping

from ..helps import len_print
from ..data_builders.build_jobs_players_list import (
    _build_boxing_labels,
    _build_champion_labels,
    _build_general_scope_labels,
    _build_jobs_player_variants,
    _build_skating_labels,
    _build_team_sport_labels,
    _build_world_champion_labels,
    _merge_maps,
)
from ..data_builders.jobs_defs import GenderedLabel, GenderedLabelMap
from ..sports import SPORTS_KEYS_FOR_LABEL, SPORTS_KEYS_FOR_TEAM
from ..utils import open_json_file

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


SPORT_JOB_VARIANTS_additional = {
    "sports executives": {"males": "مسيرو رياضية", "females": "مسيرات رياضية"},
    "sports coaches": {"males": "مدربو رياضية", "females": "مدربات رياضية"},
    "sports journalists": {"males": "صحفيو رياضية", "females": "صحفيات رياضية"},
    "sports biography": {"males": "أعلام رياضة", "females": ""},
    "sports players": {"males": "لاعبو رياضية", "females": "لاعبات رياضية"},
    "sports managers": {"males": "مدربو رياضية", "females": "مدربات رياضية"},
    "sports announcers": {"males": "مذيعو رياضية", "females": "مذيعات رياضية"},
    "sports referees": {"males": "حكام رياضية", "females": "حكمات رياضية"},
    "sports scouts": {"males": "كشافة رياضية", "females": "كشافة رياضية"},
    "canadian football players": {
        "males": "لاعبو كرة قدم كندية",
        "females": "لاعبات كرة قدم كندية",
    },
    "canadian football biography": {"males": "أعلام كرة قدم كندية", "females": ""},
    "canadian football centres": {
        "males": "لاعبو وسط كرة قدم كندية",
        "females": "لاعبات وسط كرة قدم كندية",
    },
    "canadian football defensive backs": {
        "males": "مدافعون خلفيون كرة قدم كندية",
        "females": "مدافعات خلفيات كرة قدم كندية",
    },
    "canadian football defensive linemen": {
        "males": "مدافعو خط كرة قدم كندية",
        "females": "مدافعات خط كرة قدم كندية",
    },
    "canadian football fullbacks": {
        "males": "مدافعو كرة قدم كندية",
        "females": "مدافعات كرة قدم كندية",
    },
    "canadian football guards": {"males": "حراس كرة قدم كندية", "females": "حراس كرة قدم كندية"},
    "canadian football linebackers": {
        "males": "أظهرة كرة قدم كندية",
        "females": "ظهيرات كرة قدم كندية",
    },
    "canadian football offensive linemen": {
        "males": "مهاجمو خط كرة قدم كندية",
        "females": "مهاجمات خط كرة قدم كندية",
    },
    "canadian football placekickers": {
        "males": "مسددو كرة قدم كندية",
        "females": "مسددات كرة قدم كندية",
    },
    "canadian football quarterbacks": {
        "males": "أظهرة رباعيون كرة قدم كندية",
        "females": "ظهيرات رباعيات كرة قدم كندية",
    },
    "canadian football running backs": {
        "males": "راكضون للخلف كرة قدم كندية",
        "females": "راكضات للخلف كرة قدم كندية",
    },
    "canadian football scouts": {"males": "كشافة كرة قدم كندية", "females": "كشافة كرة قدم كندية"},
    "canadian football tackles": {
        "males": "مصطدمو كرة قدم كندية",
        "females": "مصطدمات كرة قدم كندية",
    },
    "canadian football wide receivers": {
        "males": "مستقبلون واسعون كرة قدم كندية",
        "females": "مستقبلات واسعات كرة قدم كندية",
    },
}

# ---------------------------------------------------------------------------
# Data assembly

# SPORT_JOB_VARIANTS = _build_sports_job_variants(SPORTS_KEYS_FOR_JOBS, FOOTBALL_KEYS_PLAYERS)
SPORT_JOB_VARIANTS = open_json_file("SPORT_JOB_VARIANTS_found.json") or {}
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

SPORT_JOB_VARIANTS.update(SPORT_JOB_VARIANTS_additional)

# TODO: these 2 should be removed
CHAMPION_LABELS = _build_champion_labels(SPORTS_KEYS_FOR_LABEL)
WORLD_CHAMPION_LABELS = _build_world_champion_labels(SPORTS_KEYS_FOR_TEAM)


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
