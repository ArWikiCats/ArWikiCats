"""
Tests
"""
import pytest

from src.make2_bots.jobs_bots.get_helps import get_con_3


def test_get_con_3():
    # Test with an empty list of keys (should return empty tuple)
    result = get_con_3("test category", "nat")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)
