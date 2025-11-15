"""
Tests
"""
import pytest

from src.make2_bots.jobs_bots.bot_te_4 import nat_match, te_2018_with_nat, Jobs_in_Multi_Sports

def test_nat_match():
    # Test with a basic input
    result = nat_match("anti-us sentiment")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = nat_match("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = nat_match("category:anti-uk sentiment")
    assert isinstance(result_various, str)

def test_te_2018_with_nat():
    # Test with basic input
    result = te_2018_with_nat("test category")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = te_2018_with_nat("")
    assert isinstance(result_empty, str)

    # Test with reference category
    result_with_ref = te_2018_with_nat("sports category", "reference")
    assert isinstance(result_with_ref, str)

def test_jobs_in_multi_sports():
    # Test with a basic input
    result = Jobs_in_Multi_Sports("football players")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = Jobs_in_Multi_Sports("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = Jobs_in_Multi_Sports("basketball coaches")
    assert isinstance(result_various, str)
