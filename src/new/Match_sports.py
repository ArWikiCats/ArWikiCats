# -*- coding: utf-8 -*-
"""
Single-file test implementation for the 'xoxo' sports template resolver.
"""

import re
import pytest
from typing import Dict, Optional, Tuple


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

_sorted_sports = sorted(SPORTS_EN_TO_AR.keys(), key=len, reverse=True)
SPORTS_PATTERN = re.compile(r"(?i)\b(" + "|".join(re.escape(k) for k in _sorted_sports) + r")\b")
WHITESPACE_NORM = re.compile(r"\s+")


def _normalize(text: str) -> str:
    return WHITESPACE_NORM.sub(" ", text.lower()).strip()


def find_sport(title_en: str) -> Optional[Tuple[str, str]]:
    m = SPORTS_PATTERN.search(_normalize(title_en))
    if not m:
        return None
    sport_en = m.group(1).lower()
    return (sport_en, SPORTS_EN_TO_AR[sport_en])


def make_template_key(title_en: str, sport_en: str) -> str:
    text = re.sub(rf"(?i)\b{re.escape(sport_en)}\b", "xoxo", _normalize(title_en))
    text = text.replace("–", "-")
    return WHITESPACE_NORM.sub(" ", text).strip()


def resolve_team_label(title_en: str) -> str:
    found = find_sport(title_en)
    if not found:
        return ""
    sport_en, sport_ar = found
    template_key = make_template_key(title_en, sport_en)

    if template_key in TEMPLATES_TEAMS:
        return TEMPLATES_TEAMS[template_key].format(sport_ar=sport_ar)

    relaxed = template_key.replace("men's", "mens").replace("women's", "womens")
    if relaxed in TEMPLATES_TEAMS:
        return TEMPLATES_TEAMS[relaxed].format(sport_ar=sport_ar)

    tokens = [t for t in template_key.split(" ") if t]
    alt_tokens = ["xoxo" if t == "xoxo" else (t[:-1] if t.endswith("s") else t) for t in tokens]
    alt_key = " ".join(alt_tokens)
    if alt_key in TEMPLATES_TEAMS:
        return TEMPLATES_TEAMS[alt_key].format(sport_ar=sport_ar)
    return ""
# -*- coding: utf-8 -*-
"""
Manual test runner for resolve_team_label without pytest.
"""

def manual_test_resolve_team_label():
    tests = [
        ("men's football world cup", "كأس العالم للرجال في كرة القدم"),
        ("women's basketball world cup", "كأس العالم للسيدات في كرة السلة"),
        ("softball world cup", "كأس العالم في سوفتبول"),
        ("men's volleyball world championship", "بطولة العالم للرجال في كرة الطائرة"),
        ("women's handball world championship", "بطولة العالم للسيدات في كرة اليد"),
        ("rugby union world championship", "بطولة العالم في اتحاد الرجبي"),
        ("men's football asian championship", "بطولة آسيا للرجال في كرة القدم"),
        ("men's futsal league", "دوري الرجال في كرة الصالات"),
        ("women's cricket league", "دوري السيدات في كريكيت"),
        ("baseball league", "الدوري في بيسبول"),
        ("u23 football championship", "بطولة تحت 23 سنة في كرة القدم"),
        ("u17 basketball world cup", "كأس العالم تحت 17 سنة في كرة السلة"),
        ("wheelchair tennis", "تنس على كراسي متحركة"),
        ("sport climbing racing", "سباقات تسلق"),
        ("men's national football team", "منتخب كرة القدم الوطني للرجال"),
        ("women's national volleyball team", "منتخب كرة الطائرة الوطني للسيدات"),
        ("national basketball team", "المنتخب الوطني في كرة السلة"),
        ("random unknown title", ""),
    ]

    passed = 0
    failed = 0

    for title_en, expected in tests:
        result = resolve_team_label(title_en)
        if result == expected:
            print(f"✅ PASS: {title_en!r}")
            passed += 1
        else:
            print(f"❌ FAIL: {title_en!r}\n   expected={expected!r}\n   got={result!r}")
            failed += 1

    print(f"\nSummary: {passed} passed, {failed} failed, total {len(tests)}")


# Run directly
if __name__ == "__main__":
    manual_test_resolve_team_label()

# ---------- tests ----------
