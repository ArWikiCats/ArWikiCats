"""
Tests
"""
import pytest

from src.make2_bots.matables_bots.table1_bot import get_KAKO


fast_data = {
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data(category, expected) -> None:

    label = get_KAKO(category)
    assert label.strip() == expected


def test_get_kako():
    # Test with a basic input
    result = get_KAKO("test")
    assert isinstance(result, str)

    result_empty = get_KAKO("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = get_KAKO("unknown_key")
    assert isinstance(result_various, str)
