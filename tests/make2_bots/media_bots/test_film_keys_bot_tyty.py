"""
Tests
"""

import pytest

from ArWikiCats.make_bots.media_bots.film_keys_bot_tyty import get_films_key_tyty

fast_data2 = {
    "3d low-budget films": "أفلام ثلاثية الأبعاد منخفضة التكلفة",
    "heist historical television commercials": "إعلانات تجارية تلفزيونية سرقة تاريخية",
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


@pytest.mark.parametrize("category, expected", fast_data2.items(), ids=list(fast_data2.keys()))
@pytest.mark.fast
def test_get_films_key_tyty(category: str, expected: str) -> None:
    label = get_films_key_tyty(category)
    assert label == expected
