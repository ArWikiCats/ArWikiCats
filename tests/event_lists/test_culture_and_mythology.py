#
from src import new_func_lab
from load_one_data import ye_test_one_dataset

data = {
    "Category:Berlin University of the Arts": "تصنيف:جامعة برلين للفنون",
    "Category:Celtic mythology in popular culture": "تصنيف:أساطير كلتية في الثقافة الشعبية",
    "Category:Ethnic groups of the Dominican Republic": "تصنيف:مجموعات عرقية في جمهورية الدومينيكان",
    "Category:Russian folklore characters": "تصنيف:شخصيات فلكلورية روسية",
    "Category:Scottish popular culture": "تصنيف:ثقافة شعبية إسكتلندية",
    "Category:Scottish traditions": "تصنيف:تراث إسكتلندي"
}


def test_culture_and_mythology():
    print(f"len of data: {len(data)}")
    ye_test_one_dataset(data, new_func_lab)
