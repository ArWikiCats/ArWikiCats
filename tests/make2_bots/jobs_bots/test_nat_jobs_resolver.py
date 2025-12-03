"""
Tests
"""

import pytest

from ArWikiCats.make_bots.jobs_bots.nat_jobs_resolver import get_label

test_data2 = {
    "welsh people": "ويلزيون",
    "writers people": "كتاب",
    "yemeni people": "يمنيون",
    "yemeni writers": "كتاب يمنيون",
    "yemeni male writers": "كتاب ذكور يمنيون",
    "greek-american male writers": "كتاب ذكور أمريكيون يونانيون",

}


@pytest.mark.parametrize("category,expected", test_data2.items(), ids=test_data2.keys())
def test_nat_pattern_multi(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = get_label(category)
    assert result == expected
