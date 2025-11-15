"""
Tests
"""
import pytest

from src.make2_bots.date_bots.with_years_bot import Try_With_Years

def test_try_with_years():
    # Test basic functionality - should return a string
    result = Try_With_Years("2020 election")
    assert isinstance(result, str)

    # Test with year at end
    result_year_end = Try_With_Years("American Soccer League (1933–83)")
    assert isinstance(result_year_end, str)

    # Test with political term
    result_political = Try_With_Years("116th united states congress")
    assert isinstance(result_political, str)

    # Test empty string
    result_empty = Try_With_Years("")
    assert isinstance(result_empty, str)

    # Test with no year pattern
    result_no_year = Try_With_Years("random category")
    assert isinstance(result_no_year, str)
