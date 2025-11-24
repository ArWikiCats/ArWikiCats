#!/usr/bin/python3
""" """

import pytest
from src.translations.sports_formats_oioioi.bot import (
    get_start_p17,
)

data = {
    "swiss wheelchair curling championship": ("{nat} wheelchair curling championship", "swiss"),
    "canadian open tennis": ("{nat} open tennis", "canadian"),
    "caribbean handball championship": ("{nat} handball championship", "caribbean"),
    "european motocross championship": ("{nat} motocross championship", "european"),
    "central american women's handball championship": ("{nat} women's handball championship", "central american"),
    "european athletics u23 championships": ("{nat} athletics u23 championships", "european"),
    "european cricket championship": ("{nat} cricket championship", "european"),

}


@pytest.mark.parametrize("category, expected", data.items(), ids=list(data.keys()))
@pytest.mark.fast
def test_get_start_p17(category, expected) -> None:
    sport_format_key, country_start = get_start_p17(category)
    expected_1, expected_2 = expected

    assert sport_format_key == expected_1
    assert country_start == expected_2
