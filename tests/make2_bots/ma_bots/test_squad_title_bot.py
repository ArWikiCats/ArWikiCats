"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.squad_title_bot import get_squad_title

def test_get_squad_title():
    # Test with a basic input
    result = get_squad_title("test squad")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = get_squad_title("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = get_squad_title("football team")
    assert isinstance(result_various, str)
