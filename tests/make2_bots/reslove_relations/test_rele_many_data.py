#
import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats.new_resolvers.relations_resolver import new_relations_resolvers
from ArWikiCats.make_bots.reslove_relations.rele import resolve_relations_label

data_0 = {
    "africanamerican–asian-american relations": "العلاقات الأمريكية الآسيوية الأمريكية الإفريقية",
    "africanamerican–jewish relations": "العلاقات الأمريكية الإفريقية اليهودية",
    "african–native american relations": "العلاقات الأمريكية الأصلية الإفريقية",
    "arab–american relations": "العلاقات الأمريكية العربية",
    "cambodian–vietnamese war": "الحرب الفيتنامية الكمبودية",
    "canada–oceanian relations": "العلاقات الأوقيانوسية الكندية",
    "chadian–libyan war": "الحرب التشادية الليبية",
    "democratic-republic-of-congo–republic-of ireland relations": "العلاقات الأيرلندية الكونغوية الديمقراطية",
    "dutch–portuguese war": "الحرب البرتغالية الهولندية",
    "ecuadorian–peruvian war": "الحرب الإكوادورية البيروية",
    "egyptian–ottoman war": "الحرب العثمانية المصرية",
    "eritrean–ethiopian war": "الحرب الإثيوبية الإريترية",
    "german–romania military relations": "العلاقات الألمانية الرومانية العسكرية",
    "hungarian–czechoslovak war": "الحرب التشيكوسلوفاكية المجرية",
    "hungarian–romanian war": "الحرب الرومانية المجرية",
    "mexican–american war": "الحرب الأمريكية المكسيكية",
    "native american–jewish relations": "العلاقات الأمريكية الأصلية اليهودية",
    "philippine–american war": "الحرب الأمريكية الفلبينية",
    "polish–lithuanian war": "الحرب البولندية الليتوانية",
    "polish–soviet war": "الحرب البولندية السوفيتية",
    "polish–ukrainian war": "الحرب الأوكرانية البولندية",
    "republic-of ireland–united kingdom border crossings": "معابر الحدود الأيرلندية البريطانية",
    "republic-of ireland–united kingdom border": "الحدود الأيرلندية البريطانية",
    "roman–iranian relations": "العلاقات الإيرانية الرومانية",
    "scottish–norwegian war": "الحرب الإسكتلندية النرويجية",
    "sinhalese–portuguese war": "الحرب البرتغالية السنهالية",
    "slovak–hungarian war": "الحرب السلوفاكية المجرية",
    "soviet–afghan war": "الحرب الأفغانية السوفيتية",
    "spanish–american war": "الحرب الأمريكية الإسبانية",
    "swedish–norwegian war": "الحرب السويدية النرويجية",
    "ukrainian–soviet war": "الحرب الأوكرانية السوفيتية",
    "united kingdom–asian relations": "العلاقات الآسيوية البريطانية",
    "united kingdom–middle eastern relations": "العلاقات البريطانية الشرقية الأوسطية",
    "united kingdom–oceanian relations": "العلاقات الأوقيانوسية البريطانية",
    "united states–asian relations": "العلاقات الآسيوية الأمريكية",
    "united states–central american relations": "العلاقات الأمريكية الأمريكية الأوسطية",
    "united states–european relations": "العلاقات الأمريكية الأوروبية",
    "united states–middle eastern relations": "العلاقات الأمريكية الشرقية الأوسطية",
    "united states–north american relations": "العلاقات الأمريكية الأمريكية الشمالية",
    "united states–oceanian relations": "العلاقات الأمريكية الأوقيانوسية",
    "united states–south american relations": "العلاقات الأمريكية الأمريكية الجنوبية"
}

data_3 = {
}


@pytest.mark.parametrize("category, expected", data_0.items(), ids=data_0.keys())
@pytest.mark.fast
def test_data_0(category: str, expected: str) -> None:
    label = new_relations_resolvers(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
@pytest.mark.fast
def test_data_3(category: str, expected: str) -> None:
    label = new_relations_resolvers(category)
    assert label == expected


to_test = [
    ("test_relations_0", data_0),
    # ("test_relations_3", data_3),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, new_relations_resolvers)
    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
