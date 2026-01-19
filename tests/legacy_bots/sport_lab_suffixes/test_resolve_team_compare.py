"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test, dump_same_and_not_same

from ArWikiCats.new_resolvers.sports_resolvers.legacy_sports_bots.sport_jobs_keys_suffixes import resolve_sport_jobs_keys_and_suffix
from ArWikiCats.new_resolvers.sports_resolvers.raw_sports.raw_sports_jobs_key import resolve_sport_label_by_jobs_key

test_data = {
}


@pytest.mark.parametrize("category, expected_key", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_resolve_team_suffix(category: str, expected_key: str) -> None:
    label = resolve_sport_jobs_keys_and_suffix(category)
    assert label == expected_key


@pytest.mark.parametrize("category, expected_key", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_resolve_sport_label_by_jobs_key(category: str, expected_key: str) -> None:
    label = resolve_sport_label_by_jobs_key(category)
    assert label == expected_key


to_test = [
    ("test_resolve_team_suffix", test_data, resolve_sport_jobs_keys_and_suffix),
    ("test_resolve_sport_label_by_jobs_key", test_data, resolve_sport_label_by_jobs_key),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
