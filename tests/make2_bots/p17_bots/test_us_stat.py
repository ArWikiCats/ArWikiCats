"""
Tests
"""
import pytest

from src.make2_bots.p17_bots.us_stat import Work_US_State

def test_work_us_state():
    # Test with a simple US state
    result = Work_US_State("california")
    assert isinstance(result, str)

    # Test with state that has a suffix like "state"
    result_with_suffix = Work_US_State("california state")
    assert isinstance(result_with_suffix, str)

    # Test with empty string
    result_empty = Work_US_State("")
    assert result_empty == ""

    # Test with whitespace
    result_whitespace = Work_US_State("   new york   ")
    assert isinstance(result_whitespace, str)
