#!/usr/bin/python3
""" """

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.sports_resolvers.raw_sports_with_suffixes import wrap_team_xo_normal_2025_with_ends

test_find_teams_bot_data_0 = {}

test_find_teams_bot_data = {
    "acrobatic gymnastics junior world championships": "بطولة العالم للجمباز الاكروباتيكي للناشئين",
    "acrobatic gymnastics world championships": "بطولة العالم للجمباز الاكروباتيكي",
    "amateur handball world cup": "كأس العالم لكرة اليد للهواة",
    "basketball junior world championships": "بطولة العالم لكرة السلة للناشئين",
    "beach volleyball world championships": "بطولة العالم لكرة الطائرة الشاطئية",
    "cross-country skiing world championships": "بطولة العالم للتزلج الريفي",
    "goalball world championships": "بطولة العالم لكرة الهدف",
    "international basketball council": "المجلس الدولي لكرة السلة",
    "international cricket council": "المجلس الدولي للكريكت",
    "international snowboarding council": "المجلس الدولي للتزلج على الثلوج",
    "international volleyball council": "المجلس الدولي لكرة الطائرة",
    "international handball council": "المجلس الدولي لكرة اليد",
    "men's softball world championship": "بطولة العالم للكرة اللينة للرجال",
    "men's handball championship": "بطولة لكرة اليد للرجال",
    "men's handball world championship": "بطولة العالم لكرة اليد للرجال",
    "men's handball world cup": "كأس العالم لكرة اليد للرجال",
    "motocross world championship": "بطولة العالم للموتو كروس",
    "outdoor world handball championship": "بطولة العالم لكرة اليد في الهواء الطلق",
    "racquetball world championships": "بطولة العالم لكرة الراح",
    "rhythmic gymnastics world championships": "بطولة العالم للجمباز الإيقاعي",
    "rugby world junior championship": "بطولة العالم للرجبي للناشئين",
    "sailing world championship": "بطولة العالم للإبحار",
    "sailing world championships": "بطولة العالم للإبحار",
    "wheelchair basketball world championships": "بطولة العالم لكرة السلة على الكراسي المتحركة",
    "wheelchair handball world championship": "بطولة العالم لكرة اليد على الكراسي المتحركة",
    "women's basketball world championships": "بطولة العالم لكرة السلة للسيدات",
    "women's world wheelchair basketball championship": "بطولة العالم لكرة السلة على الكراسي المتحركة للسيدات",
    "women's world handball championship": "بطولة العالم لكرة اليد للسيدات",
    "women's handball championship": "بطولة لكرة اليد للسيدات",
    "women's handball world championship": "بطولة العالم لكرة اليد للسيدات",
    "women's handball world cup": "كأس العالم لكرة اليد للسيدات",
    "world amateur boxing championships": "بطولة العالم للبوكسينغ للهواة",
    "world amateur handball championship": "بطولة العالم لكرة اليد للهواة",
    "world aquatics championships competitors": "منافسو بطولة العالم للرياضات المائية",
    "world archery championships": "بطولة العالم للنبالة",
    "world athletics championships": "بطولة العالم لألعاب القوى",
    "world athletics championships medalists": "فائزون بميداليات بطولة العالم لألعاب القوى",
    "world boxing championships": "بطولة العالم للبوكسينغ",
    "world champion national handball teams": "أبطال بطولة العالم لكرة اليد",
    "world fencing championships medalists": "فائزون بميداليات بطولة العالم لمبارزة سيف الشيش",
    "world figure skating championships medalists": "فائزون بميداليات بطولة العالم للتزلج الفني",
    "world handball junior championship": "بطولة العالم لكرة اليد للناشئين",
    "world junior basketball championships": "بطولة العالم لكرة السلة للناشئين",
    "world junior ice hockey championships": "بطولة العالم لهوكي الجليد للناشئين",
    "world junior rugby championships": "بطولة العالم للرجبي للناشئين",
    "world junior short track speed skating championships": "بطولة العالم للتزلج على مسار قصير للناشئين",
    "world junior squash championships": "بطولة العالم للاسكواش للناشئين",
    "world junior wrestling championships": "بطولة العالم للمصارعة للناشئين",
    "world junior handball championship": "بطولة العالم لكرة اليد للناشئين",
    "world netball championship": "بطولة العالم لكرة الشبكة",
    "world netball championships": "بطولة العالم لكرة الشبكة",
    "world outdoor bowls championship": "بطولة العالم للبولينج في الهواء الطلق",
    "world outdoor handball championship": "بطولة العالم لكرة اليد في الهواء الطلق",
    "world rowing championships medalists": "فائزون بميداليات بطولة العالم للتجديف",
    "world skateboarding championship medalists": "فائزون بميداليات بطولة العالم للتزلج على اللوح",
    "world taekwondo championships": "بطولة العالم للتايكوندو",
    "world wheelchair curling championship": "بطولة العالم للكيرلنغ على الكراسي المتحركة",
    "world wheelchair rugby championships": "بطولة العالم للرجبي على الكراسي المتحركة",
    "world wheelchair handball championship": "بطولة العالم لكرة اليد على الكراسي المتحركة",
    "world wrestling championships": "بطولة العالم للمصارعة",
    "world handball amateur championship": "بطولة العالم لكرة اليد للهواة",
    "world handball championship competitors": "منافسو بطولة العالم لكرة اليد",
    "world handball championship medalists": "فائزون بميداليات بطولة العالم لكرة اليد",
    "world handball championship": "بطولة العالم لكرة اليد",
    "world handball youth championship": "بطولة العالم لكرة اليد للشباب",
    "world youth handball championship": "بطولة العالم لكرة اليد للشباب",
    "handball amateur world championship": "بطولة العالم لكرة اليد للهواة",
    "handball junior world championship": "بطولة العالم لكرة اليد للناشئين",
    "handball world amateur championship": "بطولة العالم لكرة اليد للهواة",
    "handball world championship": "بطولة العالم لكرة اليد",
    "handball world cup": "كأس العالم لكرة اليد",
    "handball world junior championship": "بطولة العالم لكرة اليد للناشئين",
    "handball world youth championship": "بطولة العالم لكرة اليد للشباب",
    "handball youth world championship": "بطولة العالم لكرة اليد للشباب",
    "youth handball world cup": "كأس العالم لكرة اليد للشباب",
}


@pytest.mark.parametrize("category, expected", test_find_teams_bot_data.items(), ids=test_find_teams_bot_data.keys())
@pytest.mark.fast
def test_Get_New_team_xo_data(category: str, expected: str) -> None:
    label1 = wrap_team_xo_normal_2025_with_ends(category)
    assert isinstance(label1, str)
    assert label1 == expected


@pytest.mark.parametrize(
    "category, expected", test_find_teams_bot_data_0.items(), ids=test_find_teams_bot_data_0.keys()
)
@pytest.mark.fast
def test_test_find_teams_bot_data_0(category: str, expected: str) -> None:
    label1 = wrap_team_xo_normal_2025_with_ends(category)
    assert isinstance(label1, str)
    assert label1 == expected


TEMPORAL_CASES = [
    ("test_find_teams_bot", test_find_teams_bot_data, wrap_team_xo_normal_2025_with_ends),
    # ("test_find_teams_bot_with_additional", test_find_teams_bot_data_with_additional, wrap_team_xo_normal_2025_with_ends),
]


@pytest.mark.parametrize("name,data,callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
