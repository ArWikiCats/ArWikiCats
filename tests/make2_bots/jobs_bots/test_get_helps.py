"""
Tests
"""
import pytest

from src.make2_bots.jobs_bots.get_helps import get_con_3

def test_get_con_3():
    # Test with an empty list of keys (should return empty tuple)
    result = get_con_3("test category", [], "nat")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

    # Test with basic inputs
    # Since the function needs specific keys to match against, we'll test with expected behavior
    result_various = get_con_3("american people politics", ["american"], "nat")
    assert isinstance(result_various, tuple)
    assert len(result_various) == 2
    assert isinstance(result_various[0], str)
    assert isinstance(result_various[1], str)

    # Test with empty string
    result_empty = get_con_3("", [], "nat")
    assert isinstance(result_empty, tuple)
    assert len(result_empty) == 2
    assert isinstance(result_empty[0], str)
    assert isinstance(result_empty[1], str)
