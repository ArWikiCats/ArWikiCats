"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers import resolve_jobs_main

main_data = {
    "new zealand emigrants": "نيوزيلنديون مهاجرون",
    "yemeni emigrants": "يمنيون مهاجرون",
}


@pytest.mark.parametrize("category, expected", main_data.items(), ids=main_data.keys())
@pytest.mark.fast
def test_resolve_by_countries_names(category: str, expected: str) -> None:
    label = resolve_jobs_main(category)
    assert label == expected
