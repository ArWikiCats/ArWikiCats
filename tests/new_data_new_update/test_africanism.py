#
import pytest
from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset, dump_diff

data = {
    "Category:Pan-Africanism": "تصنيف:وحدة أفريقية",
    "Category:Pan-Africanism by continent": "تصنيف:وحدة أفريقية حسب القارة",
    "Category:Pan-Africanism by country": "تصنيف:وحدة أفريقية حسب البلد",
    "Category:Pan-Africanism in Africa": "تصنيف:وحدة أفريقية في إفريقيا",
    "Category:Pan-Africanism in Burkina Faso": "تصنيف:وحدة أفريقية في بوركينا فاسو",
    "Category:Pan-Africanism in Europe": "تصنيف:وحدة أفريقية في أوروبا",
    "Category:Pan-Africanism in Ghana": "تصنيف:وحدة أفريقية في غانا",
    "Category:Pan-Africanism in Ivory Coast": "تصنيف:وحدة أفريقية في ساحل العاج",
    "Category:Pan-Africanism in Kenya": "تصنيف:وحدة أفريقية في كينيا",
    "Category:Pan-Africanism in Lesotho": "تصنيف:وحدة أفريقية في ليسوتو",
    "Category:Pan-Africanism in Liberia": "تصنيف:وحدة أفريقية في ليبيريا",
    "Category:Pan-Africanism in Mali": "تصنيف:وحدة أفريقية في مالي",
    "Category:Pan-Africanism in Nigeria": "تصنيف:وحدة أفريقية في نيجيريا",
    "Category:Pan-Africanism in North America": "تصنيف:وحدة أفريقية في أمريكا الشمالية",
    "Category:Pan-Africanism in South Africa": "تصنيف:وحدة أفريقية في جنوب إفريقيا",
    "Category:Pan-Africanism in South America": "تصنيف:وحدة أفريقية في أمريكا الجنوبية",
    "Category:Pan-Africanism in the Caribbean": "تصنيف:وحدة أفريقية في الكاريبي",
    "Category:Pan-Africanism in the United Kingdom": "تصنيف:وحدة أفريقية في المملكة المتحدة",
    "Category:Pan-Africanism in the United States": "تصنيف:وحدة أفريقية في الولايات المتحدة",
    "Category:Pan-Africanism in Togo": "تصنيف:وحدة أفريقية في توغو",
    "Category:Pan-Africanism in Zimbabwe": "تصنيف:وحدة أفريقية في زيمبابوي",

    "Category:Pan-Africanist organisations in the Caribbean": "تصنيف:منظمات وحدوية أفريقية في الكاريبي",
    "Category:Pan-Africanist organizations": "تصنيف:منظمات وحدوية أفريقية",
    "Category:Pan-Africanist organizations in Africa": "تصنيف:منظمات وحدوية أفريقية في إفريقيا",
    "Category:Pan-Africanist organizations in Europe": "تصنيف:منظمات وحدوية أفريقية في أوروبا",
    "Category:Pan-Africanist political parties": "تصنيف:أحزاب سياسية وحدوية إفريقية",
    "Category:Pan-Africanist political parties in Africa": "تصنيف:أحزاب سياسية وحدوية إفريقية في إفريقيا",
    "Category:Pan-Africanist political parties in the Caribbean": "تصنيف:أحزاب سياسية وحدوية إفريقية في الكاريبي",

    "Category:Pan-African organizations": "تصنيف:منظمات قومية أفريقية",
    "Category:Pan-African Parliament": "تصنيف:البرلمان الإفريقي",
    "Category:Pan-African Democratic Party politicians": "تصنيف:سياسيو الحزب الديمقراطي الوحدوي الإفريقي",

    "Category:Pan-Africanists": "تصنيف:وحدويون أفارقة",
    "Category:Pan-Africanists by continent": "تصنيف:وحدويون أفارقة حسب القارة",
    "Category:Pan-Africanists by nationality": "تصنيف:وحدويون أفارقة حسب الجنسية",
    "Category:South American pan-Africanists": "تصنيف:وحدويون أفارقة أمريكيون جنوبيون",

}


@pytest.mark.slow
def test_africanism():
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_africanism")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


africanism_empty = {
    "Category:Pan Africanist Congress of Azania": "",
    "Category:Pan Africanist Congress of Azania politicians": "",
    "Category:Pan-African media companies": "",
    "Category:Pan-African Patriotic Convergence politicians": "",
    "Category:Pan-African Socialist Party politicians": "",
    "Category:Pan-African Union for Social Democracy politicians": "",
}


@pytest.mark.skip("Need more work")
def test_africanism_empty():
    expected, diff_result = ye_test_one_dataset(africanism_empty, new_func_lab_final_label)

    dump_diff(diff_result, "test_africanism_empty")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
