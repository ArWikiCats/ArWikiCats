"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.legacy_resolvers_bots.country2_label_bot import make_cnt_lab

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


@pytest.mark.parametrize("category, ar", make_cnt_lab_data.items(), ids=make_cnt_lab_data.keys())
@pytest.mark.fast
def test_make_cnt_lab_data(category: str, ar: str) -> None:
    label = make_cnt_lab(
        country=f"kingdom-of {category}",
        part_2_label=ar,
        part_1_label="مملكة",
        part_1_normalized="kingdom of",
        part_2_normalized=category,
        ar_separator=" ",
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
    "yugoslavia": ("communist party-of yugoslavia", "يوغسلافيا", "الحزب الشيوعي في يوغسلافيا"),
}


@pytest.mark.parametrize("country, part_2_label, expected", party_data.values(), ids=party_data.keys())
@pytest.mark.fast
def test_make_cnt_lab_communist_party(country: str, part_2_label: str, expected: str) -> None:
    label = make_cnt_lab(
        country=country,
        part_2_label=part_2_label,
        part_1_label="الحزب الشيوعي في ",
        part_1_normalized="communist party of",
        part_2_normalized=country.replace("communist party-of ", ""),
        ar_separator=" ",
    )

    assert label == expected


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


@pytest.mark.parametrize("category, ar", congress_data.items(), ids=congress_data.keys())
@pytest.mark.fast
def test_congress_data(category: str, ar: str) -> None:
    label = f"الكونغرس الأمريكي {ar}"
    result = make_cnt_lab(
        country=f"acts of {category} united states congress",
        part_2_label=label,
        part_1_label="أفعال",
        part_1_normalized="acts of",
        part_2_normalized=f"{category} united states congress",
        ar_separator=" ",
    )

    assert result == f"أفعال {label}"
