"""
Tests
"""

import pytest

from ArWikiCats.main_processers.nat_pattern import get_label

test_data = {
    # standard
    "welsh people": "ويلزيون",
    "yemeni people": "يمنيون",
    "yemeni men": "رجال يمنيون",

}


@pytest.mark.parametrize("category,expected", test_data.items(), ids=test_data.keys())
def test_nat_pattern(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = get_label(category)
    assert result == expected
