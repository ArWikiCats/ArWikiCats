"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.films_resolvers.resolve_films_labels_and_time import get_films_key_tyty_new_and_time

fast_data_with_nats = {
    "northern ireland": "",
    "northern ireland films 2020": "",
    "2020 northern ireland films": "أفلام أيرلندية شمالية في 2020",
    "2020 northern ireland": "",
    "2020 Australian children's animated superhero film characters": "شخصيات أفلام رسوم متحركة أبطال خارقين أسترالية للأطفال في 2020",
    "20th-century supernatural thriller films": "أفلام إثارة خارقة للطبيعة في القرن 20",
    "20th-century american animated short television series": "مسلسلات تلفزيونية رسوم متحركة قصيرة أمريكية في القرن 20",
    "20th-century american drama television series": "مسلسلات تلفزيونية درامية أمريكية في القرن 20",
    # nats
    "20th-century action classical albums": "ألبومات كلاسيكية حركة في القرن 20",
    "20th-century yemeni action classical albums": "ألبومات كلاسيكية حركة يمنية في القرن 20",
    "20th-century yemeni novellas": "روايات قصيرة يمنية في القرن 20",
    "20th-century yemeni films": "أفلام يمنية في القرن 20",
    "20th-century Yemeni action films": "أفلام حركة يمنية في القرن 20",
    "20th-century Yemeni action drama films": "أفلام حركة درامية يمنية في القرن 20",
    "20th-century Yemeni upcoming horror films": "أفلام رعب قادمة يمنية في القرن 20",
    "20th-century Yemeni horror upcoming films": "أفلام رعب قادمة يمنية في القرن 20",
    "20th-century Yemeni upcoming films": "أفلام قادمة يمنية في القرن 20",
    "20th-century heist japanese horror films": "أفلام سرقة رعب يابانية في القرن 20",
    "20th-century Yemeni action thriller adult animated supernatural films": "أفلام إثارة حركة رسوم متحركة خارقة للطبيعة للكبار يمنية في القرن 20",
}

fast_data_no_nats = {
    # films keys
    "2020s 3d low-budget films": "أفلام ثلاثية الأبعاد منخفضة التكلفة في عقد 2020",
    "2020s low-budget 3d films": "أفلام ثلاثية الأبعاد منخفضة التكلفة في عقد 2020",
    "2020s heist historical television commercials": "إعلانات تجارية تلفزيونية سرقة تاريخية في عقد 2020",
    "2020s adult animated supernatural films": "أفلام رسوم متحركة خارقة للطبيعة للكبار في عقد 2020",
    "2020s heist holocaust films": "أفلام سرقة هولوكوستية في عقد 2020",
    "2020s heist hood films": "أفلام سرقة هود في عقد 2020",
    "2020s heist horror films": "أفلام سرقة رعب في عقد 2020",
    "2020s heist independent films": "أفلام سرقة مستقلة في عقد 2020",
    "2020s heist interactive films": "أفلام سرقة تفاعلية في عقد 2020",
    "2020s heist internet films": "أفلام سرقة إنترنت في عقد 2020",
    "2020s heist joker films": "أفلام سرقة جوكر في عقد 2020",
    "2020s heist kaiju films": "أفلام سرقة كايجو في عقد 2020",
    "20th-century heist kung fu films": "أفلام سرقة كونغ فو في القرن 20",
    "20th-century heist latin films": "أفلام سرقة لاتينية في القرن 20",
    "20th-century heist legal films": "أفلام سرقة قانونية في القرن 20",
    "20th-century psychological horror black-and-white films": "أفلام رعب نفسي أبيض وأسود في القرن 20",
    "20th-century psychological horror bollywood films": "أفلام رعب نفسي بوليوود في القرن 20",
    "20th-century action sports films": "أفلام حركة رياضية في القرن 20",
    "20th-century action spy films": "أفلام حركة تجسسية في القرن 20",
    "20th-century action street fighter films": "أفلام حركة قتال شوارع في القرن 20",
    "20th-century action student films": "أفلام حركة طلاب في القرن 20",
    "20th-century action submarines films": "أفلام حركة غواصات في القرن 20",
    "20th-century action super robot films": "أفلام حركة آلية خارقة في القرن 20",
    "20th-century action superhero films": "أفلام حركة أبطال خارقين في القرن 20",
    "20th-century action supernatural films": "أفلام حركة خارقة للطبيعة في القرن 20",
    "20th-century action supernatural drama films": "أفلام حركة دراما خارقة للطبيعة في القرن 20",
    "20th-century action survival films": "أفلام حركة البقاء على قيد الحياة في القرن 20",
    "20th-century action teen films": "أفلام حركة مراهقة في القرن 20",
    "20th-century action thriller 3d films": "أفلام إثارة حركة ثلاثية الأبعاد في القرن 20",
    "20th-century action thriller 4d films": "أفلام إثارة حركة رباعية الأبعاد في القرن 20",
    "20th-century action thriller action films": "أفلام إثارة حركة حركة في القرن 20",
    "20th-century action thriller action comedy films": "أفلام إثارة حركة حركة كوميدية في القرن 20",
    "20th-century action thriller adaptation films": "أفلام إثارة حركة مقتبسة في القرن 20",
    "20th-century action thriller adult animated films": "أفلام إثارة حركة رسوم متحركة للكبار في القرن 20",
    "20th-century action thriller adult animated drama films": "أفلام إثارة حركة رسوم متحركة دراما للكبار في القرن 20",
    "20th-century action thriller adult animated supernatural films": "أفلام إثارة حركة رسوم متحركة خارقة للطبيعة للكبار في القرن 20",
    "20th-century action thriller adventure films": "أفلام إثارة حركة مغامرات في القرن 20",
    "20th-century action thriller animated films": "أفلام إثارة حركة رسوم متحركة في القرن 20",
    "20th-century action thriller animated science films": "أفلام إثارة حركة علمية رسوم متحركة في القرن 20",
    "20th-century action thriller animated short films": "أفلام إثارة حركة رسوم متحركة قصيرة في القرن 20",
    "20th-century psychological horror buddy films": "أفلام رعب نفسي رفقاء في القرن 20",
    "2010 psychological horror cancelled films": "أفلام رعب نفسي ملغية في 2010",
}


@pytest.mark.parametrize("category, expected", fast_data_no_nats.items(), ids=fast_data_no_nats.keys())
@pytest.mark.fast
def test_get_films_key_tyty(category: str, expected: str) -> None:
    label2 = get_films_key_tyty_new_and_time(category)
    assert label2 == expected


@pytest.mark.parametrize("category, expected", fast_data_with_nats.items(), ids=fast_data_with_nats.keys())
@pytest.mark.fast
def test_fast_data_with_nats(category: str, expected: str) -> None:
    label2 = get_films_key_tyty_new_and_time(category)
    assert label2 == expected


to_test = [
    ("test_get_films_key_tyty", fast_data_no_nats, get_films_key_tyty_new_and_time),
    ("test_fast_data_with_nats", fast_data_with_nats, get_films_key_tyty_new_and_time),
]


@pytest.mark.parametrize("name,data, callback", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
