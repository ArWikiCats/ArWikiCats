"""
tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test, dump_same_and_not_same

from ArWikiCats.new_resolvers.nationalities_resolvers.nationalities_double_v2 import resolve_by_nats_double_v2

males_tests = {
    "jewish persian": "فرس يهود",
    "jewish russian": "روس يهود",
}

female_tests = {
    "arab jewish surnames": "ألقاب يهودية عربية",
    "arab-jewish surnames": "ألقاب يهودية عربية",
    "russian jewish surnames": "ألقاب يهودية روسية",
    "russian-jewish surnames": "ألقاب يهودية روسية",
    "jewish french culture": "ثقافة فرنسية يهودية",
    "jewish danish families": "عائلات دنماركية يهودية",
    "jewish chinese families": "عائلات صينية يهودية",
    "jewish canadian television series": "مسلسلات تلفزيونية كندية يهودية",
    "jewish canadian culture": "ثقافة كندية يهودية",
    "jewish canadian families": "عائلات كندية يهودية",
    "jewish argentine culture": "ثقافة أرجنتينية يهودية",
    "jewish austrian families": "عائلات نمساوية يهودية",
    "jewish british culture": "ثقافة بريطانية يهودية",
    "jewish british families": "عائلات بريطانية يهودية",
    "jewish-austrian families": "عائلات نمساوية يهودية",
    "jewish-british families": "عائلات بريطانية يهودية",
    "jewish-canadian families": "عائلات كندية يهودية",
    "jewish-chinese families": "عائلات صينية يهودية",
    "jewish-danish families": "عائلات دنماركية يهودية",
    "jewish-french families": "عائلات فرنسية يهودية",
    "jewish-german families": "عائلات ألمانية يهودية",
    "jewish-hungarian families": "عائلات مجرية يهودية",
    "jewish-italian families": "عائلات إيطالية يهودية",
    "jewish-polish families": "عائلات بولندية يهودية",
    "jewish-portuguese families": "عائلات برتغالية يهودية",
    "jewish south african families": "عائلات جنوب إفريقية يهودية",
    "jewish roman wars": "حروب رومانية يهودية",
    "jewish polish families": "عائلات بولندية يهودية",
    "jewish portuguese families": "عائلات برتغالية يهودية",
    "jewish-roman wars": "حروب رومانية يهودية",
    "jewish-south african families": "عائلات جنوب إفريقية يهودية",
    "jewish french families": "عائلات فرنسية يهودية",
    "jewish german culture": "ثقافة ألمانية يهودية",
    "jewish israeli culture": "ثقافة إسرائيلية يهودية",
    "jewish italian families": "عائلات إيطالية يهودية",
    "jewish german families": "عائلات ألمانية يهودية",
    "jewish hungarian families": "عائلات مجرية يهودية",
}

male_tests = {
    "jewish-afghan history": "تاريخ أفغاني يهودي",
    "jewish afghan history": "تاريخ أفغاني يهودي",
    "jewish albanian history": "تاريخ ألباني يهودي",
    "jewish algerian history": "تاريخ جزائري يهودي",
    "jewish angolan history": "تاريخ أنغولي يهودي",
    "jewish argentine history": "تاريخ أرجنتيني يهودي",
    "jewish armenian history": "تاريخ أرميني يهودي",
    "jewish australian history": "تاريخ أسترالي يهودي",
    "jewish austrian history": "تاريخ نمساوي يهودي",
    "jewish azerbaijani history": "تاريخ أذربيجاني يهودي",
    "jewish bangladeshi history": "تاريخ بنغلاديشي يهودي",
    "jewish belarusian history": "تاريخ بيلاروسي يهودي",
    "jewish belgian history": "تاريخ بلجيكي يهودي",
    "jewish bosnian history": "تاريخ بوسني يهودي",
    "jewish brazilian history": "تاريخ برازيلي يهودي",
    "jewish british history": "تاريخ بريطاني يهودي",
    "jewish bulgarian history": "تاريخ بلغاري يهودي",
    "jewish canadian cuisine": "مطبخ كندي يهودي",
    "jewish canadian history": "تاريخ كندي يهودي",
    "jewish canadian literature": "أدب كندي يهودي",
    "jewish cape verdean history": "تاريخ رأس أخضري يهودي",
    "jewish chilean history": "تاريخ تشيلي يهودي",
    "jewish chinese history": "تاريخ صيني يهودي",
    "jewish christian literature": "أدب مسيحي يهودي",
    "jewish croatian history": "تاريخ كرواتي يهودي",
    "jewish cuban history": "تاريخ كوبي يهودي",
    "jewish cypriot history": "تاريخ قبرصي يهودي",
    "jewish czech history": "تاريخ تشيكي يهودي",
    "jewish danish history": "تاريخ دنماركي يهودي",
    "jewish dutch history": "تاريخ هولندي يهودي",
    "jewish egyptian history": "تاريخ مصري يهودي",
    "jewish english history": "تاريخ إنجليزي يهودي",
    "jewish eritrean history": "تاريخ إريتري يهودي",
    "jewish estonian history": "تاريخ إستوني يهودي",
    "jewish ethiopian history": "تاريخ إثيوبي يهودي",
    "jewish finnish history": "تاريخ فنلندي يهودي",
    "jewish french history": "تاريخ فرنسي يهودي",
    "jewish georgian history": "تاريخ جورجي يهودي",
    "jewish gibraltarian history": "تاريخ جبل طارقي يهودي",
    "jewish greek history": "تاريخ يهودي يوناني",
    "jewish guatemalan history": "تاريخ غواتيمالي يهودي",
    "jewish hong kong history": "تاريخ هونغ كونغي يهودي",
    "jewish hungarian history": "تاريخ مجري يهودي",
    "jewish indian history": "تاريخ هندي يهودي",
    "jewish indonesian history": "تاريخ إندونيسي يهودي",
    "jewish iraqi history": "تاريخ عراقي يهودي",
    "jewish irish history": "تاريخ أيرلندي يهودي",
    "jewish italian history": "تاريخ إيطالي يهودي",
    "jewish jamaican history": "تاريخ جامايكي يهودي",
    "jewish japanese history": "تاريخ ياباني يهودي",
    "jewish jordanian history": "تاريخ أردني يهودي",
    "jewish kenyan history": "تاريخ كيني يهودي",
    "jewish kosovan history": "تاريخ كوسوفي يهودي",
    "jewish kurdish history": "تاريخ كردي يهودي",
    "jewish latvian history": "تاريخ لاتفي يهودي",
    "jewish lebanese history": "تاريخ لبناني يهودي",
    "jewish libyan history": "تاريخ ليبي يهودي",
    "jewish lithuanian history": "تاريخ ليتواني يهودي",
    "jewish luxembourgian history": "تاريخ لوكسمبورغي يهودي",
    "jewish macedonian history": "تاريخ مقدوني يهودي",
    "jewish malagasy history": "تاريخ مدغشقري يهودي",
    "jewish mexican history": "تاريخ مكسيكي يهودي",
    "jewish moldovan history": "تاريخ مولدوفي يهودي",
    "jewish moroccan history": "تاريخ مغربي يهودي",
    "jewish nepalese history": "تاريخ نيبالي يهودي",
    "jewish nigerian history": "تاريخ نيجيري يهودي",
    "jewish norwegian history": "تاريخ نرويجي يهودي",
    "jewish pakistani history": "تاريخ باكستاني يهودي",
    "jewish peruvian history": "تاريخ بيروي يهودي",
    "jewish polish history": "تاريخ بولندي يهودي",
    "jewish portuguese history": "تاريخ برتغالي يهودي",
    "jewish romanian history": "تاريخ روماني يهودي",
    "jewish russian history": "تاريخ روسي يهودي",
    "jewish saudiarabian history": "تاريخ سعودي يهودي",
    "jewish scottish history": "تاريخ إسكتلندي يهودي",
    "jewish serbian history": "تاريخ صربي يهودي",
    "jewish slovak history": "تاريخ سلوفاكي يهودي",
    "jewish slovenian history": "تاريخ سلوفيني يهودي",
    "jewish south african history": "تاريخ جنوب إفريقي يهودي",
    "jewish south korean history": "تاريخ كوري جنوبي يهودي",
    "jewish spanish history": "تاريخ إسباني يهودي",
    "jewish sudanese history": "تاريخ سوداني يهودي",
    "jewish surinamese history": "تاريخ سورينامي يهودي",
    "jewish swedish history": "تاريخ سويدي يهودي",
    "jewish swiss history": "تاريخ سويسري يهودي",
    "jewish syrian history": "تاريخ سوري يهودي",
    "jewish tunisian history": "تاريخ تونسي يهودي",
    "jewish turkish history": "تاريخ تركي يهودي",
    "jewish ugandan history": "تاريخ أوغندي يهودي",
    "jewish ukrainian history": "تاريخ أوكراني يهودي",
    "jewish uruguayan history": "تاريخ أوروغوياني يهودي",
    "jewish uzbek history": "تاريخ أوزبكي يهودي",
    "jewish venezuelan history": "تاريخ فنزويلي يهودي",
    "jewish vietnamese history": "تاريخ فيتنامي يهودي",
    "jewish welsh history": "تاريخ ويلزي يهودي",
    "jewish yemeni history": "تاريخ يمني يهودي",
    "jewish zimbabwean history": "تاريخ زيمبابوي يهودي",
    "persian jewish cuisine": "مطبخ فارسي يهودي",
}

tests_ready = {
    "jewish german history": "تاريخ يهودي ألماني",
    "german jewish history": "تاريخ يهودي ألماني",
}


@pytest.mark.parametrize("category, expected_key", tests_ready.items(), ids=tests_ready.keys())
@pytest.mark.fast
def test_tests_ready(category: str, expected_key: str) -> None:
    label2 = resolve_by_nats_double_v2(category)
    assert label2 == expected_key


@pytest.mark.parametrize("category, expected_key", male_tests.items(), ids=male_tests.keys())
@pytest.mark.fast
def test_male_tests(category: str, expected_key: str) -> None:
    label2 = resolve_by_nats_double_v2(category)
    assert label2 == expected_key


@pytest.mark.parametrize("category, expected_key", female_tests.items(), ids=female_tests.keys())
@pytest.mark.fast
def test_female_tests(category: str, expected_key: str) -> None:
    label2 = resolve_by_nats_double_v2(category)
    assert label2 == expected_key


to_test = [
    ("test_female_tests", female_tests, resolve_by_nats_double_v2),
    ("test_male_tests", male_tests, resolve_by_nats_double_v2),
    ("test_tests_ready", tests_ready, resolve_by_nats_double_v2),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_non_dump(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
