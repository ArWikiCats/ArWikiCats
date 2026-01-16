"""
Tests
"""

from typing import Callable

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.countries_names_with_sports.p17_sport_to_move_under import resolve_sport_under_labels

# =========================================================
#
# =========================================================

data_no_nats = {
    "softball national youth womens under-24 teams": "منتخبات كرة لينة تحت 24 سنة للشابات",
    "national mens under-19 softball teams": "منتخبات كرة لينة تحت 19 سنة للرجال",
    "multi-national womens under-19 football teams": "منتخبات كرة قدم تحت 19 سنة متعددة الجنسيات للسيدات",
}

data_with_nats = {
    "egypt under-19 international players": "لاعبون تحت 19 سنة دوليون من مصر",
    "aruba men's under-20 international footballers": "لاعبو منتخب أروبا تحت 20 سنة لكرة القدم للرجال",
    "egypt amateur under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للهواة",
    "egypt amateur under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للهواة",
    "egypt amateur under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للهواة",
    "egypt amateur under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للهواة",
    "egypt men's a' under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للرجال للمحليين",
    "egypt men's a' under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للرجال للمحليين",
    "egypt men's a' under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للرجال للمحليين",
    "egypt men's a' under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للرجال للمحليين",
    "egypt men's b under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم الرديف للرجال",
    "egypt men's b under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم الرديف للرجال",
    "egypt men's b under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم الرديف للرجال",
    "egypt men's b under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم الرديف للرجال",
    "egypt men's under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للرجال",
    "egypt men's under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للرجال",
    "egypt men's under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للرجال",
    "egypt men's under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للرجال",
    "egypt men's youth under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للشباب",
    "egypt men's youth under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للشباب",
    "egypt men's youth under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للشباب",
    "egypt men's youth under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للشباب",
    "egypt under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم",
    "egypt under-19 international managers": "مدربون تحت 19 سنة دوليون من مصر",
    "egypt under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم",
    "egypt under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم",
    "egypt under-20 international managers": "مدربون تحت 20 سنة دوليون من مصر",
    "egypt under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم",
    "egypt women's under-19 international footballers": "لاعبات منتخب مصر تحت 19 سنة لكرة القدم للسيدات",
    "egypt women's under-19 international soccer players": "لاعبات منتخب مصر تحت 19 سنة لكرة القدم للسيدات",
    "egypt women's under-20 international footballers": "لاعبات منتخب مصر تحت 20 سنة لكرة القدم للسيدات",
    "egypt women's under-20 international soccer players": "لاعبات منتخب مصر تحت 20 سنة لكرة القدم للسيدات",
    "egypt women's youth under-19 international footballers": "لاعبات منتخب مصر تحت 19 سنة لكرة القدم للشابات",
    "egypt women's youth under-19 international soccer players": "لاعبات منتخب مصر تحت 19 سنة لكرة القدم للشابات",
    "egypt women's youth under-20 international footballers": "لاعبات منتخب مصر تحت 20 سنة لكرة القدم للشابات",
    "egypt women's youth under-20 international soccer players": "لاعبات منتخب مصر تحت 20 سنة لكرة القدم للشابات",
    "egypt youth under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للشباب",
    "egypt youth under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للشباب",
    "egypt youth under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للشباب",
    "egypt youth under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للشباب",
    "lithuania men's under-21 international footballers": "لاعبو منتخب ليتوانيا تحت 21 سنة لكرة القدم للرجال",
    "mauritania men's under-20 international footballers": "لاعبو منتخب موريتانيا تحت 20 سنة لكرة القدم للرجال",
    "yemen under-13 international footballers": "لاعبو منتخب اليمن تحت 13 سنة لكرة القدم",
    "yemen under-14 international footballers": "لاعبو منتخب اليمن تحت 14 سنة لكرة القدم",
}


@pytest.mark.parametrize("category, expected", data_no_nats.items(), ids=data_no_nats.keys())
@pytest.mark.fast
def test_data_no_nats(category: str, expected: str) -> None:
    label2 = resolve_sport_under_labels(category)
    assert label2 == expected


@pytest.mark.parametrize("category, expected", data_with_nats.items(), ids=data_with_nats.keys())
@pytest.mark.fast
def test_data_with_nats(category: str, expected: str) -> None:
    label2 = resolve_sport_under_labels(category)
    assert label2 == expected


# =========================================================
#           DUMP
# =========================================================


TEMPORAL_CASES = [
    ("test_data_no_nats", data_no_nats, resolve_sport_under_labels),
    ("test_data_with_nats", data_with_nats, resolve_sport_under_labels),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback, do_strip=False)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
