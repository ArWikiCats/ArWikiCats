"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers import main_jobs_resolvers

main_data = {
    "new zealand emigrants": "نيوزيلنديون مهاجرون",
    "yemeni emigrants": "يمنيون مهاجرون",
    "the caribbean": "",
    "caribbean": "",
}


@pytest.mark.parametrize("category, expected", main_data.items(), ids=main_data.keys())
@pytest.mark.fast
def test_main_jobs_resolvers(category: str, expected: str) -> None:
    label = main_jobs_resolvers(category)
    assert label == expected
