"""
Tests
"""
import pytest

from src.make2_bots.jobs_bots.te4_bots.for_me import Work_for_New_2018_men_Keys_with_all, Work_for_me, add_all

def test_work_for_new_2018_men_keys_with_all():
    # Test with basic inputs using a valid country code
    result = Work_for_New_2018_men_Keys_with_all("test category", "united states", "players")
    assert isinstance(result, str)

    # Test with empty strings
    result_empty = Work_for_New_2018_men_Keys_with_all("", "", "")
    assert isinstance(result_empty, str)

    # Test with various inputs using valid country codes
    result_various = Work_for_New_2018_men_Keys_with_all("sports", "france", "coaches")
    assert isinstance(result_various, str)

def test_work_for_me():
    # Test with basic inputs using a valid country code
    result = Work_for_me("test category", "united states", "players")
    assert isinstance(result, str)

    # Test with empty strings
    result_empty = Work_for_me("", "", "")
    assert isinstance(result_empty, str)

    # Test with various inputs using valid country codes
    result_various = Work_for_me("sports", "france", "athletes")
    assert isinstance(result_various, str)

def test_add_all():
    # Test with a basic input
    result = add_all("test label")
    assert isinstance(result, str)
    assert "ال" in result  # The function adds "ال" prefix

    # Test with empty string
    result_empty = add_all("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = add_all("another label")
    assert isinstance(result_various, str)
