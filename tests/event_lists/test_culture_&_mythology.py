#
from src import new_func_lab

data = {
    "Category:Berlin University of the Arts": "تصنيف:جامعة برلين للفنون",
    "Category:Celtic mythology in popular culture": "تصنيف:أساطير كلتية في الثقافة الشعبية",
    "Category:Ethnic groups of the Dominican Republic": "تصنيف:مجموعات عرقية في جمهورية الدومينيكان",
    "Category:Russian folklore characters": "تصنيف:شخصيات فلكلورية روسية",
    "Category:Scottish popular culture": "تصنيف:ثقافة شعبية إسكتلندية",
    "Category:Scottish traditions": "تصنيف:تراث إسكتلندي"
}


def ye_test_one_dataset(dataset):
    print(f"len of dataset: {len(dataset)}")
    org = {}
    diff = {}
    data = {x: v for x, v in dataset.items() if v}
    for cat, ar in data.items():
        result = new_func_lab(cat)
        if result == ar:
            assert result == ar
        else:
            org[cat] = ar
            diff[cat] = result

    assert org == diff
