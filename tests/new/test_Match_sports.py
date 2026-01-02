# -*- coding: utf-8 -*-
"""
test runner for resolve_team_label.
"""

import pytest

from ArWikiCats.new.Match_sports import SPORTS_EN_TO_AR, resolve_team_label

BASIC_EXAMPLES = [
    ("men's football world cup", "كأس العالم للرجال في كرة القدم"),
    ("women's basketball world cup", "كأس العالم للسيدات في كرة السلة"),
    ("womens basketball world cup", "كأس العالم للسيدات في كرة السلة"),
    ("softball world cup", "كأس العالم في سوفتبول"),
    ("men's volleyball world championship", "بطولة العالم للرجال في كرة الطائرة"),
    ("women's handball world championship", "بطولة العالم للسيدات في كرة اليد"),
    ("rugby union world championship", "بطولة العالم في اتحاد الرجبي"),
    ("men's football asian championship", "بطولة آسيا للرجال في كرة القدم"),
    ("men's futsal league", "دوري الرجال في كرة الصالات"),
    ("women's cricket league", "دوري السيدات في كريكت"),
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


# ----------------------------------------------------------------------
# Expanded: Cases for all sports (simple "X league" form)
# Ensures every sport resolves properly in at least one template.
# ----------------------------------------------------------------------
SPORT_SIMPLE_CASES = [(f"{en_sport} league", f"الدوري في {sport_ar}") for en_sport, sport_ar in SPORTS_EN_TO_AR.items()]


# ----------------------------------------------------------------------
# Expanded: Gender variations for each sport using “world cup”
# ----------------------------------------------------------------------
SPORT_GENDER_CASES = []
for en_sport, sport_ar in SPORTS_EN_TO_AR.items():
    SPORT_GENDER_CASES.extend(
        [
            (f"men's {en_sport} world cup", f"كأس العالم للرجال في {sport_ar}"),
            (f"women's {en_sport} world cup", f"كأس العالم للسيدات في {sport_ar}"),
            (f"{en_sport} world cup", f"كأس العالم في {sport_ar}"),
        ]
    )


# ----------------------------------------------------------------------
# Bad / dirty input formatting
# ----------------------------------------------------------------------
FORMATTING_CASES = [
    ("   mens   football   world   cup   ", "كأس العالم للرجال في كرة القدم"),
    ("   men's   football   world   cup   ", "كأس العالم للرجال في كرة القدم"),
    ("MEN'S FOOTBALL WORLD CUP", "كأس العالم للرجال في كرة القدم"),
    ("men's football   world   championship", "بطولة العالم للرجال في كرة القدم"),
    ("womens   volleyball   league", "دوري السيدات في كرة الطائرة"),
    ("women's   volleyball   league", "دوري السيدات في كرة الطائرة"),
    ("u23   football   championship", "بطولة تحت 23 سنة في كرة القدم"),
]


# ----------------------------------------------------------------------
# Negative tests: must all return ""
# ----------------------------------------------------------------------
NEGATIVE_CASES = [
    ("unknown sport world cup", ""),
    ("men's unknownsport league", ""),
    ("wheelchair unknownsport", ""),
    ("xoxo", ""),
    ("world cup only", ""),
    ("football somethingelse cup", ""),  # unrecognized template
]


# ----------------------------------------------------------------------
# Combine All Tests
# ----------------------------------------------------------------------
ALL_CASES = BASIC_EXAMPLES + SPORT_SIMPLE_CASES + SPORT_GENDER_CASES + FORMATTING_CASES + NEGATIVE_CASES


@pytest.mark.parametrize(
    "category, expected",
    ALL_CASES,
    ids=[c[0] for c in ALL_CASES],
)
@pytest.mark.fast
def test_resolve_team_label(category: str, expected: str) -> None:
    """Ensure team label resolution works for all template variations."""
    assert resolve_team_label(category) == expected
