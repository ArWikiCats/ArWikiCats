"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.list_cat_format import list_of_cat_func

def test_list_of_cat_func():
    # Test with basic inputs
    result = list_of_cat_func("test category", "test label", "list of {}", False)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

    # Test with various inputs including foot_ballers=True
    result_footballers = list_of_cat_func("football category", "football label", "list of {}", True)
    assert isinstance(result_footballers, tuple)
    assert len(result_footballers) == 2
    assert isinstance(result_footballers[0], str)
    assert isinstance(result_footballers[1], str)

    # Test with empty strings
    result_empty = list_of_cat_func("", "", "{}", False)
    assert isinstance(result_empty, tuple)
    assert len(result_empty) == 2
    assert isinstance(result_empty[0], str)
    assert isinstance(result_empty[1], str)
