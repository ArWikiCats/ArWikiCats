#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_2 = {
    "Fictional Buddhist nuns": "راهبات بوذيات خياليات",
    "20th-century American Buddhist nuns": "راهبات بوذيات أمريكيات في القرن 20",
    "21st-century American Buddhist nuns": "راهبات بوذيات أمريكيات في القرن 21",
    "10th-century Buddhist nuns": "راهبات بوذيات في القرن 10",
    "10th-century Christian nuns": "راهبات مسيحيات في القرن 10",
    "11th-century Buddhist nuns": "راهبات بوذيات في القرن 11",
    "11th-century Christian nuns": "راهبات مسيحيات في القرن 11",
    "12th-century Buddhist nuns": "راهبات بوذيات في القرن 12",
    "12th-century Christian nuns": "راهبات مسيحيات في القرن 12",
    "13th-century Buddhist nuns": "راهبات بوذيات في القرن 13",
    "13th-century Christian nuns": "راهبات مسيحيات في القرن 13",
    "14th-century Buddhist nuns": "راهبات بوذيات في القرن 14",
    "14th-century Christian nuns": "راهبات مسيحيات في القرن 14",
    "15th-century Buddhist nuns": "راهبات بوذيات في القرن 15",
    "15th-century Christian nuns": "راهبات مسيحيات في القرن 15",
    "16th-century Buddhist nuns": "راهبات بوذيات في القرن 16",
    "16th-century Christian nuns": "راهبات مسيحيات في القرن 16",
    "17th-century Buddhist nuns": "راهبات بوذيات في القرن 17",
    "17th-century Christian nuns": "راهبات مسيحيات في القرن 17",
    "18th-century Buddhist nuns": "راهبات بوذيات في القرن 18",
    "18th-century Christian nuns": "راهبات مسيحيات في القرن 18",
    "19th-century Anglican nuns": "راهبات أنجليكيات في القرن 19",
    "19th-century Australian Christian nuns": "راهبات مسيحيات أستراليات في القرن 19",
    "19th-century British Anglican nuns": "راهبات أنجليكيات بريطانيات في القرن 19",
    "19th-century Buddhist nuns": "راهبات بوذيات في القرن 19",
    "19th-century Christian nuns": "راهبات مسيحيات في القرن 19",
    "1st-century Buddhist nuns": "راهبات بوذيات في القرن 1",
    "20th-century Anglican nuns": "راهبات أنجليكيات في القرن 20",
    "20th-century Australian Christian nuns": "راهبات مسيحيات أستراليات في القرن 20",
    "20th-century British Anglican nuns": "راهبات أنجليكيات بريطانيات في القرن 20",
    "20th-century Buddhist nuns": "راهبات بوذيات في القرن 20",
    "20th-century Christian nuns": "راهبات مسيحيات في القرن 20",
    "21st-century Anglican nuns": "راهبات أنجليكيات في القرن 21",
    "21st-century Australian Christian nuns": "راهبات مسيحيات أستراليات في القرن 21",
    "21st-century British Anglican nuns": "راهبات أنجليكيات بريطانيات في القرن 21",
    "21st-century Buddhist nuns": "راهبات بوذيات في القرن 21",
    "21st-century Christian nuns": "راهبات مسيحيات في القرن 21",
    "3rd-century BC Buddhist nuns": "راهبات بوذيات في القرن 3 ق م",
    "4th-century Buddhist nuns": "راهبات بوذيات في القرن 4",
    "4th-century Christian nuns": "راهبات مسيحيات في القرن 4",
    "5th-century Buddhist nuns": "راهبات بوذيات في القرن 5",
    "5th-century Christian nuns": "راهبات مسيحيات في القرن 5",
    "6th-century Buddhist nuns": "راهبات بوذيات في القرن 6",
    "6th-century Christian nuns": "راهبات مسيحيات في القرن 6",
    "7th-century Buddhist nuns": "راهبات بوذيات في القرن 7",
    "7th-century Christian nuns": "راهبات مسيحيات في القرن 7",
    "8th-century Buddhist nuns": "راهبات بوذيات في القرن 8",
    "8th-century Christian nuns": "راهبات مسيحيات في القرن 8",
    "9th-century Buddhist nuns": "راهبات بوذيات في القرن 9",
    "9th-century Christian nuns": "راهبات مسيحيات في القرن 9",
    "American Buddhist nuns": "راهبات بوذيات أمريكيات",
    "American Christian nuns": "راهبات مسيحيات أمريكيات",
    "American Hindu nuns": "راهبات هندوسيات أمريكيات",
    "Australian Christian nuns": "راهبات مسيحيات أستراليات",
    "Belgian Buddhist nuns": "راهبات بوذيات بلجيكيات",
    "British Anglican nuns": "راهبات أنجليكيات بريطانيات",
    "British Buddhist nuns": "راهبات بوذيات بريطانيات",
    "Buddhist nuns by century": "راهبات بوذيات حسب القرن",
    "Buddhist nuns by nationality": "راهبات بوذيات حسب الجنسية",
    "Buddhist nuns of Nara period": "راهبات بوذيات في فترة نارا",
    "Chinese Buddhist nuns": "راهبات بوذيات صينيات",
    "Christian nuns by century": "راهبات مسيحيات حسب القرن",
    "Fictional Christian nuns": "راهبات مسيحيات خياليات",
    "French Buddhist nuns": "راهبات بوذيات فرنسيات",
    "German Buddhist nuns": "راهبات بوذيات ألمانيات",
    "Indian Buddhist nuns": "راهبات بوذيات هنديات",
    "Indian Hindu nuns": "راهبات هندوسيات هنديات",
    "Indonesian Buddhist nuns": "راهبات بوذيات إندونيسيات",
    "Irish Buddhist nuns": "راهبات بوذيات أيرلنديات",
    "Italian Buddhist nuns": "راهبات بوذيات إيطاليات",
    "Japanese Buddhist nuns by period": "راهبات بوذيات يابانيات حسب الحقبة",
    "Japanese Buddhist nuns": "راهبات بوذيات يابانيات",
    "Korean Buddhist nuns": "راهبات بوذيات كوريات",
    "Nepalese Buddhist nuns": "راهبات بوذيات نيباليات",
    "Scottish Buddhist nuns": "راهبات بوذيات إسكتلنديات",
    "Singaporean Buddhist nuns": "راهبات بوذيات سنغافوريات",
    "South Korean Buddhist nuns": "راهبات بوذيات كوريات جنوبيات",
    "Taiwanese Buddhist nuns": "راهبات بوذيات تايوانيات",
    "Thai Buddhist nuns": "راهبات بوذيات تايلنديات",
    "Vietnamese Buddhist nuns": "راهبات بوذيات فيتناميات",
}

to_test = [
    ("test_nuns_2", data_2),
]


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_nuns_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
