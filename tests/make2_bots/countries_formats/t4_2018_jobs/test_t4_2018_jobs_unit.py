"""
Tests
"""

import pytest

from src.make2_bots.countries_formats.t4_2018_jobs import te4_2018_Jobs

te4_2018_Jobs_data = {
    "egyptian male sport shooters": "لاعبو رماية ذكور مصريون",
    "cypriot emigrants": "قبرصيون مهاجرون",
}


@pytest.mark.parametrize("category, expected_key", te4_2018_Jobs_data.items(), ids=list(te4_2018_Jobs_data.keys()))
@pytest.mark.slow
def test_te4_2018_Jobs_data(category, expected_key) -> None:
    label = te4_2018_Jobs(category)
    assert label.strip() == expected_key
