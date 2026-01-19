#!/usr/bin/python3
""" """

import functools

from ....helps import logger
from ....translations.sports.Sport_key import (
    SPORTS_KEYS_FOR_TEAM,
)
from ....translations_formats import FormatData
from .data import teams_formatted_data


@functools.lru_cache(maxsize=1)
def _load_teams_bot() -> FormatData:
    return FormatData(
        teams_formatted_data,
        SPORTS_KEYS_FOR_TEAM,
        key_placeholder="{en_sport}",
        value_placeholder="{sport_team}",
    )


@functools.lru_cache(maxsize=None)
def resolve_sport_label_by_teams_key(category: str, default: str = "") -> str:
    """Search for a team-related label, returning ``default`` when missing."""
    category = category.replace("championships", "championship")
    teams_bot = _load_teams_bot()
    result = teams_bot.search(category) or default
    logger.info_if_or_debug(f"<<yellow>> end resolve_sport_label_by_teams_key: {category=}, {result=}", result)
    return result


__all__ = [
    "resolve_sport_label_by_teams_key",
]
