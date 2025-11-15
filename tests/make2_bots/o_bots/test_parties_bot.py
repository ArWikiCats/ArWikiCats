"""
Tests
"""
import pytest

from src.make2_bots.o_bots.parties_bot import get_parties_lab_old, get_parties_lab

def test_get_parties_lab_old():
    # Test with a basic input
    result = get_parties_lab_old("democratic party")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = get_parties_lab_old("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = get_parties_lab_old("some party")
    assert isinstance(result_various, str)

def test_get_parties_lab():
    # Test with a basic input
    result = get_parties_lab("republican party")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = get_parties_lab("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = get_parties_lab("some party")
    assert isinstance(result_various, str)
