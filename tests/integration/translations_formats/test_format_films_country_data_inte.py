#!/usr/bin/python3
"""Integration tests for format_films_country_data and"""

import pytest

from ArWikiCats.translations import Nat_women, film_keys_for_female
from ArWikiCats.translations_formats import MultiDataFormatterDataDouble, format_films_country_data


@pytest.fixture
def yc_bot() -> MultiDataFormatterDataDouble:
    # Template data with both nationality and sport placeholders
    formatted_data = {
        "{nat_en} films": "أفلام {nat_ar}",
        "{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}",
        "{nat_en} {film_key} television commercials": "إعلانات تجارية تلفزيونية {film_ar} {nat_ar}",
    }
    other_formatted_data = {
        "{film_key} films": "أفلام {film_ar}",
        "{film_key} television commercials": "إعلانات تجارية تلفزيونية {film_ar}",
    }

    # film_keys_for_female
    data_list2 = {
        "action comedy": "حركة كوميدية",
        "action thriller": "إثارة حركة",
        "action": "حركة",
        "drama": "درامية",
        "upcoming": "قادمة",
        "horror": "رعب",
        "black-and-white": "أبيض وأسود",
        "psychological horror": "رعب نفسي",
    }

    put_label_last = {
        "low-budget",
        "christmas",
        "lgbtq-related",
        "upcoming",
    }

    bot = format_films_country_data(
        formatted_data=formatted_data,
        data_list=Nat_women,
        key_placeholder="{nat_en}",
        value_placeholder="{nat_ar}",
        data_list2=film_keys_for_female,
        key2_placeholder="{film_key}",
        value2_placeholder="{film_ar}",
        text_after="",
        text_before="",
        other_formatted_data=other_formatted_data,
    )
    bot.other_bot.update_put_label_last(put_label_last)

    return bot


test_data_standard = {
    # standard
    # yc_bot.search_all(category)
    "yemeni films": "أفلام يمنية",
    "Yemeni action films": "أفلام حركة يمنية",
    "Yemeni action drama films": "أفلام حركة درامية يمنية",
    "Yemeni upcoming horror films": "أفلام رعب قادمة يمنية",
    "Yemeni horror upcoming films": "أفلام رعب قادمة يمنية",
    "Yemeni upcoming films": "أفلام قادمة يمنية",
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


@pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
def test_year_country_combinations(yc_bot: MultiDataFormatterDataDouble, category: str, expected: str) -> None:
    """
    Test
    """
    result = yc_bot.search_all(category)
    assert result == expected


country_bot_data = [
    # without films keys to test yc_bot.country_bot.search(category)
    ("Yemeni films", "أفلام يمنية"),
]


@pytest.mark.parametrize("category,expected", country_bot_data, ids=[x[0] for x in country_bot_data])
def test_country_bot(yc_bot: MultiDataFormatterDataDouble, category: str, expected: str) -> None:
    """
    Test
    """
    result = yc_bot.country_bot.search(category)
    assert result == expected


other_bot_data = {
    # without nationality to test yc_bot.other_bot.search(category)
    "black-and-white films": "أفلام أبيض وأسود",
    "black-and-white action films": "أفلام أبيض وأسود حركة",
    "drama action television commercials": "إعلانات تجارية تلفزيونية درامية حركة",
    "horror upcoming films": "أفلام رعب قادمة",
    "psychological horror films": "أفلام رعب نفسي",
    "psychological horror black-and-white films": "أفلام رعب نفسي أبيض وأسود",
}


@pytest.mark.parametrize("category,expected", other_bot_data.items(), ids=other_bot_data.keys())
def test_other_bot(yc_bot: MultiDataFormatterDataDouble, category: str, expected: str) -> None:
    """
    Test
    """
    result = yc_bot.other_bot.search(category)
    assert result == expected


# --- match_key --------------------------------------------------------

test_match_key_data = {
    "Yemeni action films": "action",
    "Yemeni action drama films": "action drama",
    "Yemeni upcoming horror films": "upcoming horror",
    "Yemeni black-and-white films": "black-and-white",
}


@pytest.mark.parametrize("category, expected", test_match_key_data.items(), ids=test_match_key_data.keys())
@pytest.mark.fast
def test_match_key(yc_bot: MultiDataFormatterDataDouble, category: str, expected: str) -> None:
    result = yc_bot.other_bot.match_key(category)
    assert result == expected
