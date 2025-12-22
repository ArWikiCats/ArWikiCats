#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data1 = {
    "Category:African-American history by state": "تصنيف:تاريخ أمريكي إفريقي حسب الولاية",
    "Category:Airlines by dependent territory": "تصنيف:شركات طيران حسب الأقاليم التابعة",
    "Category:Ambassadors by country of origin": "تصنيف:سفراء حسب البلد الأصل",
    "Category:Ambassadors by mission country": "تصنيف:سفراء حسب بلد البعثة",
    "Category:American basketball coaches by state": "تصنيف:مدربو كرة سلة أمريكيون حسب الولاية",
    "Category:American culture by state": "تصنيف:ثقافة أمريكية حسب الولاية",
    "Category:Awards by country": "تصنيف:جوائز حسب البلد",
    "Category:Books about politics by country": "تصنيف:كتب عن سياسة حسب البلد",
    "Category:Categories by province of Saudi Arabia": "تصنيف:تصنيفات حسب المقاطعة في السعودية",
    "Category:Demographics of the United States by state": "تصنيف:التركيبة السكانية في الولايات المتحدة حسب الولاية",
    "Category:Destroyed churches by country": "تصنيف:كنائس مدمرة حسب البلد",
    "Category:Drama films by country": "تصنيف:أفلام درامية حسب البلد",
    "Category:Economic history of the United States by state": "تصنيف:تاريخ الولايات المتحدة الاقتصادي حسب الولاية",
    "Category:Economy of the United States by state": "تصنيف:اقتصاد الولايات المتحدة حسب الولاية",
    "Category:Environment of the United States by state or territory": "تصنيف:بيئة الولايات المتحدة حسب الولاية أو الإقليم",
    "Category:Expatriate association football managers by country of residence": "تصنيف:مدربو كرة قدم مغتربون حسب بلد الإقامة",
    "Category:Films by city": "تصنيف:أفلام حسب المدينة",
    "Category:Films by country": "تصنيف:أفلام حسب البلد",
    "Category:Geography of the United States by state": "تصنيف:جغرافيا الولايات المتحدة حسب الولاية",
    "Category:Handball competitions by country": "تصنيف:منافسات كرة يد حسب البلد",
    "Category:History of the American Revolution by state": "تصنيف:تاريخ الثورة الأمريكية حسب الولاية",
}

data2 = {
    "Category:History of the United States by period by state": "تصنيف:تاريخ الولايات المتحدة حسب الحقبة حسب الولاية",
    "Category:History of the United States by state": "تصنيف:تاريخ الولايات المتحدة حسب الولاية",
    "Category:Images of the United States by state": "تصنيف:صور من الولايات المتحدة حسب الولاية",
    "Category:Ivorian diaspora by country": "تصنيف:شتات إيفواري حسب البلد",
    "Category:Legal history of the United States by state": "تصنيف:تاريخ الولايات المتحدة القانوني حسب الولاية",
    "Category:Military history of the United States by state": "تصنيف:تاريخ الولايات المتحدة العسكري حسب الولاية",
    "Category:Military organization by country": "تصنيف:منظمات عسكرية حسب البلد",
    "Category:Multi-sport clubs by country": "تصنيف:أندية متعددة الرياضات حسب البلد",
    "Category:Mystery films by country": "تصنيف:أفلام غموض حسب البلد",
    "Category:National youth sports teams by country": "تصنيف:منتخبات رياضية وطنية شبابية حسب البلد",
    "Category:Native American history by state": "تصنيف:تاريخ الأمريكيين الأصليين حسب الولاية",
    "Category:Native American tribes by state": "تصنيف:قبائل أمريكية أصلية حسب الولاية",
    "Category:Olympic figure skaters by country": "تصنيف:متزلجون فنيون أولمبيون حسب البلد",
    "Category:Penal systems by country": "تصنيف:قانون العقوبات حسب البلد",
    "Category:People by former country": "تصنيف:أشخاص حسب البلد السابق",
    "Category:Political history of the United States by state or territory": "تصنيف:تاريخ الولايات المتحدة السياسي حسب الولاية أو الإقليم",
    "Category:Politics of the United States by state": "تصنيف:سياسة الولايات المتحدة حسب الولاية",
    "Category:Protected areas of the United States by state": "تصنيف:مناطق محمية في الولايات المتحدة حسب الولاية",
    "Category:Road bridges by country": "تصنيف:جسور طرق حسب البلد",
    "Category:Society of the United States by state": "تصنيف:مجتمع الولايات المتحدة حسب الولاية",
    "Category:Television series by city of location": "تصنيف:مسلسلات تلفزيونية حسب مدينة الموقع",
    "Category:Television shows by city of setting": "تصنيف:عروض تلفزيونية حسب مدينة الأحداث",
    "Category:Television stations by country": "تصنيف:محطات تلفزيونية حسب البلد",
    "Category:books about politics by country": "تصنيف:كتب عن سياسة حسب البلد",
    "Category:films by country": "تصنيف:أفلام حسب البلد",
}


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_geography_by_1(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_geography_by_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_geography_by_1", data1),
    ("test_geography_by_2", data2),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
