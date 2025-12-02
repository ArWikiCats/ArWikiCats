"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.media_bots.film_keys_bot_tyty import search_multi

test_data = {
    "upcoming christmas": "{tyty} قادمة عيد الميلاد",
    "christmas upcoming": "{tyty} قادمة عيد الميلاد",
    "action comedy drama": "{tyty} حركة كوميدية درامية",
    "action comedy fiction": "{tyty} حركة كوميدية خيالية",
    "action comedy thriller": "{tyty} حركة كوميدية إثارة",
    "christmas low-budget": "{tyty} عيد الميلاد منخفضة التكلفة",
    "lgbt-related lgbtq-related": "{tyty} متعلقة بإل جي بي تي متعلقة بإل جي بي تي كيو",
    "lgbt-related lgbtqrelated": "{tyty} متعلقة بإل جي بي تي متعلقة بإل جي بي تي كيو",
    "lgbt-related low-budget": "{tyty} متعلقة بإل جي بي تي منخفضة التكلفة",
    "lgbt-related upcoming": "{tyty} متعلقة بإل جي بي تي قادمة",
    "lgbtq-related lgbt-related": "{tyty} متعلقة بإل جي بي تي متعلقة بإل جي بي تي كيو",
    "lgbtq-related low-budget": "{tyty} متعلقة بإل جي بي تي كيو منخفضة التكلفة",
    "lgbtq-related upcoming": "{tyty} متعلقة بإل جي بي تي كيو قادمة",
    "lgbtqrelated lgbt-related": "{tyty} متعلقة بإل جي بي تي متعلقة بإل جي بي تي كيو",
    "lgbtqrelated low-budget": "{tyty} متعلقة بإل جي بي تي كيو منخفضة التكلفة",
    "lgbtqrelated upcoming": "{tyty} متعلقة بإل جي بي تي كيو قادمة",
    "lgbt-related low-budget": "{tyty} متعلقة بإل جي بي تي منخفضة التكلفة",
    "lgbt-related upcoming": "{tyty} متعلقة بإل جي بي تي قادمة",
    "low-budget christmas": "{tyty} عيد الميلاد منخفضة التكلفة",
    "low-budget lgbt-related": "{tyty} متعلقة بإل جي بي تي منخفضة التكلفة",
    "low-budget lgbtq-related": "{tyty} متعلقة بإل جي بي تي كيو منخفضة التكلفة",
    "low-budget lgbtqrelated": "{tyty} متعلقة بإل جي بي تي كيو منخفضة التكلفة",
    "low-budget lgbt-related": "{tyty} متعلقة بإل جي بي تي منخفضة التكلفة",
    "low-budget upcoming": "{tyty} منخفضة التكلفة قادمة",
    "musical comedy drama": "{tyty} موسيقية كوميديا درامية",
    "musical comedy fiction": "{tyty} موسيقية كوميديا خيالية",
    "musical comedy horror": "{tyty} موسيقية كوميدية رعب",
    "romantic comedy drama": "{tyty} رومانسية كوميديا درامية",
    "romantic comedy fiction": "{tyty} رومانسية كوميديا خيالية",
    "romantic comedy horror": "{tyty} رومانسية كوميدية رعب",
    "upcoming lgbt-related": "{tyty} متعلقة بإل جي بي تي قادمة",
    "upcoming lgbtq-related": "{tyty} متعلقة بإل جي بي تي كيو قادمة",
    "upcoming lgbtqrelated": "{tyty} متعلقة بإل جي بي تي كيو قادمة",
    "upcoming lgbt-related": "{tyty} متعلقة بإل جي بي تي قادمة",
    "upcoming low-budget": "{tyty} منخفضة التكلفة قادمة",
    "zombie comedy drama": "{tyty} زومبي كوميديا درامية",
    "zombie comedy fiction": "{tyty} زومبي كوميديا خيالية",
    "zombie comedy horror": "{tyty} زومبي كوميدية رعب",
    "zombie comedy thriller": "{tyty} زومبي كوميديا إثارة"
}


@pytest.mark.parametrize("category, expected", test_data.items(), ids=list(test_data.keys()))
@pytest.mark.skip2
def test_search_multi(category: str, expected: str) -> None:
    label = search_multi(category)
    assert label == expected


to_test = [
    ("test_search_multi", test_data, search_multi),
]


@pytest.mark.parametrize("name,data, callback", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str], callback) -> None:

    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    # dump_diff(expected, f"{name}_expected")

    assert diff_result == expected, f"Differences found: {len(diff_result)}"
