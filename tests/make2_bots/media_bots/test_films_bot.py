"""
Tests
"""
import pytest

from src.make2_bots.media_bots.films_bot import te_films


fast_data = {
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data(category, expected) -> None:

    label = te_films(category)
    assert label.strip() == expected


def test_test_films():
    # Test with a basic input
    result = te_films("action films")
    assert isinstance(result, str)

    result_empty = te_films("")
    assert isinstance(result_empty, str)

    # Test with reference category
    result_with_ref = te_films("drama movies", "movies")
    assert isinstance(result_with_ref, str)
