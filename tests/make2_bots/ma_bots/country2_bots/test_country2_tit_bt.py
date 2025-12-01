"""
TODO: write tests
"""

import pytest

from ArWikiCats.make_bots.ma_bots.country2_bots.country2_tit_bt import (
    country_2_tit,
    country_2_title_work,
    make_conas,
    separator_arabic_resolve,
)


@pytest.mark.fast
def test_make_conas() -> None:
    # Test with basic inputs
    result = make_conas("in", "test in country")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

    # Test with different separator
    result_various = make_conas("from", "test from country")
    assert isinstance(result_various, tuple)
    assert len(result_various) == 2
    assert isinstance(result_various[0], str)
    assert isinstance(result_various[1], str)

    # Test with another valid separator
    result_other = make_conas("to", "test to country")
    assert isinstance(result_other, tuple)
    assert len(result_other) == 2
    assert isinstance(result_other[0], str)
    assert isinstance(result_other[1], str)


@pytest.mark.fast
def test_make_sps() -> None:
    # Test with basic inputs
    result = separator_arabic_resolve("to", "test label", "ambassadors of")
    assert isinstance(result, str)

    # Test with different parameters
    result_various = separator_arabic_resolve("in", "test label", "test")
    assert isinstance(result_various, str)

    # Test with empty strings
    result_empty = separator_arabic_resolve("", "", "")
    assert isinstance(result_empty, str)


@pytest.mark.fast
def test_country_2_tit() -> None:
    # Test with basic inputs
    result = country_2_tit("in", "test in country")
    assert isinstance(result, str)

    # Test with years enabled
    result_with_years = country_2_tit("from", "test from country", True)
    assert isinstance(result_with_years, str)

    # Test with years disabled
    result_without_years = country_2_tit("to", "test to country", False)
    assert isinstance(result_without_years, str)


@pytest.mark.fast
def test_country_2_title_work() -> None:
    # Test with basic input
    result = country_2_title_work("test in country")
    assert isinstance(result, str)

    # Test with years enabled
    result_with_years = country_2_title_work("test from country", True)
    assert isinstance(result_with_years, str)

    # Test with years disabled
    result_without_years = country_2_title_work("test to country", False)
    assert isinstance(result_without_years, str)

    # Test with empty string
    result_empty = country_2_title_work("")
    assert isinstance(result_empty, str)
