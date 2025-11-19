# -*- coding: utf-8 -*-
"""
test runner for resolve_team_label.
"""
import pytest

from src.new.Match_sports import resolve_team_label

examples = [
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


@pytest.mark.parametrize(
    "category, expected",
    examples,
    ids=[k[0] for k in examples],
)
@pytest.mark.fast
def test_resolve_team_label(category: str, expected: str) -> None:

    assert resolve_team_label(category) == expected
