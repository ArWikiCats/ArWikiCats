"""
Tests
"""

import pytest
from typing import Callable

from load_one_data import dump_diff, one_dump_test
from ArWikiCats.make_bots.countries_formats.p17_bot_sport import (
    get_sport_formts_enar_p17_jobs,
)

# =========================================================
#                   get_sport_formts_enar_p17_jobs
# =========================================================


data2 = {
    "football manager history": "تاريخ مدربو كرة قدم {}",
    "international soccer players": "لاعبو كرة قدم دوليون من {}",
    "international women's rugby sevens players": "لاعبات سباعيات رجبي دوليات من {}",
    "men's international soccer players": "لاعبو كرة قدم دوليون من {}",
    "summer olympics football": "كرة قدم {} في الألعاب الأولمبية الصيفية",
    "winter olympics softball": "كرة لينة {} في الألعاب الأولمبية الشتوية",
    "women's international rugby union players": "لاعبات اتحاد رجبي دوليات من {}",
}


@pytest.mark.parametrize("category, expected_key", data2.items(), ids=list(data2.keys()))
@pytest.mark.fast
def test_get_sport_formts_enar_p17_jobs(category: str, expected_key: str) -> None:
    label = get_sport_formts_enar_p17_jobs(category)
    assert label == expected_key


# =========================================================
#                   DUMP
# =========================================================

TEMPORAL_CASES = [
    ("test_get_sport_formts_enar_p17_jobs", data2, get_sport_formts_enar_p17_jobs),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback, do_strip=False)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
