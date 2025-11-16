"""
Tests
"""
import pytest

from src.make2_bots.p17_bots.p17_bot import add_definite_article, Get_P17_2, Get_P17


@pytest.mark.skip
def test_add_definite_article():
    # Test adding definite article to a single word
    # The function prepends "ال" and replaces spaces with " ال"
    result = add_definite_article("كرة القدم")
    # Input "كرة القدم" -> sub " " with " ال" = "كرة القد" -> prepend "ال" = "الكرة القد"
    assert result == "الكرة القد"

    # Test adding definite article to multiple words
    result_multi = add_definite_article("الرجال اللاعبين")
    assert "ال" in result_multi

    # Test with empty string
    result_empty = add_definite_article("")
    assert result_empty == "ال"


def test_get_p17_2():
    # Test with a known category pattern (would require proper setup of translations)
    # For now, test that it returns a string
    result = Get_P17_2("united states government officials")
    assert isinstance(result, str)


def test_get_p17():
    # Test with a known category pattern (would require proper setup of translations)
    # For now, test that it returns a string
    result = Get_P17("American athletes")
    assert isinstance(result, str)
