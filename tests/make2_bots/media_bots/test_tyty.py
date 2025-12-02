"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.media_bots.film_keys_bot_tyty import search_multi

test_data = {
    "christmas upcoming": "{tyty} قادمة عيد الميلاد",
    "upcoming christmas": "{tyty} عيد الميلاد قادمة",
    "action comedy drama": "{tyty} حركة كوميدية درامية",
    "action comedy fiction": "{tyty} حركة كوميدية خيالية",
    "action comedy thriller": "{tyty} حركة كوميدية إثارة",
    "adult animated supernatural drama": "{tyty} رسوم متحركة خارقة للطبيعة للكبار درامية",
    "animated science fantasy": "{tyty} علمية رسوم متحركة فانتازيا",
    "animated science fiction": "{tyty} علمية رسوم متحركة خيالية",
    "black comedy drama": "{tyty} كوميدية سوداء درامية",
    "black comedy fiction": "{tyty} كوميدية سوداء خيالية",
    "black comedy horror": "{tyty} كوميدية سوداء رعب",
    "black comedy thriller": "{tyty} كوميدية سوداء إثارة",
    "children's animated science": "{tyty} رسوم متحركة أطفال علمية",
    "children's animated short": "{tyty} رسوم متحركة أطفال قصيرة",
    "children's comedy drama": "{tyty} أطفال كوميدية درامية",
    "children's comedy fiction": "{tyty} أطفال كوميدية خيالية",
    "children's comedy thriller": "{tyty} أطفال كوميدية إثارة",
    "christmas low-budget": "{tyty} عيد الميلاد منخفضة التكلفة",
    "crime comedy drama": "{tyty} جنائية كوميدية درامية",
    "crime comedy fiction": "{tyty} جنائية كوميدية خيالية",
    "crime comedy horror": "{tyty} جنائية كوميدية رعب",
    "crime comedy thriller": "{tyty} جنائية كوميدية إثارة",
    "criminal comedy drama": "{tyty} كوميديا الجريمة درامية",
    "criminal comedy fiction": "{tyty} كوميديا الجريمة خيالية",
    "criminal comedy horror": "{tyty} كوميديا الجريمة رعب",
    "criminal comedy thriller": "{tyty} كوميديا الجريمة إثارة",
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
    "lgbtrelated low-budget": "{tyty} متعلقة بإل جي بي تي منخفضة التكلفة",
    "lgbtrelated upcoming": "{tyty} متعلقة بإل جي بي تي قادمة",
    "low-budget christmas": "{tyty} عيد الميلاد منخفضة التكلفة",
    "low-budget lgbt-related": "{tyty} متعلقة بإل جي بي تي منخفضة التكلفة",
    "low-budget lgbtq-related": "{tyty} متعلقة بإل جي بي تي كيو منخفضة التكلفة",
    "low-budget lgbtqrelated": "{tyty} متعلقة بإل جي بي تي كيو منخفضة التكلفة",
    "low-budget lgbtrelated": "{tyty} متعلقة بإل جي بي تي منخفضة التكلفة",
    "low-budget upcoming": "{tyty} منخفضة التكلفة قادمة",
    "musical comedy drama": "{tyty} موسيقية كوميديا درامية",
    "musical comedy fiction": "{tyty} موسيقية كوميديا خيالية",
    "musical comedy horror": "{tyty} موسيقية كوميدية رعب",
    "musical comedy thriller": "{tyty} كوميديا موسيقية إثارة",
    "romantic comedy drama": "{tyty} رومانسية كوميديا درامية",
    "romantic comedy fiction": "{tyty} رومانسية كوميديا خيالية",
    "romantic comedy horror": "{tyty} رومانسية كوميدية رعب",
    "romantic comedy thriller": "{tyty} كوميديا رومانسية إثارة",
    "science fiction action thriller": "{tyty} خيال علمي وحركة إثارة",
    "upcoming christmas": "{tyty} عيد الميلاد قادمة",
    "upcoming lgbt-related": "{tyty} متعلقة بإل جي بي تي قادمة",
    "upcoming lgbtq-related": "{tyty} متعلقة بإل جي بي تي كيو قادمة",
    "upcoming lgbtqrelated": "{tyty} متعلقة بإل جي بي تي كيو قادمة",
    "upcoming lgbtrelated": "{tyty} متعلقة بإل جي بي تي قادمة",
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
