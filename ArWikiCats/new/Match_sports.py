# -*- coding: utf-8 -*-
"""
Single-file test implementation for the 'xoxo' sports template resolver.
"""

import functools
import re
from typing import Dict

from ..translations_formats import FormatData

TEMPLATES_TEAMS: Dict[str, str] = {
    "men's xoxo world cup": "كأس العالم للرجال في {sport_ar}",
    "women's xoxo world cup": "كأس العالم للسيدات في {sport_ar}",
    "xoxo world cup": "كأس العالم في {sport_ar}",
    "men's xoxo world championship": "بطولة العالم للرجال في {sport_ar}",
    "women's xoxo world championship": "بطولة العالم للسيدات في {sport_ar}",
    "xoxo world championship": "بطولة العالم في {sport_ar}",
    "men's xoxo asian championship": "بطولة آسيا للرجال في {sport_ar}",
    "women's xoxo asian championship": "بطولة آسيا للسيدات في {sport_ar}",
    "xoxo asian championship": "بطولة آسيا في {sport_ar}",
    "men's xoxo league": "دوري الرجال في {sport_ar}",
    "women's xoxo league": "دوري السيدات في {sport_ar}",
    "xoxo league": "الدوري في {sport_ar}",
    "men's xoxo cup": "كأس الرجال في {sport_ar}",
    "women's xoxo cup": "كأس السيدات في {sport_ar}",
    "xoxo cup": "الكأس في {sport_ar}",
    "u23 xoxo championship": "بطولة تحت 23 سنة في {sport_ar}",
    "u20 xoxo championship": "بطولة تحت 20 سنة في {sport_ar}",
    "u17 xoxo world cup": "كأس العالم تحت 17 سنة في {sport_ar}",
    "wheelchair xoxo world championship": "بطولة العالم للكراسي المتحركة في {sport_ar}",
    "wheelchair xoxo": "{sport_ar} على كراسي متحركة",
    "xoxo racing": "سباقات {sport_ar}",
    "men's national xoxo team": "منتخب {sport_ar} الوطني للرجال",
    "women's national xoxo team": "منتخب {sport_ar} الوطني للسيدات",
    "national xoxo team": "المنتخب الوطني في {sport_ar}",
}
# ---------- team_job.py ----------
SPORTS_EN_TO_AR: Dict[str, str] = {
    "association football": "كرة القدم",
    "football": "كرة القدم",
    "futsal": "كرة الصالات",
    "softball": "سوفتبول",
    "baseball": "بيسبول",
    "basketball": "كرة السلة",
    "volleyball": "كرة الطائرة",
    "handball": "كرة اليد",
    "rugby union": "اتحاد الرجبي",
    "rugby league": "رجبي ليغ",
    "hockey": "هوكي",
    "field hockey": "هوكي الحقول",
    "ice hockey": "هوكي الجليد",
    "cricket": "كريكيت",
    "tennis": "تنس",
    "table tennis": "تنس الطاولة",
    "badminton": "بادمنتون",
    "wrestling": "مصارعة",
    "boxing": "ملاكمة",
    "kick boxing": "كيك بوكسينغ",
    "martial arts": "فنون قتالية",
    "aquatic sports": "رياضات مائية",
    "shooting": "رماية",
    "sport climbing": "تسلق",
    "motorsports": "رياضة محركات",
    "automobile racing": "سباق سيارات",
    "gaelic football": "كرة القدم الغيلية",
}

WHITESPACE_NORM = re.compile(r"\s+")


def _normalize(text: str) -> str:
    """Lowercase and collapse whitespace for consistent matching."""
    return WHITESPACE_NORM.sub(" ", text.lower()).strip().replace("–", "-")


def _expand_templates(templates: Dict[str, str]) -> Dict[str, str]:
    """Add relaxed variants that mirror the previous manual fallbacks."""

    expanded = dict(templates)

    for key, value in list(templates.items()):
        relaxed_key = key.replace("men's", "mens").replace("women's", "womens")
        expanded.setdefault(relaxed_key, value)

        tokens = ["xoxo" if token == "xoxo" else (token[:-1] if token.endswith("s") else token) for token in key.split(" ")]
        alt_key = " ".join(tokens)
        expanded.setdefault(alt_key, value)

    return expanded


@functools.lru_cache(maxsize=1)
def _load_sports_bot() -> FormatData:
    """Create a shared FormatData instance for sports template resolution."""

    expanded_templates = _expand_templates(TEMPLATES_TEAMS)
    return FormatData(
        expanded_templates,
        SPORTS_EN_TO_AR,
        key_placeholder="xoxo",
        value_placeholder="{sport_ar}",
    )


def resolve_team_label(title_en: str) -> str:
    """Resolve an Arabic team label for a sports title using FormatData."""

    bot = _load_sports_bot()
    normalized_title = _normalize(title_en)
    return bot.search(normalized_title)
