#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

fast_data_1 = {
    "People executed in British North America by hanging": "أشخاص أعدموا في أمريكا الشمالية البريطانية بالشنق",
    "People executed in the Holy Roman Empire by burning": "أشخاص أعدموا في الإمبراطورية الرومانية المقدسة بالحرق",
    "People executed in the Holy Roman Empire by decapitation": "أشخاص أعدموا في الإمبراطورية الرومانية المقدسة بقطع الرأس",

    "Works about foreign relations of the United States": "أعمال عن علاقات خارجية الولايات المتحدة",
    "Books about foreign relations of the United States": "كتب عن علاقات خارجية الولايات المتحدة",
    "National youth sports teams of the United States": "منتخبات رياضية وطنية شبابية الولايات المتحدة",
    "Women's national sports teams of the United States": "منتخبات رياضية وطنية نسائية الولايات المتحدة",
    "Men's national sports teams of the United States": "منتخبات رياضية وطنية رجالية الولايات المتحدة",
    "Members of the Riksdag 2010–2010": "أعضاء البرلمان السويدي 2010–2010",
    "wheelchair basketball players in turkey": "لاعبو كرة سلة على كراسي متحركة في تركيا",
    "field hockey players in germany": "لاعبو هوكي ميدان في ألمانيا",
    "baseball players in florida": "لاعبو كرة قاعدة في فلوريدا",
    "baseball players in south korea": "لاعبو كرة قاعدة في كوريا الجنوبية",
    "basketball players in lebanon": "لاعبو كرة سلة في لبنان",
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
