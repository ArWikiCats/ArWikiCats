#
import pytest

from ArWikiCats import resolve_label_ar

examples = {
    "18th-century Dutch explorers": "مستكشفون هولنديون في القرن 18",
    "20th-century Albanian sports coaches": "مدربو رياضة ألبان في القرن 20",
    "19th-century actors": "ممثلون في القرن 19",
    "2000s American films": "أفلام أمريكية في عقد 2000",
    "2017 American television series debuts": "مسلسلات تلفزيونية أمريكية بدأ عرضها في 2017",
    "2017 American television series endings": "مسلسلات تلفزيونية أمريكية انتهت في 2017",
    "19th-century actors by religion": "ممثلون في القرن 19 حسب الدين",
    "19th-century people by religion": "أشخاص في القرن 19 حسب الدين",
}

TEMPORAL_CASES = [
    ("temporal_1", examples),
]


@pytest.mark.parametrize("category, expected", examples.items(), ids=examples.keys())
def test_add_in(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected
