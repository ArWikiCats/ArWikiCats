#!/usr/bin/python3
""" """

import functools

from ....helps import logger
from ....translations.sports.Sport_key import (
    SPORTS_KEYS_FOR_TEAM,
)
from ....translations_formats import FormatData

teams_formatted_data = {
    "amateur {en_sport} world cup": "كأس العالم {sport_team} للهواة",
    "mens {en_sport} world cup": "كأس العالم {sport_team} للرجال",
    "womens {en_sport} world cup": "كأس العالم {sport_team} للسيدات",
    "{en_sport} world cup": "كأس العالم {sport_team}",
    "youth {en_sport} world cup": "كأس العالم {sport_team} للشباب",
    "international {en_sport} council": "المجلس الدولي {sport_team}",
    "mens {en_sport} championship": "بطولة {sport_team} للرجال",
    "mens {en_sport} world championship": "بطولة العالم {sport_team} للرجال",
    "outdoor world {en_sport} championship": "بطولة العالم {sport_team} في الهواء الطلق",
    "womens world {en_sport} championship": "بطولة العالم {sport_team} للسيدات",
    "womens {en_sport} championship": "بطولة {sport_team} للسيدات",
    "womens {en_sport} world championship": "بطولة العالم {sport_team} للسيدات",
    "world amateur {en_sport} championship": "بطولة العالم {sport_team} للهواة",
    "world champion national {en_sport} teams": "أبطال بطولة العالم {sport_team}",
    "world junior {en_sport} championship": "بطولة العالم {sport_team} للناشئين",
    "world outdoor {en_sport} championship": "بطولة العالم {sport_team} في الهواء الطلق",
    "world wheelchair {en_sport} championship": "بطولة العالم {sport_team} على الكراسي المتحركة",
    "world {en_sport} amateur championship": "بطولة العالم {sport_team} للهواة",
    "world {en_sport} championship": "بطولة العالم {sport_team}",
    "world {en_sport} championship competitors": "منافسو بطولة العالم {sport_team}",
    "world {en_sport} championship medalists": "فائزون بميداليات بطولة العالم {sport_team}",
    "world {en_sport} junior championship": "بطولة العالم {sport_team} للناشئين",
    "world {en_sport} youth championship": "بطولة العالم {sport_team} للشباب",
    "world youth {en_sport} championship": "بطولة العالم {sport_team} للشباب",
    "{en_sport} amateur world championship": "بطولة العالم {sport_team} للهواة",
    "{en_sport} junior world championship": "بطولة العالم {sport_team} للناشئين",
    "{en_sport} world amateur championship": "بطولة العالم {sport_team} للهواة",
    "{en_sport} world championship": "بطولة العالم {sport_team}",
    "{en_sport} world junior championship": "بطولة العالم {sport_team} للناشئين",
    "{en_sport} world youth championship": "بطولة العالم {sport_team} للشباب",
    "{en_sport} youth world championship": "بطولة العالم {sport_team} للشباب",
    # world championships in athletics
    "world championship in {en_sport}": "بطولة العالم {sport_team}",
    "world championship in {en_sport} athletes": "عداؤو بطولة العالم {sport_team}",
}


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
