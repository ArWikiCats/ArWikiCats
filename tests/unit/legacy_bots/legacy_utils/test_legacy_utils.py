"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.legacy_utils import get_type_country, split_text_by_separator

data = [
    ("1450s disestablishments in arizona territory", "in", ("1450s disestablishments ", " arizona territory")),
]


@pytest.mark.parametrize("category, separator, output", data, ids=[x[0] for x in data])
@pytest.mark.fast
def test_get_type_country_data(category: str, separator: str, output: str) -> None:
    label = get_type_country(category, separator)
    assert label == output
    part_1, part_2 = split_text_by_separator(separator, category)
    assert part_1.strip() == output[0].strip()
    assert part_2.strip() == output[1].strip()


data_for = [
    ("african games gold medalists for chad", "for", ("african games gold medalists ", " chad")),
    ("olympic silver medalists for finland", "for", ("olympic silver medalists ", " finland")),
    ("paralympic competitors for cyprus", "for", ("paralympic competitors ", " cyprus")),
    ("summer olympics competitors for peru", "for", ("summer olympics competitors ", " peru")),
]


@pytest.mark.parametrize("category, separator, output", data_for, ids=[x[0] for x in data_for])
@pytest.mark.fast
def test_get_type_country_data_for(category: str, separator: str, output: str) -> None:
    label = get_type_country(category, separator)
    part_1, part_2 = split_text_by_separator(separator, category)

    assert part_1.strip() == output[0].strip()
    assert part_2.strip() == output[1].strip()

    assert label[0].strip() == output[0].strip()
