"""
Tests
"""
import pytest

from src.make2_bots.sports_bots.sport_lab_suffixes import get_teams_new

get_teams_new_data = {
}


@pytest.mark.parametrize("category, expected_key", get_teams_new_data.items(), ids=list(get_teams_new_data.keys()))
@pytest.mark.fast
def test_get_teams_new_data(category, expected_key) -> None:

    label = get_teams_new(category)
    assert label.strip() == expected_key


def test_get_teams_new():
    # Test with a basic input
    result = get_teams_new("football team")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = get_teams_new("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = get_teams_new("basketball team")
    assert isinstance(result_various, str)
