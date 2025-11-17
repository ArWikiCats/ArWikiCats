"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.end_start_bots.fax2 import get_episodes

data = [
    ("2016 American television", "2016 American television", "حلقات {}"),
    ("Game of Thrones (season 1)", "Game of Thrones", "حلقات {} الموسم 1"),
    ("", "", "حلقات {}"),
]


@pytest.mark.parametrize(
    "text, expected1, expected2",
    data,
    ids=[x[0] for x in data],
)

@pytest.mark.fast
def test_get_episodes(text, expected1, expected2):
    list_of_cat, category3 = get_episodes(f"{text} episodes")
    assert isinstance(list_of_cat, str)
    assert isinstance(category3, str)
    assert category3 == expected1
    assert list_of_cat == expected2
