"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.arlabel_bots.bot_type_country import get_type_country

def test_get_type_country():
    # Test with basic inputs
    result = get_type_country("test in country", "in")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

    # Test with different separator
    result_various = get_type_country("test from country", "from")
    assert isinstance(result_various, tuple)
    assert len(result_various) == 2
    assert isinstance(result_various[0], str)
    assert isinstance(result_various[1], str)

    # Test with empty strings
    result_empty = get_type_country("", "")
    assert isinstance(result_empty, tuple)
    assert len(result_empty) == 2
    assert isinstance(result_empty[0], str)
    assert isinstance(result_empty[1], str)