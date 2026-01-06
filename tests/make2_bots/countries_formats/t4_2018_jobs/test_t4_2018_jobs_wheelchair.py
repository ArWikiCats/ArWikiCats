"""
Tests
"""

import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test

from ArWikiCats.make_bots.countries_formats.t4_2018_jobs import te4_2018_Jobs
from ArWikiCats.new_resolvers.jobs_resolvers import resolve_jobs_main
from ArWikiCats.new_resolvers.nationalities_resolvers import resolve_nationalities_main
from ArWikiCats.new_resolvers.reslove_all import new_resolvers_all
from ArWikiCats.new_resolvers.sports_resolvers import resolve_sports_main

wheelchair_data_0 = {
    "american men wheelchair racers": "متسابقو كراسي متحركة أمريكيون",
    "american men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة أمريكيون",
    "australian men wheelchair racers": "متسابقو كراسي متحركة أستراليون",
    "australian men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة أستراليون",
    "austrian men wheelchair racers": "متسابقو كراسي متحركة نمساويون",
    "belgian men wheelchair racers": "متسابقو كراسي متحركة بلجيكيون",
    "british men wheelchair racers": "متسابقو كراسي متحركة بريطانيون",
    "british men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة بريطانيون",
    "brazilian men wheelchair racers": "متسابقو كراسي متحركة برازيليون",
    "cameroonian men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة كاميرونيون",
    "canadian men wheelchair racers": "متسابقو كراسي متحركة كنديون",
    "canadian men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة كنديون",
    "english men wheelchair racers": "متسابقو كراسي متحركة إنجليز",
    "finnish men wheelchair racers": "متسابقو كراسي متحركة فنلنديون",
    "dutch men wheelchair racers": "متسابقو كراسي متحركة هولنديون",
    "dutch men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة هولنديون",
    "chinese men wheelchair racers": "متسابقو كراسي متحركة صينيون",
    "french men wheelchair racers": "متسابقو كراسي متحركة فرنسيون",
    "french men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة فرنسيون",
    "gabonese men wheelchair racers": "متسابقو كراسي متحركة غابونيون",
    "german men wheelchair racers": "متسابقو كراسي متحركة ألمان",
    "german men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة ألمان",
    "irish men wheelchair racers": "متسابقو كراسي متحركة أيرلنديون",
    "israeli men wheelchair racers": "متسابقو كراسي متحركة إسرائيليون",
    "israeli men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة إسرائيليون",
    "japanese men wheelchair racers": "متسابقو كراسي متحركة يابانيون",
    "japanese men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة يابانيون",
    "kuwaiti men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة كويتيون",
    "mexican men wheelchair racers": "متسابقو كراسي متحركة مكسيكيون",
    "spanish men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة إسبان",
    "swiss men wheelchair racers": "متسابقو كراسي متحركة سويسريون",
    "swiss men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة سويسريون",
    "turkish men's wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة أتراك",
    "welsh men wheelchair racers": "متسابقو كراسي متحركة ويلزيون",
}

wheelchair_data_1 = {
    "american wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة أمريكيون",
    "american wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة أمريكيون",
    "american wheelchair curling champions": "أبطال الكيرلنغ على الكراسي المتحركة أمريكيون",
    "american wheelchair discus throwers": "رماة قرص على الكراسي المتحركة أمريكيون",
    "american wheelchair racers": "متسابقو كراسي متحركة أمريكيون",
    "american wheelchair rugby players": "لاعبو رجبي على كراسي متحركة أمريكيون",
    "american wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة أمريكيون",
    "american women wheelchair racers": "متسابقات كراسي متحركة أمريكيات",
    "australian wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة أستراليون",
    "australian wheelchair racers": "متسابقو كراسي متحركة أستراليون",
    "australian wheelchair rugby players": "لاعبو رجبي على كراسي متحركة أستراليون",
    "australian wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة أستراليون",
    "australian women wheelchair racers": "متسابقات كراسي متحركة أستراليات",
    "austrian wheelchair racers": "متسابقو كراسي متحركة نمساويون",
    "belgian wheelchair racers": "متسابقو كراسي متحركة بلجيكيون",
    "belgian women wheelchair racers": "متسابقات كراسي متحركة بلجيكيات",
    "brazilian wheelchair racers": "متسابقو كراسي متحركة برازيليون",
    "brazilian women wheelchair racers": "متسابقات كراسي متحركة برازيليات",
    "british wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة بريطانيون",
    "british wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة بريطانيون",
    "british wheelchair racers": "متسابقو كراسي متحركة بريطانيون",
    "british wheelchair rugby players": "لاعبو رجبي على كراسي متحركة بريطانيون",
    "british wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة بريطانيون",
    "british women wheelchair racers": "متسابقات كراسي متحركة بريطانيات",
    "cameroonian wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة كاميرونيون",
    "canadian male wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة ذكور كنديون",
    "canadian wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة كنديون",
    "canadian wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة كنديون",
    "canadian wheelchair curling champions": "أبطال الكيرلنغ على الكراسي المتحركة كنديون",
    "canadian wheelchair racers": "متسابقو كراسي متحركة كنديون",
    "canadian wheelchair rugby players": "لاعبو رجبي على كراسي متحركة كنديون",
    "canadian women wheelchair racers": "متسابقات كراسي متحركة كنديات",
    "chinese wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة صينيون",
    "chinese wheelchair racers": "متسابقو كراسي متحركة صينيون",
    "chinese women wheelchair racers": "متسابقات كراسي متحركة صينيات",
    "czech wheelchair racers": "متسابقو كراسي متحركة تشيكيون",
    "danish wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة دنماركيون",
    "danish wheelchair racers": "متسابقو كراسي متحركة دنماركيون",
    "dutch wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة هولنديون",
    "dutch wheelchair racers": "متسابقو كراسي متحركة هولنديون",
    "dutch wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة هولنديون",
    "dutch women wheelchair racers": "متسابقات كراسي متحركة هولنديات",
    "emirati wheelchair racers": "متسابقو كراسي متحركة إماراتيون",
    "english wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة إنجليز",
    "english wheelchair racers": "متسابقو كراسي متحركة إنجليز",
    "english women wheelchair racers": "متسابقات كراسي متحركة إنجليزيات",
    "finnish wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة فنلنديون",
    "finnish wheelchair curling champions": "أبطال الكيرلنغ على الكراسي المتحركة فنلنديون",
    "finnish wheelchair racers": "متسابقو كراسي متحركة فنلنديون",
    "finnish women wheelchair racers": "متسابقات كراسي متحركة فنلنديات",
    "french wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة فرنسيون",
    "french wheelchair racers": "متسابقو كراسي متحركة فرنسيون",
    "french wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة فرنسيون",
    "gabonese wheelchair racers": "متسابقو كراسي متحركة غابونيون",
    "german wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة ألمان",
    "german wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة ألمان",
    "german wheelchair racers": "متسابقو كراسي متحركة ألمان",
    "german wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة ألمان",
    "irish wheelchair racers": "متسابقو كراسي متحركة أيرلنديون",
    "irish women wheelchair racers": "متسابقات كراسي متحركة أيرلنديات",
    "israeli wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة إسرائيليون",
    "israeli wheelchair racers": "متسابقو كراسي متحركة إسرائيليون",
    "israeli wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة إسرائيليون",
    "italian wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة إيطاليون",
    "italian wheelchair racers": "متسابقو كراسي متحركة إيطاليون",
    "japanese wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة يابانيون",
    "japanese wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة يابانيون",
    "japanese wheelchair racers": "متسابقو كراسي متحركة يابانيون",
    "japanese wheelchair rugby players": "لاعبو رجبي على كراسي متحركة يابانيون",
    "japanese wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة يابانيون",
    "japanese women wheelchair racers": "متسابقات كراسي متحركة يابانيات",
    "kuwaiti wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة كويتيون",
    "kuwaiti wheelchair racers": "متسابقو كراسي متحركة كويتيون",
    "latvian wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة لاتفيون",
    "lithuanian wheelchair racers": "متسابقو كراسي متحركة ليتوانيون",
    "macedonian wheelchair racers": "متسابقو كراسي متحركة مقدونيون",
    "mexican wheelchair racers": "متسابقو كراسي متحركة مكسيكيون",
    "mexican women wheelchair racers": "متسابقات كراسي متحركة مكسيكيات",
    "norwegian wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة نرويجيون",
    "norwegian wheelchair racers": "متسابقو كراسي متحركة نرويجيون",
    "polish wheelchair racers": "متسابقو كراسي متحركة بولنديون",
    "russian wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة روس",
    "russian wheelchair racers": "متسابقو كراسي متحركة روس",
    "sammarinese wheelchair racers": "متسابقو كراسي متحركة سان مارينيون",
    "scottish wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة إسكتلنديون",
    "scottish wheelchair curling champions": "أبطال الكيرلنغ على الكراسي المتحركة إسكتلنديون",
    "scottish wheelchair racers": "متسابقو كراسي متحركة إسكتلنديون",
    "scottish women wheelchair racers": "متسابقات كراسي متحركة إسكتلنديات",
    "slovak wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة سلوفاكيون",
    "south korean wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة كوريون جنوبيون",
    "south korean wheelchair racers": "متسابقو كراسي متحركة كوريون جنوبيون",
    "spanish wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة إسبان",
    "spanish wheelchair fencers": "مبارزون على الكراسي المتحركة إسبان",
    "spanish wheelchair racers": "متسابقو كراسي متحركة إسبان",
    "spanish wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة إسبان",
    "swedish wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة سويديون",
    "swedish wheelchair curling champions": "أبطال الكيرلنغ على الكراسي المتحركة سويديون",
    "swedish wheelchair racers": "متسابقو كراسي متحركة سويديون",
    "swedish wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة سويديون",
    "swiss wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة سويسريون",
    "swiss wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة سويسريون",
    "swiss wheelchair curling champions": "أبطال الكيرلنغ على الكراسي المتحركة سويسريون",
    "swiss wheelchair racers": "متسابقو كراسي متحركة سويسريون",
    "swiss wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة سويسريون",
    "swiss women wheelchair racers": "متسابقات كراسي متحركة سويسريات",
    "thai wheelchair racers": "متسابقو كراسي متحركة تايلنديون",
    "thai wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة تايلنديون",
    "tunisian wheelchair racers": "متسابقو كراسي متحركة تونسيون",
    "turkish wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة أتراك",
    "turkish wheelchair racers": "متسابقو كراسي متحركة أتراك",
    "turkish wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة أتراك",
    "turkish women wheelchair racers": "متسابقات كراسي متحركة تركيات",
    "welsh wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة ويلزيون",
    "welsh wheelchair racers": "متسابقو كراسي متحركة ويلزيون",
    "welsh women wheelchair racers": "متسابقات كراسي متحركة ويلزيات",
    "wheelchair basketball coaches": "مدربو كرة سلة على كراسي متحركة",
    "wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة",
    "wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة",
    "wheelchair fencers": "مبارزون على الكراسي المتحركة",
    "wheelchair racers": "متسابقو كراسي متحركة",
    "wheelchair rugby coaches": "مدربو رجبي على كراسي متحركة",
    "wheelchair rugby players": "لاعبو رجبي على كراسي متحركة",
    "wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة",
    "zambian wheelchair racers": "متسابقو كراسي متحركة زامبيون",

}


@pytest.mark.parametrize("category, expected_key", wheelchair_data_1.items(), ids=wheelchair_data_1.keys())
@pytest.mark.slow
def test_wheelchair_data(category: str, expected_key: str) -> None:
    label1 = te4_2018_Jobs(category)
    assert label1 == expected_key

    # label2 = new_resolvers_all(category)
    # assert label2 == expected_key


to_test = [
    ("test_wheelchair_data", wheelchair_data_1),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, new_resolvers_all)
    dump_diff(diff_result, name)

    # dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
