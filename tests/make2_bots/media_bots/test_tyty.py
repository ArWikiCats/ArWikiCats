"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.media_bots.film_keys_bot_tyty import search_multi
from ArWikiCats.make_bots.media_bots.tyty_new_format import search_multi_new

test_data = {
    "lgbtq-related low-budget": "{tyty} متعلقة بإل جي بي تي كيو منخفضة التكلفة",
    "lgbtq-related upcoming": "{tyty} متعلقة بإل جي بي تي كيو قادمة",
    "low-budget lgbtq-related": "{tyty} متعلقة بإل جي بي تي كيو منخفضة التكلفة",
    "upcoming lgbtq-related": "{tyty} متعلقة بإل جي بي تي كيو قادمة",
    "black christmas": "{tyty} سوداء عيد الميلاد",
    "black-and-white christmas": "{tyty} أبيض وأسود عيد الميلاد",
    "upcoming christmas": "{tyty} قادمة عيد الميلاد",
    "christmas upcoming": "{tyty} قادمة عيد الميلاد",
    "action comedy drama": "{tyty} حركة كوميدية درامية",
    "action comedy fiction": "{tyty} حركة كوميدية خيالية",
    "action comedy thriller": "{tyty} حركة كوميدية إثارة",
    "christmas low-budget": "{tyty} عيد الميلاد منخفضة التكلفة",
    "low-budget christmas": "{tyty} عيد الميلاد منخفضة التكلفة",
    "low-budget upcoming": "{tyty} منخفضة التكلفة قادمة",
    "upcoming low-budget": "{tyty} منخفضة التكلفة قادمة",
    "heist kung fu": "{tyty} سرقة كونغ فو",
    "heist historical": "{tyty} سرقة تاريخية",
    "historical heist": "{tyty} سرقة تاريخية",
    "action thriller adult animated supernatural": "{tyty} إثارة حركة رسوم متحركة خارقة للطبيعة للكبار",
    "psychological horror cancelled": "{tyty} رعب نفسي ملغية",

}

test_data_2 = {
    "musical comedy drama": "{tyty} كوميديا موسيقية درامية",
    "musical comedy fiction": "{tyty} كوميديا موسيقية خيالية",
    "musical comedy horror": "{tyty} كوميديا موسيقية رعب",
    "romantic comedy drama": "{tyty} كوميديا رومانسية درامية",
    "romantic comedy fiction": "{tyty} كوميديا رومانسية خيالية",
    "romantic comedy horror": "{tyty} كوميديا رومانسية رعب",
    "zombie comedy drama": "{tyty} كوميديا الزومبي درامية",
    "zombie comedy fiction": "{tyty} كوميديا الزومبي خيالية",
    "zombie comedy horror": "{tyty} كوميديا الزومبي رعب",
    "zombie comedy thriller": "{tyty} كوميديا الزومبي إثارة"
}


@pytest.mark.parametrize("category, expected", test_data.items(), ids=list(test_data.keys()))
@pytest.mark.fast
def test_search_multi(category: str, expected: str) -> None:
    label1 = search_multi(category)
    assert label1 == expected

    label2 = search_multi_new(category)
    assert label2 == expected


to_test = [
    ("test_search_multi", test_data, search_multi),
    ("test_search_multi_new", test_data, search_multi_new),

    ("test_search_multi_test_data_2", test_data_2, search_multi),
    ("test_search_multi_new_test_data_2", test_data_2, search_multi_new),
]


@pytest.mark.parametrize("name,data, callback", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str], callback) -> None:

    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    # dump_diff(expected, f"{name}_expected")

    assert diff_result == expected, f"Differences found: {len(diff_result)}"
