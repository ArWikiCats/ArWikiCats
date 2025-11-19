#
import pytest
from load_one_data import dump_diff, ye_test_one_dataset

from src import new_func_lab_final_label


@pytest.mark.fast
def test_geography_by_1():
    data = {
        "Category:African-American history by state": "تصنيف:تاريخ أمريكي إفريقي حسب الولاية",
        "Category:Airlines by dependent territory": "تصنيف:شركات طيران حسب الأقاليم التابعة",
        "Category:Ambassadors by country of origin": "تصنيف:سفراء حسب البلد الأصل",
        "Category:Ambassadors by mission country": "تصنيف:سفراء حسب بلد البعثة",
        "Category:American Civil War by state navigational boxes": "تصنيف:صناديق تصفح الحرب الأهلية الأمريكية حسب الولاية",
        "Category:American basketball coaches by state": "تصنيف:مدربو كرة سلة أمريكيون حسب الولاية",
        "Category:American culture by state": "تصنيف:ثقافة أمريكية حسب الولاية",
        "Category:Awards by country": "تصنيف:جوائز حسب البلد",
        "Category:Books about politics by country": "تصنيف:كتب عن سياسة حسب البلد",
        "Category:Categories by province of Saudi Arabia": "تصنيفات حسب الإقليم في السعودية",
    }
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_geography_by_1")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


def test_geography_by_2():
    data = {
        "Category:Demographics of the United States by state": "تصنيف:التركيبة السكانية في الولايات المتحدة حسب الولاية",
        "Category:Destroyed churches by country": "تصنيف:كنائس مدمرة حسب البلد",
        "Category:Drama films by country": "تصنيف:أفلام درامية حسب البلد",
        "Category:Economic history of the United States by state": "تصنيف:تاريخ الولايات المتحدة الاقتصادي حسب الولاية",
        "Category:Economy of the United States by state": "تصنيف:اقتصاد الولايات المتحدة حسب الولاية",
        "Category:Environment of the United States by state or territory": "تصنيف:بيئة الولايات المتحدة حسب الولاية أو الإقليم",
        "Category:Expatriate association football managers by country of residence": "تصنيف:مدربو كرة قدم مغتربون حسب بلد الإقامة",
        "Category:Films by city of shooting location": "تصنيف:أفلام حسب مدينة التصوير",
        "Category:Films by city": "تصنيف:أفلام حسب المدينة",
        "Category:Films by country": "تصنيف:أفلام حسب البلد",
    }
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_geography_by_2")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


def test_geography_by_3():
    data = {
        "Category:Geography of the United States by state": "تصنيف:جغرافيا الولايات المتحدة حسب الولاية",
        "Category:Handball competitions by country": "تصنيف:منافسات كرة يد حسب البلد",
        "Category:History of the American Revolution by state": "تصنيف:تاريخ الثورة الأمريكية حسب الولاية",
        "Category:History of the United States by period by state": "تصنيف:تاريخ الولايات المتحدة حسب الحقبة حسب الولاية",
        "Category:History of the United States by state": "تصنيف:تاريخ الولايات المتحدة حسب الولاية",
        "Category:Images of the United States by state": "تصنيف:صور من الولايات المتحدة حسب الولاية",
        "Category:Ivorian diaspora by country": "تصنيف:شتات إيفواري حسب البلد",
        "Category:Legal history of the United States by state": "تصنيف:تاريخ الولايات المتحدة القانوني حسب الولاية",
        "Category:Military history of the United States by state": "تصنيف:تاريخ الولايات المتحدة العسكري حسب الولاية",
        "Category:Military organization by country": "تصنيف:منظمات عسكرية حسب البلد",
    }

    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_geography_by_3")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.slow
def test_geography_by_4():
    data = {
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
    }
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_geography_by_4")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


def test_geography_by_5():
    data = {
        "Category:Protected areas of the United States by state": "تصنيف:مناطق محمية في الولايات المتحدة حسب الولاية",
        "Category:Road bridges by country": "تصنيف:جسور طرق حسب البلد",
        "Category:Society of the United States by state": "تصنيف:مجتمع الولايات المتحدة حسب الولاية",
        "Category:Television series by city of location": "تصنيف:مسلسلات تلفزيونية حسب مدينة الموقع",
        "Category:Television series by country of shooting location": "تصنيف:مسلسلات تلفزيونية حسب بلد التصوير",
        "Category:Television shows by city of setting": "تصنيف:عروض تلفزيونية حسب مدينة الأحداث",
        "Category:Television stations by country": "تصنيف:محطات تلفزيونية حسب البلد",
        "Category:books about politics by country": "تصنيف:كتب عن سياسة حسب البلد",
        "Category:films by country": "تصنيف:أفلام حسب البلد",
    }
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_geography_by_5")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
