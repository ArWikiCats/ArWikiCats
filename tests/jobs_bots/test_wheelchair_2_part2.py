"""Unit tests"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

fencers_rugby = {
    "Category:Paralympic medalists in wheelchair basketball": "تصنيف:فائزون بميداليات الألعاب البارالمبية في كرة السلة على الكراسي المتحركة",
    "Category:Paralympic medalists in wheelchair curling": "تصنيف:فائزون بميداليات الألعاب البارالمبية في الكيرلنغ على الكراسي المتحركة",
    "Category:Paralympic medalists in wheelchair fencing": "تصنيف:فائزون بميداليات الألعاب البارالمبية في مبارزة سيف الشيش على الكراسي المتحركة",
    "Category:Paralympic medalists in wheelchair rugby": "تصنيف:فائزون بميداليات الألعاب البارالمبية في الرجبي على الكراسي المتحركة",
    "Category:Paralympic medalists in wheelchair tennis": "تصنيف:فائزون بميداليات الألعاب البارالمبية في كرة المضرب على الكراسي المتحركة",
    "Category:Paralympic wheelchair basketball coaches": "تصنيف:مدربو كرة سلة على كراسي متحركة في الألعاب البارالمبية",
    "Category:Paralympic wheelchair basketball players by country": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية حسب البلد",
    "Category:Paralympic wheelchair basketball players by year": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية حسب السنة",
    "Category:Paralympic wheelchair basketball players for Australia": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في أستراليا",
    "Category:Paralympic wheelchair basketball players for Canada": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في كندا",
    "Category:Paralympic wheelchair basketball players for France": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في فرنسا",
    "Category:Paralympic wheelchair basketball players for Germany": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في ألمانيا",
    "Category:Paralympic wheelchair basketball players for Great Britain": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في بريطانيا العظمى",
    "Category:Paralympic wheelchair basketball players for Israel": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في إسرائيل",
    "Category:Paralympic wheelchair basketball players for Japan": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في اليابان",
    "Category:Paralympic wheelchair basketball players for South Africa": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في جنوب إفريقيا",
    "Category:Paralympic wheelchair basketball players for Spain": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في إسبانيا",
    "Category:Paralympic wheelchair basketball players for the Netherlands": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في هولندا",
    "Category:Paralympic wheelchair basketball players for the United States": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في الولايات المتحدة",
    "Category:Paralympic wheelchair basketball players for Turkey": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية في تركيا",
    "Category:Paralympic wheelchair basketball players": "تصنيف:لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية",
    "Category:Paralympic wheelchair curlers by country": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية حسب البلد",
    "Category:Paralympic wheelchair curlers by year": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية حسب السنة",
    "Category:Paralympic wheelchair curlers for Canada": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في كندا",
    "Category:Paralympic wheelchair curlers for China": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في الصين",
    "Category:Paralympic wheelchair curlers for Denmark": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في الدنمارك",
    "Category:Paralympic wheelchair curlers for Finland": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في فنلندا",
    "Category:Paralympic wheelchair curlers for Germany": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في ألمانيا",
    "Category:Paralympic wheelchair curlers for Great Britain": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في بريطانيا العظمى",
    "Category:Paralympic wheelchair curlers for Italy": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في إيطاليا",
    "Category:Paralympic wheelchair curlers for Japan": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في اليابان",
    "Category:Paralympic wheelchair curlers for Latvia": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في لاتفيا",
    "Category:Paralympic wheelchair curlers for Norway": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في النرويج",
    "Category:Paralympic wheelchair curlers for Russia": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في روسيا",
    "Category:Paralympic wheelchair curlers for Slovakia": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في سلوفاكيا",
    "Category:Paralympic wheelchair curlers for South Korea": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في كوريا الجنوبية",
    "Category:Paralympic wheelchair curlers for Sweden": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في السويد",
    "Category:Paralympic wheelchair curlers for Switzerland": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في سويسرا",
    "Category:Paralympic wheelchair curlers for the United States": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية في الولايات المتحدة",
    "Category:Paralympic wheelchair curlers": "تصنيف:لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية",
    "Category:Paralympic wheelchair fencers by country": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية حسب البلد",
    "Category:Paralympic wheelchair fencers by year": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية حسب السنة",
    "Category:Paralympic wheelchair fencers for Australia": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في أستراليا",
    "Category:Paralympic wheelchair fencers for Belarus": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في روسيا البيضاء",
    "Category:Paralympic wheelchair fencers for Brazil": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في البرازيل",
    "Category:Paralympic wheelchair fencers for Canada": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في كندا",
    "Category:Paralympic wheelchair fencers for China": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في الصين",
    "Category:Paralympic wheelchair fencers for France": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في فرنسا",
    "Category:Paralympic wheelchair fencers for Georgia (country)": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في جورجيا",
    "Category:Paralympic wheelchair fencers for Germany": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في ألمانيا",
    "Category:Paralympic wheelchair fencers for Great Britain": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في بريطانيا العظمى",
    "Category:Paralympic wheelchair fencers for Hong Kong": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في هونغ كونغ",
    "Category:Paralympic wheelchair fencers for Hungary": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في المجر",
    "Category:Paralympic wheelchair fencers for Iraq": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في العراق",
    "Category:Paralympic wheelchair fencers for Israel": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في إسرائيل",
    "Category:Paralympic wheelchair fencers for Italy": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في إيطاليا",
    "Category:Paralympic wheelchair fencers for Japan": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في اليابان",
    "Category:Paralympic wheelchair fencers for Latvia": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في لاتفيا",
    "Category:Paralympic wheelchair fencers for Poland": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في بولندا",
    "Category:Paralympic wheelchair fencers for Russia": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في روسيا",
    "Category:Paralympic wheelchair fencers for Spain": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في إسبانيا",
    "Category:Paralympic wheelchair fencers for Thailand": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في تايلاند",
    "Category:Paralympic wheelchair fencers for the United States": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في الولايات المتحدة",
    "Category:Paralympic wheelchair fencers for Turkey": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في تركيا",
    "Category:Paralympic wheelchair fencers for Ukraine": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية في أوكرانيا",
    "Category:Paralympic wheelchair fencers": "تصنيف:مبارزون على الكراسي المتحركة في الألعاب البارالمبية",
    "Category:Paralympic wheelchair rugby coaches": "تصنيف:مدربو رجبي على كراسي متحركة في الألعاب البارالمبية",
    "Category:Paralympic wheelchair rugby players by country": "تصنيف:لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية حسب البلد",
    "Category:Paralympic wheelchair rugby players by year": "تصنيف:لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية حسب السنة",
    "Category:Paralympic wheelchair rugby players for Australia": "تصنيف:لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية في أستراليا",
    "Category:Paralympic wheelchair rugby players for Canada": "تصنيف:لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية في كندا",
    "Category:Paralympic wheelchair rugby players for Great Britain": "تصنيف:لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية في بريطانيا العظمى",
    "Category:Paralympic wheelchair rugby players for Japan": "تصنيف:لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية في اليابان",
    "Category:Paralympic wheelchair rugby players for New Zealand": "تصنيف:لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية في نيوزيلندا",
    "Category:Paralympic wheelchair rugby players for the United States": "تصنيف:لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية في الولايات المتحدة",
    "Category:Paralympic wheelchair rugby players": "تصنيف:لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية",
}


wheelchair_tennis = {
    "Category:Paralympic wheelchair tennis players by country": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية حسب البلد",
    "Category:Paralympic wheelchair tennis players by year": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية حسب السنة",
    "Category:Paralympic wheelchair tennis players for Argentina": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في الأرجنتين",
    "Category:Paralympic wheelchair tennis players for Australia": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في أستراليا",
    "Category:Paralympic wheelchair tennis players for Austria": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في النمسا",
    "Category:Paralympic wheelchair tennis players for Belgium": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في بلجيكا",
    "Category:Paralympic wheelchair tennis players for Brazil": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في البرازيل",
    "Category:Paralympic wheelchair tennis players for Canada": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في كندا",
    "Category:Paralympic wheelchair tennis players for Chile": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في تشيلي",
    "Category:Paralympic wheelchair tennis players for China": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في الصين",
    "Category:Paralympic wheelchair tennis players for Colombia": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في كولومبيا",
    "Category:Paralympic wheelchair tennis players for France": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في فرنسا",
    "Category:Paralympic wheelchair tennis players for Germany": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في ألمانيا",
    "Category:Paralympic wheelchair tennis players for Great Britain": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في بريطانيا العظمى",
    "Category:Paralympic wheelchair tennis players for Hungary": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في المجر",
    "Category:Paralympic wheelchair tennis players for Israel": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في إسرائيل",
    "Category:Paralympic wheelchair tennis players for Japan": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في اليابان",
    "Category:Paralympic wheelchair tennis players for Poland": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في بولندا",
    "Category:Paralympic wheelchair tennis players for South Africa": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في جنوب إفريقيا",
    "Category:Paralympic wheelchair tennis players for Spain": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في إسبانيا",
    "Category:Paralympic wheelchair tennis players for Sri Lanka": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في سريلانكا",
    "Category:Paralympic wheelchair tennis players for Sweden": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في السويد",
    "Category:Paralympic wheelchair tennis players for Switzerland": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في سويسرا",
    "Category:Paralympic wheelchair tennis players for Thailand": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في تايلاند",
    "Category:Paralympic wheelchair tennis players for the Netherlands": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في هولندا",
    "Category:Paralympic wheelchair tennis players for the United States": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في الولايات المتحدة",
    "Category:Paralympic wheelchair tennis players for Turkey": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية في تركيا",
    "Category:Paralympic wheelchair tennis players": "تصنيف:لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية",
}


test_data = [
    ("test_wheelchair_fencers_rugby", fencers_rugby),
    ("test_wheelchair_tennis", wheelchair_tennis),
]


@pytest.mark.parametrize("category, expected", fencers_rugby.items(), ids=fencers_rugby.keys())
@pytest.mark.fast
def test_wheelchair_fencers_rugby(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", wheelchair_tennis.items(), ids=wheelchair_tennis.keys())
@pytest.mark.fast
def test_wheelchair_tennis(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.dump
@pytest.mark.parametrize("name,data", test_data)
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
