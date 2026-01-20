#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

geography_us_1 = {
    "Louisiana": "لويزيانا",
    "Maine": "مين",
    "Kansas": "كانساس",
    "Kentucky": "كنتاكي",
    "Indiana": "إنديانا",
    "Iowa": "آيوا",
    "Idaho": "أيداهو",
    "Illinois": "إلينوي",
    "Georgia (U.S. state)": "ولاية جورجيا",
    "Hawaii": "هاواي",
    "Florida": "فلوريدا",
    "Delaware": "ديلاوير",
    "Connecticut": "كونيتيكت",
    "Colorado": "كولورادو",
    "California": "كاليفورنيا",
    "Alabama": "ألاباما",
    "Alaska": "ألاسكا",
    "Arizona": "أريزونا",
}

geography_us_2 = {
    "Missouri": "ميزوري",
    "Nebraska": "نبراسكا",
    "Nevada": "نيفادا",
    "New Hampshire": "نيوهامشير",
    "New Jersey": "نيوجيرسي",
    "New Mexico": "نيومكسيكو",
    "New York (state)": "ولاية نيويورك",
    "North Carolina": "كارولاينا الشمالية",
    "North Dakota": "داكوتا الشمالية",
    "Nuclear power by country": "طاقة نووية حسب البلد",
    "Ohio": "أوهايو",
    "Oklahoma": "أوكلاهوما",
    "Pennsylvania": "بنسلفانيا",
    "Oregon": "أوريغن",
    "Utah": "يوتا",
    "Vermont": "فيرمونت",
    "Virginia": "فرجينيا",
    "Washington (state)": "ولاية واشنطن",
}

geography_us_3 = {
    "Wyoming": "وايومنغ",
    "West Virginia": "فرجينيا الغربية",
    "Texas": "تكساس",
    "Tennessee": "تينيسي",
    "South Carolina": "كارولاينا الجنوبية",
    "Rhode Island": "رود آيلاند",
    "South Dakota": "داكوتا الجنوبية",
    "Wisconsin": "ويسكونسن",
    "Arkansas": "أركنساس",
    "Maryland": "ماريلند",
    "Massachusetts": "ماساتشوستس",
    "Michigan": "ميشيغان",
    "Minnesota": "منيسوتا",
    "Mississippi": "مسيسيبي",
    "Montana": "مونتانا",
}

test_data = [
    ("test_geography_us_1", geography_us_1),
    ("test_geography_us_2", geography_us_2),
    ("test_geography_us_3", geography_us_3),
]


@pytest.mark.parametrize("category, expected", geography_us_1.items(), ids=geography_us_1.keys())
@pytest.mark.fast
def test_geography_us_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", geography_us_2.items(), ids=geography_us_2.keys())
@pytest.mark.fast
def test_geography_us_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", geography_us_3.items(), ids=geography_us_3.keys())
@pytest.mark.fast
def test_geography_us_3(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", test_data)
@pytest.mark.dump
def test_geography_us(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
