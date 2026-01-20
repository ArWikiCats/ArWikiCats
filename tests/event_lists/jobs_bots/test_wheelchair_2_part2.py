"""Unit tests"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

fencers_rugby = {
    "Paralympic medalists in wheelchair basketball": "فائزون بميداليات الألعاب البارالمبية في كرة السلة على الكراسي المتحركة",
    "Paralympic medalists in wheelchair curling": "فائزون بميداليات الألعاب البارالمبية في الكيرلنغ على الكراسي المتحركة",
    "Paralympic medalists in wheelchair fencing": "فائزون بميداليات الألعاب البارالمبية في مبارزة سيف الشيش على الكراسي المتحركة",
    "Paralympic medalists in wheelchair rugby": "فائزون بميداليات الألعاب البارالمبية في الرجبي على الكراسي المتحركة",
    "Paralympic medalists in wheelchair tennis": "فائزون بميداليات الألعاب البارالمبية في كرة المضرب على الكراسي المتحركة",
    "Paralympic wheelchair basketball coaches": "مدربو كرة سلة على كراسي متحركة في الألعاب البارالمبية",
    "Paralympic wheelchair basketball players by country": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية حسب البلد",
    "Paralympic wheelchair basketball players by year": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية حسب السنة",
    "Paralympic wheelchair basketball players for Australia": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في أستراليا",
    "Paralympic wheelchair basketball players for Canada": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في كندا",
    "Paralympic wheelchair basketball players for France": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في فرنسا",
    "Paralympic wheelchair basketball players for Germany": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في ألمانيا",
    "Paralympic wheelchair basketball players for Great Britain": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في بريطانيا العظمى",
    "Paralympic wheelchair basketball players for Israel": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في إسرائيل",
    "Paralympic wheelchair basketball players for Japan": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في اليابان",
    "Paralympic wheelchair basketball players for South Africa": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في جنوب إفريقيا",
    "Paralympic wheelchair basketball players for Spain": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في إسبانيا",
    "Paralympic wheelchair basketball players for the Netherlands": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في هولندا",
    "Paralympic wheelchair basketball players for the United States": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في الولايات المتحدة",
    "Paralympic wheelchair basketball players for Turkey": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في تركيا",
    "Paralympic wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية",
    "Paralympic wheelchair curlers by country": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية حسب البلد",
    "Paralympic wheelchair curlers by year": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية حسب السنة",
    "Paralympic wheelchair curlers for Canada": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في كندا",
    "Paralympic wheelchair curlers for China": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في الصين",
    "Paralympic wheelchair curlers for Denmark": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في الدنمارك",
    "Paralympic wheelchair curlers for Finland": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في فنلندا",
    "Paralympic wheelchair curlers for Germany": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في ألمانيا",
    "Paralympic wheelchair curlers for Great Britain": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في بريطانيا العظمى",
    "Paralympic wheelchair curlers for Italy": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في إيطاليا",
    "Paralympic wheelchair curlers for Japan": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في اليابان",
    "Paralympic wheelchair curlers for Latvia": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في لاتفيا",
    "Paralympic wheelchair curlers for Norway": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في النرويج",
    "Paralympic wheelchair curlers for Russia": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في روسيا",
    "Paralympic wheelchair curlers for Slovakia": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في سلوفاكيا",
    "Paralympic wheelchair curlers for South Korea": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في كوريا الجنوبية",
    "Paralympic wheelchair curlers for Sweden": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في السويد",
    "Paralympic wheelchair curlers for Switzerland": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في سويسرا",
    "Paralympic wheelchair curlers for the United States": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في الولايات المتحدة",
    "Paralympic wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية",
    "Paralympic wheelchair fencers by country": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية حسب البلد",
    "Paralympic wheelchair fencers by year": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية حسب السنة",
    "Paralympic wheelchair fencers for Australia": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في أستراليا",
    "Paralympic wheelchair fencers for Belarus": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في روسيا البيضاء",
    "Paralympic wheelchair fencers for Brazil": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في البرازيل",
    "Paralympic wheelchair fencers for Canada": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في كندا",
    "Paralympic wheelchair fencers for China": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في الصين",
    "Paralympic wheelchair fencers for France": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في فرنسا",
    "Paralympic wheelchair fencers for Georgia (country)": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في جورجيا",
    "Paralympic wheelchair fencers for Germany": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في ألمانيا",
    "Paralympic wheelchair fencers for Great Britain": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في بريطانيا العظمى",
    "Paralympic wheelchair fencers for Hong Kong": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في هونغ كونغ",
    "Paralympic wheelchair fencers for Hungary": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في المجر",
    "Paralympic wheelchair fencers for Iraq": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في العراق",
    "Paralympic wheelchair fencers for Israel": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في إسرائيل",
    "Paralympic wheelchair fencers for Italy": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في إيطاليا",
    "Paralympic wheelchair fencers for Japan": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في اليابان",
    "Paralympic wheelchair fencers for Latvia": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في لاتفيا",
    "Paralympic wheelchair fencers for Poland": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في بولندا",
    "Paralympic wheelchair fencers for Russia": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في روسيا",
    "Paralympic wheelchair fencers for Spain": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في إسبانيا",
    "Paralympic wheelchair fencers for Thailand": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في تايلاند",
    "Paralympic wheelchair fencers for the United States": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في الولايات المتحدة",
    "Paralympic wheelchair fencers for Turkey": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في تركيا",
    "Paralympic wheelchair fencers for Ukraine": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية في أوكرانيا",
    "Paralympic wheelchair fencers": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية",
    "Paralympic wheelchair rugby coaches": "مدربو رجبي على كراسي متحركة في الألعاب البارالمبية",
    "Paralympic wheelchair rugby players by country": "لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية حسب البلد",
    "Paralympic wheelchair rugby players by year": "لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية حسب السنة",
    "Paralympic wheelchair rugby players for Australia": "لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية في أستراليا",
    "Paralympic wheelchair rugby players for Canada": "لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية في كندا",
    "Paralympic wheelchair rugby players for Great Britain": "لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية في بريطانيا العظمى",
    "Paralympic wheelchair rugby players for Japan": "لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية في اليابان",
    "Paralympic wheelchair rugby players for New Zealand": "لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية في نيوزيلندا",
    "Paralympic wheelchair rugby players for the United States": "لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية في الولايات المتحدة",
    "Paralympic wheelchair rugby players": "لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية",
}


wheelchair_tennis = {
    "Paralympic wheelchair tennis players by country": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية حسب البلد",
    "Paralympic wheelchair tennis players by year": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية حسب السنة",
    "Paralympic wheelchair tennis players for Argentina": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في الأرجنتين",
    "Paralympic wheelchair tennis players for Australia": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في أستراليا",
    "Paralympic wheelchair tennis players for Austria": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في النمسا",
    "Paralympic wheelchair tennis players for Belgium": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في بلجيكا",
    "Paralympic wheelchair tennis players for Brazil": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في البرازيل",
    "Paralympic wheelchair tennis players for Canada": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في كندا",
    "Paralympic wheelchair tennis players for Chile": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في تشيلي",
    "Paralympic wheelchair tennis players for China": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في الصين",
    "Paralympic wheelchair tennis players for Colombia": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في كولومبيا",
    "Paralympic wheelchair tennis players for France": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في فرنسا",
    "Paralympic wheelchair tennis players for Germany": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في ألمانيا",
    "Paralympic wheelchair tennis players for Great Britain": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في بريطانيا العظمى",
    "Paralympic wheelchair tennis players for Hungary": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في المجر",
    "Paralympic wheelchair tennis players for Israel": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في إسرائيل",
    "Paralympic wheelchair tennis players for Japan": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في اليابان",
    "Paralympic wheelchair tennis players for Poland": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في بولندا",
    "Paralympic wheelchair tennis players for South Africa": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في جنوب إفريقيا",
    "Paralympic wheelchair tennis players for Spain": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في إسبانيا",
    "Paralympic wheelchair tennis players for Sri Lanka": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في سريلانكا",
    "Paralympic wheelchair tennis players for Sweden": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في السويد",
    "Paralympic wheelchair tennis players for Switzerland": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في سويسرا",
    "Paralympic wheelchair tennis players for Thailand": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في تايلاند",
    "Paralympic wheelchair tennis players for the Netherlands": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في هولندا",
    "Paralympic wheelchair tennis players for the United States": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في الولايات المتحدة",
    "Paralympic wheelchair tennis players for Turkey": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في تركيا",
    "Paralympic wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية",
}


test_data = [
    ("test_wheelchair_fencers_rugby", fencers_rugby),
    ("test_wheelchair_tennis", wheelchair_tennis),
]


@pytest.mark.parametrize("category, expected", fencers_rugby.items(), ids=fencers_rugby.keys())
@pytest.mark.fast
def test_wheelchair_fencers_rugby(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", wheelchair_tennis.items(), ids=wheelchair_tennis.keys())
@pytest.mark.fast
def test_wheelchair_tennis(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.dump
@pytest.mark.parametrize("name,data", test_data)
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
