"""
Tests
"""

import pytest

from ArWikiCats.make_bots.countries_formats.t4_2018_jobs import te4_2018_Jobs

te4_2018_Jobs_data = {
    "egyptian male sport shooters": "لاعبو رماية ذكور مصريون",
    "cypriot emigrants": "قبرصيون مهاجرون",
}


@pytest.mark.parametrize("category, expected_key", te4_2018_Jobs_data.items(), ids=list(te4_2018_Jobs_data.keys()))
@pytest.mark.slow
def test_te4_2018_Jobs_data(category: str, expected_key: str) -> None:
    label = te4_2018_Jobs(category)
    assert label == expected_key
