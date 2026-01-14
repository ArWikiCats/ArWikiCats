"""Regression tests for translated labels in the mixed datasets."""

from __future__ import annotations

import pytest

from ArWikiCats.translations.mixed import Newkey, all_keys2, all_keys4, keys_23


@pytest.mark.parametrize(
    ("mapping", "key", "expected"),
    [
        pytest.param(all_keys2.BOOK_CATEGORIES, "publications", "منشورات", id="books_publications"),
        pytest.param(keys_23.ANTI_SUFFIXES, "publications", "منشورات", id="keys23_publications"),
        pytest.param(all_keys2.BOOK_CATEGORIES, "short stories", "قصص قصيرة", id="books_short_stories"),
        pytest.param(keys_23.ANTI_SUFFIXES, "short stories", "قصص قصيرة", id="keys23_short_stories"),
    ],
)
@pytest.mark.dict
def test_corrected_arabic_translations(mapping: dict[str, str], key: str, expected: str) -> None:
    """Verify that key translations use the corrected Arabic phrases."""

    assert mapping[key] == expected


def test_newkey_publishing_phrase() -> None:
    """The helper dictionaries should provide the corrected publishing term."""

    assert Newkey.AFTER_TYPE_FEMALE["publishing"] == "منشورات"


def test_women_competitions_use_correct_spelling() -> None:
    """Ensure the women's competitions render with the corrected Arabic term."""

    assert "للسيدات" in all_keys4.new2019["uci women's world tour"]


def test_time_trial_translations_include_against_the_clock() -> None:
    """Check the updated phrase "ضد الساعة" is present in time trial entries."""

    assert "ضد الساعة" in all_keys4.new2019["uci road world championships – men's team time trial"]
    assert "ضد الساعة" in all_keys4.new2019["uci track cycling world championships – women's 500 m time trial"]
