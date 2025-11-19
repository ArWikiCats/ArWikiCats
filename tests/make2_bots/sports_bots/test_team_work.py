"""
Tests
"""
import pytest

from src.make2_bots.sports_bots.team_work import Get_Club, Get_team_work_Club

fast_data = {
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data(category, expected) -> None:

    label = Get_team_work_Club(category)
    assert label.strip() == expected


def test_get_club():
    # Test with a basic category that might have a club
    result = Get_Club("football players")
    assert isinstance(result, str) or isinstance(result, dict)

    # Test with return_tab option
    result_with_tab = Get_Club("football players", return_tab=True)
    assert isinstance(result_with_tab, dict)

    result_empty = Get_Club("")
    assert isinstance(result_empty, str) or isinstance(result_with_tab, dict)


def test_get_team_work_club():
    # Test basic functionality
    result = Get_team_work_Club("football players")
    assert isinstance(result, str)

    result_empty = Get_team_work_Club("")
    assert isinstance(result_empty, str)

    # Test with different categories
    result_various = Get_team_work_Club("basketball teams")
    assert isinstance(result_various, str)
