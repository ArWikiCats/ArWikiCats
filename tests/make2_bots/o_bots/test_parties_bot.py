"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.o_bots.parties_bot import get_parties_lab

fast_data = {}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_fast_data(category: str, expected: str) -> None:
    label = get_parties_lab(category)
    assert label == expected


def test_get_parties_lab() -> None:
    # Test with a basic input
    result = get_parties_lab("republican party")
    assert isinstance(result, str)

    result_empty = get_parties_lab("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = get_parties_lab("some party")
    assert isinstance(result_various, str)
