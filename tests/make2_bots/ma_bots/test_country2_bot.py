"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.country2_bot import Get_country2

def test_get_country2():
    # Test with a basic input
    result = Get_country2("test country")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = Get_country2("")
    assert isinstance(result_empty, str)

    # Test with years disabled
    result_without_years = Get_country2("test country", False)
    assert isinstance(result_without_years, str)