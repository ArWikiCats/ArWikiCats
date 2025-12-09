"""
Tests
"""

import pytest

from ArWikiCats.main_processers.nat_women_time_pattern import get_label

test_data = {
    # standard
    "Category:2000 American films": "تصنيف:أفلام أمريكية في 2000",
    "Category:2020s American films": "تصنيف:أفلام أمريكية في عقد 2020",
    "Category:2020s the American films": "تصنيف:أفلام أمريكية في عقد 2020",
    "Category:turkish general election june 2015": "تصنيف:الانتخابات التشريعية التركية يونيو 2015",
    "Category:turkish general election november 2015": "تصنيف:الانتخابات التشريعية التركية نوفمبر 2015",
}


@pytest.mark.parametrize("category,expected", test_data.items(), ids=test_data.keys())
def test_country_time_pattern(category: str, expected: str) -> None:
    """Test all year-country translation patterns."""
    result = get_label(category)
    assert result == expected
