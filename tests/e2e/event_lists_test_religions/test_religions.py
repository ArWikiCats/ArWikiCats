#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

religions_data = {
    "Conspiracy theories involving Muslims": "نظريات مؤامرة تشمل مسلمون",
    "Discrimination against Muslims": "تمييز ضد مسلمون",
    "Jews and Judaism in Appalachia": "اليهود واليهودية في الأبالاش",
    "Massacres of Muslims": "مذابح في مسلمون",
    "Muslims from Alabama": "مسلمون من ألاباما",
    "Muslims from Arizona": "مسلمون من أريزونا",
    "Muslims from Arkansas": "مسلمون من أركنساس",
    "Muslims from California": "مسلمون من كاليفورنيا",
    "Muslims from Colorado": "مسلمون من كولورادو",
    "Muslims from Connecticut": "مسلمون من كونيتيكت",
    "Muslims from Delaware": "مسلمون من ديلاوير",
    "Muslims from Florida": "مسلمون من فلوريدا",
    "Muslims from Georgia (country)": "مسلمون من جورجيا",
    "Muslims from Georgia (U.S. state)": "مسلمون من ولاية جورجيا",
    "Muslims from Idaho": "مسلمون من أيداهو",
    "Muslims from Illinois": "مسلمون من إلينوي",
    "Muslims from Indiana": "مسلمون من إنديانا",
    "Muslims from Iowa": "مسلمون من آيوا",
    "Muslims from Kansas": "مسلمون من كانساس",
    "Muslims from Kentucky": "مسلمون من كنتاكي",
    "Muslims from Louisiana": "مسلمون من لويزيانا",
    "Muslims from Maine": "مسلمون من مين",
    "Muslims from Maryland": "مسلمون من ماريلند",
    "Muslims from Massachusetts": "مسلمون من ماساتشوستس",
    "Muslims from Michigan": "مسلمون من ميشيغان",
    "Muslims from Minnesota": "مسلمون من منيسوتا",
    "Muslims from Mississippi": "مسلمون من مسيسيبي",
    "Muslims from Missouri": "مسلمون من ميزوري",
    "Muslims from Nebraska": "مسلمون من نبراسكا",
    "Muslims from Nevada": "مسلمون من نيفادا",
    "Muslims from New Hampshire": "مسلمون من نيوهامشير",
    "Muslims from New Jersey": "مسلمون من نيوجيرسي",
    "Muslims from New Mexico": "مسلمون من نيومكسيكو",
    "Muslims from New York (state)": "مسلمون من ولاية نيويورك",
    "Muslims from North Carolina": "مسلمون من كارولاينا الشمالية",
    "Muslims from North Dakota": "مسلمون من داكوتا الشمالية",
    "Muslims from Ohio": "مسلمون من أوهايو",
    "Muslims from Oklahoma": "مسلمون من أوكلاهوما",
    "Muslims from Oregon": "مسلمون من أوريغن",
    "Muslims from Overseas France": "مسلمون من مقاطعات وأقاليم ما وراء البحار الفرنسية",
    "Muslims from Pennsylvania": "مسلمون من بنسلفانيا",
    "Muslims from Rhode Island": "مسلمون من رود آيلاند",
    "Muslims from Réunion": "مسلمون من لا ريونيون",
    "Muslims from Tennessee": "مسلمون من تينيسي",
    "Muslims from Texas": "مسلمون من تكساس",
    "Muslims from Ottoman Empire": "مسلمون من الدولة العثمانية",
    "Muslims from Russian Empire": "مسلمون من الإمبراطورية الروسية",
    "Muslims from Virginia": "مسلمون من فرجينيا",
    "Muslims from Washington (state)": "مسلمون من ولاية واشنطن",
    "Muslims from Wisconsin": "مسلمون من ويسكونسن",
    "Muslims": "مسلمون",
    "Persecution of Muslims": "اضطهاد مسلمون",
    "Violence against Muslims by continent": "عنف ضد مسلمون حسب القارة",
    "Violence against Muslims by country": "عنف ضد مسلمون حسب البلد",
    "Violence against Muslims in Asia": "عنف ضد مسلمون في آسيا",
    "Violence against Muslims in North America": "عنف ضد مسلمون في أمريكا الشمالية",
    "Violence against Muslims": "عنف ضد مسلمون",
}

data2 = {
    "Jewish television": "التلفزة اليهودية",
    "Christian television": "التلفزة المسيحية",
    "Jewish musical groups": "فرق موسيقية يهودية",
    "Christian musical groups": "فرق موسيقية مسيحية",
    "Pakistan Muslim League (N)": "الرابطة الإسلامية الباكستانية (ن)",
    "Pakistan Muslim League (Q)": "الجماعة الإسلامية الباكستانية (ق)",
    "People of Jewish Agency for Israel": "أشخاص من الوكالة اليهودية",
    "Police of Nazi Germany": "شرطة ألمانيا النازية",
    "Presidents of Pakistan Muslim League (N)": "رؤساء الرابطة الإسلامية الباكستانية (ن)",
    "Heads of Jewish Agency for Israel": "قادة الوكالة اليهودية",
    "Jewish Agency for Israel": "الوكالة اليهودية",
    "Anti-Jewish pogroms in Russian Empire": "برنامج إبادة اليهود في الإمبراطورية الروسية",
    "Jews from French Mandate for Syria and Lebanon": "يهود من الانتداب الفرنسي على سوريا ولبنان",
}


@pytest.mark.parametrize("category, expected", religions_data.items(), ids=religions_data.keys())
def test_religions_data(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


to_test = [
    ("test_religions_data_1", religions_data),
    ("test_religions_data_2", data2),
]

test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
