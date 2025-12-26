#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data1 = {
    "Category:Pan-Africanism": "تصنيف:وحدة إفريقية",
    "Category:Pan-Africanism by continent": "تصنيف:وحدة إفريقية حسب القارة",
    "Category:Pan-Africanism by country": "تصنيف:وحدة إفريقية حسب البلد",
    "Category:Pan-Africanism in Africa": "تصنيف:وحدة إفريقية في إفريقيا",
    "Category:Pan-Africanism in Burkina Faso": "تصنيف:وحدة إفريقية في بوركينا فاسو",
    "Category:Pan-Africanism in Europe": "تصنيف:وحدة إفريقية في أوروبا",
    "Category:Pan-Africanism in Ghana": "تصنيف:وحدة إفريقية في غانا",
    "Category:Pan-Africanism in Ivory Coast": "تصنيف:وحدة إفريقية في ساحل العاج",
    "Category:Pan-Africanism in Kenya": "تصنيف:وحدة إفريقية في كينيا",
    "Category:Pan-Africanism in Lesotho": "تصنيف:وحدة إفريقية في ليسوتو",
    "Category:Pan-Africanism in Liberia": "تصنيف:وحدة إفريقية في ليبيريا",
    "Category:Pan-Africanism in Mali": "تصنيف:وحدة إفريقية في مالي",
    "Category:Pan-Africanism in Nigeria": "تصنيف:وحدة إفريقية في نيجيريا",
    "Category:Pan-Africanism in North America": "تصنيف:وحدة إفريقية في أمريكا الشمالية",
    "Category:Pan-Africanism in South Africa": "تصنيف:وحدة إفريقية في جنوب إفريقيا",
    "Category:Pan-Africanism in South America": "تصنيف:وحدة إفريقية في أمريكا الجنوبية",
    "Category:Pan-Africanism in the Caribbean": "تصنيف:وحدة إفريقية في الكاريبي",
    "Category:Pan-Africanism in the United Kingdom": "تصنيف:وحدة إفريقية في المملكة المتحدة",
    "Category:Pan-Africanism in the United States": "تصنيف:وحدة إفريقية في الولايات المتحدة",
    "Category:Pan-Africanism in Togo": "تصنيف:وحدة إفريقية في توغو",
    "Category:Pan-Africanism in Zimbabwe": "تصنيف:وحدة إفريقية في زيمبابوي",
    "Category:Pan-Africanist organisations in the Caribbean": "تصنيف:منظمات وحدوية إفريقية في الكاريبي",
    "Category:Pan-Africanist organizations": "تصنيف:منظمات وحدوية إفريقية",
    "Category:Pan-Africanist organizations in Africa": "تصنيف:منظمات وحدوية إفريقية في إفريقيا",
    "Category:Pan-Africanist organizations in Europe": "تصنيف:منظمات وحدوية إفريقية في أوروبا",
    "Category:Pan-Africanist political parties": "تصنيف:أحزاب سياسية وحدوية إفريقية",
    "Category:Pan-Africanist political parties in Africa": "تصنيف:أحزاب سياسية وحدوية إفريقية في إفريقيا",
    "Category:Pan-Africanist political parties in the Caribbean": "تصنيف:أحزاب سياسية وحدوية إفريقية في الكاريبي",
    "Category:Pan-African organizations": "تصنيف:منظمات قومية إفريقية",
    "Category:Pan-African Parliament": "تصنيف:البرلمان الإفريقي",
    "Category:Pan-African Democratic Party politicians": "تصنيف:سياسيو الحزب الديمقراطي الوحدوي الإفريقي",
    "Category:Pan-Africanists": "تصنيف:وحدويون أفارقة",
    "Category:Pan-Africanists by continent": "تصنيف:وحدويون أفارقة حسب القارة",
    "Category:Pan-Africanists by nationality": "تصنيف:وحدويون أفارقة حسب الجنسية",
    "Category:South American pan-Africanists": "تصنيف:وحدويون أفارقة أمريكيون جنوبيون",
}


africanism_empty = {
    "Category:Pan Africanist Congress of Azania": "",
    "Category:Pan Africanist Congress of Azania politicians": "",
    "Category:Pan-African media companies": "",
    "Category:Pan-African Patriotic Convergence politicians": "",
    "Category:Pan-African Socialist Party politicians": "",
    "Category:Pan-African Union for Social Democracy politicians": "",
}


TEMPORAL_CASES = [
    ("test_africanism", data1),
    ("test_africanism_empty", africanism_empty),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_africanism(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", africanism_empty.items(), ids=africanism_empty.keys())
@pytest.mark.fast
def test_africanism_empty(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
