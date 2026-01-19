"""
Tests
"""

from typing import Callable

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.sports_resolvers.nationalities_and_sports import resolve_nats_sport_multi_v2

the_female_data = {
    "new zealand rugby league chairmen and investors": "رؤساء ومسيرو الدوري النيوزيلندي للرجبي",
    "welsh rugby league": "الدوري الويلزي للرجبي",
    "welsh rugby league chairmen and investors": "رؤساء ومسيرو الدوري الويلزي للرجبي",
    "welsh rugby union": "اتحاد الرجبي الويلزي",
    "welsh rugby union chairmen and investors": "رؤساء ومسيرو اتحاد الرجبي الويلزي",
    "english rugby union chairmen and investors": "رؤساء ومسيرو اتحاد الرجبي الإنجليزي",
    "french rugby union chairmen and investors": "رؤساء ومسيرو اتحاد الرجبي الفرنسي",
    "lithuanian basketball chairmen and investors": "رؤساء ومسيرو كرة السلة الليتوانية",
    "greek volleyball chairmen and investors": "رؤساء ومسيرو كرة الطائرة اليونانية",
    "greek basketball chairmen and investors": "رؤساء ومسيرو كرة السلة اليونانية",
    "saudiarabian football chairmen and investors": "رؤساء ومسيرو كرة القدم السعودية",
    # "saudi arabian football chairmen and investors": "رؤساء ومسيرو كرة القدم السعودية",
    "palestinian football chairmen and investors": "رؤساء ومسيرو كرة القدم الفلسطينية",
    "swiss football chairmen and investors": "رؤساء ومسيرو كرة القدم السويسرية",
    "egyptian football chairmen and investors": "رؤساء ومسيرو كرة القدم المصرية",
    "british football chairmen and investors": "رؤساء ومسيرو كرة القدم البريطانية",
    "new zealand association football chairmen and investors": "رؤساء ومسيرو كرة القدم النيوزيلندية",
    "paraguayan football chairmen and investors": "رؤساء ومسيرو كرة القدم البارغوايانية",
    "togolese football chairmen and investors": "رؤساء ومسيرو كرة القدم التوغوية",
    "uruguayan football chairmen and investors": "رؤساء ومسيرو كرة القدم الأوروغويانية",
    "russian football chairmen and investors": "رؤساء ومسيرو كرة القدم الروسية",
    "english football chairmen and investors": "رؤساء ومسيرو كرة القدم الإنجليزية",
    "emirati football chairmen and investors": "رؤساء ومسيرو كرة القدم الإماراتية",
    "filipino football chairmen and investors": "رؤساء ومسيرو كرة القدم الفلبينية",
    "indian football chairmen and investors": "رؤساء ومسيرو كرة القدم الهندية",
    "chinese football chairmen and investors": "رؤساء ومسيرو كرة القدم الصينية",
    "cypriot football chairmen and investors": "رؤساء ومسيرو كرة القدم القبرصية",
    "israeli football chairmen and investors": "رؤساء ومسيرو كرة القدم الإسرائيلية",
    "lithuanian football chairmen and investors": "رؤساء ومسيرو كرة القدم الليتوانية",
    "belgian football chairmen and investors": "رؤساء ومسيرو كرة القدم البلجيكية",
    "romanian football chairmen and investors": "رؤساء ومسيرو كرة القدم الرومانية",
    "italian football chairmen and investors": "رؤساء ومسيرو كرة القدم الإيطالية",
    "bahraini football chairmen and investors": "رؤساء ومسيرو كرة القدم البحرينية",
    "welsh football chairmen and investors": "رؤساء ومسيرو كرة القدم الويلزية",
    "iraqi football chairmen and investors": "رؤساء ومسيرو كرة القدم العراقية",
    "norwegian football chairmen and investors": "رؤساء ومسيرو كرة القدم النرويجية",
    "spanish football chairmen and investors": "رؤساء ومسيرو كرة القدم الإسبانية",
    "ghanaian football chairmen and investors": "رؤساء ومسيرو كرة القدم الغانية",
    "nigerian football chairmen and investors": "رؤساء ومسيرو كرة القدم النيجيرية",
    "french football chairmen and investors": "رؤساء ومسيرو كرة القدم الفرنسية",
    "argentine football chairmen and investors": "رؤساء ومسيرو كرة القدم الأرجنتينية",
    "danish football chairmen and investors": "رؤساء ومسيرو كرة القدم الدنماركية",
    "south korean football chairmen and investors": "رؤساء ومسيرو كرة القدم الكورية الجنوبية",
    "icelandic football chairmen and investors": "رؤساء ومسيرو كرة القدم الآيسلندية",
    "republic of ireland association football chairmen and investors": "رؤساء ومسيرو كرة القدم الأيرلندية",
    "latvian football chairmen and investors": "رؤساء ومسيرو كرة القدم اللاتفية",
    "greek football chairmen and investors": "رؤساء ومسيرو كرة القدم اليونانية",
    "serbian football chairmen and investors": "رؤساء ومسيرو كرة القدم الصربية",
    "iranian football chairmen and investors": "رؤساء ومسيرو كرة القدم الإيرانية",
    "bolivian football chairmen and investors": "رؤساء ومسيرو كرة القدم البوليفية",
    "australian soccer chairmen and investors": "رؤساء ومسيرو كرة القدم الأسترالية",
    "moroccan football chairmen and investors": "رؤساء ومسيرو كرة القدم المغربية",
    "austrian football chairmen and investors": "رؤساء ومسيرو كرة القدم النمساوية",
    "portuguese football chairmen and investors": "رؤساء ومسيرو كرة القدم البرتغالية",
    "czech football chairmen and investors": "رؤساء ومسيرو كرة القدم التشيكية",
    "thai football chairmen and investors": "رؤساء ومسيرو كرة القدم التايلندية",
    "singaporean football chairmen and investors": "رؤساء ومسيرو كرة القدم السنغافورية",
    "turkish football chairmen and investors": "رؤساء ومسيرو كرة القدم التركية",
    "indonesian football chairmen and investors": "رؤساء ومسيرو كرة القدم الإندونيسية",
    "qatari football chairmen and investors": "رؤساء ومسيرو كرة القدم القطرية",
    "brazilian football chairmen and investors": "رؤساء ومسيرو كرة القدم البرازيلية",
    "swedish football chairmen and investors": "رؤساء ومسيرو كرة القدم السويدية",
    "dutch football chairmen and investors": "رؤساء ومسيرو كرة القدم الهولندية",
    "american soccer chairmen and investors": "رؤساء ومسيرو كرة القدم الأمريكية",
    "german football chairmen and investors": "رؤساء ومسيرو كرة القدم الألمانية",
    "ukrainian football chairmen and investors": "رؤساء ومسيرو كرة القدم الأوكرانية",
    "japanese football chairmen and investors": "رؤساء ومسيرو كرة القدم اليابانية",
    "canadian soccer chairmen and investors": "رؤساء ومسيرو كرة القدم الكندية",
    "mexican football chairmen and investors": "رؤساء ومسيرو كرة القدم المكسيكية",
}

data6 = {
    "georgia (country) freestyle wrestling federation": "الاتحاد الجورجي للمصارعة الحرة",
    "philippine sailing (sport) federation": "الاتحاد الفلبيني لرياضة الإبحار",
}

ar_sport_team_data = {
    # "Yemeni football championships clubs": "أندية بطولة اليمن لكرة القدم",
    "british softball championshipszz": "بطولة المملكة المتحدة للكرة اللينة",
    "ladies british softball tour": "بطولة المملكة المتحدة للكرة اللينة للسيدات",
    "british football tour": "بطولة المملكة المتحدة لكرة القدم",
    "Yemeni football championships": "بطولة اليمن لكرة القدم",
    "german figure skating championships": "بطولة ألمانيا للتزلج الفني",
    "british figure skating championships": "بطولة المملكة المتحدة للتزلج الفني",
}


sport_jobs_female_data = {
    "dominican republic national football teams": "منتخبات كرة قدم وطنية دومينيكانية",
    "yemeni national softball teams": "منتخبات كرة لينة وطنية يمنية",
    "Women's National Basketball League": "الدوري الوطني لكرة السلة للسيدات",
    "northern ireland": "",
}


@pytest.mark.parametrize("category, expected_key", the_female_data.items(), ids=the_female_data.keys())
@pytest.mark.fast
def test_the_female_data(category: str, expected_key: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected_key


@pytest.mark.parametrize("category, expected_key", ar_sport_team_data.items(), ids=ar_sport_team_data.keys())
@pytest.mark.fast
def test_ar_sport_team_data(category: str, expected_key: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected_key


@pytest.mark.parametrize("category, expected_key", sport_jobs_female_data.items(), ids=sport_jobs_female_data.keys())
@pytest.mark.fast
def test_sport_jobs_female_data(category: str, expected_key: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected_key


TEMPORAL_CASES = [
    ("test_resolve_nats_sport_multi_v2", data6, resolve_nats_sport_multi_v2),
    ("test_ar_sport_team_data", ar_sport_team_data, resolve_nats_sport_multi_v2),
    ("test_sport_jobs_female_data", sport_jobs_female_data, resolve_nats_sport_multi_v2),
    ("test_sport_jobs_the_female_data", the_female_data, resolve_nats_sport_multi_v2),
]


@pytest.mark.dump
@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback, do_strip=True)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
