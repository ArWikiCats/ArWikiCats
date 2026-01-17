"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.ma_bots2.lab import get_type_country

data = [
    ("1450s disestablishments in arizona territory", "in", ("1450s disestablishments ", " arizona territory")),
]


@pytest.mark.parametrize("category, separator, output", data, ids=[x[0] for x in data])
@pytest.mark.fast
def test_get_type_country_data(category: str, separator: str, output: str) -> None:
    label = get_type_country(category, separator)
    assert label == output
