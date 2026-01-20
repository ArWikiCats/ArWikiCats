"""Unit tests"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

test_1 = {
    "Wheelchair basketball": "كرة السلة على الكراسي المتحركة",
}

wheelchair_by_nats = {
    "Spanish men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة إسبان",
    "Swiss men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة سويسريون",
    "Turkish men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة أتراك",
    "Swiss Wheelchair Curling Championship": "بطولة سويسرا للكيرلنغ على الكراسي المتحركة",
    "European Wheelchair Basketball Championship": "بطولة أوروبا لكرة السلة على الكراسي المتحركة",
    "Parapan American Games medalists in wheelchair basketball": "فائزون بميداليات ألعاب بارابان الأمريكية في كرة السلة على الكراسي المتحركة",
    "Parapan American Games medalists in wheelchair tennis": "فائزون بميداليات ألعاب بارابان الأمريكية في كرة المضرب على الكراسي المتحركة",
    "Parapan American Games wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة في ألعاب بارابان الأمريكية",
    "Parapan American Games wheelchair rugby players": "لاعبو رجبي على كراسي متحركة في ألعاب بارابان الأمريكية",
    "Parapan American Games wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة في ألعاب بارابان الأمريكية",
    "Russian wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة روس",
    "Scottish wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة إسكتلنديون",
    "Scottish wheelchair curling champions": "أبطال الكيرلنغ على الكراسي المتحركة إسكتلنديون",
    "Slovak wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة سلوفاكيون",
    "South Korean wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة كوريون جنوبيون",
    "Spanish wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة إسبان",
    "Spanish wheelchair fencers": "مبارزون على الكراسي المتحركة إسبان",
    "Spanish wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة إسبان",
    "Swedish wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة سويديون",
    "Swedish wheelchair curling champions": "أبطال الكيرلنغ على الكراسي المتحركة سويديون",
    "Swedish wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة سويديون",
    "Swiss wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة سويسريون",
    "Swiss wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة سويسريون",
    "Swiss wheelchair curling champions": "أبطال الكيرلنغ على الكراسي المتحركة سويسريون",
    "Swiss wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة سويسريون",
    "Thai wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة تايلنديون",
    "Turkish wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة أتراك",
    "Turkish wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة أتراك",
    "Turkish women's wheelchair basketball players": "لاعبات كرة سلة على كراسي متحركة تركيات",
    "Welsh wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة ويلزيون",
}


wheelchair_basketball = {
    "Wheelchair basketball at the 2020 Parapan American Games": "كرة السلة على الكراسي المتحركة في ألعاب بارابان الأمريكية 2020",
    "Wheelchair basketball at the 2020 Summer Paralympics": "كرة السلة على الكراسي المتحركة في الألعاب البارالمبية الصيفية 2020",
    "Wheelchair basketball at the Asian Para Games": "كرة السلة على الكراسي المتحركة في الألعاب البارالمبية الآسيوية",
    "Wheelchair basketball at the Parapan American Games": "كرة السلة على الكراسي المتحركة في ألعاب بارابان الأمريكية",
    "Wheelchair basketball at the Summer Paralympics": "كرة السلة على الكراسي المتحركة في الألعاب البارالمبية الصيفية",
    "Wheelchair basketball by country": "كرة السلة على الكراسي المتحركة حسب البلد",
    "Wheelchair basketball by year": "كرة السلة على الكراسي المتحركة حسب السنة",
    "Wheelchair basketball coaches": "مدربو كرة سلة على كراسي متحركة",
    "Wheelchair basketball competitions between national teams": "منافسات كرة سلة على كراسي متحركة بين منتخبات وطنية",
    "Wheelchair basketball competitions in Europe": "منافسات كرة سلة على كراسي متحركة في أوروبا",
    "Wheelchair basketball competitions": "منافسات كرة سلة على كراسي متحركة",
    "Wheelchair basketball in Australia": "كرة السلة على الكراسي المتحركة في أستراليا",
    "Wheelchair basketball in Cameroon": "كرة السلة على الكراسي المتحركة في الكاميرون",
    "Wheelchair basketball in Canada": "كرة السلة على الكراسي المتحركة في كندا",
    "Wheelchair basketball in China": "كرة السلة على الكراسي المتحركة في الصين",
    "Wheelchair basketball in France": "كرة السلة على الكراسي المتحركة في فرنسا",
    "Wheelchair basketball in Germany": "كرة السلة على الكراسي المتحركة في ألمانيا",
    "Wheelchair basketball in Israel": "كرة السلة على الكراسي المتحركة في إسرائيل",
    "Wheelchair basketball in Japan": "كرة السلة على الكراسي المتحركة في اليابان",
    "Wheelchair basketball in Kuwait": "كرة السلة على الكراسي المتحركة في الكويت",
    "Wheelchair basketball in New Zealand": "كرة السلة على الكراسي المتحركة في نيوزيلندا",
    "Wheelchair basketball in Poland": "كرة السلة على الكراسي المتحركة في بولندا",
    "Wheelchair basketball in South Korea": "كرة السلة على الكراسي المتحركة في كوريا الجنوبية",
    "Wheelchair basketball in Spain": "كرة السلة على الكراسي المتحركة في إسبانيا",
    "Wheelchair basketball in Switzerland": "كرة السلة على الكراسي المتحركة في سويسرا",
    "Wheelchair basketball in Thailand": "كرة السلة على الكراسي المتحركة في تايلاند",
    "Wheelchair basketball in the Netherlands": "كرة السلة على الكراسي المتحركة في هولندا",
    "Wheelchair basketball in the Philippines": "كرة السلة على الكراسي المتحركة في الفلبين",
    "Wheelchair basketball in the United Kingdom": "كرة السلة على الكراسي المتحركة في المملكة المتحدة",
    "Wheelchair basketball in the United States": "كرة السلة على الكراسي المتحركة في الولايات المتحدة",
    "Wheelchair basketball in Turkey": "كرة السلة على الكراسي المتحركة في تركيا",
}


wheelchair_sports = {
    "Wheelchair basketball templates": "قوالب كرة السلة على الكراسي المتحركة",
    "Wheelchair rugby templates": "قوالب الرجبي على الكراسي المتحركة",
    "Wheelchair basketball leagues": "دوريات كرة سلة على كراسي متحركة",
    "Wheelchair basketball players at the 2020 Parapan American Games": "لاعبو كرة سلة على كراسي متحركة في ألعاب بارابان الأمريكية 2020",
    "Wheelchair basketball players at the 2020 Summer Paralympics": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية الصيفية 2020",
    "Wheelchair basketball players by nationality": "لاعبو كرة سلة على كراسي متحركة حسب الجنسية",
    "Wheelchair basketball players in Turkey by team": "لاعبو كرة سلة على كراسي متحركة في تركيا حسب الفريق",
    "Wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة",
    "Wheelchair basketball teams by country": "فرق كرة السلة على الكراسي المتحركة حسب البلد",
    "Wheelchair basketball teams in Greece": "فرق كرة السلة على الكراسي المتحركة في اليونان",
    "Wheelchair basketball teams in Spain": "فرق كرة السلة على الكراسي المتحركة في إسبانيا",
    "Wheelchair basketball teams in Turkey": "فرق كرة السلة على الكراسي المتحركة في تركيا",
    "Wheelchair basketball teams": "فرق كرة السلة على الكراسي المتحركة",
    "Wheelchair basketball terminology": "مصطلحات كرة سلة على كراسي متحركة",
    "Wheelchair basketball venues in Turkey": "ملاعب كرة السلة على الكراسي المتحركة في تركيا",
    "Wheelchair Basketball World Championship": "بطولة العالم لكرة السلة على الكراسي المتحركة",
    "Wheelchair curlers at the 2020 Winter Paralympics": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية الشتوية 2020",
    "Wheelchair curlers by nationality": "لاعبو كيرلنغ على الكراسي المتحركة حسب الجنسية",
    "Wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة",
    "Wheelchair curling at the 2020 Winter Paralympics": "الكيرلنغ على الكراسي المتحركة في الألعاب البارالمبية الشتوية 2020",
    "Wheelchair curling at the Winter Paralympics": "الكيرلنغ على الكراسي المتحركة في الألعاب البارالمبية الشتوية",
    "Wheelchair curling": "الكيرلنغ على الكراسي المتحركة",
    "Wheelchair discus throwers": "رماة قرص على الكراسي المتحركة",
    "Wheelchair fencers at the 2020 Summer Paralympics": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية الصيفية 2020",
    "Wheelchair fencers": "مبارزون على الكراسي المتحركة",
    "Wheelchair fencing at the 2020 Summer Paralympics": "مبارزة سيف الشيش على الكراسي المتحركة في الألعاب البارالمبية الصيفية 2020",
    "Wheelchair fencing at the Summer Paralympics": "مبارزة سيف الشيش على الكراسي المتحركة في الألعاب البارالمبية الصيفية",
    "Wheelchair fencing": "مبارزة سيف الشيش على الكراسي المتحركة",
    "Wheelchair handball competitions": "منافسات كرة يد على كراسي متحركة",
    "Wheelchair handball": "كرة اليد على الكراسي المتحركة",
    "Wheelchair racing at the Summer Olympics": "سباق الكراسي المتحركة في الألعاب الأولمبية الصيفية",
    "Wheelchair racing": "سباق الكراسي المتحركة",
    "Wheelchair rugby at the 2020 Parapan American Games": "الرجبي على الكراسي المتحركة في ألعاب بارابان الأمريكية 2020",
    "Wheelchair rugby at the 2020 Summer Paralympics": "الرجبي على الكراسي المتحركة في الألعاب البارالمبية الصيفية 2020",
    "Wheelchair rugby at the 2020 World Games": "الرجبي على الكراسي المتحركة في دورة الألعاب العالمية 2020",
    "Wheelchair rugby at the Parapan American Games": "الرجبي على الكراسي المتحركة في ألعاب بارابان الأمريكية",
    "Wheelchair rugby at the Summer Paralympics": "الرجبي على الكراسي المتحركة في الألعاب البارالمبية الصيفية",
    "Wheelchair rugby at the World Games": "الرجبي على الكراسي المتحركة في دورة الألعاب العالمية",
    "Wheelchair rugby coaches": "مدربو رجبي على كراسي متحركة",
    "Wheelchair rugby competitions": "منافسات رجبي على كراسي متحركة",
    "Wheelchair rugby people": "أعلام رجبي على كراسي متحركة",
    "Wheelchair rugby players at the 2020 Parapan American Games": "لاعبو رجبي على كراسي متحركة في ألعاب بارابان الأمريكية 2020",
    "Wheelchair rugby players at the 2020 Summer Paralympics": "لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية الصيفية 2020",
    "Wheelchair rugby players by nationality": "لاعبو رجبي على كراسي متحركة حسب الجنسية",
    "Wheelchair rugby players": "لاعبو رجبي على كراسي متحركة",
    "Wheelchair rugby": "الرجبي على الكراسي المتحركة",
    "Wheelchair tennis at the 2020 Parapan American Games": "كرة المضرب على الكراسي المتحركة في ألعاب بارابان الأمريكية 2020",
    "Wheelchair tennis at the 2020 Summer Paralympics": "كرة المضرب على الكراسي المتحركة في الألعاب البارالمبية الصيفية 2020",
    "Wheelchair tennis at the Asian Para Games": "كرة المضرب على الكراسي المتحركة في الألعاب البارالمبية الآسيوية",
    "Wheelchair tennis at the Parapan American Games": "كرة المضرب على الكراسي المتحركة في ألعاب بارابان الأمريكية",
    "Wheelchair tennis at the Summer Paralympics": "كرة المضرب على الكراسي المتحركة في الألعاب البارالمبية الصيفية",
    "Wheelchair tennis in Spain": "كرة المضرب على الكراسي المتحركة في إسبانيا",
    "Wheelchair tennis players at the 2020 Asian Para Games": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية الآسيوية 2020",
    "Wheelchair tennis players at the 2020 Parapan American Games": "لاعبو كرة مضرب على كراسي متحركة في ألعاب بارابان الأمريكية 2020",
    "Wheelchair tennis players at the 2020 Summer Paralympics": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية الصيفية 2020",
    "Wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة",
    "Wheelchair tennis": "كرة المضرب على الكراسي المتحركة",
    "Women's wheelchair basketball players by nationality": "لاعبات كرة سلة على كراسي متحركة حسب الجنسية",
    "Women's wheelchair basketball players": "لاعبات كرة سلة على كراسي متحركة",
    "World wheelchair curling champions": "أبطال العالم للكيرلنغ على الكراسي المتحركة",
    "Years in wheelchair rugby": "سنوات في الرجبي على الكراسي المتحركة",
}

TEMPORAL_CASES = [
    ("test_wheelchair_by_nats", wheelchair_by_nats),
    ("test_wheelchair_basketball", wheelchair_basketball),
    ("test_wheelchair_sports", wheelchair_sports),
]


@pytest.mark.parametrize("category, expected", test_1.items(), ids=test_1.keys())
@pytest.mark.fast
def test_wheelchair_first(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", wheelchair_by_nats.items(), ids=wheelchair_by_nats.keys())
@pytest.mark.fast
def test_wheelchair_by_nats(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", wheelchair_basketball.items(), ids=wheelchair_basketball.keys())
@pytest.mark.fast
def test_wheelchair_basketball(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", wheelchair_sports.items(), ids=wheelchair_sports.keys())
@pytest.mark.fast
def test_wheelchair_sports(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
