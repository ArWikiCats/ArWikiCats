"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.o_bots.peoples_resolver import make_people_lab

fast_data = {
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_make_people_lab(category: str, expected: str) -> None:
    label = make_people_lab(category)
    assert label == expected
