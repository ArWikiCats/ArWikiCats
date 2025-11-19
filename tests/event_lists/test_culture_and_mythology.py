#
from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset, dump_diff

data = {
    "Category:Berlin University of the Arts": "تصنيف:جامعة برلين للفنون",
    "Category:Celtic mythology in popular culture": "تصنيف:أساطير كلتية في الثقافة الشعبية",
    "Category:Ethnic groups of the Dominican Republic": "تصنيف:مجموعات عرقية في جمهورية الدومينيكان",
    "Category:Russian folklore characters": "تصنيف:شخصيات فلكلورية روسية",
    "Category:Scottish popular culture": "تصنيف:ثقافة شعبية إسكتلندية",
    "Category:Scottish traditions": "تصنيف:تراث إسكتلندي",
}


def test_culture_and_mythology():
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_culture_and_mythology")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
