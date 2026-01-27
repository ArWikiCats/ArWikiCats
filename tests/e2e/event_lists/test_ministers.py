#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

test_skip = {"Jewish-American history in New York City": ""}

examples_1 = {
    "Ministers for foreign affairs of Papua New Guinea": "وزراء شؤون خارجية بابوا غينيا الجديدة",
    "Justice ministers of Papua New Guinea": "وزراء عدل بابوا غينيا الجديدة",
    "Women government ministers of Antigua and Barbuda": "وزيرات أنتيغويات وبربوديات",
    "Agriculture ministers of Antigua and Barbuda": "وزراء زراعة أنتيغوا وباربودا",
    "Energy ministers of Antigua and Barbuda": "وزراء طاقة أنتيغوا وباربودا",
    "Tourism ministers of Antigua and Barbuda": "وزراء سياحة أنتيغوا وباربودا",
    "Trade ministers of Antigua and Barbuda": "وزراء تجارة أنتيغوا وباربودا",
    "Culture ministers of Uganda": "وزراء ثقافة أوغندا",
    "Defence ministers of Kuwait": "وزراء دفاع الكويت",
    "Education ministers of Afghanistan": "وزراء تعليم أفغانستان",
    "Finance ministers of Tunisia": "وزراء مالية تونس",
    "Foreign ministers of South Sudan": "وزراء خارجية جنوب السودان",
    "Labour ministers of Chad": "وزراء عمل تشاد",
    "Ministers for foreign affairs of Ireland": "وزراء شؤون خارجية أيرلندا",
    "Trade ministers of Indonesia": "وزراء تجارة إندونيسيا",
    "Transport ministers of Argentina": "وزراء نقل الأرجنتين",
    "Transport ministers of Liberia": "وزراء نقل ليبيريا",
    "Foreign trade ministers of Netherlands": "وزراء تجارة خارجية هولندا",
    "Social affairs ministers of Uganda": "وزراء شؤون اجتماعية أوغندا",
    "Trade ministers of Togo": "وزراء تجارة توغو",
    "Ministers for Foreign Affairs of Abkhazia": "وزراء شؤون خارجية أبخازيا",
    "Ministers for Foreign Affairs of Singapore": "وزراء شؤون خارجية سنغافورة",
    "Ministers for Foreign Affairs of Luxembourg": "وزراء شؤون خارجية لوكسمبورغ",
    "Ministers for Internal Affairs of Abkhazia": "وزراء شؤون داخلية أبخازيا",
    "Ministers for Public Works of Luxembourg": "وزراء أشغال عامة لوكسمبورغ",
    "Housing ministers of Abkhazia": "وزراء إسكان أبخازيا",
    "Economy ministers of Latvia": "وزراء اقتصاد لاتفيا",
    "Ministers of Economics of Latvia": "وزراء الاقتصاد في لاتفيا",
    "Religious affairs ministers of Yemen": "وزراء شؤون دينية اليمن",
}

examples_2 = {
    "Agriculture ministers of Azerbaijan": "وزراء زراعة أذربيجان",
    "Agriculture ministers of Maldives": "وزراء زراعة جزر المالديف",
    "Communications ministers of Azerbaijan": "وزراء اتصالات أذربيجان",
    "Communications ministers of Comoros": "وزراء اتصالات جزر القمر",
    "Culture ministers of Gabon": "وزراء ثقافة الغابون",
    "Education ministers of Comoros": "وزراء تعليم جزر القمر",
    "Electricity and water ministers of Somalia": "وزراء كهرباء ومياه الصومال",
    "Energy ministers of Gabon": "وزراء طاقة الغابون",
    "Finance ministers of Burundi": "وزراء مالية بوروندي",
    "Health ministers of Comoros": "وزراء صحة جزر القمر",
    "Industry ministers of Togo": "وزراء صناعة توغو",
    "Interior ministers of Uganda": "وزراء داخلية أوغندا",
    "Justice ministers of Djibouti": "وزراء عدل جيبوتي",
    "Justice ministers of Comoros": "وزراء عدل جزر القمر",
    "Justice ministers of Gambia": "وزراء عدل غامبيا",
    "Labour ministers of Gabon": "وزراء عمل الغابون",
    "Labour ministers of Sudan": "وزراء عمل السودان",
    "Labour ministers of Comoros": "وزراء عمل جزر القمر",
    "Ministers for culture of Abkhazia": "وزراء ثقافة أبخازيا",
    "Oil ministers of Gabon": "وزراء بترول الغابون",
    "Planning ministers of Comoros": "وزراء تخطيط جزر القمر",
    "Transport ministers of Gabon": "وزراء نقل الغابون",
    "Science ministers of Spain": "وزراء العلم إسبانيا",
    "Water ministers of Mauritania": "وزراء مياه موريتانيا",
    "Ministers of Housing of Abkhazia": "وزراء إسكان أبخازيا",
    "Ministers of Religious Affairs of the Netherlands": "وزراء شؤون دينية هولندا",
    "Women government ministers of Latvia": "وزيرات لاتفيات",
    "Women's ministers of Fiji": "وزيرات فيجي",
    "Ministers of Labour and Social Security of Turkey": "وزراء عمل وضمان اجتماعي تركيا",
}

TEMPORAL_CASES = [
    ("test_ministers_1", examples_1),
    ("test_ministers_2", examples_2),
]


@pytest.mark.parametrize("category, expected", examples_1.items(), ids=examples_1.keys())
@pytest.mark.fast
def test_ministers_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", examples_2.items(), ids=examples_2.keys())
@pytest.mark.fast
def test_ministers_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
