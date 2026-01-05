#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

religions_data = {
    "Children's books about Islam and Muslims": "تصنيف:كتب أطفال عن الإسلام ومسلمون",
    "Conspiracy theories involving Muslims": "تصنيف:نظريات مؤامرة تشمل مسلمون",
    "Discrimination against Muslims": "تصنيف:تمييز ضد مسلمون",
    "Jews and Judaism in Appalachia": "تصنيف:اليهود واليهودية في الأبالاش",
    "Massacres of Muslims": "تصنيف:مذابح في مسلمون",
    "Muslims from Alabama": "تصنيف:مسلمون من ألاباما",
    "Muslims from Arizona": "تصنيف:مسلمون من أريزونا",
    "Muslims from Arkansas": "تصنيف:مسلمون من أركنساس",
    "Muslims from California": "تصنيف:مسلمون من كاليفورنيا",
    "Muslims from Colorado": "تصنيف:مسلمون من كولورادو",
    "Muslims from Connecticut": "تصنيف:مسلمون من كونيتيكت",
    "Muslims from Delaware": "تصنيف:مسلمون من ديلاوير",
    "Muslims from Florida": "تصنيف:مسلمون من فلوريدا",
    "Muslims from Georgia (country)": "تصنيف:مسلمون من جورجيا",
    "Muslims from Georgia (U.S. state)": "تصنيف:مسلمون من ولاية جورجيا",
    "Muslims from Idaho": "تصنيف:مسلمون من أيداهو",
    "Muslims from Illinois": "تصنيف:مسلمون من إلينوي",
    "Muslims from Indiana": "تصنيف:مسلمون من إنديانا",
    "Muslims from Iowa": "تصنيف:مسلمون من آيوا",
    "Muslims from Kansas": "تصنيف:مسلمون من كانساس",
    "Muslims from Kentucky": "تصنيف:مسلمون من كنتاكي",
    "Muslims from Louisiana": "تصنيف:مسلمون من لويزيانا",
    "Muslims from Maine": "تصنيف:مسلمون من مين",
    "Muslims from Maryland": "تصنيف:مسلمون من ماريلند",
    "Muslims from Massachusetts": "تصنيف:مسلمون من ماساتشوستس",
    "Muslims from Michigan": "تصنيف:مسلمون من ميشيغان",
    "Muslims from Minnesota": "تصنيف:مسلمون من منيسوتا",
    "Muslims from Mississippi": "تصنيف:مسلمون من مسيسيبي",
    "Muslims from Missouri": "تصنيف:مسلمون من ميزوري",
    "Muslims from Nebraska": "تصنيف:مسلمون من نبراسكا",
    "Muslims from Nevada": "تصنيف:مسلمون من نيفادا",
    "Muslims from New Hampshire": "تصنيف:مسلمون من نيوهامشير",
    "Muslims from New Jersey": "تصنيف:مسلمون من نيوجيرسي",
    "Muslims from New Mexico": "تصنيف:مسلمون من نيومكسيكو",
    "Muslims from New York (state)": "تصنيف:مسلمون من ولاية نيويورك",
    "Muslims from North Carolina": "تصنيف:مسلمون من كارولاينا الشمالية",
    "Muslims from North Dakota": "تصنيف:مسلمون من داكوتا الشمالية",
    "Muslims from Ohio": "تصنيف:مسلمون من أوهايو",
    "Muslims from Oklahoma": "تصنيف:مسلمون من أوكلاهوما",
    "Muslims from Oregon": "تصنيف:مسلمون من أوريغن",
    "Muslims from Overseas France": "تصنيف:مسلمون من مقاطعات وأقاليم ما وراء البحار الفرنسية",
    "Muslims from Pennsylvania": "تصنيف:مسلمون من بنسلفانيا",
    "Muslims from Rhode Island": "تصنيف:مسلمون من رود آيلاند",
    "Muslims from Réunion": "تصنيف:مسلمون من لا ريونيون",
    "Muslims from Tennessee": "تصنيف:مسلمون من تينيسي",
    "Muslims from Texas": "تصنيف:مسلمون من تكساس",
    "Muslims from Ottoman Empire": "تصنيف:مسلمون من الدولة العثمانية",
    "Muslims from Russian Empire": "تصنيف:مسلمون من الإمبراطورية الروسية",
    "Muslims from Virginia": "تصنيف:مسلمون من فرجينيا",
    "Muslims from Washington (state)": "تصنيف:مسلمون من ولاية واشنطن",
    "Muslims from Wisconsin": "تصنيف:مسلمون من ويسكونسن",
    "Muslims": "تصنيف:مسلمون",
    "Persecution of Muslims": "تصنيف:اضطهاد مسلمون",
    "Violence against Muslims by continent": "تصنيف:عنف ضد مسلمون حسب القارة",
    "Violence against Muslims by country": "تصنيف:عنف ضد مسلمون حسب البلد",
    "Violence against Muslims in Asia": "تصنيف:عنف ضد مسلمون في آسيا",
    "Violence against Muslims in North America": "تصنيف:عنف ضد مسلمون في أمريكا الشمالية",
    "Violence against Muslims": "تصنيف:عنف ضد مسلمون",
}

data2 = {
    "Jewish television": "تصنيف:التلفزة اليهودية",
    "Christian television": "تصنيف:التلفزة المسيحية",
    "Jewish musical groups": "تصنيف:فرق موسيقية يهودية",
    "Christian musical groups": "تصنيف:فرق موسيقية مسيحية",
    "Pakistan Muslim League (N)": "تصنيف:الرابطة الإسلامية الباكستانية (ن)",
    "Pakistan Muslim League (Q)": "تصنيف:الجماعة الإسلامية الباكستانية (ق)",
    "People of Jewish Agency for Israel": "تصنيف:أشخاص من الوكالة اليهودية",
    "Police of Nazi Germany": "تصنيف:شرطة ألمانيا النازية",
    "Presidents of Pakistan Muslim League (N)": "تصنيف:رؤساء الرابطة الإسلامية الباكستانية (ن)",
    "Heads of Jewish Agency for Israel": "تصنيف:قادة الوكالة اليهودية",
    "Jewish Agency for Israel": "تصنيف:الوكالة اليهودية",
    "Anti-Jewish pogroms in Russian Empire": "تصنيف:برنامج إبادة اليهود في الإمبراطورية الروسية",
    "Jews from French Mandate for Syria and Lebanon": "تصنيف:يهود من الانتداب الفرنسي على سوريا ولبنان",
}


@pytest.mark.parametrize("category, expected", religions_data.items(), ids=religions_data.keys())
def test_religions_data(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


to_test = [
    ("test_religions_data_1", religions_data),
    ("test_religions_data_2", data2),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    # add_result = {x: v for x, v in data.items() if x in diff_result and "" == diff_result.get(x)}
    # dump_diff(add_result, f"{name}_add")
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
