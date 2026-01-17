"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers import main_jobs_resolvers

te4_2018_Jobs_data = {
    "egyptian male sport shooters": "لاعبو رماية ذكور مصريون",
    "cypriot emigrants": "قبرصيون مهاجرون",
}


@pytest.mark.parametrize("category, expected_key", te4_2018_Jobs_data.items(), ids=te4_2018_Jobs_data.keys())
@pytest.mark.unit
def test_te4_2018_Jobs_data(category: str, expected_key: str) -> None:
    label2 = main_jobs_resolvers(category)
    assert label2 == expected_key
