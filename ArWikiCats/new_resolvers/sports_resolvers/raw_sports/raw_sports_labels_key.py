#!/usr/bin/python3
""" """

import functools

from ....helps import logger
from ....translations.sports.Sport_key import (
    SPORTS_KEYS_FOR_LABEL,
)
from ....translations_formats import FormatData
from .data import labels_formatted_data


@functools.lru_cache(maxsize=1)
def _load_labels_bot() -> FormatData:
    return FormatData(
        labels_formatted_data,
        SPORTS_KEYS_FOR_LABEL,
        key_placeholder="{en_sport}",
        value_placeholder="{sport_label}",
    )


@functools.lru_cache(maxsize=None)
def resolve_sport_label_by_labels_key(category: str, default: str = "") -> str:
    """Search for a team-related label, returning ``default`` when missing."""
    category = category.replace("championships", "championship")
    labels_bot = _load_labels_bot()
    result = labels_bot.search(category) or default
    logger.info_if_or_debug(f"<<yellow>> end resolve_sport_label_by_labels_key: {category=}, {result=}", result)
    return result


__all__ = [
    "resolve_sport_label_by_labels_key",
]
