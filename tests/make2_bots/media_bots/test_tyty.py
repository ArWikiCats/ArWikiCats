"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.media_bots.tyty_new_format import search_multi_new

keys_in_films_key_333 = {
    "action comedy": "{tyty} حركة كوميدية",
    "action thriller": "{tyty} حركة إثارة",
    "adult animated drama": "{tyty} رسوم متحركة للكبار درامية",
    "adult animated supernatural": "{tyty} رسوم متحركة للكبار خارقة للطبيعة",
    "animated science": "{tyty} رسوم متحركة علمية",
    "animated short": "{tyty} رسوم متحركة قصيرة",
    "black comedy": "{tyty} سوداء كوميدية",
    "children's animated": "{tyty} أطفال رسوم متحركة",
    "children's comedy": "{tyty} أطفال كوميدية",
    "comedy drama": "{tyty} كوميدية درامية",
    "comedy fiction": "{tyty} كوميدية خيالية",
    "comedy horror": "{tyty} كوميدية رعب",
    "comedy thriller": "{tyty} كوميدية إثارة",
    "crime comedy": "{tyty} جريمة كوميدية",
    "crime thriller": "{tyty} جريمة إثارة",
    "criminal comedy": "{tyty} جنائية كوميدية",
    "detective fiction": "{tyty} مباحث خيالية",
    "erotic thriller": "{tyty} إغرائية إثارة",
    "legal drama": "{tyty} قانونية درامية",
    "legal thriller": "{tyty} قانونية إثارة",
    "musical comedy": "{tyty} موسيقية كوميدية",
    "political fiction": "{tyty} سياسية خيالية",
    "political thriller": "{tyty} سياسية إثارة",
    "psychological horror": "{tyty} نفسية رعب",
    "psychological thriller": "{tyty} نفسية إثارة",
    "romantic comedy": "{tyty} رومانسية كوميدية",
    "science fantasy": "{tyty} علمية فانتازيا",
    "science fiction": "{tyty} علمية خيالية",
    "science fiction action": "{tyty} خيال علمي حركة",
    "science fiction thriller": "{tyty} خيال علمي إثارة",
    "silent short": "{tyty} صامتة قصيرة",
    "speculative fiction": "{tyty} تأملية خيالية",
    "supernatural drama": "{tyty} خارقة للطبيعة درامية",
    "zombie comedy": "{tyty} زومبي كوميدية"
}


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

test_data_3 = {
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


@pytest.mark.parametrize("category, expected", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_search_multi(category: str, expected: str) -> None:
    label1 = search_multi_new(category)
    assert label1 == expected


test_put_label_last_data = {
    "action lgbtq-related": "{tyty} حركة متعلقة بإل جي بي تي كيو",
    "lgbtq-related action": "{tyty} حركة متعلقة بإل جي بي تي كيو",
    "lgbtq-related drama": "{tyty} درامية متعلقة بإل جي بي تي كيو",
    "lgbtq-related horror": "{tyty} رعب متعلقة بإل جي بي تي كيو",
    "lgbtq-related latin": "{tyty} لاتينية متعلقة بإل جي بي تي كيو",

    "low-budget science": "{tyty} علمية منخفضة التكلفة",
    "christmas science": "{tyty} علمية عيد الميلاد",
    "upcoming horror": "{tyty} رعب قادمة",
    "3d low-budget": "{tyty} ثلاثية الأبعاد منخفضة التكلفة",
    "low-budget 3d": "{tyty} ثلاثية الأبعاد منخفضة التكلفة",
    "low-budget action": "{tyty} حركة منخفضة التكلفة",
}


@pytest.mark.parametrize("category, expected", test_put_label_last_data.items(), ids=test_put_label_last_data.keys())
@pytest.mark.fast
def test_put_label_last(category: str, expected: str) -> None:

    label2 = search_multi_new(category)
    assert label2 == expected


fast_data2 = {
    "heist kung fu": "{tyty} سرقة كونغ فو",
    "heist historical": "{tyty} سرقة تاريخية",
    "action thriller adult animated supernatural": "{tyty} إثارة حركة رسوم متحركة خارقة للطبيعة للكبار",
    "psychological horror cancelled": "{tyty} رعب نفسي ملغية",
}


@pytest.mark.parametrize("category, expected", fast_data2.items(), ids=fast_data2.keys())
@pytest.mark.fast
def test_search_multi_z(category: str, expected: str) -> None:
    label2 = search_multi_new(category)
    assert label2 == expected


to_test = [
    ("test_search_multi", test_data, search_multi_new),
    ("test_search_multi_new", test_data, search_multi_new),
    ("test_search_multi_test_data_3", test_data_3, search_multi_new),
    ("test_put_label_last", test_put_label_last_data, search_multi_new),
    ("test_search_multi_z", fast_data2, search_multi_new),
]


@pytest.mark.parametrize("name,data, callback", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str], callback) -> None:

    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    # dump_diff(expected, f"{name}_expected")

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
