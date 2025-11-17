"""
Tests
"""
import pytest

from src.make2_bots.jobs_bots.jobs_mainbot import Jobs

# @pytest.mark.skip


def test_jobs():
    # Test with basic inputs
    result = Jobs("test category", "united states", "players")
    assert isinstance(result, str)
    assert result == ""

    # Test with empty strings
    result_empty = Jobs("", "", "")
    assert isinstance(result_empty, str)
    assert result_empty == ""

    # Test with type parameter
    result_with_type = Jobs("sports", "france", "athletes")
    assert isinstance(result_with_type, str)
    assert result_with_type == ""

    # Test with tab parameter - avoid the error by testing parameters individually
    result_with_mens_tab = Jobs("category", "united states", "workers", "رجال")
    assert isinstance(result_with_mens_tab, str)
    assert result_with_mens_tab == "عمال رجال"

    result_with_womens_tab = Jobs("category", "united states", "workers", "سيدات")
    assert isinstance(result_with_womens_tab, str)
    assert result_with_womens_tab == " عمال سيدات"
