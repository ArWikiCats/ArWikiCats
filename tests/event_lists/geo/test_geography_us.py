#
import pytest
from load_one_data import dump_diff, ye_test_one_dataset

from src import new_func_lab_final_label

geography_us_1 = {
    "Category:Louisiana": "تصنيف:لويزيانا",
    "Category:Maine": "تصنيف:مين",
    "Category:Kansas": "تصنيف:كانساس",
    "Category:Kentucky": "تصنيف:كنتاكي",
    "Category:Indiana": "تصنيف:إنديانا",
    "Category:Iowa": "تصنيف:آيوا",
    "Category:Idaho": "تصنيف:أيداهو",
    "Category:Illinois": "تصنيف:إلينوي",
    "Category:Georgia (U.S. state)": "تصنيف:ولاية جورجيا",
    "Category:Hawaii": "تصنيف:هاواي",
    "Category:Florida": "تصنيف:فلوريدا",
    "Category:Delaware": "تصنيف:ديلاوير",
    "Category:Connecticut": "تصنيف:كونيتيكت",
    "Category:Colorado": "تصنيف:كولورادو",
    "Category:California": "تصنيف:كاليفورنيا",
    "Category:Alabama": "تصنيف:ألاباما",
    "Category:Alaska": "تصنيف:ألاسكا",
    "Category:Arizona": "تصنيف:أريزونا",
}

geography_us_2 = {
    "Category:Missouri": "تصنيف:ميزوري",
    "Category:Nebraska": "تصنيف:نبراسكا",
    "Category:Nevada": "تصنيف:نيفادا",
    "Category:New Hampshire": "تصنيف:نيوهامشير",
    "Category:New Jersey": "تصنيف:نيوجيرسي",
    "Category:New Mexico": "تصنيف:نيومكسيكو",
    "Category:New York (state)": "تصنيف:ولاية نيويورك",
    "Category:North Carolina": "تصنيف:كارولاينا الشمالية",
    "Category:North Dakota": "تصنيف:داكوتا الشمالية",
    "Category:Nuclear power by country": "تصنيف:طاقة نووية حسب البلد",
    "Category:Ohio": "تصنيف:أوهايو",
    "Category:Oklahoma": "تصنيف:أوكلاهوما",
    "Category:Pennsylvania": "تصنيف:بنسلفانيا",
    "Category:Oregon": "تصنيف:أوريغون",
    "Category:Utah": "تصنيف:يوتا",
    "Category:Vermont": "تصنيف:فيرمونت",
    "Category:Virginia": "تصنيف:فرجينيا",
    "Category:Washington (state)": "تصنيف:ولاية واشنطن",
}

geography_us_3 = {
    "Category:Wyoming": "تصنيف:وايومنغ",
    "Category:West Virginia": "تصنيف:فيرجينيا الغربية",
    "Category:Texas": "تصنيف:تكساس",
    "Category:Tennessee": "تصنيف:تينيسي",
    "Category:South Carolina": "تصنيف:كارولاينا الجنوبية",
    "Category:Rhode Island": "تصنيف:رود آيلاند",
    "Category:South Dakota": "تصنيف:داكوتا الجنوبية",
    "Category:Wisconsin": "تصنيف:ويسكونسن",
    "Category:Arkansas": "تصنيف:أركنساس",
    "Category:Maryland": "تصنيف:ماريلند",
    "Category:Massachusetts": "تصنيف:ماساتشوستس",
    "Category:Michigan": "تصنيف:ميشيغان",
    "Category:Minnesota": "تصنيف:منيسوتا",
    "Category:Mississippi": "تصنيف:مسيسيبي",
    "Category:Montana": "تصنيف:مونتانا",
}

test_data = [
    ("geography_us_1", geography_us_1),
    ("geography_us_2", geography_us_2),
    ("geography_us_3", geography_us_3),
]


@pytest.mark.parametrize("name,data", test_data)
@pytest.mark.slow
def test_geography_us(name, data):
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
