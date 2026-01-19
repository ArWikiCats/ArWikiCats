#!/usr/bin/python3
""" """

import functools

from ....helps import logger
from ....translations.sports.Sport_key import (
    SPORTS_KEYS_FOR_JOBS,
)
from ....translations_formats import FormatData
from .data import jobs_formatted_data


@functools.lru_cache(maxsize=1)
def _load_bot() -> FormatData:
    return FormatData(
        jobs_formatted_data,
        SPORTS_KEYS_FOR_JOBS,
        key_placeholder="{en_sport}",
        value_placeholder="{sport_jobs}",
    )


@functools.lru_cache(maxsize=None)
def resolve_sport_label_by_jobs_key(category: str, default: str = "") -> str:
    """Search for a job-related sports label, returning ``default`` when missing."""
    jobs_bot = _load_bot()
    result = jobs_bot.search(category) or default
    logger.info_if_or_debug(f"<<yellow>> end resolve_sport_label_by_jobs_key: {category=}, {result=}", result)
    return result


__all__ = [
    "resolve_sport_label_by_jobs_key",
]
