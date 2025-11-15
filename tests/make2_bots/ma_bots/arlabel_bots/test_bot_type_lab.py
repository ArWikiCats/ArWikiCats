"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.arlabel_bots.bot_type_lab import get_Type_lab

def test_get_type_lab():
    # Test with basic inputs
    result = get_Type_lab("from", "women", "women", "us")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], bool)

    # Test with different parameters
    result_various = get_Type_lab("to", "sports", "sports", "uk")
    assert isinstance(result_various, tuple)
    assert len(result_various) == 2
    assert isinstance(result_various[0], str)
    assert isinstance(result_various[1], bool)

    # Test with empty strings
    result_empty = get_Type_lab("", "", "", "")
    assert isinstance(result_empty, tuple)
    assert len(result_empty) == 2
    assert isinstance(result_empty[0], str)
    assert isinstance(result_empty[1], bool)