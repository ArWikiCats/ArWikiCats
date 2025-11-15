"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.dodo_bots.reg_result import get_reg_result, Typies

def test_get_reg_result():
    # Test with basic inputs
    result = get_reg_result("test category", "test category", "test category", "test")
    assert hasattr(result, 'year')
    assert hasattr(result, 'typeo')
    assert hasattr(result, 'In')
    assert hasattr(result, 'country')
    assert hasattr(result, 'cat_test')

    # Test with different parameters
    result_various = get_reg_result("category:year in type", "category:year in type", "year in type", "test")
    assert hasattr(result_various, 'year')
    assert hasattr(result_various, 'typeo')
    assert hasattr(result_various, 'In')
    assert hasattr(result_various, 'country')
    assert hasattr(result_various, 'cat_test')

def test_typies():
    # Test that Typies class can be instantiated
    typies_instance = Typies(year="2020", typeo="test", In="in", country="us", cat_test="test")
    assert typies_instance.year == "2020"
    assert typies_instance.typeo == "test"
    assert typies_instance.In == "in"
    assert typies_instance.country == "us"
    assert typies_instance.cat_test == "test"

    # Test with empty values
    typies_empty = Typies(year="", typeo="", In="", country="", cat_test="")
    assert typies_empty.year == ""
    assert typies_empty.typeo == ""
    assert typies_empty.In == ""
    assert typies_empty.country == ""
    assert typies_empty.cat_test == ""