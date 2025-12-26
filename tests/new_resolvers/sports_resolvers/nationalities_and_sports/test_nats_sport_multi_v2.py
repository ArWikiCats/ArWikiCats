"""
Tests
"""

from typing import Callable

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.sports_resolvers.nationalities_and_sports import resolve_nats_sport_multi_v2

data6 = {
    "georgia (country) freestyle wrestling federation": "الاتحاد الجورجي للمصارعة الحرة",
    "philippine sailing (sport) federation": "الاتحاد الفلبيني لرياضة الإبحار",
}

ar_sport_team_data = {
    # "Yemeni football championships clubs": "أندية بطولة اليمن لكرة القدم",
    "british softball championshipszz": "بطولة المملكة المتحدة للكرة اللينة",
    "ladies british softball tour": "بطولة المملكة المتحدة للكرة اللينة للسيدات",
    "british football tour": "بطولة المملكة المتحدة لكرة القدم",
    "Yemeni football championships": "بطولة اليمن لكرة القدم",
    "german figure skating championships": "بطولة ألمانيا للتزلج الفني",
    "british figure skating championships": "بطولة المملكة المتحدة للتزلج الفني",
}


sport_jobs_female_data = {
    "dominican republic national football teams": "منتخبات كرة قدم وطنية دومينيكانية",
    "yemeni national softball teams": "منتخبات كرة لينة وطنية يمنية",
    "Women's National Basketball League": "الدوري الوطني لكرة السلة للسيدات",
    "northern ireland": "",
}


@pytest.mark.parametrize("category, expected_key", ar_sport_team_data.items(), ids=ar_sport_team_data.keys())
@pytest.mark.fast
def test_ar_sport_team_data(category: str, expected_key: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected_key


@pytest.mark.parametrize("category, expected_key", sport_jobs_female_data.items(), ids=sport_jobs_female_data.keys())
@pytest.mark.fast
def test_sport_jobs_female_data(category: str, expected_key: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected_key


TEMPORAL_CASES = [
    ("test_resolve_nats_sport_multi_v2", data6, resolve_nats_sport_multi_v2),
    ("test_ar_sport_team_data", ar_sport_team_data, resolve_nats_sport_multi_v2),
    ("test_sport_jobs_female_data", sport_jobs_female_data, resolve_nats_sport_multi_v2),
]


@pytest.mark.dump
@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback, do_strip=True)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
