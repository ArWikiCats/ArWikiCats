"""
Tests
"""

import pytest

from ArWikiCats.make_bots.ma_bots.country2_bots.cn_lab import make_cnt_lab

make_cnt_lab_data = {
    "jerusalem": "القدس",
    "georgia": "جورجيا",
    "naples": "نابولي",
    "sicily": "صقلية",
    "sardinia": "سردينيا",
    "lagos": "ولاية لاغوس",
    "hanover": "هانوفر",
    "saxony": "ساكسونيا",
    "morocco": "المغرب",
    "galicia": "منطقة غاليسيا",
}


@pytest.mark.parametrize("category, ar", make_cnt_lab_data.items(), ids=list(make_cnt_lab_data.keys()))
@pytest.mark.fast
def test_make_cnt_lab_data(category, ar) -> None:
    label = make_cnt_lab(
        tat_o="-of ",
        country2=f"kingdom-of {category}",
        c_2_l=ar,
        c_1_l="مملكة",
        cona_1="kingdom of",
        cona_2=category,
        sps=" ",
    )
    assert label == f"مملكة {ar}"


party_data = {
    "vietnam": ("communist party-of vietnam", "فيتنام", "الحزب الشيوعي في فيتنام"),
    "bosnia and herzegovina": (
        "communist party-of bosnia and herzegovina",
        "البوسنة والهرسك",
        "الحزب الشيوعي في البوسنة والهرسك",
    ),
    "cuba": ("communist party-of cuba", "كوبا", "الحزب الشيوعي في كوبا"),
    "soviet union": ("communist party-of soviet union", "الاتحاد السوفيتي", "الحزب الشيوعي في الاتحاد السوفيتي"),
    "yugoslavia": ("communist party-of yugoslavia", "يوغوسلافيا", "الحزب الشيوعي في يوغوسلافيا"),
}


@pytest.mark.parametrize("country2, c_2_l, expected", party_data.values(), ids=list(party_data.keys()))
@pytest.mark.fast
def test_make_cnt_lab_communist_party(country2, c_2_l, expected) -> None:
    label = make_cnt_lab(
        tat_o="-of ",
        country2=country2,
        c_2_l=c_2_l,
        c_1_l="الحزب الشيوعي في ",
        cona_1="communist party of",
        cona_2=country2.replace("communist party-of ", ""),
        sps=" ",
    )

    assert label == expected


def test_make_cnt_lab() -> None:
    result1 = make_cnt_lab(
        tat_o=" in ",
        country2="university of arts in belgrade",
        c_2_l="بلغراد",
        c_1_l="جامعة {} للفنون في",
        cona_1="university of arts",
        cona_2="belgrade",
        sps=" في ",
    )
    assert isinstance(result1, str)
    assert result1 == "جامعة بلغراد للفنون"

    result1 = make_cnt_lab(
        tat_o=" of ",
        country2="by medium from insular areas of united states",
        c_2_l="الولايات المتحدة",
        c_1_l="حسب الوسط من المناطق المعزولة في ",
        cona_1="by medium from insular areas of",
        cona_2="united states",
        sps=" ",
    )
    assert isinstance(result1, str)
    assert result1 == "حسب الوسط من المناطق المعزولة في الولايات المتحدة"

    # Test with basic inputs
    result = make_cnt_lab("in", "test in country", "country label", "test label", "test", "country", " ")
    assert isinstance(result, str)

    # Test with different parameters
    result_various = make_cnt_lab(
        "from", "test from country", "country label2", "test label2", "test2", "country2", " من "
    )
    assert isinstance(result_various, str)

    # Test with empty strings
    result_empty = make_cnt_lab("", "", "", "", "", "", "")
    assert isinstance(result_empty, str)

    # Test with empty strings


congress_data = {
    "103rd": "الثالث بعد المئة",
    "104th": "الرابع بعد المئة",
    "100th": "المئة",
    "101st": "الأول بعد المئة",
    "102nd": "الثاني بعد المئة",
    "105th": "الخامس بعد المئة",
    "106th": "السادس بعد المئة",
    "107th": "السابع بعد المئة",
    "108th": "الثامن بعد المئة",
    "109th": "التاسع بعد المئة",
    "10th": "العاشر",
    "110th": "العاشر بعد المئة",
    "111th": "الحادي عشر بعد المئة",
    "112th": "الثاني عشر بعد المئة",
    "113th": "الثالث عشر بعد المئة",
    "114th": "الرابع عشر بعد المئة",
    "115th": "الخامس عشر بعد المئة",
    "116th": "السادس عشر بعد المئة",
    "117th": "السابع عشر بعد المئة",
    "118th": "الثامن عشر بعد المئة",
    "119th": "التاسع عشر بعد المئة",
    "11th": "الحادي عشر",
    "12th": "الثاني عشر",
    "13th": "الثالث عشر",
    "14th": "الرابع عشر",
    "15th": "الخامس عشر",
    "16th": "السادس عشر",
}


@pytest.mark.parametrize("category, ar", congress_data.items(), ids=list(congress_data.keys()))
@pytest.mark.fast
def test_congress_data(category, ar) -> None:
    label = f"الكونغرس الأمريكي {ar}"
    result = make_cnt_lab(
        tat_o=" of ",
        country2=f"acts of {category} united states congress",
        c_2_l=label,
        c_1_l="أفعال",
        cona_1="acts of",
        cona_2=f"{category} united states congress",
        sps=" ",
    )

    assert result == f"أفعال {label}"
