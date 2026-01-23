#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

data1 = {
    "African-American history by state": "تاريخ أمريكي إفريقي حسب الولاية",
    "Airlines by dependent territory": "شركات طيران حسب الأقاليم التابعة",
    "Ambassadors by country of origin": "سفراء حسب البلد الأصل",
    "Ambassadors by mission country": "سفراء حسب بلد البعثة",
    "American basketball coaches by state": "مدربو كرة سلة أمريكيون حسب الولاية",
    "American culture by state": "ثقافة أمريكية حسب الولاية",
    "Awards by country": "جوائز حسب البلد",
    "Books about politics by country": "كتب عن سياسة حسب البلد",
    "Categories by province of Saudi Arabia": "تصنيفات حسب المقاطعة في السعودية",
    "Demographics of the United States by state": "التركيبة السكانية في الولايات المتحدة حسب الولاية",
    "Destroyed churches by country": "كنائس مدمرة حسب البلد",
    "Drama films by country": "أفلام درامية حسب البلد",
    "Economic history of the United States by state": "تاريخ الولايات المتحدة الاقتصادي حسب الولاية",
    "Economy of the United States by state": "اقتصاد الولايات المتحدة حسب الولاية",
    "Environment of the United States by state or territory": "بيئة الولايات المتحدة حسب الولاية أو الإقليم",
    "Expatriate association football managers by country of residence": "مدربو كرة قدم مغتربون حسب بلد الإقامة",
    "Films by city": "أفلام حسب المدينة",
    "Films by country": "أفلام حسب البلد",
    "Geography of the United States by state": "جغرافيا الولايات المتحدة حسب الولاية",
    "Handball competitions by country": "منافسات كرة يد حسب البلد",
    "History of the American Revolution by state": "تاريخ الثورة الأمريكية حسب الولاية",
}

data2 = {
    "Coptic diaspora by country": "شتات قبطي حسب البلد",
    "Coptic diaspora in Africa": "شتات قبطي في إفريقيا",
    "Coptic diaspora in Australia": "شتات قبطي في أستراليا",
    "Coptic diaspora in Canada": "شتات قبطي في كندا",
    "Coptic diaspora in Europe": "شتات قبطي في أوروبا",
    "Coptic diaspora in North America": "شتات قبطي في أمريكا الشمالية",
    "Coptic diaspora in United States": "شتات قبطي في الولايات المتحدة",
    "History of the United States by period by state": "تاريخ الولايات المتحدة حسب الحقبة حسب الولاية",
    "History of the United States by state": "تاريخ الولايات المتحدة حسب الولاية",
    "Images of the United States by state": "صور من الولايات المتحدة حسب الولاية",
    "Ivorian diaspora by country": "شتات إيفواري حسب البلد",
    "Legal history of the United States by state": "تاريخ الولايات المتحدة القانوني حسب الولاية",
    "Military history of the United States by state": "تاريخ الولايات المتحدة العسكري حسب الولاية",
    "Military organization by country": "منظمات عسكرية حسب البلد",
    "Multi-sport clubs by country": "أندية متعددة الرياضات حسب البلد",
    "Mystery films by country": "أفلام غموض حسب البلد",
    "National youth sports teams by country": "منتخبات رياضية وطنية شبابية حسب البلد",
    "Native American tribes by state": "قبائل أمريكية أصلية حسب الولاية",
    "Olympic figure skaters by country": "متزلجون فنيون أولمبيون حسب البلد",
    "Penal systems by country": "قانون العقوبات حسب البلد",
    "People by former country": "أشخاص حسب البلد السابق",
    "Political history of the United States by state or territory": "تاريخ الولايات المتحدة السياسي حسب الولاية أو الإقليم",
    "Politics of the United States by state": "سياسة الولايات المتحدة حسب الولاية",
    "Protected areas of the United States by state": "مناطق محمية في الولايات المتحدة حسب الولاية",
    "Road bridges by country": "جسور طرق حسب البلد",
    "Society of the United States by state": "مجتمع الولايات المتحدة حسب الولاية",
    "Television series by city of location": "مسلسلات تلفزيونية حسب مدينة الموقع",
    "Television shows by city of setting": "عروض تلفزيونية حسب مدينة الأحداث",
    "Television stations by country": "محطات تلفزيونية حسب البلد",
    "books about politics by country": "كتب عن سياسة حسب البلد",
    "films by country": "أفلام حسب البلد",
}


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_geography_by_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_geography_by_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_geography_by_1", data1),
    ("test_geography_by_2", data2),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
