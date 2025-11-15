"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.arlabel_bots.bot_con_lab import get_con_lab

def test_get_con_lab():
    # Test with basic inputs
    result = get_con_lab("from", True, "from", "test country", "test country")
    assert isinstance(result, str)

    # Test with different parameters
    result_various = get_con_lab("in", False, "in", "us", "us")
    assert isinstance(result_various, str)

    # Test with empty strings
    result_empty = get_con_lab("", False, "", "", "")
    assert isinstance(result_empty, str)