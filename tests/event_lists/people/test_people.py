import pytest
from load_one_data import dump_diff, ye_test_one_dataset_new


@pytest.mark.slow
def test_people_1():
    data = {
        "Category:People executed by Afghanistan": "تصنيف:أشخاص أعدموا من قبل أفغانستان",
        "Category:People in arts occupations by nationality": "تصنيف:مهن أشخاص في الفنون حسب الجنسية",
        "Category:People of Ivorian descent": "تصنيف:أشخاص من أصل إيفواري",
        "Category:Polish women by occupation": "تصنيف:بولنديات حسب المهنة",
        "Category:Portuguese healthcare managers": "تصنيف:مدراء رعاية صحية برتغاليون",
        "Category:Prisoners and detainees of Afghanistan": "تصنيف:سجناء ومعتقلون في أفغانستان",
        "Category:Prisons in Afghanistan": "تصنيف:سجون في أفغانستان",
        "Category:Scholars by subfield": "تصنيف:دارسون حسب الحقل الفرعي",
        "Category:Women in business by nationality": "تصنيف:سيدات أعمال حسب الجنسية",
        "Category:women in business": "تصنيف:سيدات أعمال",
    }

    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset_new(data)

    dump_diff(diff_result, "test_people_1")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


def test_people_2():
    data = {
        "Category:Iranian nuclear medicine physicians": "تصنيف:أطباء طب نووي إيرانيون",
        "Category:Israeli people of Northern Ireland descent": "تصنيف:إسرائيليون من أصل أيرلندي شمالي",
        "Category:Italian defectors to the Soviet Union": "تصنيف:إيطاليون منشقون إلى الاتحاد السوفيتي",
        "Category:Ivorian American": "تصنيف:أمريكيون إيفواريون",
        "Category:Ivorian diaspora in Asia": "تصنيف:شتات إيفواري في آسيا",
        "Category:Medical doctors by specialty and nationality": "تصنيف:أطباء حسب التخصص والجنسية",
        "Category:Multi-instrumentalists": "تصنيف:عازفون على عدة آلات",
        "Category:People by nationality and status": "تصنيف:أشخاص حسب الجنسية والحالة",
    }
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset_new(data)

    dump_diff(diff_result, "test_people_2")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


def test_people_3():
    data = {
        "Category:Canadian nuclear medicine physicians": "تصنيف:أطباء طب نووي كنديون",
        "Category:Croatian nuclear medicine physicians": "تصنيف:أطباء طب نووي كروات",
        "Category:Expatriate male actors in New Zealand": "تصنيف:ممثلون ذكور مغتربون في نيوزيلندا",
        "Category:Expatriate male actors": "تصنيف:ممثلون ذكور مغتربون",
        "Category:German nuclear medicine physicians": "تصنيف:أطباء طب نووي ألمان",
        "Category:Immigrants to New Zealand": "تصنيف:مهاجرون إلى نيوزيلندا",
        "Category:Immigration to New Zealand": "تصنيف:الهجرة إلى نيوزيلندا",
        "Category:Internees at the Sheberghan Prison": "تصنيف:معتقلين في سجن شيبرغان",
    }
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset_new(data)

    dump_diff(diff_result, "test_people_3")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


def test_people_4():
    data = {
        "Category:Afghan diplomats": "تصنيف:دبلوماسيون أفغان",
        "Category:Ambassadors of Afghanistan": "تصنيف:سفراء أفغانستان",
        "Category:Ambassadors of the Ottoman Empire": "تصنيف:سفراء الدولة العثمانية",
        "Category:Ambassadors to the Ottoman Empire": "تصنيف:سفراء لدى الدولة العثمانية",
        "Category:American nuclear medicine physicians": "تصنيف:أطباء طب نووي أمريكيون",
        "Category:Argentine multi-instrumentalists": "تصنيف:عازفون على عدة آلات أرجنتينيون",
        "Category:Attacks on diplomatic missions": "تصنيف:هجمات على بعثات دبلوماسية",
        "Category:Australian Internet celebrities": "تصنيف:مشاهير إنترنت أستراليون",
    }
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset_new(data)

    dump_diff(diff_result, "test_people_4")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
