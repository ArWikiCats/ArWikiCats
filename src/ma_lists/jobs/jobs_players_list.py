"""Utilities for gendered Arabic player labels and related helpers.

The legacy implementation of this module relied on a large, mutable script that
loaded JSON dictionaries and updated them in place.  The refactor exposes typed
constants and helper functions that retain the original Arabic content while
being easier to reason about and test.
"""

from __future__ import annotations

from typing import Dict, Mapping

from ..sports.Sport_key import (
    Sports_Keys_For_Jobs,
    Sports_Keys_For_Label,
    Sports_Keys_For_Team,
)
from .jobs_defs import (
    GenderedLabel,
    GenderedLabelMap,
    gendered_label,
    join_terms,
    load_gendered_label_map,
)

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

SKATING_DISCIPLINE_LABELS: Mapping[str, GenderedLabel] = {
    "nordic combined": gendered_label("تزلج نوردي مزدوج", "تزل نوردي مزدوج"),
    "speed": gendered_label("سرعة", "سرعة"),
    "roller": gendered_label("بالعجلات", "بالعجلات"),
    "alpine": gendered_label("منحدرات ثلجية", "منحدرات ثلجية"),
    "short track speed": gendered_label("مسار قصير", "مسار قصير"),
}

TEAM_SPORT_TRANSLATIONS: Mapping[str, str] = {
    "croquet players": "",
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
    "managers": gendered_label("مدربون", "مدربات"),
    "competitors": gendered_label("منافسون", "منافسات"),
    "coaches": gendered_label("مدربون", "مدربات"),
}

SPORT_SCOPE_ROLES: Mapping[str, GenderedLabel] = {
    "paralympic": gendered_label("بارالمبيون", "بارالمبيات"),
    "olympics": gendered_label("أولمبيون", "أولمبيات"),
    "sports": gendered_label("رياضيون", "رياضيات"),
}

STATIC_PLAYER_LABELS: GenderedLabelMap = {
    "national team coaches": gendered_label("مدربو فرق وطنية", "مدربات فرق وطنية"),
    "national team managers": gendered_label("مدربو فرق وطنية", "مدربات فرق وطنية"),
    "sports agents": gendered_label("وكلاء رياضات", "وكيلات رياضات"),
    "expatriate sprtspeople": gendered_label("رياضيون مغتربون", "رياضيات مغتربات"),
    "expatriate sportspeople": gendered_label("رياضيون مغتربون", "رياضيات مغتربات"),
}

FREESTYLE_SWIMMERS_LABEL: GenderedLabel = gendered_label(
    "سباحو تزلج حر", "سباحات تزلج حر"
)

# ---------------------------------------------------------------------------
# Builders


def _build_boxing_labels(weights: Mapping[str, str]) -> GenderedLabelMap:
    """Return gendered labels for boxing weight classes."""

    result: GenderedLabelMap = {}
    for weight_key, arabic_label in weights.items():
        if not arabic_label:
            continue
        weight_boxers_key = f"{weight_key} boxers"
        result[weight_boxers_key] = gendered_label(
            join_terms("ملاكمو", arabic_label),
            join_terms("ملاكمات", arabic_label),
        )
        result[f"world {weight_key} boxing champions"] = gendered_label(
            join_terms("أبطال العالم للملاكمة فئة", arabic_label),
            "",
        )
    return result


def _build_skating_labels(labels: Mapping[str, GenderedLabel]) -> GenderedLabelMap:
    """Create labels for skating and skiing disciplines."""

    result: GenderedLabelMap = {}
    for discipline_key, discipline_labels in labels.items():
        result[f"{discipline_key} skaters"] = gendered_label(
            join_terms("متزلجو", discipline_labels["mens"]),
            join_terms("متزلجات", discipline_labels["womens"]),
        )
        result[f"{discipline_key} skiers"] = gendered_label(
            join_terms("متزحلقو", discipline_labels["mens"]),
            join_terms("متزحلقات", discipline_labels["womens"]),
        )
    return result


def _build_team_sport_labels(translations: Mapping[str, str]) -> GenderedLabelMap:
    """Translate team sport categories into gendered Arabic labels."""

    result: GenderedLabelMap = {}
    for english_key, arabic_value in translations.items():
        if not arabic_value:
            continue
        result[english_key] = gendered_label(
            join_terms("لاعبو", arabic_value),
            join_terms("لاعبات", arabic_value),
        )
    return result


def _build_jobs_player_variants(players: Mapping[str, GenderedLabel]) -> GenderedLabelMap:
    """Generate derivative labels for the base player dataset."""

    result: GenderedLabelMap = {}
    for english_key, labels in players.items():
        mens_label = labels.get("mens", "")
        womens_label = labels.get("womens", "")
        if not (mens_label or womens_label):
            continue
        lowered_key = english_key.lower()
        result[lowered_key] = gendered_label(mens_label, womens_label)
        result[f"olympic {lowered_key}"] = gendered_label(
            join_terms(mens_label, "أولمبيون"),
            join_terms(womens_label, "أولمبيات"),
        )
        result[f"international {lowered_key}"] = gendered_label(
            join_terms(mens_label, "دوليون"),
            join_terms(womens_label, "دوليات"),
        )
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
            result[composite_key] = gendered_label(
                join_terms(role_labels["mens"], scope_labels["mens"]),
                join_terms(role_labels["womens"], scope_labels["womens"]),
            )
    return result


def _build_champion_labels(labels: Mapping[str, str]) -> GenderedLabelMap:
    """Create champion labels from the sport label mapping."""

    result: GenderedLabelMap = {}
    for sport_key, arabic_label in labels.items():
        composite_key = f"{sport_key.lower()} champions"
        result[composite_key] = gendered_label(
            join_terms("أبطال", arabic_label),
            "",
        )
    return result


def _build_world_champion_labels(labels: Mapping[str, str]) -> GenderedLabelMap:
    """Create world champion labels from team descriptors."""

    result: GenderedLabelMap = {}
    for sport_key, arabic_label in labels.items():
        composite_key = f"world {sport_key.lower()} champions"
        result[composite_key] = gendered_label(
            join_terms("أبطال العالم", arabic_label),
            "",
        )
    return result


def _build_sports_job_variants(
    sport_jobs: Mapping[str, str],
    football_roles: Mapping[str, GenderedLabel],
) -> tuple[GenderedLabelMap, Dict[str, str]]:
    """Create commentators, announcers, and other job variants."""

    result: GenderedLabelMap = {}
    female_aliases: Dict[str, str] = {}

    for job_key, arabic_label in sport_jobs.items():
        lowered_job_key = job_key.lower()
        result[f"{lowered_job_key} biography"] = gendered_label(
            join_terms("أعلام", arabic_label),
            "",
        )
        result[f"{lowered_job_key} commentators"] = gendered_label(
            join_terms("معلقو", arabic_label),
            join_terms("معلقات", arabic_label),
        )
        result[f"{lowered_job_key} announcers"] = gendered_label(
            join_terms("مذيعو", arabic_label),
            join_terms("مذيعات", arabic_label),
        )
        result[f"{lowered_job_key} stage winners"] = gendered_label(
            join_terms("فائزون في مراحل", arabic_label),
            join_terms("فائزات في مراحل", arabic_label),
        )
        result[f"{lowered_job_key} coaches"] = gendered_label(
            join_terms("مدربو", arabic_label),
            join_terms("مدربات", arabic_label),
        )
        result[f"{lowered_job_key} executives"] = gendered_label(
            join_terms("مسيرو", arabic_label),
            join_terms("مسيرات", arabic_label),
        )
        result[f"{lowered_job_key} sprtspeople"] = gendered_label(
            join_terms("رياضيو", arabic_label),
            join_terms("رياضيات", arabic_label),
        )
        result[f"{lowered_job_key} sportspeople"] = gendered_label(
            join_terms("رياضيو", arabic_label),
            join_terms("رياضيات", arabic_label),
        )

        # Provide a category entry for women's players to preserve the legacy API.
        female_aliases[f"women's {lowered_job_key} players"] = join_terms(
            "لاعبات", arabic_label, "نسائية"
        )

        for football_key, football_labels in football_roles.items():
            lowered_football_key = football_key.lower()
            olympic_key = f"olympic {lowered_job_key} {lowered_football_key}"
            result[olympic_key] = gendered_label(
                join_terms(football_labels["mens"], arabic_label, "أولمبيون"),
                join_terms(football_labels["womens"], arabic_label, "أولمبيات"),
            )

            mens_category = join_terms(football_labels["mens"], arabic_label, "رجالية")
            # When a feminine variant is not provided we reuse the masculine form
            # to match the historical dataset behaviour.
            womens_category = football_labels["womens"] or football_labels["mens"]
            womens_category = join_terms(womens_category, arabic_label, "رجالية")
            mens_key = f"men's {lowered_job_key} {lowered_football_key}"
            result[mens_key] = gendered_label(mens_category, womens_category)

            composite_key = f"{lowered_job_key} {lowered_football_key}"
            result[composite_key] = gendered_label(
                join_terms(football_labels["mens"], arabic_label),
                join_terms(football_labels["womens"], arabic_label),
            )

    return result, female_aliases


def _merge_maps(*maps: Mapping[str, GenderedLabel]) -> GenderedLabelMap:
    """Merge multiple :class:`GenderedLabelMap` instances."""

    merged: GenderedLabelMap = {}
    for source in maps:
        merged.update(source)
    return merged


# ---------------------------------------------------------------------------
# Data assembly

FOOTBALL_KEYS_PLAYERS: GenderedLabelMap = load_gendered_label_map(
    "jobs_Football_Keys_players"
)
JOBS_PLAYERS: GenderedLabelMap = load_gendered_label_map("Jobs_players")
JOBS_PLAYERS.setdefault("freestyle swimmers", FREESTYLE_SWIMMERS_LABEL)

BASE_PLAYER_VARIANTS = _build_jobs_player_variants(JOBS_PLAYERS)
SKATING_LABELS = {
    key: value
    for key, value in _build_skating_labels(SKATING_DISCIPLINE_LABELS).items()
    if key not in BASE_PLAYER_VARIANTS
}
TEAM_SPORT_LABELS = _build_team_sport_labels(TEAM_SPORT_TRANSLATIONS)
BOXING_LABELS = _build_boxing_labels(BOXING_WEIGHT_TRANSLATIONS)
GENERAL_SCOPE_LABELS = _build_general_scope_labels(GENERAL_SPORT_ROLES, SPORT_SCOPE_ROLES)
CHAMPION_LABELS = _build_champion_labels(Sports_Keys_For_Label)
WORLD_CHAMPION_LABELS = _build_world_champion_labels(Sports_Keys_For_Team)
SPORT_JOB_VARIANTS, FEMALE_JOBS_TO = _build_sports_job_variants(
    Sports_Keys_For_Jobs,
    FOOTBALL_KEYS_PLAYERS,
)

PLAYERS_TO_MEN_WOMENS_JOBS: GenderedLabelMap = _merge_maps(
    TEAM_SPORT_LABELS,
    SKATING_LABELS,
    BOXING_LABELS,
    GENERAL_SCOPE_LABELS,
    CHAMPION_LABELS,
    WORLD_CHAMPION_LABELS,
    SPORT_JOB_VARIANTS,
    BASE_PLAYER_VARIANTS,
    STATIC_PLAYER_LABELS,
)

# ---------------------------------------------------------------------------
# Backwards compatible exports

Jobs_players: GenderedLabelMap = JOBS_PLAYERS
Football_Keys_players: GenderedLabelMap = FOOTBALL_KEYS_PLAYERS
players_to_Men_Womens_Jobs: GenderedLabelMap = PLAYERS_TO_MEN_WOMENS_JOBS
Female_Jobs_to: Dict[str, str] = FEMALE_JOBS_TO

__all__ = [
    "BOXING_LABELS",
    "BOXING_WEIGHT_TRANSLATIONS",
    "FEMALE_JOBS_TO",
    "FOOTBALL_KEYS_PLAYERS",
    "GENERAL_SCOPE_LABELS",
    "GENERAL_SPORT_ROLES",
    "JOBS_PLAYERS",
    "PLAYERS_TO_MEN_WOMENS_JOBS",
    "SKATING_DISCIPLINE_LABELS",
    "SKATING_LABELS",
    "SPORT_SCOPE_ROLES",
    "SPORT_JOB_VARIANTS",
    "STATIC_PLAYER_LABELS",
    "TEAM_SPORT_LABELS",
    "TEAM_SPORT_TRANSLATIONS",
    "WORLD_CHAMPION_LABELS",
    # Backwards compatible exports
    "Football_Keys_players",
    "Jobs_players",
    "Female_Jobs_to",
    "players_to_Men_Womens_Jobs",
]
