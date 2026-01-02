#!/usr/bin/python3
""" """

import functools
import re

from ...helps import logger
from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS

Sports_Keys_For_Jobs_simple = {
    "wheelchair automobile racing": "سباق سيارات على كراسي متحركة",
    "gaelic football racing": "سباق كرة قدم غالية",
    "wheelchair gaelic football": "كرة قدم غالية على كراسي متحركة",
    "kick boxing racing": "سباق كيك بوكسينغ",
    "wheelchair kick boxing": "كيك بوكسينغ على كراسي متحركة",
    "sport climbing racing": "سباق تسلق",
    "wheelchair sport climbing": "تسلق على كراسي متحركة",
    "aquatic sports racing": "سباق رياضات مائية",
    "wheelchair aquatic sports": "رياضات مائية على كراسي متحركة",
    "shooting": "رماية",
    "shooting racing": "سباق رماية",
    "wheelchair shooting": "رماية على كراسي متحركة",
    "motorsports racing": "سباق رياضة محركات",
    "futsal": "كرة صالات",
    "darts": "سهام مريشة",
    "basketball": "كرة سلة",
    "esports": "رياضة إلكترونية",
    "canoeing": "ركوب الكنو",
    "dressage": "ترويض خيول",
    "canoe sprint": "سباق قوارب",
    "gymnastics": "جمباز",
    "korfball": "كورفبال",
    "fifa futsal world cup racing": "سباق كأس العالم لكرة الصالات",
    "wheelchair fifa futsal world cup": "كأس العالم لكرة الصالات على كراسي متحركة",
    "fifa world cup racing": "سباق كأس العالم لكرة القدم",
    "wheelchair fifa world cup": "كأس العالم لكرة القدم على كراسي متحركة",
    "multi-sport racing": "سباق رياضية متعددة",
    "wheelchair multi-sport": "رياضية متعددة على كراسي متحركة",
    "beach handball racing": "سباق كرة يد شاطئية",
    "wheelchair beach handball": "كرة يد شاطئية على كراسي متحركة",
    "shot put racing": "سباق دفع ثقل",
    "wheelchair shot put": "دفع ثقل على كراسي متحركة",
}


@functools.lru_cache(maxsize=1)
def _load_regex() -> re.Pattern:
    """Return the compiled regex pattern for matching sport keys."""
    if len(SPORTS_KEYS_FOR_JOBS) > 1000:
        logger.debug(f">keys_to_pattern(): len(new_pattern keys) = {len(SPORTS_KEYS_FOR_JOBS):,}")

    data_List_sorted = sorted(
        SPORTS_KEYS_FOR_JOBS.keys(),
        key=lambda k: (-k.count(" "), -len(k)),
    )
    alternation = "|".join(map(re.escape, [n.lower() for n in data_List_sorted]))

    new_pattern = rf"(?<!\w)({alternation})(?!\w)"

    RE_KEYS_NEW = re.compile(new_pattern, re.I)

    return RE_KEYS_NEW


@functools.lru_cache(maxsize=10000)
def match_sport_key(category: str) -> str:
    """Return the matched sport key within the provided category string."""
    RE_KEYS_NEW = _load_regex()
    match = RE_KEYS_NEW.search(f" {category} ")
    if match:
        return match.group(1)
    return ""


__all__ = [
    "match_sport_key",
]
