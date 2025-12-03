"""
Tests
"""

import pytest

from ArWikiCats.make_bots.media_bots.film_keys_bot_tyty import get_films_key_tyty, search_multi
from ArWikiCats.make_bots.media_bots.tyty_new_format import get_films_key_tyty_new, search_multi_new

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


@pytest.mark.parametrize("category, expected", test_put_label_last_data.items(), ids=list(test_put_label_last_data.keys()))
@pytest.mark.fast
def test_put_label_last(category: str, expected: str) -> None:

    label1 = search_multi(category)
    assert label1 == expected

    label2 = search_multi_new(category)
    assert label2 == expected


fast_data1 = {
    "3d low-budget films": "أفلام ثلاثية الأبعاد منخفضة التكلفة",
    "low-budget 3d films": "أفلام ثلاثية الأبعاد منخفضة التكلفة",
    "heist historical television commercials": "إعلانات تجارية تلفزيونية سرقة تاريخية",
    "adult animated supernatural films": "أفلام رسوم متحركة خارقة للطبيعة للكبار",
    "heist holocaust films": "أفلام سرقة هولوكوستية",
    "heist hood films": "أفلام سرقة هود",
    "heist horror films": "أفلام سرقة رعب",
    "heist independent films": "أفلام سرقة مستقلة",
    "heist interactive films": "أفلام سرقة تفاعلية",
    "heist internet films": "أفلام سرقة إنترنت",
    "heist japanese horror films": "أفلام سرقة رعب يابانية",
    "heist joker films": "أفلام سرقة جوكر",
    "heist kaiju films": "أفلام سرقة كايجو",
    "heist kung fu films": "أفلام سرقة كونغ فو",
    "heist latin films": "أفلام سرقة لاتينية",
    "heist legal films": "أفلام سرقة قانونية",
    "psychological horror black-and-white films": "أفلام رعب نفسي أبيض وأسود",
    "psychological horror bollywood films": "أفلام رعب نفسي بوليوود",
    "action sports films": "أفلام حركة رياضية",
    "action spy films": "أفلام حركة تجسسية",
    "action street fighter films": "أفلام حركة قتال شوارع",
    "action student films": "أفلام حركة طلاب",
    "action submarines films": "أفلام حركة غواصات",
    "action super robot films": "أفلام حركة آلية خارقة",
    "action superhero films": "أفلام حركة خارقة",
    "action supernatural films": "أفلام حركة خارقة للطبيعة",
    "action supernatural drama films": "أفلام حركة دراما خارقة للطبيعة",
    "action survival films": "أفلام حركة البقاء على قيد الحياة",
    "action teen films": "أفلام حركة مراهقة",
    "action television films": "أفلام حركة تلفزيونية",
    "action thriller 3d films": "أفلام إثارة حركة ثلاثية الأبعاد",
    "action thriller 4d films": "أفلام إثارة حركة رباعية الأبعاد",
    "action thriller action films": "أفلام إثارة حركة حركة",
    "action thriller action comedy films": "أفلام إثارة حركة حركة كوميدية",
    "action thriller adaptation films": "أفلام إثارة حركة مقتبسة",
    "action thriller adult animated films": "أفلام إثارة حركة رسوم متحركة للكبار",
    "action thriller adult animated drama films": "أفلام إثارة حركة رسوم متحركة دراما للكبار",
    "action thriller adult animated supernatural films": "أفلام إثارة حركة رسوم متحركة خارقة للطبيعة للكبار",
    "action thriller adventure films": "أفلام إثارة حركة مغامرات",
    "action thriller animated films": "أفلام إثارة حركة رسوم متحركة",
    "action thriller animated science films": "أفلام إثارة حركة علمية رسوم متحركة",
    "action thriller animated short films": "أفلام إثارة حركة رسوم متحركة قصيرة",
    "psychological horror buddy films": "أفلام رعب نفسي رفقاء",
    "psychological horror cancelled films": "أفلام رعب نفسي ملغية",
}


fast_data2 = {
    "heist kung fu": "{tyty} سرقة كونغ فو",
    "heist historical": "{tyty} سرقة تاريخية",
    "action thriller adult animated supernatural": "{tyty} إثارة حركة رسوم متحركة خارقة للطبيعة للكبار",
    "psychological horror cancelled": "{tyty} رعب نفسي ملغية",
}


@pytest.mark.parametrize("category, expected", fast_data2.items(), ids=list(fast_data2.keys()))
@pytest.mark.fast
def test_search_multi(category: str, expected: str) -> None:
    label = search_multi(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", fast_data1.items(), ids=list(fast_data1.keys()))
@pytest.mark.fast
def test_get_films_key_tyty(category: str, expected: str) -> None:
    label1 = get_films_key_tyty(category)
    assert label1 == expected

    label2 = get_films_key_tyty_new(category)
    assert label2 == expected


to_test = [
    ("test_get_films_key_tyty", fast_data1, get_films_key_tyty),
    ("test_put_label_last", test_put_label_last_data, search_multi),
    ("test_search_multi", fast_data2, search_multi),
]

from load_one_data import dump_diff, one_dump_test


@pytest.mark.parametrize("name,data, callback", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str], callback) -> None:

    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
