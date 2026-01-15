import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats.new_resolvers.relations_resolver import new_relations_resolvers as resolve_relations_label


fast_data = {
    "Georgia (country)–Luxembourg relations": "العلاقات الجورجية اللوكسمبورغية",
    "France–Papua New Guinea relations": "العلاقات الغينية الفرنسية",
    "Democratic republic of congo–Norway relations": "العلاقات الكونغوية الديمقراطية النرويجية",
    "Albania–Democratic republic of congo relations": "العلاقات الألبانية الكونغوية الديمقراطية",
    "Algeria–Democratic republic of congo relations": "العلاقات الجزائرية الكونغوية الديمقراطية",
    "Angola–Democratic republic of congo border": "الحدود الأنغولية الكونغوية الديمقراطية",
    "Angola–Democratic republic of congo relations": "العلاقات الأنغولية الكونغوية الديمقراطية",
    "Angola–Guinea-Bissau relations": "العلاقات الأنغولية الغينية البيساوية",
    "Angola–republic of congo border": "الحدود الأنغولية الكونغوية",
    "Argentina–Democratic republic of congo relations": "العلاقات الأرجنتينية الكونغوية الديمقراطية",
    "Australia–Democratic republic of congo relations": "العلاقات الأسترالية الكونغوية الديمقراطية",
    "Austria–Democratic republic of congo relations": "العلاقات الكونغوية الديمقراطية النمساوية",
    "Azerbaijan–Democratic republic of congo relations": "العلاقات الأذربيجانية الكونغوية الديمقراطية",
    "Azerbaijan–Guinea-Bissau relations": "العلاقات الأذربيجانية الغينية البيساوية",
    "Bahrain–Democratic republic of congo relations": "العلاقات البحرينية الكونغوية الديمقراطية",
    "Belgium–Guinea-Bissau relations": "العلاقات البلجيكية الغينية البيساوية",
    "Brazil–Guinea-Bissau relations": "العلاقات البرازيلية الغينية البيساوية",
    "Bulgaria–Democratic republic of congo relations": "العلاقات البلغارية الكونغوية الديمقراطية",
    "Bulgaria–Guinea-Bissau relations": "العلاقات البلغارية الغينية البيساوية",
    "Burkina Faso–Democratic republic of congo relations": "العلاقات البوركينابية الكونغوية الديمقراطية",
    "Burundi–Democratic republic of congo border": "الحدود البوروندية الكونغوية الديمقراطية",
    "Burundi–Democratic republic of congo relations": "العلاقات البوروندية الكونغوية الديمقراطية",
    "Canada–Democratic republic of congo relations": "العلاقات الكندية الكونغوية الديمقراطية",
    "Cape Verde–Democratic republic of congo relations": "العلاقات الرأس الأخضرية الكونغوية الديمقراطية",
    "Cape Verde–Guinea-Bissau relations": "العلاقات الرأس الأخضرية الغينية البيساوية",
    "Central African Republic–Democratic republic of congo relations": "العلاقات الإفريقية الأوسطية الكونغوية الديمقراطية",
    "Chad–Democratic republic of congo relations": "العلاقات التشادية الكونغوية الديمقراطية",
    "China–Democratic republic of congo relations": "العلاقات الصينية الكونغوية الديمقراطية",
    "China–Guinea-Bissau relations": "العلاقات الصينية الغينية البيساوية",
    "Croatia–Democratic republic of congo relations": "العلاقات الكرواتية الكونغوية الديمقراطية",
    "Cyprus–Democratic republic of congo relations": "العلاقات القبرصية الكونغوية الديمقراطية",
    "Cyprus–Guinea-Bissau relations": "العلاقات الغينية البيساوية القبرصية",
    "Czech Republic–Democratic republic of congo relations": "العلاقات التشيكية الكونغوية الديمقراطية",
    "Democratic republic of congo–republic of congo border": "الحدود الكونغوية الكونغوية الديمقراطية",
    "Democratic republic of congo–republic of congo border crossings": "معابر الحدود الكونغوية الكونغوية الديمقراطية",
    "Egypt–Guinea-Bissau relations": "العلاقات الغينية البيساوية المصرية",
    "Ethiopia–Guinea-Bissau relations": "العلاقات الإثيوبية الغينية البيساوية",
    "Finland–Guinea-Bissau relations": "العلاقات الغينية البيساوية الفنلندية",
    "France–Guinea-Bissau relations": "العلاقات الغينية البيساوية الفرنسية",
    "Gabon–republic of congo relations": "العلاقات الغابونية الكونغوية",
    "Georgia (country)–Guinea-Bissau relations": "العلاقات الجورجية الغينية البيساوية",
    "Greece–Guinea-Bissau relations": "العلاقات الغينية البيساوية اليونانية",
    "Iran–republic of congo relations": "العلاقات الإيرانية الكونغوية",
    "Malta–republic of congo relations": "العلاقات الكونغوية المالطية",
    "Netherlands–republic of congo relations": "العلاقات الكونغوية الهولندية",
    "democratic-republic-of-congo–libya relations": "العلاقات الكونغوية الديمقراطية الليبية",
    "democratic-republic-of-congo–netherlands relations": "العلاقات الكونغوية الديمقراطية الهولندية",
    "Democratic republic of congo–Libya relations": "العلاقات الكونغوية الديمقراطية الليبية",
    "Democratic republic of congo–Netherlands relations": "العلاقات الكونغوية الديمقراطية الهولندية",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.slow
def test_resolve_relations_label(category: str, expected: str) -> None:
    label = resolve_relations_label(category)
    assert label == expected


to_test = [
    ("test_fast_data", fast_data),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_relations_label)
    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
