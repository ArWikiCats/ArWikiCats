#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

test_skip = {
    "Category:Jewish-American history in New York City": ""
}

examples_1 = {
    "Category:Foreign trade ministers of Netherlands": "تصنيف:وزراء تجارة خارجية هولندا",
    "Category:Social affairs ministers of Uganda": "تصنيف:وزراء شؤون اجتماعية أوغندا",
    "Category:Trade ministers of Togo": "تصنيف:وزراء تجارة توغو",
    "Category:Ministers for Foreign Affairs of Abkhazia": "تصنيف:وزراء شؤون خارجية أبخازيا",
    "Category:Ministers for Foreign Affairs of Singapore": "تصنيف:وزراء شؤون خارجية سنغافورة",
    "Category:Ministers for Foreign Affairs of Luxembourg": "تصنيف:وزراء شؤون خارجية لوكسمبورغ",
    "Category:Ministers for Internal Affairs of Abkhazia": "تصنيف:وزراء شؤون داخلية أبخازيا",
    "Category:Ministers for Public Works of Luxembourg": "تصنيف:وزراء أشغال عامة لوكسمبورغ",
    "Category:Housing ministers of Abkhazia": "تصنيف:وزراء إسكان أبخازيا",
    "Category:Economy ministers of Latvia": "تصنيف:وزراء اقتصاد لاتفيا",
    "Category:Ministers of Economics of Latvia": "تصنيف:وزراء الاقتصاد في لاتفيا",
    "Category:Religious affairs ministers of Yemen": "تصنيف:وزراء شؤون دينية اليمن",
}

examples_2 = {
    "Category:Agriculture ministers of Azerbaijan": "تصنيف:وزراء زراعة أذربيجان",
    "Category:Agriculture ministers of Maldives": "تصنيف:وزراء زراعة جزر المالديف",
    "Category:Communications ministers of Azerbaijan": "تصنيف:وزراء اتصالات أذربيجان",
    "Category:Communications ministers of Comoros": "تصنيف:وزراء اتصالات جزر القمر",
    "Category:Culture ministers of Gabon": "تصنيف:وزراء ثقافة الغابون",
    "Category:Education ministers of Comoros": "تصنيف:وزراء تعليم جزر القمر",
    "Category:Electricity and water ministers of Somalia": "تصنيف:وزراء كهرباء ومياه الصومال",
    "Category:Energy ministers of Gabon": "تصنيف:وزراء طاقة الغابون",
    "Category:Finance ministers of Burundi": "تصنيف:وزراء مالية بوروندي",
    "Category:Health ministers of Comoros": "تصنيف:وزراء صحة جزر القمر",
    "Category:Industry ministers of Togo": "تصنيف:وزراء صناعة توغو",
    "Category:Interior ministers of Uganda": "تصنيف:وزراء داخلية أوغندا",
    "Category:Justice ministers of Djibouti": "تصنيف:وزراء عدل جيبوتي",
    "Category:Justice ministers of Comoros": "تصنيف:وزراء عدل جزر القمر",
    "Category:Justice ministers of Gambia": "تصنيف:وزراء عدل غامبيا",
    "Category:Labour ministers of Gabon": "تصنيف:وزراء عمل الغابون",
    "Category:Labour ministers of Sudan": "تصنيف:وزراء عمل السودان",
    "Category:Labour ministers of Comoros": "تصنيف:وزراء عمل جزر القمر",
    "Category:Ministers for culture of Abkhazia": "تصنيف:وزراء ثقافة أبخازيا",
    "Category:Oil ministers of Gabon": "تصنيف:وزراء بترول الغابون",
    "Category:Planning ministers of Comoros": "تصنيف:وزراء تخطيط جزر القمر",
    "Category:Transport ministers of Gabon": "تصنيف:وزراء نقل الغابون",
    "Category:Science ministers of Spain": "تصنيف:وزراء العلم إسبانيا",
    "Category:Water ministers of Mauritania": "تصنيف:وزراء مياه موريتانيا",
    "Category:Ministers of Housing of Abkhazia": "تصنيف:وزراء إسكان أبخازيا",
    "Category:Ministers of Religious Affairs of the Netherlands": "تصنيف:وزراء شؤون دينية هولندا",
    "Category:Women government ministers of Latvia": "تصنيف:وزيرات لاتفيات",
    "Category:Women's ministers of Fiji": "تصنيف:وزيرات فيجي",
    "Category:Ministers of Labour and Social Security of Turkey": "تصنيف:وزراء عمل وضمان اجتماعي تركيا",
}

TEMPORAL_CASES = [
    ("test_ministers_1", examples_1),
    ("test_ministers_2", examples_2),
]


@pytest.mark.parametrize("category, expected", examples_1.items(), ids=examples_1.keys())
@pytest.mark.fast
def test_ministers_1(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", examples_2.items(), ids=examples_2.keys())
@pytest.mark.fast
def test_ministers_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
