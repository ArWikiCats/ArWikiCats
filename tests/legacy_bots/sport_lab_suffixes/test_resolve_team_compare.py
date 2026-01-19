"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test, dump_same_and_not_same

from ArWikiCats.new_resolvers.sports_resolvers.legacy_sports_bots.sport_jobs_keys_suffixes import resolve_sport_jobs_keys_and_suffix
from ArWikiCats.new_resolvers.sports_resolvers.raw_sports import resolve_sport_label_by_jobs_key  # wrap_team_xo_normal_2025

test_data = {
    "short track speed skating cup": "كأس تزلج على مسار قصير",
    "wheelchair basketball cup": "كأس كرة سلة على كراسي متحركة",
    "luge cup": "كأس زحف ثلجي",
    "motorsports racing cup": "كأس سباق رياضة محركات",
    "speed skating cup": "كأس تزلج سريع",
    "motocross cup": "كأس موتو كروس",
    "pencak silat cup": "كأس بنكات سيلات",
    "pesäpallo cup": "كأس بيسبالو",
    "roller hockey (quad) cup": "كأس هوكي دحرجة",
    "association football cup": "كأس كرة قدم",
    "kick boxing racing cup": "كأس سباق كيك بوكسينغ",
    "shot put racing cup": "كأس سباق دفع ثقل",
    "luge racing cup": "كأس سباق زحف ثلجي",
    "water skiing cup": "كأس تزلج على الماء",
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
