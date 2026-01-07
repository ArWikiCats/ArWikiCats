#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data_0 = {
    "20th-century men from Northern Ireland": "رجال من أيرلندا الشمالية في القرن 20",
    "21st-century men from Northern Ireland": "رجال من أيرلندا الشمالية في القرن 21",
    "brazilian women's rights activists": "برازيليون ناشطون في حقوق المرأة",
    "burmese men marathon runners": "عداؤو ماراثون رجال بورميون",
    "canadian men": "رجال كنديون",
    "Category:Men's basketball players from Northern Ireland": "تصنيف:لاعبو كرة سلة من أيرلندا الشمالية",
    "Category:Men's footballers in Papua New Guinea": "تصنيف:لاعبو كرة قدم في بابوا غينيا الجديدة",
    "expatriate men's footballers": "لاعبو كرة قدم رجالية مغتربون",
    "expatriate men's soccer players": "لاعبو كرة قدم رجالية مغتربون",
    "Fictional Buddhist nuns": "تصنيف:بوذيون خياليون",
    "men's footballers in togo": "لاعبو كرة قدم في توغو",
    "Nazis executed by the British military": "نازيون أعدموا من قبل الجيش البريطاني",
    "People executed by the British military": "أشخاص أعدموا من قبل الجيش البريطاني",
    "People executed by the French military": "أشخاص أعدموا من قبل الجيش الفرنسي",
    "puerto rican men high jumpers": "متسابقو قفز عالي رجال بورتوريكيون",
    "turkish women's rights activists": "أتراك ناشطون في حقوق المرأة",
    "women in danish military": "المرأة في الجيش الدنماركي",
}

data_1 = {
    "Category:20th-century American Buddhist nuns": "تصنيف:راهبات بوذيات أمريكيات في القرن 20",
    "Category:21st-century American Buddhist nuns": "تصنيف:راهبات بوذيات أمريكيات في القرن 21",
    "Category:Chilean men shot putters": "تصنيف:لاعبو دفع ثقل تشيليون",
    "Category:Somalian men sprinters": "تصنيف:عداؤون سريعون صوماليون",
    "Category:Sculptures of men in England": "تصنيف:منحوتات في رجال في إنجلترا",
    "Category:Sculptures of men in London": "تصنيف:منحوتات في رجال في لندن"
}

data_2 = {
    "10th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 10",
    "10th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 10",
    "11th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 11",
    "11th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 11",
    "12th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 12",
    "12th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 12",
    "13th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 13",
    "13th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 13",
    "14th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 14",
    "14th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 14",
    "15th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 15",
    "15th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 15",
    "16th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 16",
    "16th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 16",
    "17th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 17",
    "17th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 17",
    "18th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 18",
    "18th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 18",
    "19th-century Anglican nuns": "تصنيف:راهبات أنجليكيات في القرن 19",
    "19th-century Australian Christian nuns": "تصنيف:راهبات مسيحيات أستراليات في القرن 19",
    "19th-century British Anglican nuns": "تصنيف:راهبات أنجليكيات بريطانيات في القرن 19",
    "19th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 19",
    "19th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 19",
    "1st-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 1",
    "20th-century Anglican nuns": "تصنيف:راهبات أنجليكيات في القرن 20",
    "20th-century Australian Christian nuns": "تصنيف:راهبات مسيحيات أستراليات في القرن 20",
    "20th-century British Anglican nuns": "تصنيف:راهبات أنجليكيات بريطانيات في القرن 20",
    "20th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 20",
    "20th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 20",
    "21st-century Anglican nuns": "تصنيف:راهبات أنجليكيات في القرن 21",
    "21st-century Australian Christian nuns": "تصنيف:راهبات مسيحيات أستراليات في القرن 21",
    "21st-century British Anglican nuns": "تصنيف:راهبات أنجليكيات بريطانيات في القرن 21",
    "21st-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 21",
    "21st-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 21",
    "3rd-century BC Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 3 ق م",
    "4th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 4",
    "4th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 4",
    "5th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 5",
    "5th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 5",
    "6th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 6",
    "6th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 6",
    "7th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 7",
    "7th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 7",
    "8th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 8",
    "8th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 8",
    "9th-century Buddhist nuns": "تصنيف:راهبات بوذيات في القرن 9",
    "9th-century Christian nuns": "تصنيف:راهبات مسيحيات في القرن 9",
    "American Buddhist nuns": "تصنيف:راهبات بوذيات أمريكيات",
    "American Christian nuns": "تصنيف:راهبات مسيحيات أمريكيات",
    "American Hindu nuns": "تصنيف:راهبات هندوسيات أمريكيات",
    "Australian Christian nuns": "تصنيف:راهبات مسيحيات أستراليات",
    "Belgian Buddhist nuns": "تصنيف:راهبات بوذيات بلجيكيات",
    "British Anglican nuns": "تصنيف:راهبات أنجليكيات بريطانيات",
    "British Buddhist nuns": "تصنيف:راهبات بوذيات بريطانيات",
    "Buddhist nuns by century": "تصنيف:راهبات بوذيات حسب القرن",
    "Buddhist nuns by nationality": "تصنيف:راهبات بوذيات حسب الجنسية",
    "Buddhist nuns of Nara period": "تصنيف:راهبات بوذيات في فترة نارا",
    "Chinese Buddhist nuns": "تصنيف:راهبات بوذيات صينيات",
    "Christian nuns by century": "تصنيف:راهبات مسيحيات حسب القرن",
    "Fictional Christian nuns": "تصنيف:راهبات مسيحيات خياليون",
    "French Buddhist nuns": "تصنيف:راهبات بوذيات فرنسيات",
    "German Buddhist nuns": "تصنيف:راهبات بوذيات ألمانيات",
    "Indian Buddhist nuns": "تصنيف:راهبات بوذيات هنديات",
    "Indian Hindu nuns": "تصنيف:راهبات هندوسيات هنديات",
    "Indonesian Buddhist nuns": "تصنيف:راهبات بوذيات إندونيسيات",
    "Irish Buddhist nuns": "تصنيف:راهبات بوذيات أيرلنديات",
    "Italian Buddhist nuns": "تصنيف:راهبات بوذيات إيطاليات",
    "Japanese Buddhist nuns by period": "تصنيف:راهبات بوذيات يابانيات حسب الحقبة",
    "Japanese Buddhist nuns": "تصنيف:راهبات بوذيات يابانيات",
    "Korean Buddhist nuns": "تصنيف:راهبات بوذيات كوريات",
    "Nepalese Buddhist nuns": "تصنيف:راهبات بوذيات نيباليات",
    "Scottish Buddhist nuns": "تصنيف:راهبات بوذيات إسكتلنديات",
    "Singaporean Buddhist nuns": "تصنيف:راهبات بوذيات سنغافوريات",
    "South Korean Buddhist nuns": "تصنيف:راهبات بوذيات كوريات جنوبيات",
    "Taiwanese Buddhist nuns": "تصنيف:راهبات بوذيات تايوانيات",
    "Thai Buddhist nuns": "تصنيف:راهبات بوذيات تايلنديات",
    "Vietnamese Buddhist nuns": "تصنيف:راهبات بوذيات فيتناميات",
}

data_3 = {
    "Category:Algerian men middle-distance runners": "تصنيف:عداؤو مسافات متوسطة جزائريون",
    "Category:Austrian Giro d'Italia stage winners": "تصنيف:فائزون في مراحل طواف إيطاليا نمساويون",
    "Category:Azerbaijani men marathon runners": "تصنيف:عداؤو ماراثون أذربيجانيون",
    "Category:Brazilian men sprinters": "تصنيف:عداؤون سريعون برازيليون",
    "Category:Burmese men long-distance runners": "تصنيف:عداؤو مسافات طويلة بورميون",
    "Category:Estonian men long-distance runners": "تصنيف:عداؤو مسافات طويلة إستونيون",
    "Category:Gibraltarian men athletes": "تصنيف:لاعبو قوى جبل طارقيون",
    "Category:Guatemalan men middle-distance runners": "تصنيف:عداؤو مسافات متوسطة غواتيماليون",
    "Category:Haitian men athletes": "تصنيف:لاعبو قوى هايتيون",
    "Category:Icelandic deaf people": "تصنيف:أعلام آيسلنديون صم",
    "Category:Iranian men athletes": "تصنيف:لاعبو قوى إيرانيون",
    "Category:Iraqi men middle-distance runners": "تصنيف:عداؤو مسافات متوسطة عراقيون",
    "Category:Kyrgyzstani men marathon runners": "تصنيف:عداؤو ماراثون قيرغيزستانيون",
    "Category:Liechtenstein men sprinters": "تصنيف:عداؤون سريعون ليختنشتانيون",
    "Category:Macedonian men sprinters": "تصنيف:عداؤون سريعون مقدونيون",
    "Category:Men discus throwers": "تصنيف:رماة قرص",
    "Category:Men's footballers in Mongolia": "تصنيف:لاعبو كرة قدم في منغوليا",
    "Category:Nicaraguan men high jumpers": "تصنيف:متسابقو قفز عالي نيكاراغويون",
    "Category:Russian men pole vaulters": "تصنيف:قافزون بالزانة روس",
    "Category:Taiwanese men long jumpers": "تصنيف:لاعبو قفز طويل تايوانيون",
    "Category:Trinidad and Tobago men discus throwers": "تصنيف:رماة قرص ترنيداديون",
    "Category:Abolitionists from Wisconsin": "تصنيف:مناهضون للعبودية من ويسكونسن",
    "Category:Albanian women's rights activists": "تصنيف:ألبان ناشطون في حقوق المرأة",
    "Category:Botswana women's rights activists": "تصنيف:بوتسوانيون ناشطون في حقوق المرأة",
    "Category:Venezuelan women's rights activists": "تصنيف:فنزويليون ناشطون في حقوق المرأة"
}

to_test = [
    ("test_nuns_0", data_0),
    ("test_nuns_1", data_1),
    ("test_nuns_2", data_2),
    ("test_nuns_3", data_3),
]


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_nuns_1(category: str, expected: str) -> None:
    """
    pytest tests/event_lists/test_2.py::test_nuns_1
    """
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_nuns_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
@pytest.mark.fast
def test_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
