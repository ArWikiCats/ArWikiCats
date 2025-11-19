"""
Tests
"""

import pytest

from src.make2_bots.o_bots.fax import te_language

fast_data = {}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data(category, expected) -> None:

    label = te_language(category)
    assert label.strip() == expected


def test_te_language():
    # Test with a basic input
    result = te_language("english language")
    assert isinstance(result, str)

    result_empty = te_language("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = te_language("french literature")
    assert isinstance(result_various, str)
