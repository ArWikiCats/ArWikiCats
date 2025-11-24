#!/usr/bin/python3
""" """

import pytest
from load_one_data import dump_diff, ye_test_one_dataset
from src.translations.sports_formats_oioioi.bot import (
    sport_lab_oioioi_load,
)

data = {
    "chinese amateur boxing championship": "x",
    "chinese amateur boxing championships": "x",
    "chinese championships (boxing)": "x",
    "chinese championships boxing": "x",
    "chinese current boxing seasons": "x",
    "chinese defunct indoor boxing clubs": "x",
    "chinese defunct indoor boxing coaches": "x",
    "chinese defunct indoor boxing competitions": "x",
    "chinese defunct indoor boxing cups": "x",
    "chinese defunct indoor boxing leagues": "x",
    "chinese defunct boxing clubs": "x",
    "chinese defunct boxing coaches": "x",
    "chinese defunct boxing competitions": "x",
    "chinese defunct boxing cup competitions": "x",
    "chinese defunct boxing cups": "x",
    "chinese defunct boxing leagues": "x",
    "chinese defunct outdoor boxing clubs": "x",
    "chinese defunct outdoor boxing coaches": "x",
    "chinese defunct outdoor boxing competitions": "x",
    "chinese defunct outdoor boxing cups": "x",
    "chinese defunct outdoor boxing leagues": "x",
    "chinese domestic boxing": "x",
    "chinese domestic boxing clubs": "x",
    "chinese domestic boxing coaches": "x",
    "chinese domestic boxing competitions": "x",
    "chinese domestic boxing cup": "x",
    "chinese domestic boxing cups": "x",
    "chinese domestic boxing leagues": "x",
    "chinese domestic women's boxing clubs": "x",
    "chinese domestic women's boxing coaches": "x",
    "chinese domestic women's boxing competitions": "x",
    "chinese domestic women's boxing cups": "x",
    "chinese domestic women's boxing leagues": "x",
    "chinese indoor boxing": "x",
    "chinese indoor boxing clubs": "x",
    "chinese indoor boxing coaches": "x",
    "chinese indoor boxing competitions": "x",
    "chinese indoor boxing cups": "x",
    "chinese indoor boxing leagues": "x",
    "chinese men's boxing championship": "x",
    "chinese men's boxing championships": "x",
    "chinese men's boxing national team": "x",
    "chinese men's u23 national boxing team": "x",
    "chinese boxing chairmen and investors": "x",
    "chinese boxing championship": "x",
    "chinese boxing championships": "x",
    "chinese boxing clubs": "x",
    "chinese boxing coaches": "x",
    "chinese boxing competitions": "x",
    "chinese boxing cup competitions": "x",
    "chinese boxing cups": "x",
    "chinese boxing indoor championship": "x",
    "chinese boxing indoor championships": "x",
    "chinese boxing junior championships": "x",
    "chinese boxing leagues": "x",
    "chinese boxing national team": "x",
    "chinese boxing u-13 championships": "x",
    "chinese boxing u-14 championships": "x",
    "chinese boxing u-15 championships": "x",
    "chinese boxing u-16 championships": "x",
    "chinese boxing u-17 championships": "x",
    "chinese boxing u-18 championships": "x",
    "chinese boxing u-19 championships": "x",
    "chinese boxing u-20 championships": "x",
    "chinese boxing u-21 championships": "x",
    "chinese boxing u-23 championships": "x",
    "chinese boxing u-24 championships": "x",
    "chinese boxing u13 championships": "x",
    "chinese boxing u14 championships": "x",
    "chinese boxing u15 championships": "x",
    "chinese boxing u16 championships": "x",
    "chinese boxing u17 championships": "x",
    "chinese boxing u18 championships": "x",
    "chinese boxing u19 championships": "x",
    "chinese boxing u20 championships": "x",
    "chinese boxing u21 championships": "x",
    "chinese boxing u23 championships": "x",
    "chinese boxing u24 championships": "x",
    "chinese open (boxing)": "x",
    "chinese open boxing": "x",
    "chinese outdoor boxing": "x",
    "chinese outdoor boxing championship": "x",
    "chinese outdoor boxing championships": "x",
    "chinese outdoor boxing clubs": "x",
    "chinese outdoor boxing coaches": "x",
    "chinese outdoor boxing competitions": "x",
    "chinese outdoor boxing cups": "x",
    "chinese outdoor boxing leagues": "x",
    "chinese professional boxing clubs": "x",
    "chinese professional boxing coaches": "x",
    "chinese professional boxing competitions": "x",
    "chinese professional boxing cups": "x",
    "chinese professional boxing leagues": "x",
    "chinese women's boxing": "x",
    "chinese women's boxing championship": "x",
    "chinese women's boxing championships": "x",
    "chinese youth boxing championship": "x",
    "chinese youth boxing championships": "x"
}


def test_sport_lab_oioioi_load():
    expected, diff_result = ye_test_one_dataset(data, sport_lab_oioioi_load)

    dump_diff(diff_result, "test_sport_lab_oioioi_load")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.parametrize("category, expected", data.items(), ids=list(data.keys()))
@pytest.mark.skip2
def test_sport_lab_oioioi_load_data(category, expected) -> None:
    label1 = sport_lab_oioioi_load(category)
    assert isinstance(label1, str)
    assert label1.strip() == expected
