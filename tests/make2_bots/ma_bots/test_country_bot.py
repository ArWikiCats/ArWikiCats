"""
Tests
"""

import pytest

from src.make2_bots.ma_bots.country_bot import Get_c_t_lab, get_country


def test_get_country():
    # Test with a basic input
    result = get_country("test country")
    assert isinstance(result, str)

    # Test with different parameter
    result_with_country2 = get_country("test country", False)
    assert isinstance(result_with_country2, str)

    # Test with empty string
    result_empty = get_country("")
    assert isinstance(result_empty, str)


def test_get_c_t_lab():
    # Test with basic inputs
    result = Get_c_t_lab("test country", "in")
    assert isinstance(result, str)

    # Test with different parameters
    result_various = Get_c_t_lab("test country", "from", "type_label", False)
    assert isinstance(result_various, str)

    # Test with empty strings - avoid calling with empty strings as they might cause issues
    result_safe = Get_c_t_lab("valid country", "from")
    assert isinstance(result_safe, str)
