"""
Tests
"""
import pytest

from src.make2_bots.jobs_bots.jobs_mainbot import Jobs2, Jobs

def test_jobs2():
    # Test with basic inputs
    result = Jobs2("test category", "us", "players")
    assert isinstance(result, str)

    # Test with empty strings
    result_empty = Jobs2("", "", "")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = Jobs2("sports category", "uk", "coaches")
    assert isinstance(result_various, str)

def test_jobs():
    # Test with basic inputs
    result = Jobs("test category", "us", "players")
    assert isinstance(result, str)

    # Test with empty strings
    result_empty = Jobs("", "", "")
    assert isinstance(result_empty, str)

    # Test with type parameter
    result_with_type = Jobs("sports", "fr", "athletes", "type")
    assert isinstance(result_with_type, str)

    # Test with tab parameter
    result_with_tab = Jobs("category", "de", "workers", "", {"mens": "men", "womens": "women"})
    assert isinstance(result_with_tab, str)
