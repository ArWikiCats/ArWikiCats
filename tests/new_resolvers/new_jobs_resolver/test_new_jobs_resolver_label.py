"""
Tests
"""

import pytest
from ArWikiCats.new_resolvers.new_jobs_resolver import new_jobs_resolver_label

main_data = {
    "new zealand emigrants": "نيوزيلنديون مهاجرون",
    "yemeni emigrants": "يمنيون مهاجرون",
}


@pytest.mark.parametrize("category, expected", main_data.items(), ids=main_data.keys())
@pytest.mark.fast
def test_resolve_by_countries_names(category: str, expected: str) -> None:
    label = new_jobs_resolver_label(category)
    assert label == expected
