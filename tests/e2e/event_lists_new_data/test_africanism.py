#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

data1 = {
    "Pan-Africanism": "وحدة إفريقية",
    "Pan-Africanism by continent": "وحدة إفريقية حسب القارة",
    "Pan-Africanism by country": "وحدة إفريقية حسب البلد",
    "Pan-Africanism in Africa": "وحدة إفريقية في إفريقيا",
    "Pan-Africanism in Burkina Faso": "وحدة إفريقية في بوركينا فاسو",
    "Pan-Africanism in Europe": "وحدة إفريقية في أوروبا",
    "Pan-Africanism in Ghana": "وحدة إفريقية في غانا",
    "Pan-Africanism in Ivory Coast": "وحدة إفريقية في ساحل العاج",
    "Pan-Africanism in Kenya": "وحدة إفريقية في كينيا",
    "Pan-Africanism in Lesotho": "وحدة إفريقية في ليسوتو",
    "Pan-Africanism in Liberia": "وحدة إفريقية في ليبيريا",
    "Pan-Africanism in Mali": "وحدة إفريقية في مالي",
    "Pan-Africanism in Nigeria": "وحدة إفريقية في نيجيريا",
    "Pan-Africanism in North America": "وحدة إفريقية في أمريكا الشمالية",
    "Pan-Africanism in South Africa": "وحدة إفريقية في جنوب إفريقيا",
    "Pan-Africanism in South America": "وحدة إفريقية في أمريكا الجنوبية",
    "Pan-Africanism in the Caribbean": "وحدة إفريقية في الكاريبي",
    "Pan-Africanism in the United Kingdom": "وحدة إفريقية في المملكة المتحدة",
    "Pan-Africanism in the United States": "وحدة إفريقية في الولايات المتحدة",
    "Pan-Africanism in Togo": "وحدة إفريقية في توغو",
    "Pan-Africanism in Zimbabwe": "وحدة إفريقية في زيمبابوي",
    "Pan-Africanist organisations in the Caribbean": "منظمات وحدوية إفريقية في الكاريبي",
    "Pan-Africanist organizations": "منظمات وحدوية إفريقية",
    "Pan-Africanist organizations in Africa": "منظمات وحدوية إفريقية في إفريقيا",
    "Pan-Africanist organizations in Europe": "منظمات وحدوية إفريقية في أوروبا",
    "Pan-Africanist political parties": "أحزاب سياسية وحدوية إفريقية",
    "Pan-Africanist political parties in Africa": "أحزاب سياسية وحدوية إفريقية في إفريقيا",
    "Pan-Africanist political parties in the Caribbean": "أحزاب سياسية وحدوية إفريقية في الكاريبي",
    "Pan-African organizations": "منظمات قومية إفريقية",
    "Pan-African Parliament": "البرلمان الإفريقي",
    "Pan-African Democratic Party politicians": "سياسيو الحزب الديمقراطي الوحدوي الإفريقي",
    "Pan-Africanists": "وحدويون أفارقة",
    "Pan-Africanists by continent": "وحدويون أفارقة حسب القارة",
    "Pan-Africanists by nationality": "وحدويون أفارقة حسب الجنسية",
    "South American pan-Africanists": "وحدويون أفارقة أمريكيون جنوبيون",
}


africanism_empty = {
    "Pan Africanist Congress of Azania": "",
    "Pan Africanist Congress of Azania politicians": "",
    "Pan-African media companies": "",
    "Pan-African Patriotic Convergence politicians": "",
    "Pan-African Socialist Party politicians": "",
    "Pan-African Union for Social Democracy politicians": "",
}


TEMPORAL_CASES = [
    ("test_africanism", data1),
    ("test_africanism_empty", africanism_empty),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_africanism(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", africanism_empty.items(), ids=africanism_empty.keys())
@pytest.mark.fast
def test_africanism_empty(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
