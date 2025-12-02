"""
Tests
"""

import pytest
import json
from pathlib import Path
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.media_bots.film_keys_bot_tyty import search_multi


def fast_data1():
    file_path = Path("D:/categories_bot/len_data/films_mslslat.py/tyty_data.json")
    data = json.loads(file_path.read_text(encoding="utf-8"))

    return data # dict(list(data.items())[:10000])


test_data = {
    "action comedy drama": "{tyty} حركة كوميديا درامية",
    "action comedy fiction": "{tyty} حركة كوميديا خيالية",
    "action comedy thriller": "{tyty} حركة كوميديا إثارة",
    "adult animated supernatural drama": "{tyty} رسوم متحركة للكبار دراما خارقة للطبيعة",
    "animated science fantasy": "{tyty} رسوم متحركة فنتازيا علمية",
    "animated science fiction": "{tyty} رسوم متحركة خيال علمي",
    "black comedy drama": "{tyty} سوداء كوميديا درامية",
    "black comedy fiction": "{tyty} سوداء كوميديا خيالية",
    "black comedy horror": "{tyty} سوداء كوميدية رعب",
    "black comedy thriller": "{tyty} سوداء كوميديا إثارة",
    "children's animated science": "{tyty} أطفال علمية رسوم متحركة",
    "children's animated short": "{tyty} أطفال رسوم متحركة قصيرة",
    "children's comedy drama": "{tyty} أطفال كوميديا درامية",
    "children's comedy fiction": "{tyty} أطفال كوميديا خيالية",
    "children's comedy thriller": "{tyty} أطفال كوميديا إثارة",
    "christmas low-budget": "{tyty} منخفضة التكلفة عيد الميلاد",
    "christmas upcoming": "{tyty} قادمة عيد الميلاد",
    "crime comedy drama": "{tyty} جريمة كوميديا درامية",
    "crime comedy fiction": "{tyty} جريمة كوميديا خيالية",
    "crime comedy horror": "{tyty} جريمة كوميدية رعب",
    "crime comedy thriller": "{tyty} جريمة كوميديا إثارة",
    "criminal comedy drama": "{tyty} جنائية كوميديا درامية",
    "criminal comedy fiction": "{tyty} جنائية كوميديا خيالية",
    "criminal comedy horror": "{tyty} جنائية كوميدية رعب",
    "criminal comedy thriller": "{tyty} جنائية كوميديا إثارة",
    "lgbt-related lgbtq-related": "{tyty} متعلقة بإل جي بي تي كيو متعلقة بإل جي بي تي",
    "lgbt-related lgbtqrelated": "{tyty} متعلقة بإل جي بي تي كيو متعلقة بإل جي بي تي",
    "lgbt-related low-budget": "{tyty} منخفضة التكلفة متعلقة بإل جي بي تي",
    "lgbt-related upcoming": "{tyty} قادمة متعلقة بإل جي بي تي",
    "lgbtq-related lgbt-related": "{tyty} متعلقة بإل جي بي تي كيو متعلقة بإل جي بي تي",
    "lgbtq-related low-budget": "{tyty} منخفضة التكلفة متعلقة بإل جي بي تي كيو",
    "lgbtq-related upcoming": "{tyty} قادمة متعلقة بإل جي بي تي كيو",
    "lgbtqrelated lgbt-related": "{tyty} متعلقة بإل جي بي تي كيو متعلقة بإل جي بي تي",
    "lgbtqrelated low-budget": "{tyty} منخفضة التكلفة متعلقة بإل جي بي تي كيو",
    "lgbtqrelated upcoming": "{tyty} قادمة متعلقة بإل جي بي تي كيو",
    "lgbtrelated low-budget": "{tyty} منخفضة التكلفة متعلقة بإل جي بي تي",
    "lgbtrelated upcoming": "{tyty} قادمة متعلقة بإل جي بي تي",
    "low-budget christmas": "{tyty} منخفضة التكلفة عيد الميلاد",
    "low-budget lgbt-related": "{tyty} منخفضة التكلفة متعلقة بإل جي بي تي",
    "low-budget lgbtq-related": "{tyty} منخفضة التكلفة متعلقة بإل جي بي تي كيو",
    "low-budget lgbtqrelated": "{tyty} منخفضة التكلفة متعلقة بإل جي بي تي كيو",
    "low-budget lgbtrelated": "{tyty} منخفضة التكلفة متعلقة بإل جي بي تي",
    "low-budget upcoming": "{tyty} قادمة منخفضة التكلفة",
    "musical comedy drama": "{tyty} كوميديا موسيقية درامية",
    "musical comedy fiction": "{tyty} كوميديا موسيقية خيالية",
    "musical comedy horror": "{tyty} كوميديا موسيقية رعب",
    "musical comedy thriller": "{tyty} موسيقية كوميديا إثارة",
    "romantic comedy drama": "{tyty} كوميديا رومانسية درامية",
    "romantic comedy fiction": "{tyty} كوميديا رومانسية خيالية",
    "romantic comedy horror": "{tyty} كوميديا رومانسية رعب",
    "romantic comedy thriller": "{tyty} رومانسية كوميديا إثارة",
    "science fiction action thriller": "{tyty} خيال علمي إثارة حركة",
    "upcoming christmas": "{tyty} قادمة عيد الميلاد",
    "upcoming lgbt-related": "{tyty} قادمة متعلقة بإل جي بي تي",
    "upcoming lgbtq-related": "{tyty} قادمة متعلقة بإل جي بي تي كيو",
    "upcoming lgbtqrelated": "{tyty} قادمة متعلقة بإل جي بي تي كيو",
    "upcoming lgbtrelated": "{tyty} قادمة متعلقة بإل جي بي تي",
    "upcoming low-budget": "{tyty} قادمة منخفضة التكلفة",
    "zombie comedy drama": "{tyty} كوميديا الزومبي درامية",
    "zombie comedy fiction": "{tyty} كوميديا الزومبي خيالية",
    "zombie comedy horror": "{tyty} كوميديا الزومبي رعب",
    "zombie comedy thriller": "{tyty} كوميديا الزومبي إثارة"
}

test_data = fast_data1()


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
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
