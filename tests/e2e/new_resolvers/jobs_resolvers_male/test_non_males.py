#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data1 = {
    "albanian male non-fiction writers": "كتاب غير روائيين ذكور ألبان",
    "american male non-fiction writers": "كتاب غير روائيين ذكور أمريكيون",
    "argentine male non-fiction writers": "كتاب غير روائيين ذكور أرجنتينيون",
    "australian male non-fiction writers": "كتاب غير روائيين ذكور أستراليون",
    "austrian male non-fiction writers": "كتاب غير روائيين ذكور نمساويون",
    "belarusian male non-fiction writers": "كتاب غير روائيين ذكور بيلاروسيون",
    "belgian male non-fiction writers": "كتاب غير روائيين ذكور بلجيكيون",
    "bolivian male non-fiction writers": "كتاب غير روائيين ذكور بوليفيون",
    "brazilian male non-fiction writers": "كتاب غير روائيين ذكور برازيليون",
    "british male non-fiction writers": "كتاب غير روائيين ذكور بريطانيون",
    "canadian male non-fiction writers": "كتاب غير روائيين ذكور كنديون",
    "chilean male non-fiction writers": "كتاب غير روائيين ذكور تشيليون",
    "chinese male non-fiction writers": "كتاب غير روائيين ذكور صينيون",
    "colombian male non-fiction writers": "كتاب غير روائيين ذكور كولومبيون",
    "cuban male non-fiction writers": "كتاب غير روائيين ذكور كوبيون",
    "czech male non-fiction writers": "كتاب غير روائيين ذكور تشيكيون",
    "danish male non-fiction writers": "كتاب غير روائيين ذكور دنماركيون",
    "dutch male non-fiction writers": "كتاب غير روائيين ذكور هولنديون",
    "egyptian male non-fiction writers": "كتاب غير روائيين ذكور مصريون",
    "english male non-fiction writers": "كتاب غير روائيين ذكور إنجليز",
    "estonian male non-fiction writers": "كتاب غير روائيين ذكور إستونيون",
    "finnish male non-fiction writers": "كتاب غير روائيين ذكور فنلنديون",
    "french male non-fiction writers": "كتاب غير روائيين ذكور فرنسيون",
    "german male non-fiction writers": "كتاب غير روائيين ذكور ألمان",
    "greek male non-fiction writers": "كتاب غير روائيين ذكور يونانيون",
    "haitian male non-fiction writers": "كتاب غير روائيين ذكور هايتيون",
    "hungarian male non-fiction writers": "كتاب غير روائيين ذكور مجريون",
    "indian male non-fiction writers": "كتاب غير روائيين ذكور هنود",
    "irish male non-fiction writers": "كتاب غير روائيين ذكور أيرلنديون",
    "israeli male non-fiction writers": "كتاب غير روائيين ذكور إسرائيليون",
    "italian male non-fiction writers": "كتاب غير روائيين ذكور إيطاليون",
    "jamaican male non-fiction writers": "كتاب غير روائيين ذكور جامايكيون",
    "japanese male non-fiction writers": "كتاب غير روائيين ذكور يابانيون",
    "latvian male non-fiction writers": "كتاب غير روائيين ذكور لاتفيون",
    "lithuanian male non-fiction writers": "كتاب غير روائيين ذكور ليتوانيون",
    "luxembourgian male non-fiction writers": "كتاب غير روائيين ذكور لوكسمبورغيون",
    "mexican male non-fiction writers": "كتاب غير روائيين ذكور مكسيكيون",
    "moldovan male non-fiction writers": "كتاب غير روائيين ذكور مولدوفيون",
    "norwegian male non-fiction writers": "كتاب غير روائيين ذكور نرويجيون",
    "pakistani male non-fiction writers": "كتاب غير روائيين ذكور باكستانيون",
    "palestinian male non-fiction writers": "كتاب غير روائيين ذكور فلسطينيون",
    "peruvian male non-fiction writers": "كتاب غير روائيين ذكور بيرويون",
    "polish male non-fiction writers": "كتاب غير روائيين ذكور بولنديون",
    "portuguese male non-fiction writers": "كتاب غير روائيين ذكور برتغاليون",
    "puerto rican male non-fiction writers": "كتاب غير روائيين ذكور بورتوريكيون",
    "romanian male non-fiction writers": "كتاب غير روائيين ذكور رومان",
    "russian male non-fiction writers": "كتاب غير روائيين ذكور روس",
    "scottish male non-fiction writers": "كتاب غير روائيين ذكور إسكتلنديون",
    "serbian male non-fiction writers": "كتاب غير روائيين ذكور صرب",
    "soviet male non-fiction writers": "كتاب غير روائيين ذكور سوفيت",
    "spanish male non-fiction writers": "كتاب غير روائيين ذكور إسبان",
    "swedish male non-fiction writers": "كتاب غير روائيين ذكور سويديون",
    "swiss male non-fiction writers": "كتاب غير روائيين ذكور سويسريون",
    "thai male non-fiction writers": "كتاب غير روائيين ذكور تايلنديون",
    "trinidad and tobago male non-fiction writers": "كتاب غير روائيين ذكور ترنيداديون",
    "turkish male non-fiction writers": "كتاب غير روائيين ذكور أتراك",
    "welsh male non-fiction writers": "كتاب غير روائيين ذكور ويلزيون",
}

to_test = [
    ("test_non", data1),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.slow
def test_non(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
