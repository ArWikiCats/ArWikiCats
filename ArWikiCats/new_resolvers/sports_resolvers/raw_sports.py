#!/usr/bin/python3
"""
"""

import functools

from ...helps import len_print, logger

# from ...helps.jsonl_dump import dump_data
from ...new.handle_suffixes import resolve_sport_category_suffix_with_mapping
from ...translations.sports.Sport_key import (
    SPORTS_KEYS_FOR_JOBS,
    SPORTS_KEYS_FOR_LABEL,
    SPORTS_KEYS_FOR_TEAM,
)
from ...translations_formats import FormatData
from .sport_lab2_data import jobs_formatted_data, labels_formatted_data, teams_formatted_data

labels_bot = FormatData(
    labels_formatted_data,
    SPORTS_KEYS_FOR_LABEL,
    key_placeholder="{en_sport}",
    value_placeholder="{sport_label}",
)
teams_bot = FormatData(
    teams_formatted_data,
    SPORTS_KEYS_FOR_TEAM,
    key_placeholder="{en_sport}",
    value_placeholder="{sport_team}",
)
jobs_bot = FormatData(
    jobs_formatted_data,
    SPORTS_KEYS_FOR_JOBS,
    key_placeholder="{en_sport}",
    value_placeholder="{sport_jobs}",
)


@functools.lru_cache(maxsize=1)
def _get_sorted_teams_labels() -> dict[str, str]:
    mappings_data = {
        "records and statistics": "سجلات وإحصائيات",
        "finals": "نهائيات",
        "matches": "مباريات",
        "manager history": "تاريخ مدربو",
        "tournaments": "بطولات",
        "leagues": "دوريات",
        "coaches": "مدربو",
        "clubs and teams": "أندية وفرق",
        "clubs": "أندية",
        "competitions": "منافسات",
        "chairmen and investors": "رؤساء ومسيرو",
        "cups": "كؤوس",
    }

    mappings_data = dict(
        sorted(
            mappings_data.items(),
            key=lambda k: (-k[0].count(" "), -len(k[0])),
        )
    )
    return mappings_data


def fix_result_callable(result: str, category: str, key: str, value: str) -> str:
    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    if key == "teams" and "national" in category:
        result = result.replace("فرق ", "منتخبات ")

    return result


@functools.lru_cache(maxsize=None)
def find_labels_bot(category: str, default: str = "") -> str:
    """Search for a generic sports label, returning ``default`` when missing."""
    return labels_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def find_teams_bot(category: str, default: str = "") -> str:
    """Search for a team-related label, returning ``default`` when missing."""
    category = category.replace("championships", "championship")
    return teams_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def find_jobs_bot(category: str, default: str = "") -> str:
    """Search for a job-related sports label, returning ``default`` when missing."""
    return jobs_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def wrap_team_xo_normal_2025(team: str) -> str:
    """Normalize a team string and resolve it via the available sports bots."""
    team = team.lower().replace("category:", "")
    result = find_labels_bot(team) or find_teams_bot(team) or find_jobs_bot(team) or ""
    return result.strip()


@functools.lru_cache(maxsize=10000)
def fix_keys(category: str) -> str:
    category = category.replace("'", "").lower().replace("category:", "")

    return category.strip()


def wrap_team_xo_normal_2025_with_ends(category, callback=wrap_team_xo_normal_2025) -> str:
    category = fix_keys(category)
    logger.debug(f"<<yellow>> start wrap_team_xo_normal_2025_with_ends: {category=}")
    teams_label_mappings_ends = _get_sorted_teams_labels()

    result = callback(category)

    if not result:
        result = resolve_sport_category_suffix_with_mapping(
            category=category,
            data=teams_label_mappings_ends,
            callback=callback,
            fix_result_callable=fix_result_callable,
        )

    logger.info_if_or_debug(f"<<yellow>> end wrap_team_xo_normal_2025_with_ends: {category=}, {result=}", result)
    return result


__all__ = [
    "wrap_team_xo_normal_2025",
    "find_labels_bot",
    "find_teams_bot",
    "find_jobs_bot",
    "wrap_team_xo_normal_2025_with_ends",
]
