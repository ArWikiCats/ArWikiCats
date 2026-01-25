"""Utilities for gendered Arabic player labels and related helpers.

The legacy implementation of this module relied on a large, mutable script that
loaded JSON dictionaries and updated them in place.  The refactor exposes typed
constants and helper functions that retain the original Arabic content while
being easier to reason about and test.
"""

from __future__ import annotations

from typing import Dict, Mapping

from .jobs_defs import GenderedLabel, GenderedLabelMap, combine_gender_labels

# ---------------------------------------------------------------------------
# Builders


def _build_boxing_labels(weights: Mapping[str, str]) -> GenderedLabelMap:
    """
    Builds gendered Arabic labels for boxing weight-class keys.

    Generates two entries per weight when an Arabic label is provided:
    - "<weight> boxers": both "males" and "females" Arabic forms.
    - "world <weight> boxing champions": masculine Arabic form in "males" and an empty string in "females".

    Parameters:
        weights (Mapping[str, str]): Mapping from English weight-key to Arabic label. Entries with an empty Arabic label are skipped.

    Returns:
        GenderedLabelMap: Mapping of label keys to dicts with "males" and "females" Arabic strings as described above.
    """

    result: GenderedLabelMap = {}

    for weight_key, arabic_label in weights.items():
        if not arabic_label:
            continue
        weight_boxers_key = f"{weight_key} boxers"
        result[weight_boxers_key] = {
            "males": f"ملاكمو {arabic_label}",
            "females": f"ملاكمات {arabic_label}",
        }
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
    """
    Create lowercase keys and scoped variants for a base mapping of player labels.

    Generates a new mapping that includes:
    - a lowercase-normalized entry for each input key,
    - an "olympic <key>" variant with gendered Olympic forms,
    - an "international <key>" variant with gendered international forms.
    Entries whose male and female labels are both empty are omitted.

    Parameters:
        players (Mapping[str, GenderedLabel]): Base mapping from English keys to gendered Arabic labels.

    Returns:
        GenderedLabelMap: A mapping containing lowercase keys and added "olympic" and "international" variants with corresponding gendered labels.
    """

    result: GenderedLabelMap = {}
    for english_key, labels in players.items():
        mens_label = labels.get("males", "")
        womens_label = labels.get("females", "")

        if not (mens_label or womens_label):
            continue

        lowered_key = english_key.lower()
        result[lowered_key] = {"males": mens_label, "females": womens_label}

        result[f"olympic {lowered_key}"] = {
            "males": f"{mens_label} أولمبيون",
            "females": f"{womens_label} أولمبيات",
        }
        result[f"international {lowered_key}"] = {
            "males": f"{mens_label} دوليون",
            "females": f"{womens_label} دوليات",
        }

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
            "males": f"أبطال العالم {arabic_label}",
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


__all__ = [
    "_build_boxing_labels",
    "_build_skating_labels",
    "_build_team_sport_labels",
    "_build_jobs_player_variants",
    "_build_general_scope_labels",
    "_build_champion_labels",
    "_build_world_champion_labels",
    "_build_sports_job_variants",
    "_merge_maps",
]
