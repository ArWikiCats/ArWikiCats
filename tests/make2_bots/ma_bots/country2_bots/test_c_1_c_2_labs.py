"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.country2_bots.c_1_c_2_labs import check_sources, c_1_1_lab, c_2_1_lab

def test_check_sources():
    # Test with a basic input
    result = check_sources("test input")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = check_sources("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = check_sources("film category")
    assert isinstance(result_various, str)

def test_c_1_1_lab():
    # Test with basic inputs
    result = c_1_1_lab("from", False, "test")
    assert isinstance(result, str)

    # Test with different parameters
    result_with_years = c_1_1_lab("to", True, "sports")
    assert isinstance(result_with_years, str)

    # Test with empty strings
    result_empty = c_1_1_lab("", False, "")
    assert isinstance(result_empty, str)

def test_c_2_1_lab():
    # Test with basic inputs
    result = c_2_1_lab(False, "test")
    assert isinstance(result, str)

    # Test with years enabled
    result_with_years = c_2_1_lab(True, "sports")
    assert isinstance(result_with_years, str)

    # Test with empty string
    result_empty = c_2_1_lab(False, "")
    assert isinstance(result_empty, str)
