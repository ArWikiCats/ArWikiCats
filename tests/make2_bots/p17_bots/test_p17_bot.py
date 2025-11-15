"""
Tests
"""
import pytest

from src.make2_bots.p17_bots.p17_bot import add_definite_article, Get_P17_2, Get_P17

def test_add_definite_article():
    # Test adding definite article to a single word
    result = add_definite_article("كرة القدم")
    assert result == "ال كرة القدم"  # Note: This function appears to replace spaces with " ال"

    # Test adding definite article to multiple words
    result_multi = add_definite_article("الرجال اللاعبين")
    assert "ال" in result_multi

    # Test with empty string
    result_empty = add_definite_article("")
    assert result_empty == "ال"

def test_get_p17_2():
    # Test with a known category pattern (would require proper setup of ma_lists)
    # For now, test that it returns a string
    result = Get_P17_2("united states government officials")
    assert isinstance(result, str)

def test_get_p17():
    # Test with a known category pattern (would require proper setup of ma_lists)
    # For now, test that it returns a string
    result = Get_P17("American athletes")
    assert isinstance(result, str)
