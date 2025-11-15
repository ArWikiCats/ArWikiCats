"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.country2_lab import get_lab_for_country2

def test_get_lab_for_country2():
    # Test with a basic input
    result = get_lab_for_country2("test country")
    assert isinstance(result, str)

    # Test with different parameter
    result_with_ye = get_lab_for_country2("test country", True)
    assert isinstance(result_with_ye, str)

    # Test with empty string
    result_empty = get_lab_for_country2("")
    assert isinstance(result_empty, str)