"""
Tests
"""

import pytest

from ArWikiCats.ma_bots.country2_lab import get_lab_for_country2

data = {
    "olympic gold medalists": "فائزون بميداليات ذهبية أولمبية",
    "olympic medalists": "فائزون بميداليات أولمبية",
    "women's sports": "الرياضات النسوية",
    "by state": "حسب الولاية",
    "handball competitions": "منافسات كرة يد",
    "georgia (u.s. state)": "ولاية جورجيا",
    "new hampshire": "نيوهامشير",
    "new jersey": "نيوجيرسي",
    "new mexico": "نيومكسيكو",
    "new york (state)": "ولاية نيويورك",
    "north carolina": "كارولاينا الشمالية",
    "north dakota": "داكوتا الشمالية",
    "washington (state)": "ولاية واشنطن",
    "west virginia": "فيرجينيا الغربية",
    "south carolina": "كارولاينا الجنوبية",
    "rhode island": "رود آيلاند",
    "south dakota": "داكوتا الجنوبية",
    "basketball people": "أعلام كرة سلة",
    "ice hockey people": "أعلام هوكي جليد",
    "tennis people": "أعلام كرة مضرب",
    "american television": "التلفزة الأمريكية",
    "american television series": "مسلسلات تلفزيونية أمريكية",
    "american television episodes": "حلقات تلفزيونية أمريكية",
    "american television-seasons": "مواسم تلفزيونية أمريكية",
    "american television series-debuts": "مسلسلات تلفزيونية أمريكية بدأ عرضها في",
    "american television series-endings": "مسلسلات تلفزيونية أمريكية انتهت في",
    "cape verde": "الرأس الأخضر",
    "figure skating films": "أفلام تزلج فني",
    "figure skating media": "إعلام تزلج فني",
    "figure skating": "التزلج الفني",
    "olympic swimming": "سباحة أولمبية",
    "mecha anime and manga": "أنمي ميكا",
    "gymnastics organizations": "منظمات جمباز",
    "national cricket teams": "منتخبات كريكت وطنية",
    "international women's basketball competitions": "منافسات كرة سلة دولية للسيدات",
    "water polo": "كرة الماء",
    "national women's sports teams of": "منتخبات رياضية وطنية نسائية في",
    "world judo championships": "بطولة العالم للجودو",
    "youth athletics competitions": "منافسات ألعاب قوى شبابية",
    "youth athletics": "ألعاب القوى للشباب",
    "youth sports competitions": "منافسات رياضية شبابية",
    "olympic figure skating": "تزلج فني أولمبي",
    "ski jumping": "القفز التزلجي",
    "table tennis clubs": "أندية كرة طاولة",
    "figure skating people": "أعلام تزلج فني",
    "the summer universiade": "الألعاب الجامعية الصيفية",
    "the universiade": "الألعاب الجامعية",
    "television series-endings": "مسلسلات تلفزيونية انتهت في",
    "wheelchair basketball": "كرة السلة على الكراسي المتحركة",
    "wheelchair fencing": "مبارزة سيف الشيش على الكراسي المتحركة",
    "wheelchair tennis": "كرة المضرب على الكراسي المتحركة",
    "wheelchair basketball world championships": "بطولة العالم لكرة السلة على الكراسي المتحركة",
    "national wheelchair rugby league teams": "منتخبات دوري رجبي على كراسي متحركة وطنية",
    "women's world wheelchair basketball championship": "بطولة العالم لكرة السلة على الكراسي المتحركة للسيدات",
    "paralympic medalists": "فائزون بميداليات الألعاب البارالمبية",
    "south africa": "جنوب إفريقيا",
    "south korea": "كوريا الجنوبية",
    "georgia (country)": "جورجيا",
    "hong kong": "هونغ كونغ",
    "new zealand": "نيوزيلندا",
    "sri lanka": "سريلانكا",
    "parapan american games medalists": "فائزون بميداليات ألعاب بارابان الأمريكية",
    "the summer paralympics": "الألعاب البارالمبية الصيفية",
    "wheelchair basketball competitions": "منافسات كرة سلة على كراسي متحركة",
    "wheelchair basketball leagues": "دوريات كرة سلة على كراسي متحركة",
    "wheelchair basketball teams": "فرق كرة سلة على كراسي متحركة",
    "wheelchair basketball templates": "قوالب كرة سلة على كراسي متحركة",
    "wheelchair basketball terminology": "مصطلحات كرة سلة على كراسي متحركة",
    "wheelchair basketball world championship": "بطولة العالم لكرة السلة على الكراسي المتحركة",
    "wheelchair curling": "الكيرلنغ على الكراسي المتحركة",
    "wheelchair handball competitions": "منافسات كرة يد على كراسي متحركة",
    "wheelchair handball": "كرة اليد على الكراسي المتحركة",
    "wheelchair racing": "سباق الكراسي المتحركة",
    "wheelchair rugby": "الرجبي على الكراسي المتحركة",
    "wheelchair rugby competitions": "منافسات رجبي على كراسي متحركة",
    "wheelchair rugby people": "أعلام رجبي على كراسي متحركة",
    "wheelchair rugby templates": "قوالب رجبي على كراسي متحركة",
    "wheelchair tennis tournaments": "بطولات كرة مضرب على كراسي متحركة",
    "air force ": "قوات جوية",
    "german footballers": "لاعبو كرة قدم ألمان",
    "ethiopian basketball players": "لاعبو كرة سلة إثيوبيون",
    "indian cricketers": "لاعبو كريكت هنود",
    "American Soccer League ": "دوري كرة القدم الأمريكية",
    "rugby union tournaments": "بطولات اتحاد رجبي",
    "earthquakes ": "زلازل",
    "floods ": "فيضانات",
    "basketball ": "كرة السلة",
    "latin american": "أمريكيون لاتينيون",
    " egypt": "مصر",
    " france": "فرنسا",
    " qatar": "قطر",
    "basketball  ": "كرة السلة",
    "football  ": "كرة القدم",
    "association football": "كرة قدم",
    "pan-africanist political parties": "أحزاب سياسية وحدوية إفريقية",
    "pan-african parliament": "البرلمان الإفريقي",
    "pan-african democratic party politicians": "سياسيو الحزب الديمقراطي الوحدوي الإفريقي",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=lambda x: x[0])
def test_get_lab_for_country2(category: str, expected: str) -> None:
    result = get_lab_for_country2(category)
    assert result == expected


def test_empty() -> None:
    # Test with a basic input
    result = get_lab_for_country2("test country")
    assert isinstance(result, str)

    result_empty = get_lab_for_country2("")
    assert isinstance(result_empty, str)
