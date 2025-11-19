"""
Tests
"""
import pytest

from src.make2_bots.o_bots.popl import work_peoples, make_people_lab

fast_data = {
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data(category, expected) -> None:

    label = work_peoples(category)
    assert label.strip() == expected


def test_work_peoples():
    # Test with a basic input
    result = work_peoples("test people")
    assert isinstance(result, str)

    result_empty = work_peoples("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = work_peoples("some suffix")
    assert isinstance(result_various, str)


def test_make_people_lab():
    # Test with a basic input
    result = make_people_lab("people")
    assert isinstance(result, str)

    result_empty = make_people_lab("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = make_people_lab("actors")
    assert isinstance(result_various, str)
