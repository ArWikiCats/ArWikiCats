"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers import main_jobs_resolvers
from ArWikiCats.new_resolvers.nationalities_resolvers import main_nationalities_resolvers
from ArWikiCats.new_resolvers.sports_resolvers import main_sports_resolvers

countries_en_as_nationality_keys = [
    "antigua and barbuda",
    "botswana",
    "central african republic",
    "chinese taipei",
    "democratic republic of congo",
    "democratic-republic-of-congo",
    "dominican republic",
    "federated states of micronesia",
    "federated states-of micronesia",
    "georgia (country)",
    "hong kong",
    "ireland",
    "kiribati",
    "kyrgyz",
    "lesotho",
    "liechtenstein",
    "new zealand",
    "northern ireland",
    "republic of congo",
    "republic of ireland",
    "republic-of ireland",
    "republic-of-congo",
    "são toméan",
    "trinidad and tobago",
    "turkmen",
    "turkmenistan",
    "uzbek",
    "vatican",
    "west india",
]

test_data_must_be_empty = {
    "the caribbean": "",
    "caribbean": "",
}

test_data_must_be_empty.update({x: "" for x in countries_en_as_nationality_keys})


@pytest.mark.parametrize("category, expected_key", test_data_must_be_empty.items(), ids=test_data_must_be_empty.keys())
@pytest.mark.fast
def test_main_sports_resolvers_must_be_empty(category: str, expected_key: str) -> None:
    label2 = main_sports_resolvers(category)
    assert label2 == expected_key


@pytest.mark.parametrize("category, expected_key", test_data_must_be_empty.items(), ids=test_data_must_be_empty.keys())
@pytest.mark.fast
def test_main_nationalities_resolvers_must_be_empty(category: str, expected_key: str) -> None:
    label2 = main_nationalities_resolvers(category)
    assert label2 == expected_key


@pytest.mark.parametrize("category, expected_key", test_data_must_be_empty.items(), ids=test_data_must_be_empty.keys())
@pytest.mark.fast
def test_main_jobs_resolvers_must_be_empty(category: str, expected_key: str) -> None:
    label2 = main_jobs_resolvers(category)
    assert label2 == expected_key
