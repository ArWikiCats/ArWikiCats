"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.ma_bots.ye_ts_bot import (
    find_lab,
    translate_general_category,
    work_separator_names,
)

fast_data = {}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_fast_data(category: str, expected: str) -> None:
    label = translate_general_category(category)
    assert label == expected


def test_find_lab() -> None:
    # Test with a basic input
    result = find_lab("test category", "test_category")
    assert isinstance(result, str)

    result_empty = find_lab("", "")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = find_lab("sports category", "sports_category")
    assert isinstance(result_various, str)


def test_work_separator_names() -> None:
    # Test with a basic input
    result = work_separator_names("test category", "test category", True)
    assert isinstance(result, str)

    result_empty = work_separator_names("", "", False)
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = work_separator_names("sports", "sports category", True)
    assert isinstance(result_various, str)


def test_translate_general_category() -> None:
    # Test with a basic input
    result = translate_general_category("test category")
    assert isinstance(result, str)

    result_empty = translate_general_category("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = translate_general_category("sports category", False)
    assert isinstance(result_various, str)
