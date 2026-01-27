#!/usr/bin/python3
"""Integration tests"""

import pytest

from ArWikiCats.translations_formats import FormatData

data_list = {"snooker": "سنوكر"}

formatted_data = {
    "{sport}": "{sport_label}",
    # "{sport} managers": "مدراء {sport_label}",
    "{sport} managers": "مدربو {sport_label}",
    "{sport} coaches": "مدربو {sport_label}",
    "{sport} people": "أعلام {sport_label}",
    "{sport} players": "لاعبو {sport_label}",
    "{sport} players": "لاعبو {sport_label}",
    "{sport} referees": "حكام {sport_label}",
    "{sport} squads": "تشكيلات {sport_label}",
    "{sport} finals": "نهائيات {sport_label}",
    "{sport} positions": "مراكز {sport_label}",
    "{sport} tournaments": "بطولات {sport_label}",
    "{sport} films": "أفلام {sport_label}",
    "{sport} teams": "فرق {sport_label}",
    "{sport} venues": "ملاعب {sport_label}",
    "{sport} clubs": "أندية {sport_label}",
    "{sport} organizations": "منظمات {sport_label}",
}

examples = {"snooker players": "لاعبو سنوكر"}


@pytest.fixture
def bot() -> FormatData:
    return FormatData(formatted_data, data_list, key_placeholder="{sport}", value_placeholder="{sport_label}")


@pytest.mark.parametrize(
    "category,expected_key",
    examples.items(),
    ids=[k for k in examples],
)
@pytest.mark.fast
def test_format_data(bot, category: str, expected_key: str) -> None:
    result = bot.search(category)

    assert result == expected_key


def test_1(bot) -> None:
    result = bot.search("snooker players")

    assert result == "لاعبو سنوكر"
