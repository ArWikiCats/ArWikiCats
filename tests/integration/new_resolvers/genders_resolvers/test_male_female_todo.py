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

from ArWikiCats.new_resolvers.genders_resolvers import resolve_nat_genders_pattern_v2
from ArWikiCats.new_resolvers.genders_resolvers.jobs_and_genders_resolver import genders_jobs_resolver
from ArWikiCats.new_resolvers.genders_resolvers.sports_and_genders_resolver import genders_sports_resolver

sports_data = {
    "yemeni softball players": "لاعبو ولاعبات كرة لينة يمنيون",  # x
    "yemeni men's softball players": "لاعبو كرة لينة يمنيون",  # x
    "yemeni male softball players": "لاعبو كرة لينة يمنيون",  # x
    "yemeni women's softball players": "لاعبات كرة لينة يمنيات",  # ✓
    "women's softball players": "لاعبات كرة لينة",  # ✓
}


@pytest.mark.parametrize("category,expected", sports_data.items(), ids=sports_data.keys())
def test_sports_data(category: str, expected: str) -> None:
    """Test"""
    result = genders_sports_resolver(category)
    assert result == expected
