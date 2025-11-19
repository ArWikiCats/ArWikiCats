"""
Tests
"""
import pytest

from src.make2_bots.jobs_bots.priffix_bot import priffix_Mens_work, Women_s_priffix_work

fast_data = {
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data(category, expected) -> None:

    label = priffix_Mens_work(category)
    assert label.strip() == expected


def test_priffix_mens_work():
    # Test with a basic input
    result = priffix_Mens_work("test job")
    assert isinstance(result, str)

    result_empty = priffix_Mens_work("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = priffix_Mens_work("american players")
    assert isinstance(result_various, str)


def test_women_s_priffix_work():
    # Test with a basic input
    result = Women_s_priffix_work("test job")
    assert isinstance(result, str)

    # Test with "women" in the string
    result_with_women = Women_s_priffix_work("test women")
    assert isinstance(result_with_women, str)

    # Test with empty string
    result_empty = Women_s_priffix_work("")
    assert isinstance(result_empty, str)
