#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data0 = {}

data1 = {}

data_2 = {
    "American people of North African descent": "أمريكيون من أصل شمال إفريقي",
    "Argentine people of North African descent": "أعلام أرجنتينيون من أصل شمال إفريقي",
    "Australian people of North African descent": "أستراليون من أصل شمال إفريقي",
    "Chinese people of North African descent": "صينيون من أصل شمال إفريقي",
    "Egyptian people of North African descent": "أعلام مصريون من أصل شمال إفريقي",
    "Emirati people of North African descent": "إماراتيون من أصل شمال إفريقي",
    "European people of North African descent": "أوروبيون من أصل شمال إفريقي",
    "Filipino people of North African descent": "فلبينيون من أصل شمال إفريقي",
    "French people of North African descent": "فرنسيون من أصل شمال إفريقي",
    "Hong Kong people of North African descent": "هونغ كونغيون من أصل شمال إفريقي",
    "Indian people of North African descent": "هنود من أصل شمال إفريقي",
    "Indonesian people of North African descent": "إندونيسيون من أصل شمال إفريقي",
    "Israeli people of North African-Jewish descent": "إسرائيليون من أصل يهودي شمال إفريقي",
    "Israeli people of North African descent": "إسرائيليون من أصل شمال إفريقيا",
    "Japanese people of North African descent": "يابانيون من أصل شمال إفريقي",
    "Lebanese people of North African descent": "لبنانيون من أصل شمال إفريقي",
    "Nigerian people of North African descent": "نيجيريون من أصل شمال إفريقي",
    "North African-Jewish culture in Israel": "ثقافة يهودية شمالية إفريقية في إسرائيل",
    "North African-Jewish culture in the United States": "ثقافة يهود شمال إفريقيون في الولايات المتحدة",
    "North African American culture": "ثقافة أمريكية شمالية إفريقية",
    "North African Cup Winners Cup": "كأس شمال إفريقيا للأندية الفائزة بالكؤوس",
    "North African Cup of Champions": "كأس شمال إفريقيا للأندية البطلة",
    "North African Futsal Tournament": "دورة اتحاد شمال إفريقيا لكرة القدم الخماسية",
    "North African Super Cup": "كأس سوبر شمال إفريقيا",
    "North African art": "فن شمال إفريقي",
    "North African campaign": "حملة شمال إفريقيا",
    "North African campaign films": "أفلام الجبهة في شمال إفريقيا",
    "North African cuisine": "مطبخ شمال إفريقي",
    "North African diaspora": "شتات شمال إفريقي",
    "North African diaspora in Canada": "شتات شمال إفريقي في كندا",
    "North African diaspora in France": "شتات شمال إفريقي في فرنسا",
    "North African diaspora in Israel": "شتات شمال إفريقي في إسرائيل",
    "North African diaspora in North America": "شتات شمال إفريقي في أمريكا الشمالية",
    "North African diaspora in Paris": "شتات شمال إفريقي في باريس",
    "North African diaspora in the United States": "شتات شمال إفريقي في الولايات المتحدة",
    "North African football biography stubs": "بذور أعلام كرة قدم شمال إفريقيون",
    "North African legendary creatures": "مخلوقات شمال إفريقيا الأسطورية",
    "North African musical instruments": "آلات موسيقية شمال إفريقية",
    "North African people": "شمال إفريقيون",
    "People of North African-Jewish descent": "أشخاص من أصل يهودي شمال إفريقي",
    "People of North African descent": "أشخاص من أصل شمال إفريقي",
    "Tunisian people of North African descent": "تونسيون من أصل شمال إفريقي",

}

data_3 = {
}

to_test = [
    ("test_fix_nationalities_data_2", data_2),
    # ("test_fix_nationalities_data_1", data1),
    # ("test_fix_nationalities_data_3", data_3),
]


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
def test_fix_nationalities_data_2(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
