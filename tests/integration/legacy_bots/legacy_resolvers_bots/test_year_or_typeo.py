"""
TODO: Add test data for year or typeo resolver.
"""
import pytest

from ArWikiCats.legacy_bots.legacy_resolvers_bots.year_or_typeo import label_for_startwith_year_or_typeo

data_1 = {

}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
def test_year_or_typeo_1(category: str, expected: str) -> None:
    label = label_for_startwith_year_or_typeo(category)
    assert label == expected
