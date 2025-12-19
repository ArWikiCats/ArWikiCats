#!/usr/bin/python3
"""
The categories should be like:
    - main category: softball players > لاعبو ولاعبات كرة لينة
    - male category:
        - male softball players > لاعبو كرة لينة
        - men's softball players > لاعبو كرة لينة
    - female category: women's softball players > لاعبات كرة لينة
"""

import pytest
from ArWikiCats import resolve_label_ar
from ArWikiCats.genders_processers.nat_genders_pattern import resolve_nat_genders_pattern

test_1 = {
    "yemeni softball players": "لاعبو ولاعبات كرة لينة يمنيون",        # x
    "yemeni men's softball players": "لاعبو كرة لينة يمنيون",         # x
    "yemeni male softball players": "لاعبو كرة لينة يمنيون",         # x
    "yemeni women's softball players": "لاعبات كرة لينة يمنيات",      # ✓
    "women's softball players": "لاعبات كرة لينة",      # ✓
}

test_2 = {
    "20th-century actors from Northern Ireland": "ممثلون وممثلات من أيرلندا الشمالية في القرن 20",      # x
    "20th-century male actors from Northern Ireland": "ممثلون من أيرلندا الشمالية في القرن 20",        # x
    "20th-century actresses from Northern Ireland": "ممثلات من أيرلندا الشمالية في القرن 20",           # ✓
}


@pytest.mark.parametrize("category,expected", test_1.items(), ids=test_1.keys())
@pytest.mark.skip2
def test_male_female_1(category: str, expected: str) -> None:
    """ Test """
    result = resolve_label_ar(category)
    assert result == expected


@pytest.mark.parametrize("category,expected", test_2.items(), ids=test_2.keys())
@pytest.mark.skip2
def test_male_female_2(category: str, expected: str) -> None:
    """ Test """
    result = resolve_label_ar(category)
    assert result == expected


@pytest.mark.parametrize("category,expected", test_1.items(), ids=test_1.keys())
def test_data_genders_1(category: str, expected: str) -> None:
    """ Test """
    result = resolve_nat_genders_pattern(category)
    assert result == expected
