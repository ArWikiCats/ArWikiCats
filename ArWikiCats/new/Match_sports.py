# -*- coding: utf-8 -*-
"""Format sports match categories using :class:`FormatData`."""

from functools import lru_cache
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


@lru_cache(maxsize=1)
def load_bot() -> FormatData:
    """Create and cache the sports match formatter."""

    return FormatData(
        TEMPLATES_TEAMS,
        SPORTS_EN_TO_AR,
        key_placeholder="xoxo",
        value_placeholder="{sport_ar}",
    )


def resolve_team_label(title_en: str) -> str:
    """Resolve an Arabic team label for a sports title using FormatData."""

    bot = load_bot()
    return bot.search(title_en)


__all__ = [
    "resolve_team_label",
    "load_bot",
]
