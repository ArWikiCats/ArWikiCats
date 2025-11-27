"""
Tests
"""

import pytest

from src.translations.sports_formats_2025.match_labs import find_teams_2025

data6 = {
    "georgia (country) freestyle wrestling federation": "الاتحاد الجورجي للمصارعة الحرة",
    "philippine sailing (sport) federation": "الاتحاد الفلبيني لرياضة الإبحار",
}


@pytest.mark.parametrize("category, expected_key", data6.items(), ids=list(data6.keys()))
@pytest.mark.fast
def test_find_teams_2025(category, expected_key) -> None:
    label = find_teams_2025(category)

    assert label.strip() == expected_key
