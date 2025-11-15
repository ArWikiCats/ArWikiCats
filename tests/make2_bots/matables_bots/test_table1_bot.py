"""
Tests
"""
import pytest

from src.make2_bots.matables_bots.table1_bot import get_KAKO

def test_get_kako():
    # Test with a basic input
    result = get_KAKO("test")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = get_KAKO("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = get_KAKO("unknown_key")
    assert isinstance(result_various, str)