"""
{"cate": "shi'a muslims expatriates", "country_prefix": "shi'a muslims", "category_suffix": "expatriates", "mens": "مسلمون شيعة", "womens": "مسلمات شيعيات", "country_lab": "مسلمون شيعة مغتربون"}

"""

import pytest

from ArWikiCats.make_bots.jobs_bots.relegin_jobs import (
    relegins_jobs,
    get_suffix_prefix,
)
from ArWikiCats.translations import RELIGIOUS_KEYS_PP

# new dict with only 20 items from RELIGIOUS_KEYS_PP
RELIGIOUS_KEYS_20 = {k: RELIGIOUS_KEYS_PP[k] for k in list(RELIGIOUS_KEYS_PP.keys())[:20]}


@pytest.mark.parametrize("key,data", RELIGIOUS_KEYS_20.items(), ids=[x for x in RELIGIOUS_KEYS_20])
def test_no_suffix_female(key: str, data: dict[str, str]) -> None:
    input_text = f"female {key}"
    expected = data["womens"]

    result = relegins_jobs(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"

    expected_mens = data["mens"]
    result_mens = relegins_jobs(key)
    assert result_mens == expected_mens, f"{expected_mens=}, {result_mens=}, {key=}"


data = [
    ("sufis", "صوفيون"),
    ("female sufis", "صوفيات"),
    ("shi'a muslims", "مسلمون شيعة"),
    ("female shi'a muslims", "مسلمات شيعيات"),
]


@pytest.mark.parametrize("input_text,expected", data, ids=[x[0] for x in data])
def test_no_suffix(input_text: str, expected: str) -> None:
    result = relegins_jobs(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"

    input2 = f"people {input_text}"
    result2 = relegins_jobs(input_text)
    assert result2 == expected, f"{expected=}, {result2=}, {input2=}"


test_data_2 = {
    "anglican expatriates": ("expatriates", "anglican"),
    "buddhist expatriates": ("expatriates", "buddhist"),
    "buddhist scholars of islam": ("scholars of islam", "buddhist"),
    "christian convicted-of-murder": ("convicted-of-murder", "christian"),
    "christian expatriates": ("expatriates", "christian"),
    "nazi expatriates": ("expatriates", "nazi"),
    "nazi bloggers": ("bloggers", "nazi"),
    "nazi scholars of islam": ("scholars of islam", "nazi"),
}


@pytest.mark.parametrize("input_text,expected", test_data_2.items(), ids=test_data_2.keys())
def test_get_suffix_prefix(input_text: str, expected: tuple[str, str]) -> None:
    result = get_suffix_prefix(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"
