#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

fast_data_1 = {
    "sport in khartoum": "الرياضة في الخرطوم",
    "sport in ottoman empire": "الرياضة في الدولة العثمانية",
    "sport in tuzla": "الرياضة في توزلا",
    "sport in veria": "الرياضة في فيريا",
    "sport in álava": "الرياضة في ألافا (مقاطعة)",
    "Women from Dutch Caribbean": "نساء من كاريبيون هولنديون",
    "Women from Kingdom of Prussia": "نساء من مملكة بروسيا",
    "Women from Kingdom of Travancore": "نساء من مملكة ترافنكور",
    "Women from Overseas France": "نساء من مقاطعات وأقاليم ما وراء البحار الفرنسية",
    "Defunct political parties of Islamic Republic of Iran": "أحزاب سياسية سابقة في الجمهورية الإسلامية الإيرانية",
    "People executed by hanging by country": "أشخاص أعدموا حرقاً حسب البلد",
    "Cultural depictions of sportspeople": "تصوير ثقافي عن رياضيون",
    "Scheduled sports events": "أحداث رياضية مقررة",
}

to_test = [
    ("test_sports_events_2", fast_data_1),
]


@pytest.mark.parametrize("category, expected", fast_data_1.items(), ids=fast_data_1.keys())
@pytest.mark.skip2
def test_fast_data_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


# test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
