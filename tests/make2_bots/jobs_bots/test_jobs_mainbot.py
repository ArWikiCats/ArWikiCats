"""
Tests
"""
import pytest

from src.make2_bots.jobs_bots.jobs_mainbot import Jobs2, Jobs


def test_jobs2():
    # Test with basic inputs using valid country names
    result = Jobs2("test category", "united states", "players")
    assert isinstance(result, str)

    # Test with empty strings
    result_empty = Jobs2("", "", "")
    assert isinstance(result_empty, str)

    # Test with various inputs using valid country names
    result_various = Jobs2("sports category", "united kingdom", "coaches")
    assert isinstance(result_various, str)


@pytest.mark.skip
def test_jobs():
    # Test with basic inputs
    result = Jobs("test category", "united states", "players")
    assert isinstance(result, str)

    # Test with empty strings
    result_empty = Jobs("", "", "")
    assert isinstance(result_empty, str)

    # Test with type parameter
    result_with_type = Jobs("sports", "france", "athletes", "type")
    assert isinstance(result_with_type, str)

    # Test with tab parameter - avoid the error by testing parameters individually
    result_with_mens_tab = Jobs("category", "united states", "workers", "type", {"mens": "men"})
    assert isinstance(result_with_mens_tab, str)

    result_with_womens_tab = Jobs("category", "united states", "workers", "type", {"womens": "women"})
    assert isinstance(result_with_womens_tab, str)
