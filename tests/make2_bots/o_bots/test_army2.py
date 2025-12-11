"""
Tests
"""

import pytest

from ArWikiCats.make_bots.o_bots.army2 import te_army2

fast_data = {
    "United States secretaries-of war": "وزراء حرب أمريكيون",
    "secretaries-of war of yemen": "وزراء حرب يمنيون",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data(category: str, expected: str) -> None:
    label = te_army2(category)
    assert label == expected
