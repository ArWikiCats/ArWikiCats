"""
Tests
"""

import pytest

from src.main_processers.event2bot import event2, event2_d2, stubs_label


def test_event2_d2():
    # Test with a basic input
    result = event2_d2("test category")
    assert isinstance(result, str)

    # Test with century format
    result_century = event2_d2("21st century")
    assert isinstance(result_century, str)

    # Test with empty string
    result_empty = event2_d2("")
    assert isinstance(result_empty, str)


def test_stubs_label():
    # Test with a basic input
    result = stubs_label("test category")
    assert isinstance(result, str)

    # Test with stubs format
    result_stubs = stubs_label("test stubs")
    assert isinstance(result_stubs, str)

    # Test with empty string
    result_empty = stubs_label("")
    assert isinstance(result_empty, str)


def test_event2():
    # Test with a basic input
    result = event2("test category")
    assert isinstance(result, str)

    # Test with different input
    result_various = event2("sports event")
    assert isinstance(result_various, str)

    # Test with empty string
    result_empty = event2("")
    assert isinstance(result_empty, str)
