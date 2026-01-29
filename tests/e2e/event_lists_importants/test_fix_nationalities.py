#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data0 = {
    "North African American culture": "",
    "North African Cup of Champions": "",
    "North African Futsal Tournament": "",
    "North African campaign": "",
    "North African campaign films": "",
    "North African legendary creatures": "",
}

data1 = {}

data_2 = {
    "American people of North African descent": "أمريكيون من أصل إفريقي شمالي",
    "Argentine people of North African descent": "أرجنتينيون من أصل إفريقي شمالي",
    "Australian people of North African descent": "أستراليون من أصل إفريقي شمالي",
    "Chinese people of North African descent": "صينيون من أصل إفريقي شمالي",
    "Egyptian people of North African descent": "مصريون من أصل إفريقي شمالي",
    "Emirati people of North African descent": "إماراتيون من أصل إفريقي شمالي",
    "European people of North African descent": "أوروبيون من أصل إفريقي شمالي",
    "Filipino people of North African descent": "فلبينيون من أصل إفريقي شمالي",
    "French people of North African descent": "فرنسيون من أصل إفريقي شمالي",
    "Hong Kong people of North African descent": "هونغ كونغيون من أصل إفريقي شمالي",
    "Indian people of North African descent": "هنود من أصل إفريقي شمالي",
    "Indonesian people of North African descent": "إندونيسيون من أصل إفريقي شمالي",
    "Israeli people of North African descent": "إسرائيليون من أصل إفريقي شمالي",
    "Japanese people of North African descent": "يابانيون من أصل إفريقي شمالي",
    "Lebanese people of North African descent": "لبنانيون من أصل إفريقي شمالي",
    "Nigerian people of North African descent": "نيجيريون من أصل إفريقي شمالي",
    "North African Super Cup": "كأس السوبر الإفريقي الشمالي",
    "North African art": "فن إفريقي شمالي",
    "North African cuisine": "مطبخ إفريقي شمالي",
    "North African diaspora": "شتات إفريقي شمالي",
    "North African diaspora in Canada": "شتات إفريقي شمالي في كندا",
    "North African diaspora in France": "شتات إفريقي شمالي في فرنسا",
    "North African diaspora in Israel": "شتات إفريقي شمالي في إسرائيل",
    "North African diaspora in North America": "شتات إفريقي شمالي في أمريكا الشمالية",
    "North African diaspora in Paris": "شتات إفريقي شمالي في باريس",
    "North African diaspora in the United States": "شتات إفريقي شمالي في الولايات المتحدة",
    "North African musical instruments": "آلات موسيقية إفريقية شمالية",
    "North African people": "إفريقيون شماليون",
    "People of North African descent": "أشخاص من أصل إفريقي شمالي",
    "Tunisian people of North African descent": "تونسيون من أصل إفريقي شمالي",
}
data_3 = {}

to_test = [
    ("test_fix_nationalities_data_2", data_2),
    # ("test_fix_nationalities_data_1", data1),
    # ("test_fix_nationalities_data_3", data_3),
]


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
def test_fix_nationalities_data_2(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
