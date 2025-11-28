"""
Tests
"""

import pytest

from src.make_bots.ma_bots.ar_lab import get_type_country

data = [
    ("1450s disestablishments in arizona territory", "in", ("1450s disestablishments ", " arizona territory")),
]


@pytest.mark.parametrize("category, tito, output", data, ids=[x[0] for x in data])
@pytest.mark.fast
def test_get_type_country_data(category, tito, output) -> None:
    label = get_type_country(category, tito)
    assert label == output


def test_get_type_country():
    # Test with basic inputs
    result = get_type_country("test in country", "in")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

    # Test with different separator
    result_various = get_type_country("test from country", "from")
    assert isinstance(result_various, tuple)
    assert len(result_various) == 2
    assert isinstance(result_various[0], str)
    assert isinstance(result_various[1], str)

    # Test with non-empty valid separator instead of empty strings
    result_safe = get_type_country("test of country", "of")
    assert isinstance(result_safe, tuple)
    assert len(result_safe) == 2
    assert isinstance(result_safe[0], str)
    assert isinstance(result_safe[1], str)
