#!/usr/bin/python3
""" """

import functools

from ....helps import logger
from ....new.handle_suffixes import resolve_sport_category_suffix_with_mapping
from .raw_sports_jobs_key import resolve_sport_label_by_jobs_key
from .raw_sports_teams_key import resolve_sport_label_by_teams_key
from .raw_sports_labels_key import resolve_sport_label_by_labels_key


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
def wrap_team_xo_normal_2025(team: str) -> str:
    """Normalize a team string and resolve it via the available sports bots."""
    team = team.lower().replace("category:", "")
    logger.debug(f"<<yellow>> start wrap_team_xo_normal_2025: {team=}")

    result = (
        ""
        or resolve_sport_label_by_labels_key(team)
        or resolve_sport_label_by_teams_key(team)
        or resolve_sport_label_by_jobs_key(team)
        or ""
    )

    logger.info_if_or_debug(f"<<yellow>> end wrap_team_xo_normal_2025: {team=}, {result=}", result)
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
    "resolve_sport_label_by_teams_key",
    "resolve_sport_label_by_jobs_key",
    "wrap_team_xo_normal_2025_with_ends",
]
