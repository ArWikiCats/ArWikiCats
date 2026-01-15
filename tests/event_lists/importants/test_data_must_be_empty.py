"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers import resolve_jobs_main
from ArWikiCats.new_resolvers.nationalities_resolvers import resolve_nationalities_main
from ArWikiCats.new_resolvers.sports_resolvers import resolve_sports_main
from ArWikiCats.translations import countries_en_as_nationality_keys

test_data_must_be_empty = {
    "the caribbean": "",
    "caribbean": "",
}
test_data_must_be_empty.update({x: "" for x in countries_en_as_nationality_keys})


@pytest.mark.parametrize("category, expected_key", test_data_must_be_empty.items(), ids=test_data_must_be_empty.keys())
@pytest.mark.fast
def test_resolve_sports_main_must_be_empty(category: str, expected_key: str) -> None:
    label2 = resolve_sports_main(category)
    assert label2 == expected_key


@pytest.mark.parametrize("category, expected_key", test_data_must_be_empty.items(), ids=test_data_must_be_empty.keys())
@pytest.mark.fast
def test_resolve_nationalities_main_must_be_empty(category: str, expected_key: str) -> None:
    label2 = resolve_nationalities_main(category)
    assert label2 == expected_key


@pytest.mark.parametrize("category, expected_key", test_data_must_be_empty.items(), ids=test_data_must_be_empty.keys())
@pytest.mark.fast
def test_resolve_jobs_main_must_be_empty(category: str, expected_key: str) -> None:
    label2 = resolve_jobs_main(category)
    assert label2 == expected_key
