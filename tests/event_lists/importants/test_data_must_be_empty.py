"""
Tests
"""

import pytest
from ArWikiCats.make_bots.countries_formats.t4_2018_jobs import te4_2018_Jobs
from ArWikiCats.new_resolvers.jobs_resolvers import resolve_jobs_main
from ArWikiCats.new_resolvers.nationalities_resolvers import resolve_nationalities_main
from ArWikiCats.new_resolvers.sports_resolvers import resolve_sports_main

test_data_must_be_empty = {
    "the caribbean": "",
    "caribbean": "",
}


@pytest.mark.parametrize("category, expected_key", test_data_must_be_empty.items(), ids=test_data_must_be_empty.keys())
@pytest.mark.slow
def test_te4_2018_Jobs_must_be_empty(category: str, expected_key: str) -> None:
    label1 = te4_2018_Jobs(category)
    assert label1 == expected_key


@pytest.mark.parametrize("category, expected_key", test_data_must_be_empty.items(), ids=test_data_must_be_empty.keys())
@pytest.mark.slow
def test_resolve_sports_main_must_be_empty(category: str, expected_key: str) -> None:
    label2 = resolve_sports_main(category)
    assert label2 == expected_key


@pytest.mark.parametrize("category, expected_key", test_data_must_be_empty.items(), ids=test_data_must_be_empty.keys())
@pytest.mark.slow
def test_resolve_nationalities_main_must_be_empty(category: str, expected_key: str) -> None:
    label2 = resolve_nationalities_main(category)
    assert label2 == expected_key


@pytest.mark.parametrize("category, expected_key", test_data_must_be_empty.items(), ids=test_data_must_be_empty.keys())
@pytest.mark.slow
def test_resolve_jobs_main_must_be_empty(category: str, expected_key: str) -> None:
    label2 = resolve_jobs_main(category)
    assert label2 == expected_key
