#!/usr/bin/python3
"""
"""
import functools
from ...helps import logger

label_mappings_ends = {
    "champions": "أبطال",
    "clubs": "أندية",
    "coaches": "مدربو",
    "competitions": "منافسات",
    "events": "أحداث",
    "films": "أفلام",
    "finals": "نهائيات",
    "home stadiums": "ملاعب",
    "leagues": "دوريات",
    "lists": "قوائم",
    "manager history": "تاريخ مدربو",
    "managers": "مدربو",
    "matches": "مباريات",
    "navigational boxes": "صناديق تصفح",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "organisations": "منظمات",
    "organizations": "منظمات",
    "players": "لاعبو",
    "positions": "مراكز",
    "records": "سجلات",
    "records and statistics": "سجلات وإحصائيات",
    "results": "نتائج",
    "rivalries": "دربيات",
    "scouts": "كشافة",
    "squads": "تشكيلات",
    "statistics": "إحصائيات",
    "teams": "فرق",
    "templates": "قوالب",
    "tournaments": "بطولات",
    "trainers": "مدربو",
    "umpires": "حكام",
    "venues": "ملاعب"
}

label_mappings_ends = dict(sorted(
    label_mappings_ends.items(),
    key=lambda k: (-k[0].count(" "), -len(k[0])),
))


def normalize_text(text):
    text = text.lower().replace("category:", "")
    text = text.replace("sportspeople", "sports-people")
    text = text.replace(" the ", " ")
    # text = text.replace("republic of", "republic-of")
    if text.startswith("the "):
        text = text[4:]
    return text.strip()


@functools.lru_cache(maxsize=10000)
def resolve_p17_bot_sport_suffixes(category: str, callback: callable) -> str:
    """Resolve year and job from countries using multi_bot_v4."""
    logger.debug(f"<<yellow>> start resolve_p17_bot_sport_suffixes: {category=}")

    result = ""

    category = normalize_text(category)
    for key, value in label_mappings_ends.items():
        if category.endswith(key):
            new_category = category[: -len(key)].strip()
            new_label = callback(new_category)
            if new_label:
                result = f"{value} {new_label}"
            break

    logger.debug(f"<<yellow>> end resolve_p17_bot_sport_suffixes: {category=}, {result=}")
    return result


__all__ = [
    "resolve_p17_bot_sport_suffixes",
]
