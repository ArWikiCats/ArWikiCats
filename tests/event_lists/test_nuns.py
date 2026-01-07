#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

data_0 = {
    "Nazis executed by the British military": "نازيون أعدموا من قبل بريطانيون عسكريون",
    "People executed by the British military": "أشخاص أعدموا من قبل بريطانيون عسكريون",
    "People executed by the French military": "أشخاص أعدموا من قبل فرنسيون عسكريون",
    "women in danish military": "المرأة في دنماركيون عسكريون",
    "Fictional Buddhist nuns": "راهبات بوذيات خياليات",

    "20th-century men from Northern Ireland": "رجال من أيرلندا الشمالية في القرن 20",
    "21st-century men from Northern Ireland": "رجال من أيرلندا الشمالية في القرن 21",
    "brazilian women's rights activists": "برازيليون ناشطون في حقوق المرأة",
    "burmese men marathon runners": "عداؤو ماراثون بورميون",
    "canadian men": "رجال كنديون",
    "Men's basketball players from Northern Ireland": "لاعبو كرة سلة من أيرلندا الشمالية",
    "Men's footballers in Papua New Guinea": "لاعبو كرة قدم في بابوا غينيا الجديدة",
    "expatriate men's footballers": "لاعبو كرة قدم رجالية مغتربون",
    "expatriate men's soccer players": "لاعبو كرة قدم رجالية مغتربون",
    "men's footballers in togo": "لاعبو كرة قدم في توغو",
    "puerto rican men high jumpers": "متسابقو قفز عالي بورتوريكيون",
    "turkish women's rights activists": "أتراك ناشطون في حقوق المرأة",
}

data_1 = {
    "20th-century American Buddhist nuns": "راهبات بوذيات أمريكيات في القرن 20",
    "21st-century American Buddhist nuns": "راهبات بوذيات أمريكيات في القرن 21",
    "Chilean men shot putters": "لاعبو دفع ثقل تشيليون",
    "Somalian men sprinters": "عداؤون سريعون صوماليون",
    "Sculptures of men in England": "منحوتات في رجال في إنجلترا",
    "Sculptures of men in London": "منحوتات في رجال في لندن"
}

data_2 = {
    "10th-century Buddhist nuns": "راهبات بوذيات في القرن 10",
    "10th-century Christian nuns": "راهبات مسيحيات في القرن 10",
    "11th-century Buddhist nuns": "راهبات بوذيات في القرن 11",
    "11th-century Christian nuns": "راهبات مسيحيات في القرن 11",
    "12th-century Buddhist nuns": "راهبات بوذيات في القرن 12",
    "12th-century Christian nuns": "راهبات مسيحيات في القرن 12",
    "13th-century Buddhist nuns": "راهبات بوذيات في القرن 13",
    "13th-century Christian nuns": "راهبات مسيحيات في القرن 13",
    "14th-century Buddhist nuns": "راهبات بوذيات في القرن 14",
    "14th-century Christian nuns": "راهبات مسيحيات في القرن 14",
    "15th-century Buddhist nuns": "راهبات بوذيات في القرن 15",
    "15th-century Christian nuns": "راهبات مسيحيات في القرن 15",
    "16th-century Buddhist nuns": "راهبات بوذيات في القرن 16",
    "16th-century Christian nuns": "راهبات مسيحيات في القرن 16",
    "17th-century Buddhist nuns": "راهبات بوذيات في القرن 17",
    "17th-century Christian nuns": "راهبات مسيحيات في القرن 17",
    "18th-century Buddhist nuns": "راهبات بوذيات في القرن 18",
    "18th-century Christian nuns": "راهبات مسيحيات في القرن 18",
    "19th-century Anglican nuns": "راهبات أنجليكيات في القرن 19",
    "19th-century Australian Christian nuns": "راهبات مسيحيات أستراليات في القرن 19",
    "19th-century British Anglican nuns": "راهبات أنجليكيات بريطانيات في القرن 19",
    "19th-century Buddhist nuns": "راهبات بوذيات في القرن 19",
    "19th-century Christian nuns": "راهبات مسيحيات في القرن 19",
    "1st-century Buddhist nuns": "راهبات بوذيات في القرن 1",
    "20th-century Anglican nuns": "راهبات أنجليكيات في القرن 20",
    "20th-century Australian Christian nuns": "راهبات مسيحيات أستراليات في القرن 20",
    "20th-century British Anglican nuns": "راهبات أنجليكيات بريطانيات في القرن 20",
    "20th-century Buddhist nuns": "راهبات بوذيات في القرن 20",
    "20th-century Christian nuns": "راهبات مسيحيات في القرن 20",
    "21st-century Anglican nuns": "راهبات أنجليكيات في القرن 21",
    "21st-century Australian Christian nuns": "راهبات مسيحيات أستراليات في القرن 21",
    "21st-century British Anglican nuns": "راهبات أنجليكيات بريطانيات في القرن 21",
    "21st-century Buddhist nuns": "راهبات بوذيات في القرن 21",
    "21st-century Christian nuns": "راهبات مسيحيات في القرن 21",
    "3rd-century BC Buddhist nuns": "راهبات بوذيات في القرن 3 ق م",
    "4th-century Buddhist nuns": "راهبات بوذيات في القرن 4",
    "4th-century Christian nuns": "راهبات مسيحيات في القرن 4",
    "5th-century Buddhist nuns": "راهبات بوذيات في القرن 5",
    "5th-century Christian nuns": "راهبات مسيحيات في القرن 5",
    "6th-century Buddhist nuns": "راهبات بوذيات في القرن 6",
    "6th-century Christian nuns": "راهبات مسيحيات في القرن 6",
    "7th-century Buddhist nuns": "راهبات بوذيات في القرن 7",
    "7th-century Christian nuns": "راهبات مسيحيات في القرن 7",
    "8th-century Buddhist nuns": "راهبات بوذيات في القرن 8",
    "8th-century Christian nuns": "راهبات مسيحيات في القرن 8",
    "9th-century Buddhist nuns": "راهبات بوذيات في القرن 9",
    "9th-century Christian nuns": "راهبات مسيحيات في القرن 9",
    "American Buddhist nuns": "راهبات بوذيات أمريكيات",
    "American Christian nuns": "راهبات مسيحيات أمريكيات",
    "American Hindu nuns": "راهبات هندوسيات أمريكيات",
    "Australian Christian nuns": "راهبات مسيحيات أستراليات",
    "Belgian Buddhist nuns": "راهبات بوذيات بلجيكيات",
    "British Anglican nuns": "راهبات أنجليكيات بريطانيات",
    "British Buddhist nuns": "راهبات بوذيات بريطانيات",
    "Buddhist nuns by century": "راهبات بوذيات حسب القرن",
    "Buddhist nuns by nationality": "راهبات بوذيات حسب الجنسية",
    "Buddhist nuns of Nara period": "راهبات بوذيات في فترة نارا",
    "Chinese Buddhist nuns": "راهبات بوذيات صينيات",
    "Christian nuns by century": "راهبات مسيحيات حسب القرن",
    "Fictional Christian nuns": "راهبات مسيحيات خياليون",
    "French Buddhist nuns": "راهبات بوذيات فرنسيات",
    "German Buddhist nuns": "راهبات بوذيات ألمانيات",
    "Indian Buddhist nuns": "راهبات بوذيات هنديات",
    "Indian Hindu nuns": "راهبات هندوسيات هنديات",
    "Indonesian Buddhist nuns": "راهبات بوذيات إندونيسيات",
    "Irish Buddhist nuns": "راهبات بوذيات أيرلنديات",
    "Italian Buddhist nuns": "راهبات بوذيات إيطاليات",
    "Japanese Buddhist nuns by period": "راهبات بوذيات يابانيات حسب الحقبة",
    "Japanese Buddhist nuns": "راهبات بوذيات يابانيات",
    "Korean Buddhist nuns": "راهبات بوذيات كوريات",
    "Nepalese Buddhist nuns": "راهبات بوذيات نيباليات",
    "Scottish Buddhist nuns": "راهبات بوذيات إسكتلنديات",
    "Singaporean Buddhist nuns": "راهبات بوذيات سنغافوريات",
    "South Korean Buddhist nuns": "راهبات بوذيات كوريات جنوبيات",
    "Taiwanese Buddhist nuns": "راهبات بوذيات تايوانيات",
    "Thai Buddhist nuns": "راهبات بوذيات تايلنديات",
    "Vietnamese Buddhist nuns": "راهبات بوذيات فيتناميات",
}

data_3 = {
    "Algerian men middle-distance runners": "عداؤو مسافات متوسطة جزائريون",
    "Austrian Giro d'Italia stage winners": "فائزون في مراحل طواف إيطاليا نمساويون",
    "Azerbaijani men marathon runners": "عداؤو ماراثون أذربيجانيون",
    "Brazilian men sprinters": "عداؤون سريعون برازيليون",
    "Burmese men long-distance runners": "عداؤو مسافات طويلة بورميون",
    "Estonian men long-distance runners": "عداؤو مسافات طويلة إستونيون",
    "Gibraltarian men athletes": "لاعبو قوى جبل طارقيون",
    "Guatemalan men middle-distance runners": "عداؤو مسافات متوسطة غواتيماليون",
    "Haitian men athletes": "لاعبو قوى هايتيون",
    "Icelandic deaf people": "أعلام آيسلنديون صم",
    "Iranian men athletes": "لاعبو قوى إيرانيون",
    "Iraqi men middle-distance runners": "عداؤو مسافات متوسطة عراقيون",
    "Kyrgyzstani men marathon runners": "عداؤو ماراثون قيرغيزستانيون",
    "Liechtenstein men sprinters": "عداؤون سريعون ليختنشتانيون",
    "Macedonian men sprinters": "عداؤون سريعون مقدونيون",
    "Men discus throwers": "رماة قرص",
    "Men's footballers in Mongolia": "لاعبو كرة قدم في منغوليا",
    "Nicaraguan men high jumpers": "متسابقو قفز عالي نيكاراغويون",
    "Russian men pole vaulters": "قافزون بالزانة روس",
    "Taiwanese men long jumpers": "لاعبو قفز طويل تايوانيون",
    "Trinidad and Tobago men discus throwers": "رماة قرص ترنيداديون",
    "Abolitionists from Wisconsin": "مناهضون للعبودية من ويسكونسن",
    "Albanian women's rights activists": "ألبان ناشطون في حقوق المرأة",
    "Botswana women's rights activists": "بوتسوانيون ناشطون في حقوق المرأة",
    "Venezuelan women's rights activists": "فنزويليون ناشطون في حقوق المرأة"
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
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_nuns_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
@pytest.mark.fast
def test_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
