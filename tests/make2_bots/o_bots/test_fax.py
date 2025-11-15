"""
Tests
"""
import pytest

from src.make2_bots.o_bots.fax import te_language


def test_te_language():
    # Test with a basic input
    result = te_language("english language")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = te_language("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = te_language("french literature")
    assert isinstance(result_various, str)
