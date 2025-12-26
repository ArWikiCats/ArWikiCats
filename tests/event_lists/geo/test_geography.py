#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

geography_data = {
    "Category:Culture of Westchester County, New York": "تصنيف:ثقافة مقاطعة ويستتشستر (نيويورك)",
    "Category:Economy of Westchester County, New York": "تصنيف:اقتصاد مقاطعة ويستتشستر (نيويورك)",
    "Category:Geography of Westchester County, New York": "تصنيف:جغرافيا مقاطعة ويستتشستر (نيويورك)",
    "Category:Images of Westchester County, New York": "تصنيف:صور من مقاطعة ويستتشستر (نيويورك)",
    "Category:Landforms of Westchester County, New York": "تصنيف:تضاريس مقاطعة ويستتشستر (نيويورك)",
    "Category:Languages of the Cayman Islands": "تصنيف:لغات جزر كايمان",
    "Category:Olympic gold medalists for the United States": "تصنيف:فائزون بميداليات ذهبية أولمبية من الولايات المتحدة",
    "Category:Olympic medalists for the United States": "تصنيف:فائزون بميداليات أولمبية من الولايات المتحدة",
    "Category:Protected areas of Westchester County, New York": "تصنيف:مناطق محمية في مقاطعة ويستتشستر (نيويورك)",
}

geography_in_1 = {
    "Category:Buildings and structures in the United States by state": "تصنيف:مبان ومنشآت في الولايات المتحدة حسب الولاية",
    "Category:Buildings and structures in Westchester County, New York": "تصنيف:مبان ومنشآت في مقاطعة ويستتشستر (نيويورك)",
    "Category:Cemeteries in Westchester County, New York": "تصنيف:مقابر في مقاطعة ويستتشستر (نيويورك)",
    "Category:Centuries in the United States by state": "تصنيف:قرون في الولايات المتحدة حسب الولاية",
    "Category:Christianity in Westchester County, New York": "تصنيف:المسيحية في مقاطعة ويستتشستر (نيويورك)",
    "Category:Churches in Westchester County, New York": "تصنيف:كنائس في مقاطعة ويستتشستر (نيويورك)",
    "Category:Communications in the United States by state": "تصنيف:الاتصالات في الولايات المتحدة حسب الولاية",
    "Category:Companies based in Westchester County, New York": "تصنيف:شركات مقرها في مقاطعة ويستتشستر (نيويورك)",
    "Category:Crime in Pennsylvania": "تصنيف:جريمة في بنسلفانيا",
    "Category:Crimes in Pennsylvania": "تصنيف:جرائم في بنسلفانيا",
    "Category:Crimes in the United States by state": "تصنيف:جرائم في الولايات المتحدة حسب الولاية",
    "Category:Disasters in the United States by state": "تصنيف:كوارث في الولايات المتحدة حسب الولاية",
    "Category:Education in the United States by state": "تصنيف:التعليم في الولايات المتحدة حسب الولاية",
    "Category:Rail transport in Sri Lanka by province": "تصنيف:السكك الحديدية في سريلانكا حسب المقاطعة",
    "Category:Riots and civil disorder in the United States by state": "تصنيف:شغب وعصيان مدني في الولايات المتحدة حسب الولاية",
    "Category:Schools in Westchester County, New York": "تصنيف:مدارس في مقاطعة ويستتشستر (نيويورك)",
    "Category:Science and technology in the United States by state": "تصنيف:العلوم والتقانة في الولايات المتحدة حسب الولاية",
    "Category:Slavery in the United States by state": "تصنيف:العبودية في الولايات المتحدة حسب الولاية",
    "Category:Sports venues in Westchester County, New York": "تصنيف:ملاعب رياضية في مقاطعة ويستتشستر (نيويورك)",
    "Category:Education in Westchester County, New York": "تصنيف:التعليم في مقاطعة ويستتشستر (نيويورك)",
    "Category:Films set in China by city": "تصنيف:أفلام تقع أحداثها في الصين حسب المدينة",
    "Category:Films set in Westchester County, New York": "تصنيف:أفلام تقع أحداثها في مقاطعة ويستتشستر (نيويورك)",
    "Category:Films shot in China by city": "تصنيف:أفلام مصورة في الصين حسب المدينة",
    "Category:Forts in the United States by state": "تصنيف:حصون في الولايات المتحدة حسب الولاية",
    "Category:Health in North Dakota": "تصنيف:الصحة في داكوتا الشمالية",
    "Category:Health in the United States by state": "تصنيف:الصحة في الولايات المتحدة حسب الولاية",
}

geography_in_2 = {
    "Category:Historic districts in Westchester County, New York": "تصنيف:المناطق التاريخية في مقاطعة ويستتشستر (نيويورك)",
    "Category:Historic sites in the United States by state": "تصنيف:مواقع تاريخية في الولايات المتحدة حسب الولاية",
    "Category:Historic trails and roads in the United States by state": "تصنيف:طرق وممرات تاريخية في الولايات المتحدة حسب الولاية",
    "Category:Hospitals in Westchester County, New York": "تصنيف:مستشفيات في مقاطعة ويستتشستر (نيويورك)",
    "Category:Houses in Westchester County, New York": "تصنيف:منازل في مقاطعة ويستتشستر (نيويورك)",
    "Category:Landmarks in the United States by state": "تصنيف:معالم في الولايات المتحدة حسب الولاية",
    "Category:Manufacturing in the United States by state": "تصنيف:تصنيع في الولايات المتحدة حسب الولاية",
    "Category:Museums in Westchester County, New York": "تصنيف:متاحف في مقاطعة ويستتشستر (نيويورك)",
    "Category:National Register of Historic Places in Westchester County, New York": "تصنيف:السجل الوطني للأماكن التاريخية في مقاطعة ويستتشستر (نيويورك)",
    "Category:Nature reserves in the United States by state": "تصنيف:محميات طبيعية في الولايات المتحدة حسب الولاية",
    "Category:Olympic gold medalists for the United States in alpine skiing": "تصنيف:فائزون بميداليات ذهبية أولمبية من الولايات المتحدة في التزلج على المنحدرات الثلجية",
    "Category:Parks in Westchester County, New York": "تصنيف:متنزهات في مقاطعة ويستتشستر (نيويورك)",
    "Category:People by state in the United States": "تصنيف:أشخاص حسب الولاية في الولايات المتحدة",
    "Category:Populated places in Westchester County, New York": "تصنيف:أماكن مأهولة في مقاطعة ويستتشستر (نيويورك)",
    "Category:Television shows set in Australia by city": "تصنيف:عروض تلفزيونية تقع أحداثها في أستراليا حسب المدينة",
    "Category:Tourist attractions in the United States by state": "تصنيف:مواقع جذب سياحي في الولايات المتحدة حسب الولاية",
    "Category:Tourist attractions in Westchester County, New York": "تصنيف:مواقع جذب سياحي في مقاطعة ويستتشستر (نيويورك)",
    "Category:Transportation buildings and structures in Westchester County, New York": "تصنيف:مبان ومنشآت نقل في مقاطعة ويستتشستر (نيويورك)",
    "Category:Transportation in the United States by state": "تصنيف:النقل في الولايات المتحدة حسب الولاية",
    "Category:Transportation in Westchester County, New York": "تصنيف:النقل في مقاطعة ويستتشستر (نيويورك)",
    "Category:Universities and colleges in Westchester County, New York": "تصنيف:جامعات وكليات في مقاطعة ويستتشستر (نيويورك)",
}

test_data = [
    ("test_geography", geography_data),
    ("test_geography_in_1", geography_in_1),
    ("test_geography_in_2", geography_in_2),
]


@pytest.mark.parametrize("category, expected", geography_data.items(), ids=geography_data.keys())
@pytest.mark.fast
def test_geography(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", geography_in_1.items(), ids=geography_in_1.keys())
@pytest.mark.fast
def test_geography_in_1(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", geography_in_2.items(), ids=geography_in_2.keys())
@pytest.mark.fast
def test_geography_in_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.dump
@pytest.mark.parametrize("name,data", test_data)
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
