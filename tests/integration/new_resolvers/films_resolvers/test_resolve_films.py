"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.films_resolvers.resolve_films_labels import get_films_key_tyty_new

fast_data_with_nats = {
    "animated short film comics": "قصص مصورة رسوم متحركة قصيرة",
    # "Category:American animated television films": "تصنيف:أفلام رسوم متحركة تلفزيونية أمريكية",
    "northern ireland": "",
    "supernatural thriller films": "أفلام إثارة خارقة للطبيعة",
    "american animated short television series": "مسلسلات تلفزيونية رسوم متحركة قصيرة أمريكية",
    "american drama television series": "مسلسلات تلفزيونية درامية أمريكية",
    # nats
    "action classical albums": "ألبومات كلاسيكية حركة",
    "yemeni action classical albums": "ألبومات كلاسيكية حركة يمنية",
    "yemeni novellas": "روايات قصيرة يمنية",
    "yemeni films": "أفلام يمنية",
    "Yemeni action films": "أفلام حركة يمنية",
    "Yemeni action drama films": "أفلام حركة درامية يمنية",
    "Yemeni upcoming horror films": "أفلام رعب قادمة يمنية",
    "Yemeni horror upcoming films": "أفلام رعب قادمة يمنية",
    "Yemeni upcoming films": "أفلام قادمة يمنية",
    "heist japanese horror films": "أفلام سرقة رعب يابانية",
    "Yemeni action thriller adult animated supernatural films": "أفلام إثارة حركة رسوم متحركة خارقة للطبيعة للكبار يمنية",
}

fast_data_no_nats = {
    # films keys
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
    "action supernatural films": "أفلام حركة خارقة للطبيعة",
    "action supernatural drama films": "أفلام حركة دراما خارقة للطبيعة",
    "action survival films": "أفلام حركة البقاء على قيد الحياة",
    "action teen films": "أفلام حركة مراهقة",
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


@pytest.mark.parametrize("category, expected", fast_data_no_nats.items(), ids=fast_data_no_nats.keys())
@pytest.mark.fast
def test_get_films_key_tyty(category: str, expected: str) -> None:
    label2 = get_films_key_tyty_new(category)
    assert label2 == expected


@pytest.mark.parametrize("category, expected", fast_data_with_nats.items(), ids=fast_data_with_nats.keys())
@pytest.mark.fast
def test_fast_data_with_nats(category: str, expected: str) -> None:
    label2 = get_films_key_tyty_new(category)
    assert label2 == expected


to_test = [
    ("test_get_films_key_tyty", fast_data_no_nats, get_films_key_tyty_new),
    ("test_fast_data_with_nats", fast_data_with_nats, get_films_key_tyty_new),
]


@pytest.mark.parametrize("name,data, callback", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
