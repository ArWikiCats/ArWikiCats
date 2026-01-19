"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.sports_resolvers import main_sports_resolvers

data_0 = {}

data_1 = {
    "badminton world cup": "كأس العالم لتنس الريشة",
    "biathlon world cup": "كأس العالم للبياثلون",
    "boxing world cup": "كأس العالم للبوكسينغ",
    "men's hockey world cup": "كأس العالم للهوكي للرجال",
    "national rugby union premier leagues": "دوريات اتحاد رجبي وطنية من الدرجة الممتازة",
    "netball world cup": "كأس العالم لكرة الشبكة",
    "rugby league world cup": "كأس العالم لدوري الرجبي",
    "women's cricket world cup": "كأس العالم للكريكت للسيدات",
    "women's hockey world cup": "كأس العالم للهوكي للسيدات",
    "women's softball world cup": "كأس العالم للكرة اللينة للسيدات",
    "wrestling world cup": "كأس العالم للمصارعة",
}


@pytest.mark.parametrize("category, expected_key", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_new_data(category: str, expected_key: str) -> None:
    label = main_sports_resolvers(category)
    assert label == expected_key
