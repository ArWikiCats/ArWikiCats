"""
Tests
"""
import pytest

from src.make2_bots.co_bots.filter_en import filter_cat

def test_filter_cat():
    # Test with allowed category
    result_allowed = filter_cat("Football players")
    assert result_allowed is True

    # Test with blacklisted category
    result_disambig = filter_cat("Disambiguation")
    assert result_disambig is False

    # Test with blacklisted prefix
    result_cleanup = filter_cat("Cleanup")
    assert result_cleanup is False

    # Test with Wikipedia prefix
    result_wikipedia = filter_cat("Wikipedia articles")
    assert result_wikipedia is False

    # Test with month pattern
    result_month = filter_cat("Category:Events from January 2020")
    assert result_month is False

    # Test with category: prefix
    result_category_prefix = filter_cat("category:Football")
    assert isinstance(result_category_prefix, bool)
