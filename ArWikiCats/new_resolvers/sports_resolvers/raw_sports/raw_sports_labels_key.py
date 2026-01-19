#!/usr/bin/python3
""" """

import functools

from ....helps import logger
from ....translations.sports.Sport_key import (
    SPORTS_KEYS_FOR_LABEL,
)
from ....translations_formats import FormatData

labels_formatted_data = {
    "{en_sport}": "{sport_label}",
    "{en_sport} finals": "نهائيات {sport_label}",
    "olympic gold medalists in {en_sport}": "فائزون بميداليات ذهبية أولمبية في {sport_label}",
    "olympic silver medalists in {en_sport}": "فائزون بميداليات فضية أولمبية في {sport_label}",
    "olympic bronze medalists in {en_sport}": "فائزون بميداليات برونزية أولمبية في {sport_label}",
    "{en_sport} league": "دوري {sport_label}",
    "{en_sport} champions": "أبطال {sport_label}",
    "olympics {en_sport}": "{sport_label} في الألعاب الأولمبية",
    "summer olympics {en_sport}": "{sport_label} في الألعاب الأولمبية الصيفية",
    "winter olympics {en_sport}": "{sport_label} في الألعاب الأولمبية الشتوية",
}


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
