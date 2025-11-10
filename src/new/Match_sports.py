# -*- coding: utf-8 -*-
"""
Single-file test implementation for the 'xoxo' sports template resolver.
"""

import re
import pytest
from typing import Dict, Optional, Tuple

TEMPLATES_TEAMS: Dict[str, str] = {}

# Base data
BASE_FORMATS = {
    "world cup": "كأس العالم",
    "world championship": "بطولة العالم",
    "asian championship": "بطولة آسيا",
    "league": "دوري",
    "cup": "كأس",
}

GENDERS = {
    "men's": "للرجال",
    "women's": "للسيدات",
    None: "",  # for neutral versions
}

AGE_LEVELS = {
    "u23 championship": "بطولة تحت 23 سنة",
    "u20 championship": "بطولة تحت 20 سنة",
    "u17 world cup": "كأس العالم تحت 17 سنة",
}

SPECIALS = {
    "wheelchair world championship": "بطولة العالم للكراسي المتحركة",
    "wheelchair": "{sport_ar} على كراسي متحركة",
    "racing": "سباقات {sport_ar}",
    "national team men's": "منتخب {sport_ar} الوطني للرجال",
    "national team women's": "منتخب {sport_ar} الوطني للسيدات",
    "national team": "المنتخب الوطني في {sport_ar}",
}

# --- Generate templates from combinations ---

# Regular gender × format templates
for fmt_en, fmt_ar in BASE_FORMATS.items():
    for gender_en, gender_ar in GENDERS.items():
        gender_key = f"{gender_en + ' ' if gender_en else ''}".strip()
        key = f"{gender_key}xoxo {fmt_en}"
        if gender_en:
            value = f"{fmt_ar} {gender_ar} في {{sport_ar}}"
        else:
            value = f"{fmt_ar} في {{sport_ar}}"
        TEMPLATES_TEAMS[key] = value

# Age-based templates
for k, v in AGE_LEVELS.items():
    TEMPLATES_TEAMS[f"{k.replace('championship','xoxo championship')}"] = f"{v} في {{sport_ar}}"

# Special patterns
for k, v in SPECIALS.items():
    # Handle "wheelchair xoxo" case explicitly
    if k == "wheelchair":
        TEMPLATES_TEAMS["wheelchair xoxo"] = v
    elif "national team" in k:
        # reorder "national xoxo team"
        if "men" in k:
            TEMPLATES_TEAMS["men's national xoxo team"] = v
        elif "women" in k:
            TEMPLATES_TEAMS["women's national xoxo team"] = v
        else:
            TEMPLATES_TEAMS["national xoxo team"] = v
    elif "racing" in k:
        TEMPLATES_TEAMS["xoxo racing"] = v
    else:
        TEMPLATES_TEAMS[f"wheelchair xoxo world championship"] = v

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
