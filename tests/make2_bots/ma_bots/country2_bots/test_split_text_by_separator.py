"""
TODO: write tests
"""

import pytest

from ArWikiCats.make_bots.ma_bots.country2_bots.country2_tit_bt import (
    split_text_by_separator,
)


@pytest.mark.fast
def test_split_text_by_separator_unit() -> None:
    # Test with basic inputs
    result = split_text_by_separator("in", "test in country")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

    # Test with different separator
    result_various = split_text_by_separator("from", "test from country")
    assert isinstance(result_various, tuple)
    assert len(result_various) == 2
    assert isinstance(result_various[0], str)
    assert isinstance(result_various[1], str)

    # Test with another valid separator
    result_other = split_text_by_separator("to", "test to country")
    assert isinstance(result_other, tuple)
    assert len(result_other) == 2
    assert isinstance(result_other[0], str)
    assert isinstance(result_other[1], str)


data = {
}


@pytest.mark.fast
@pytest.mark.parametrize("category, expected", data.items(), ids=lambda x: x[0])
def test_split_text_by_separator(category: str, expected: str) -> None:
    result: tuple[str, str] = split_text_by_separator(category)
    assert result == expected
