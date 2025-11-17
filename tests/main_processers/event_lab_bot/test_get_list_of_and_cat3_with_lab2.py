"""
Tests
"""
import pytest

from src.main_processers.event_lab_bot import get_list_of_and_cat3_with_lab2


@pytest.mark.fast
def test_get_list_of_and_cat3_with_lab2():
    # Test with a basic input
    result = get_list_of_and_cat3_with_lab2("test category")
    assert isinstance(result, str)

    # Test with squad templates
    result_squad = get_list_of_and_cat3_with_lab2("2020 squad templates")
    assert isinstance(result_squad, str)
    assert result_squad == "قوالب تشكيلات 2020"

    # Test with empty strings
    result_empty = get_list_of_and_cat3_with_lab2("")
    assert isinstance(result_empty, str)
    assert result_empty == ""
