#!/usr/bin/python3
""" """
import re

from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS
from .patterns import load_keys_to_pattern

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

new_pattern = load_keys_to_pattern(SPORTS_KEYS_FOR_JOBS)

RE_KEYS_NEW = re.compile(new_pattern, re.I)


def match_sport_key(category: str):
    match = RE_KEYS_NEW.search(f" {category} ")
    if match:
        return match.group(1)
    return ""


__all__ = [
    "match_sport_key",
]
