"""
Tests
"""

import re

import pytest

from ArWikiCats.new_resolvers.genders_resolvers.sports_and_genders_resolver import genders_sports_resolver

test_sport_bot_data = {
    "footballers": "لاعبو ولاعبات كرة قدم",
    "mens footballers": "لاعبو كرة قدم",
    "softball players": "لاعبو ولاعبات كرة لينة",
    "male beach soccer players": "لاعبو كرة قدم شاطئية",
    "male squash players": "لاعبو اسكواش",
    "male submission wrestling players": "لاعبو مصارعة خضوع",
    "male sumo players": "لاعبو سومو",
    "male surfing players": "لاعبو ركمجة",
    "male swimming players": "لاعبو سباحة",
    "male synchronised swimming players": "لاعبو سباحة متزامنة",
    "male synchronized swimming players": "لاعبو سباحة متزامنة",
    "female players of american-football": "لاعبات كرة قدم أمريكية",
    "male players of american-football": "لاعبو كرة قدم أمريكية",
    "players of american-football": "لاعبو ولاعبات كرة قدم أمريكية",
    "yemeni players of american-football": "لاعبو ولاعبات كرة قدم أمريكية يمنيون",
    "yemeni male players of american-football": "لاعبو كرة قدم أمريكية يمنيون",
    "yemeni female players of american-football": "لاعبات كرة قدم أمريكية يمنيات",
}


@pytest.mark.parametrize("category, expected", test_sport_bot_data.items(), ids=test_sport_bot_data.keys())
@pytest.mark.fast
def test_sport_bot(category: str, expected: str) -> None:
    label = genders_sports_resolver(category)
    assert label == expected
