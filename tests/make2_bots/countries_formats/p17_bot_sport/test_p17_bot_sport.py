"""
Tests
"""

import pytest
from typing import Callable

from load_one_data import dump_diff, one_dump_test
from ArWikiCats.make_bots.countries_formats.p17_bot_sport_new import get_p17_with_sport_new, SPORT_FORMATS_ENAR_P17_TEAM
from ArWikiCats.new_resolvers.translations_resolvers_v2.countries_names_sport_multi_v2 import sports_formatted_data

# =========================================================
#                   get_p17_with_sport_new
# =========================================================

data_0 = {
    "sweden national under-21 football team managers": "مدربو منتخب السويد لكرة القدم تحت 21 سنة",
    "france national under-21 football team": "منتخب فرنسا لكرة القدم تحت 21 سنة",
    "germany national under-21 football team managers": "مدربو منتخب ألمانيا لكرة القدم تحت 21 سنة",
    "colombia national under-20 football team managers": "مدربو منتخب كولومبيا لكرة القدم تحت 20 سنة",
    "brazil national under-23 football team results": "نتائج منتخب البرازيل لكرة القدم تحت 23 سنة",
    "australia national men's under-23 soccer team": "منتخب أستراليا لكرة القدم تحت 23 سنة للرجال",
}


@pytest.mark.parametrize("category, expected", data_0.items(), ids=data_0.keys())
@pytest.mark.fast
def test_get_p17_with_sport_1(category: str, expected: str) -> None:
    label1 = get_p17_with_sport_new(category)
    assert label1 == expected

# =========================================================
#                   DUMP
# =========================================================


TEMPORAL_CASES = [
    ("test_get_p17_with_sport_1", data_0, get_p17_with_sport_new),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback, do_strip=False)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


@pytest.mark.skip
def test_compare_data():
    # SPORT_FORMATS_ENAR_P17_TEAM
    # sports_formatted_data
    same_keys = {x: v for x, v in SPORT_FORMATS_ENAR_P17_TEAM.items() if x in sports_formatted_data and sports_formatted_data[x] == v}
    dump_diff(same_keys, "same_keys")

    diff_value = {x: v for x, v in SPORT_FORMATS_ENAR_P17_TEAM.items() if x in sports_formatted_data and sports_formatted_data[x] != v}
    dump_diff(diff_value, "same_keys_diff_value")
    assert same_keys == {}, f"Found same keys in both data sets: {same_keys}"
