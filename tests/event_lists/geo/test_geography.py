#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

geography_data = {
    "Culture of Westchester County, New York": "ثقافة مقاطعة ويستتشستر (نيويورك)",
    "Economy of Westchester County, New York": "اقتصاد مقاطعة ويستتشستر (نيويورك)",
    "Geography of Westchester County, New York": "جغرافيا مقاطعة ويستتشستر (نيويورك)",
    "Images of Westchester County, New York": "صور من مقاطعة ويستتشستر (نيويورك)",
    "Landforms of Westchester County, New York": "تضاريس مقاطعة ويستتشستر (نيويورك)",
    "Languages of the Cayman Islands": "لغات جزر كايمان",
    "Olympic gold medalists for the United States": "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة",
    "Olympic medalists for the United States": "فائزون بميداليات أولمبية من الولايات المتحدة",
    "Protected areas of Westchester County, New York": "مناطق محمية في مقاطعة ويستتشستر (نيويورك)",
}

geography_in_1 = {
    "Buildings and structures in the United States by state": "مبان ومنشآت في الولايات المتحدة حسب الولاية",
    "Buildings and structures in Westchester County, New York": "مبان ومنشآت في مقاطعة ويستتشستر (نيويورك)",
    "Cemeteries in Westchester County, New York": "مقابر في مقاطعة ويستتشستر (نيويورك)",
    "Centuries in the United States by state": "قرون في الولايات المتحدة حسب الولاية",
    "Christianity in Westchester County, New York": "المسيحية في مقاطعة ويستتشستر (نيويورك)",
    "Churches in Westchester County, New York": "كنائس في مقاطعة ويستتشستر (نيويورك)",
    "Communications in the United States by state": "الاتصالات في الولايات المتحدة حسب الولاية",
    "Companies based in Westchester County, New York": "شركات مقرها في مقاطعة ويستتشستر (نيويورك)",
    "Crime in Pennsylvania": "جريمة في بنسلفانيا",
    "Crimes in Pennsylvania": "جرائم في بنسلفانيا",
    "Crimes in the United States by state": "جرائم في الولايات المتحدة حسب الولاية",
    "Disasters in the United States by state": "كوارث في الولايات المتحدة حسب الولاية",
    "Education in the United States by state": "التعليم في الولايات المتحدة حسب الولاية",
    "Rail transport in Sri Lanka by province": "السكك الحديدية في سريلانكا حسب المقاطعة",
    "Riots and civil disorder in the United States by state": "شغب وعصيان مدني في الولايات المتحدة حسب الولاية",
    "Schools in Westchester County, New York": "مدارس في مقاطعة ويستتشستر (نيويورك)",
    "Science and technology in the United States by state": "العلوم والتقانة في الولايات المتحدة حسب الولاية",
    "Slavery in the United States by state": "العبودية في الولايات المتحدة حسب الولاية",
    "Sports venues in Westchester County, New York": "ملاعب رياضية في مقاطعة ويستتشستر (نيويورك)",
    "Education in Westchester County, New York": "التعليم في مقاطعة ويستتشستر (نيويورك)",
    "Films set in China by city": "أفلام تقع أحداثها في الصين حسب المدينة",
    "Films set in Westchester County, New York": "أفلام تقع أحداثها في مقاطعة ويستتشستر (نيويورك)",
    "Films shot in China by city": "أفلام مصورة في الصين حسب المدينة",
    "Forts in the United States by state": "حصون في الولايات المتحدة حسب الولاية",
    "Health in North Dakota": "الصحة في داكوتا الشمالية",
    "Health in the United States by state": "الصحة في الولايات المتحدة حسب الولاية",
}

geography_in_2 = {
    "Historic districts in Westchester County, New York": "المناطق التاريخية في مقاطعة ويستتشستر (نيويورك)",
    "Historic sites in the United States by state": "مواقع تاريخية في الولايات المتحدة حسب الولاية",
    "Historic trails and roads in the United States by state": "طرق وممرات تاريخية في الولايات المتحدة حسب الولاية",
    "Hospitals in Westchester County, New York": "مستشفيات في مقاطعة ويستتشستر (نيويورك)",
    "Houses in Westchester County, New York": "منازل في مقاطعة ويستتشستر (نيويورك)",
    "Landmarks in the United States by state": "معالم في الولايات المتحدة حسب الولاية",
    "Manufacturing in the United States by state": "تصنيع في الولايات المتحدة حسب الولاية",
    "Museums in Westchester County, New York": "متاحف في مقاطعة ويستتشستر (نيويورك)",
    "National Register of Historic Places in Westchester County, New York": "السجل الوطني للأماكن التاريخية في مقاطعة ويستتشستر (نيويورك)",
    "Nature reserves in the United States by state": "محميات طبيعية في الولايات المتحدة حسب الولاية",
    "Olympic gold medalists for the United States in alpine skiing": "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة في التزلج على المنحدرات الثلجية",
    "Parks in Westchester County, New York": "متنزهات في مقاطعة ويستتشستر (نيويورك)",
    "People by state in the United States": "أشخاص حسب الولاية في الولايات المتحدة",
    "Populated places in Westchester County, New York": "أماكن مأهولة في مقاطعة ويستتشستر (نيويورك)",
    "Television shows set in Australia by city": "عروض تلفزيونية تقع أحداثها في أستراليا حسب المدينة",
    "Tourist attractions in the United States by state": "مواقع جذب سياحي في الولايات المتحدة حسب الولاية",
    "Tourist attractions in Westchester County, New York": "مواقع جذب سياحي في مقاطعة ويستتشستر (نيويورك)",
    "Transportation buildings and structures in Westchester County, New York": "مبان ومنشآت نقل في مقاطعة ويستتشستر (نيويورك)",
    "Transportation in the United States by state": "النقل في الولايات المتحدة حسب الولاية",
    "Transportation in Westchester County, New York": "النقل في مقاطعة ويستتشستر (نيويورك)",
    "Universities and colleges in Westchester County, New York": "جامعات وكليات في مقاطعة ويستتشستر (نيويورك)",
}

test_data = [
    ("test_geography", geography_data),
    ("test_geography_in_1", geography_in_1),
    ("test_geography_in_2", geography_in_2),
]


@pytest.mark.parametrize("category, expected", geography_data.items(), ids=geography_data.keys())
@pytest.mark.fast
def test_geography(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", geography_in_1.items(), ids=geography_in_1.keys())
@pytest.mark.fast
def test_geography_in_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", geography_in_2.items(), ids=geography_in_2.keys())
@pytest.mark.fast
def test_geography_in_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.dump
@pytest.mark.parametrize("name,data", test_data)
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
