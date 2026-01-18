"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test, dump_same_and_not_same

from ArWikiCats.legacy_bots.sport_lab_suffixes import resolve_team_suffix
from ArWikiCats.new_resolvers.sports_resolvers.raw_sports import resolve_sport_label_by_jobs_key

by_jobs_key_test_data = {
    "orienteering cup": "كؤوس سباق موجه",
    "short track speed skating cup": "كؤوس تزلج على مسار قصير",
    "wheelchair basketball cup": "كؤوس كرة سلة على كراسي متحركة",
    "luge cup": "كؤوس زحف ثلجي",
    "motorsports racing cup": "كؤوس سباق رياضة محركات",
    "speed skating cup": "كؤوس تزلج سريع",
    "motocross cup": "كؤوس موتو كروس",
    "pencak silat cup": "كؤوس بنكات سيلات",
    "pesäpallo cup": "كؤوس بيسبالو",
    "roller hockey (quad) cup": "كؤوس هوكي دحرجة",
    "association football cup": "كؤوس كرة قدم",
    "kick boxing racing cup": "كؤوس سباق كيك بوكسينغ",
    "shot put racing cup": "كؤوس سباق دفع ثقل",
    "luge racing cup": "كؤوس سباق زحف ثلجي",
    "water skiing cup": "كؤوس تزلج على الماء"
}

team_suffix_test_data = {
    "orienteering cup": "كأس سباق موجه",
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


@pytest.mark.parametrize("category, expected_key", team_suffix_test_data.items(), ids=team_suffix_test_data.keys())
@pytest.mark.fast
def test_resolve_team_suffix(category: str, expected_key: str) -> None:
    label = resolve_team_suffix(category)
    assert label == expected_key


@pytest.mark.parametrize("category, expected_key", by_jobs_key_test_data.items(), ids=by_jobs_key_test_data.keys())
@pytest.mark.fast
def test_resolve_sport_label_by_jobs_key(category: str, expected_key: str) -> None:
    label = resolve_sport_label_by_jobs_key(category)
    assert label == expected_key


to_test = [
    ("test_resolve_team_suffix", team_suffix_test_data, resolve_team_suffix),
    ("test_resolve_sport_label_by_jobs_key", by_jobs_key_test_data, resolve_sport_label_by_jobs_key),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
