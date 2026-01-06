"""Unit tests"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

test_1 = {
    "Category:Wheelchair basketball": "تصنيف:كرة السلة على الكراسي المتحركة",
}

wheelchair_by_nats = {
    "Category:Spanish men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة إسبان",
    "Category:Swiss men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة سويسريون",
    "Category:Turkish men's wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة أتراك",
    "Category:Swiss Wheelchair Curling Championship": "تصنيف:بطولة سويسرا للكيرلنغ على الكراسي المتحركة",
    "Category:European Wheelchair Basketball Championship": "تصنيف:بطولة أوروبا لكرة السلة على الكراسي المتحركة",
    "Category:Parapan American Games medalists in wheelchair basketball": "تصنيف:فائزون بميداليات ألعاب بارابان الأمريكية في كرة السلة على الكراسي المتحركة",
    "Category:Parapan American Games medalists in wheelchair tennis": "تصنيف:فائزون بميداليات ألعاب بارابان الأمريكية في كرة المضرب على الكراسي المتحركة",
    "Category:Parapan American Games wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة في ألعاب بارابان الأمريكية",
    "Category:Parapan American Games wheelchair rugby players": "تصنيف:لاعبو رجبي على كراسي متحركة في ألعاب بارابان الأمريكية",
    "Category:Parapan American Games wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في ألعاب بارابان الأمريكية",
    "Category:Russian wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة روس",
    "Category:Scottish wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة إسكتلنديون",
    "Category:Scottish wheelchair curling champions": "تصنيف:أبطال الكيرلنغ على الكراسي المتحركة إسكتلنديون",
    "Category:Slovak wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة سلوفاكيون",
    "Category:South Korean wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة كوريون جنوبيون",
    "Category:Spanish wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة إسبان",
    "Category:Spanish wheelchair fencers": "تصنيف:مبارزون على الكراسي المتحركة إسبان",
    "Category:Spanish wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة إسبان",
    "Category:Swedish wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة سويديون",
    "Category:Swedish wheelchair curling champions": "تصنيف:أبطال الكيرلنغ على الكراسي المتحركة سويديون",
    "Category:Swedish wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة سويديون",
    "Category:Swiss wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة سويسريون",
    "Category:Swiss wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة سويسريون",
    "Category:Swiss wheelchair curling champions": "تصنيف:أبطال الكيرلنغ على الكراسي المتحركة سويسريون",
    "Category:Swiss wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة سويسريون",
    "Category:Thai wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة تايلنديون",
    "Category:Turkish wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة أتراك",
    "Category:Turkish wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة أتراك",
    "Category:Turkish women's wheelchair basketball players": "تصنيف:لاعبات كرة سلة على كراسي متحركة تركيات",
    "Category:Welsh wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة ويلزيون",
}


wheelchair_basketball = {
    "Category:Wheelchair basketball at the 2020 Parapan American Games": "تصنيف:كرة السلة على الكراسي المتحركة في ألعاب بارابان الأمريكية 2020",
    "Category:Wheelchair basketball at the 2020 Summer Paralympics": "تصنيف:كرة السلة على الكراسي المتحركة في الألعاب البارالمبية الصيفية 2020",
    "Category:Wheelchair basketball at the Asian Para Games": "تصنيف:كرة السلة على الكراسي المتحركة في الألعاب البارالمبية الآسيوية",
    "Category:Wheelchair basketball at the Parapan American Games": "تصنيف:كرة السلة على الكراسي المتحركة في ألعاب بارابان الأمريكية",
    "Category:Wheelchair basketball at the Summer Paralympics": "تصنيف:كرة السلة على الكراسي المتحركة في الألعاب البارالمبية الصيفية",
    "Category:Wheelchair basketball by country": "تصنيف:كرة السلة على الكراسي المتحركة حسب البلد",
    "Category:Wheelchair basketball by year": "تصنيف:كرة السلة على الكراسي المتحركة حسب السنة",
    "Category:Wheelchair basketball coaches": "تصنيف:مدربو كرة سلة على كراسي متحركة",
    "Category:Wheelchair basketball competitions between national teams": "تصنيف:منافسات كرة سلة على كراسي متحركة بين منتخبات وطنية",
    "Category:Wheelchair basketball competitions in Europe": "تصنيف:منافسات كرة سلة على كراسي متحركة في أوروبا",
    "Category:Wheelchair basketball competitions": "تصنيف:منافسات كرة سلة على كراسي متحركة",
    "Category:Wheelchair basketball in Australia": "تصنيف:كرة السلة على الكراسي المتحركة في أستراليا",
    "Category:Wheelchair basketball in Cameroon": "تصنيف:كرة السلة على الكراسي المتحركة في الكاميرون",
    "Category:Wheelchair basketball in Canada": "تصنيف:كرة السلة على الكراسي المتحركة في كندا",
    "Category:Wheelchair basketball in China": "تصنيف:كرة السلة على الكراسي المتحركة في الصين",
    "Category:Wheelchair basketball in France": "تصنيف:كرة السلة على الكراسي المتحركة في فرنسا",
    "Category:Wheelchair basketball in Germany": "تصنيف:كرة السلة على الكراسي المتحركة في ألمانيا",
    "Category:Wheelchair basketball in Israel": "تصنيف:كرة السلة على الكراسي المتحركة في إسرائيل",
    "Category:Wheelchair basketball in Japan": "تصنيف:كرة السلة على الكراسي المتحركة في اليابان",
    "Category:Wheelchair basketball in Kuwait": "تصنيف:كرة السلة على الكراسي المتحركة في الكويت",
    "Category:Wheelchair basketball in New Zealand": "تصنيف:كرة السلة على الكراسي المتحركة في نيوزيلندا",
    "Category:Wheelchair basketball in Poland": "تصنيف:كرة السلة على الكراسي المتحركة في بولندا",
    "Category:Wheelchair basketball in South Korea": "تصنيف:كرة السلة على الكراسي المتحركة في كوريا الجنوبية",
    "Category:Wheelchair basketball in Spain": "تصنيف:كرة السلة على الكراسي المتحركة في إسبانيا",
    "Category:Wheelchair basketball in Switzerland": "تصنيف:كرة السلة على الكراسي المتحركة في سويسرا",
    "Category:Wheelchair basketball in Thailand": "تصنيف:كرة السلة على الكراسي المتحركة في تايلاند",
    "Category:Wheelchair basketball in the Netherlands": "تصنيف:كرة السلة على الكراسي المتحركة في هولندا",
    "Category:Wheelchair basketball in the Philippines": "تصنيف:كرة السلة على الكراسي المتحركة في الفلبين",
    "Category:Wheelchair basketball in the United Kingdom": "تصنيف:كرة السلة على الكراسي المتحركة في المملكة المتحدة",
    "Category:Wheelchair basketball in the United States": "تصنيف:كرة السلة على الكراسي المتحركة في الولايات المتحدة",
    "Category:Wheelchair basketball in Turkey": "تصنيف:كرة السلة على الكراسي المتحركة في تركيا",
}


wheelchair_sports = {
    "Category:Wheelchair basketball leagues in Australia": "تصنيف:دوريات كرة السلة على الكراسي المتحركة في أستراليا",
    "Category:Wheelchair basketball leagues in Europe": "تصنيف:دوريات كرة السلة على الكراسي المتحركة في أوروبا",
    "Category:Wheelchair basketball leagues": "تصنيف:دوريات كرة سلة على كراسي متحركة",
    "Category:Wheelchair basketball players at the 2020 Parapan American Games": "تصنيف:لاعبو كرة سلة على كراسي متحركة في ألعاب بارابان الأمريكية 2020",
    "Category:Wheelchair basketball players at the 2020 Summer Paralympics": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية الصيفية 2020",
    "Category:Wheelchair basketball players by nationality": "تصنيف:لاعبو كرة سلة على كراسي متحركة حسب الجنسية",
    "Category:Wheelchair basketball players in Turkey by team": "تصنيف:لاعبو كرة سلة على كراسي متحركة في تركيا حسب الفريق",
    "Category:Wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة",
    "Category:Wheelchair basketball teams by country": "تصنيف:فرق كرة السلة على الكراسي المتحركة حسب البلد",
    "Category:Wheelchair basketball teams in Greece": "تصنيف:فرق كرة السلة على الكراسي المتحركة في اليونان",
    "Category:Wheelchair basketball teams in Spain": "تصنيف:فرق كرة السلة على الكراسي المتحركة في إسبانيا",
    "Category:Wheelchair basketball teams in Turkey": "تصنيف:فرق كرة السلة على الكراسي المتحركة في تركيا",
    "Category:Wheelchair basketball teams": "تصنيف:فرق كرة سلة على كراسي متحركة",
    "Category:Wheelchair basketball templates": "تصنيف:قوالب كرة سلة على كراسي متحركة",
    "Category:Wheelchair basketball terminology": "تصنيف:مصطلحات كرة سلة على كراسي متحركة",
    "Category:Wheelchair basketball venues in Turkey": "تصنيف:ملاعب كرة السلة على الكراسي المتحركة في تركيا",
    "Category:Wheelchair Basketball World Championship": "تصنيف:بطولة العالم لكرة السلة على الكراسي المتحركة",
    "Category:Wheelchair curlers at the 2020 Winter Paralympics": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية الشتوية 2020",
    "Category:Wheelchair curlers by nationality": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة حسب الجنسية",
    "Category:Wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة",
    "Category:Wheelchair curling at the 2020 Winter Paralympics": "تصنيف:الكيرلنغ على الكراسي المتحركة في الألعاب البارالمبية الشتوية 2020",
    "Category:Wheelchair curling at the Winter Paralympics": "تصنيف:الكيرلنغ على الكراسي المتحركة في الألعاب البارالمبية الشتوية",
    "Category:Wheelchair curling": "تصنيف:الكيرلنغ على الكراسي المتحركة",
    "Category:Wheelchair discus throwers": "تصنيف:رماة قرص على الكراسي المتحركة",
    "Category:Wheelchair fencers at the 2020 Summer Paralympics": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية الصيفية 2020",
    "Category:Wheelchair fencers": "تصنيف:مبارزون على الكراسي المتحركة",
    "Category:Wheelchair fencing at the 2020 Summer Paralympics": "تصنيف:مبارزة سيف الشيش على الكراسي المتحركة في الألعاب البارالمبية الصيفية 2020",
    "Category:Wheelchair fencing at the Summer Paralympics": "تصنيف:مبارزة سيف الشيش على الكراسي المتحركة في الألعاب البارالمبية الصيفية",
    "Category:Wheelchair fencing": "تصنيف:مبارزة سيف الشيش على الكراسي المتحركة",
    "Category:Wheelchair handball competitions": "تصنيف:منافسات كرة يد على كراسي متحركة",
    "Category:Wheelchair handball": "تصنيف:كرة اليد على الكراسي المتحركة",
    "Category:Wheelchair racing at the Summer Olympics": "تصنيف:سباق الكراسي المتحركة في الألعاب الأولمبية الصيفية",
    "Category:Wheelchair racing": "تصنيف:سباق الكراسي المتحركة",
    "Category:Wheelchair rugby at the 2020 Parapan American Games": "تصنيف:الرجبي على الكراسي المتحركة في ألعاب بارابان الأمريكية 2020",
    "Category:Wheelchair rugby at the 2020 Summer Paralympics": "تصنيف:الرجبي على الكراسي المتحركة في الألعاب البارالمبية الصيفية 2020",
    "Category:Wheelchair rugby at the 2020 World Games": "تصنيف:الرجبي على الكراسي المتحركة في دورة الألعاب العالمية 2020",
    "Category:Wheelchair rugby at the Parapan American Games": "تصنيف:الرجبي على الكراسي المتحركة في ألعاب بارابان الأمريكية",
    "Category:Wheelchair rugby at the Summer Paralympics": "تصنيف:الرجبي على الكراسي المتحركة في الألعاب البارالمبية الصيفية",
    "Category:Wheelchair rugby at the World Games": "تصنيف:الرجبي على الكراسي المتحركة في دورة الألعاب العالمية",
    "Category:Wheelchair rugby coaches": "تصنيف:مدربو رجبي على كراسي متحركة",
    "Category:Wheelchair rugby competitions": "تصنيف:منافسات رجبي على كراسي متحركة",
    "Category:Wheelchair rugby people": "تصنيف:أعلام رجبي على كراسي متحركة",
    "Category:Wheelchair rugby players at the 2020 Parapan American Games": "تصنيف:لاعبو رجبي على كراسي متحركة في ألعاب بارابان الأمريكية 2020",
    "Category:Wheelchair rugby players at the 2020 Summer Paralympics": "تصنيف:لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية الصيفية 2020",
    "Category:Wheelchair rugby players by nationality": "تصنيف:لاعبو رجبي على كراسي متحركة حسب الجنسية",
    "Category:Wheelchair rugby players": "تصنيف:لاعبو رجبي على كراسي متحركة",
    "Category:Wheelchair rugby templates": "تصنيف:قوالب رجبي على كراسي متحركة",
    "Category:Wheelchair rugby": "تصنيف:الرجبي على الكراسي المتحركة",
    "Category:Wheelchair tennis at the 2020 Parapan American Games": "تصنيف:كرة المضرب على الكراسي المتحركة في ألعاب بارابان الأمريكية 2020",
    "Category:Wheelchair tennis at the 2020 Summer Paralympics": "تصنيف:كرة المضرب على الكراسي المتحركة في الألعاب البارالمبية الصيفية 2020",
    "Category:Wheelchair tennis at the Asian Para Games": "تصنيف:كرة المضرب على الكراسي المتحركة في الألعاب البارالمبية الآسيوية",
    "Category:Wheelchair tennis at the Parapan American Games": "تصنيف:كرة المضرب على الكراسي المتحركة في ألعاب بارابان الأمريكية",
    "Category:Wheelchair tennis at the Summer Paralympics": "تصنيف:كرة المضرب على الكراسي المتحركة في الألعاب البارالمبية الصيفية",
    "Category:Wheelchair tennis in Spain": "تصنيف:كرة المضرب على الكراسي المتحركة في إسبانيا",
    "Category:Wheelchair tennis players at the 2020 Asian Para Games": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية الآسيوية 2020",
    "Category:Wheelchair tennis players at the 2020 Parapan American Games": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في ألعاب بارابان الأمريكية 2020",
    "Category:Wheelchair tennis players at the 2020 Summer Paralympics": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية الصيفية 2020",
    "Category:Wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة",
    "Category:Wheelchair tennis tournaments": "تصنيف:بطولات كرة مضرب على كراسي متحركة",
    "Category:Wheelchair tennis": "تصنيف:كرة المضرب على الكراسي المتحركة",
    "Category:Women's wheelchair basketball players by nationality": "تصنيف:لاعبات كرة سلة على كراسي متحركة حسب الجنسية",
    "Category:Women's wheelchair basketball players": "تصنيف:لاعبات كرة سلة على كراسي متحركة",
    "Category:World wheelchair curling champions": "تصنيف:أبطال العالم للكيرلنغ على الكراسي المتحركة",
    "Category:Years in wheelchair rugby": "تصنيف:سنوات في الرجبي على الكراسي المتحركة",
}

TEMPORAL_CASES = [
    ("test_wheelchair_by_nats", wheelchair_by_nats),
    ("test_wheelchair_basketball", wheelchair_basketball),
    ("test_wheelchair_sports", wheelchair_sports),
]


@pytest.mark.parametrize("category, expected", test_1.items(), ids=test_1.keys())
@pytest.mark.fast
def test_wheelchair_first(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", wheelchair_by_nats.items(), ids=wheelchair_by_nats.keys())
@pytest.mark.fast
def test_wheelchair_by_nats(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", wheelchair_basketball.items(), ids=wheelchair_basketball.keys())
@pytest.mark.fast
def test_wheelchair_basketball(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", wheelchair_sports.items(), ids=wheelchair_sports.keys())
@pytest.mark.fast
def test_wheelchair_sports(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
