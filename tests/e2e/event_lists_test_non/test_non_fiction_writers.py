#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

non_fiction_data_by = {
    "Turkish non-fiction writers by century": "كتاب غير روائيين أتراك حسب القرن",
    "Australian non-fiction writers by century": "كتاب غير روائيين أستراليون حسب القرن",
    "Brazilian non-fiction writers by century": "كتاب غير روائيين برازيليون حسب القرن",
    "Portuguese non-fiction writers by century": "كتاب غير روائيين برتغاليون حسب القرن",
    "Puerto Rican non-fiction writers by century": "كتاب غير روائيين بورتوريكيون حسب القرن",
    "Czech non-fiction writers by century": "كتاب غير روائيين تشيكيون حسب القرن",
    "Welsh non-fiction writers by century": "كتاب غير روائيين ويلزيون حسب القرن",
    "Jewish non-fiction writers by nationality": "كتاب غير روائيين يهود حسب الجنسية",
    "Greek non-fiction writers by century": "كتاب غير روائيين يونانيون حسب القرن",
    "Mexican non-fiction writers by century": "كتاب غير روائيين مكسيكيون حسب القرن",
    "Non-fiction writers from Northern Ireland by century": "كتاب غير روائيين من أيرلندا الشمالية حسب القرن",
    "Non-fiction writers by ethnicity": "كتاب غير روائيين حسب المجموعة العرقية",
    "17th-century non-fiction writers by nationality": "كتاب غير روائيين في القرن 17 حسب الجنسية",
    "18th-century non-fiction writers by nationality": "كتاب غير روائيين في القرن 18 حسب الجنسية",
}

non_fiction_data_from = {
    "20th-century non-fiction writers from Northern Ireland": "كتاب غير روائيين من أيرلندا الشمالية في القرن 20",
    "18th-century non-fiction writers from the Russian Empire": "كتاب غير روائيين من الإمبراطورية الروسية في القرن 18",
}

non_fiction_data_nats = {
    "Salvadoran non-fiction writers": "كتاب غير روائيين سلفادوريون",
    "Non-fiction writers about the United States": "كتاب غير روائيين عن الولايات المتحدة",
    "Non-fiction writers about organized crime": "كتاب غير روائيين عن جريمة منظمة",
    "Non-fiction writers about California": "كتاب غير روائيين عن كاليفورنيا",
    "Croatian non-fiction writers": "كتاب غير روائيين كروات",
    "Moldovan non-fiction writers": "كتاب غير روائيين مولدوفيون",
    "Nepalese non-fiction writers": "كتاب غير روائيين نيباليون",
    "Nicaraguan non-fiction writers": "كتاب غير روائيين نيكاراغويون",
    "British non-fiction environmental writers": "كتاب بيئة غير روائيين بريطانيون",
    "Jordanian non-fiction writers": "كتاب غير روائيين أردنيون",
    "Bahraini non-fiction writers": "كتاب غير روائيين بحرينيون",
    "Bulgarian non-fiction writers": "كتاب غير روائيين بلغاريون",
    "Panamanian non-fiction writers": "كتاب غير روائيين بنميون",
    "Burundian non-fiction writers": "كتاب غير روائيين بورونديون",
    "Gibraltarian non-fiction writers": "كتاب غير روائيين جبل طارقيون",
    "Algerian non-fiction writers": "كتاب غير روائيين جزائريون",
}

non_fiction_data_male = {
    # "New Zealand male non-fiction writers": "كتاب غير روائيين ذكور نيوزيلنديون",
    "Turkish male non-fiction writers": "كتاب غير روائيين ذكور أتراك",
    "Argentine male non-fiction writers": "كتاب غير روائيين ذكور أرجنتينيون",
    "Albanian male non-fiction writers": "كتاب غير روائيين ذكور ألبان",
    "Estonian male non-fiction writers": "كتاب غير روائيين ذكور إستونيون",
    "Israeli male non-fiction writers": "كتاب غير روائيين ذكور إسرائيليون",
    "Scottish male non-fiction writers": "كتاب غير روائيين ذكور إسكتلنديون",
    "Pakistani male non-fiction writers": "كتاب غير روائيين ذكور باكستانيون",
    "Brazilian male non-fiction writers": "كتاب غير روائيين ذكور برازيليون",
    "Portuguese male non-fiction writers": "كتاب غير روائيين ذكور برتغاليون",
    "Puerto Rican male non-fiction writers": "كتاب غير روائيين ذكور بورتوريكيون",
    "Bolivian male non-fiction writers": "كتاب غير روائيين ذكور بوليفيون",
    "Peruvian male non-fiction writers": "كتاب غير روائيين ذكور بيرويون",
    "Trinidad and Tobago male non-fiction writers": "كتاب غير روائيين ذكور ترنيداديون",
    "Czech male non-fiction writers": "كتاب غير روائيين ذكور تشيكيون",
    "Chilean male non-fiction writers": "كتاب غير روائيين ذكور تشيليون",
    "Jamaican male non-fiction writers": "كتاب غير روائيين ذكور جامايكيون",
    "Russian male non-fiction writers": "كتاب غير روائيين ذكور روس",
    "Romanian male non-fiction writers": "كتاب غير روائيين ذكور رومان",
    "Soviet male non-fiction writers": "كتاب غير روائيين ذكور سوفيت",
    "Swiss male non-fiction writers": "كتاب غير روائيين ذكور سويسريون",
    "Serbian male non-fiction writers": "كتاب غير روائيين ذكور صرب",
    "Chinese male non-fiction writers": "كتاب غير روائيين ذكور صينيون",
    "Palestinian male non-fiction writers": "كتاب غير روائيين ذكور فلسطينيون",
    "Venezuelan male non-fiction writers": "كتاب غير روائيين ذكور فنزويليون",
    "Finnish male non-fiction writers": "كتاب غير روائيين ذكور فنلنديون",
    "Cuban male non-fiction writers": "كتاب غير روائيين ذكور كوبيون",
    "Colombian male non-fiction writers": "كتاب غير روائيين ذكور كولومبيون",
    "Luxembourgian male non-fiction writers": "كتاب غير روائيين ذكور لوكسمبورغيون",
    "Lithuanian male non-fiction writers": "كتاب غير روائيين ذكور ليتوانيون",
    "Hungarian male non-fiction writers": "كتاب غير روائيين ذكور مجريون",
    "Egyptian male non-fiction writers": "كتاب غير روائيين ذكور مصريون",
    "Mexican male non-fiction writers": "كتاب غير روائيين ذكور مكسيكيون",
    "Moldovan male non-fiction writers": "كتاب غير روائيين ذكور مولدوفيون",
    "Norwegian male non-fiction writers": "كتاب غير روائيين ذكور نرويجيون",
    "Austrian male non-fiction writers": "كتاب غير روائيين ذكور نمساويون",
    "Haitian male non-fiction writers": "كتاب غير روائيين ذكور هايتيون",
    "Dutch male non-fiction writers": "كتاب غير روائيين ذكور هولنديون",
    "Welsh male non-fiction writers": "كتاب غير روائيين ذكور ويلزيون",
    "Japanese male non-fiction writers": "كتاب غير روائيين ذكور يابانيون",
    "Greek male non-fiction writers": "كتاب غير روائيين ذكور يونانيون",
}

non_fiction_data_nat_with_time = {
    "20th-century Turkish non-fiction writers": "كتاب غير روائيين أتراك في القرن 20",
    "21st-century Turkish non-fiction writers": "كتاب غير روائيين أتراك في القرن 21",
    "19th-century Australian non-fiction writers": "كتاب غير روائيين أستراليون في القرن 19",
    "17th-century Irish non-fiction writers": "كتاب غير روائيين أيرلنديون في القرن 17",
    "18th-century Irish non-fiction writers": "كتاب غير روائيين أيرلنديون في القرن 18",
    "19th-century Spanish non-fiction writers": "كتاب غير روائيين إسبان في القرن 19",
    "20th-century Spanish non-fiction writers": "كتاب غير روائيين إسبان في القرن 20",
    "17th-century Scottish non-fiction writers": "كتاب غير روائيين إسكتلنديون في القرن 17",
    "18th-century Scottish non-fiction writers": "كتاب غير روائيين إسكتلنديون في القرن 18",
    "19th-century Scottish non-fiction writers": "كتاب غير روائيين إسكتلنديون في القرن 19",
    "20th-century Scottish non-fiction writers": "كتاب غير روائيين إسكتلنديون في القرن 20",
    "19th-century Italian non-fiction writers": "كتاب غير روائيين إيطاليون في القرن 19",
    "19th-century Brazilian non-fiction writers": "كتاب غير روائيين برازيليون في القرن 19",
    "20th-century Brazilian non-fiction writers": "كتاب غير روائيين برازيليون في القرن 20",
    "21st-century Brazilian non-fiction writers": "كتاب غير روائيين برازيليون في القرن 21",
    "20th-century Portuguese non-fiction writers": "كتاب غير روائيين برتغاليون في القرن 20",
    "21st-century Portuguese non-fiction writers": "كتاب غير روائيين برتغاليون في القرن 21",
    "19th-century Belgian non-fiction writers": "كتاب غير روائيين بلجيكيون في القرن 19",
    "20th-century Bangladeshi non-fiction writers": "كتاب غير روائيين بنغلاديشيون في القرن 20",
    "21st-century Bangladeshi non-fiction writers": "كتاب غير روائيين بنغلاديشيون في القرن 21",
    "19th-century Puerto Rican non-fiction writers": "كتاب غير روائيين بورتوريكيون في القرن 19",
    "20th-century Puerto Rican non-fiction writers": "كتاب غير روائيين بورتوريكيون في القرن 20",
    "21st-century Puerto Rican non-fiction writers": "كتاب غير روائيين بورتوريكيون في القرن 21",
    "19th-century Czech non-fiction writers": "كتاب غير روائيين تشيكيون في القرن 19",
    "20th-century Czech non-fiction writers": "كتاب غير روائيين تشيكيون في القرن 20",
    "21st-century Czech non-fiction writers": "كتاب غير روائيين تشيكيون في القرن 21",
    "18th-century Danish non-fiction writers": "كتاب غير روائيين دنماركيون في القرن 18",
    "19th-century Danish non-fiction writers": "كتاب غير روائيين دنماركيون في القرن 19",
    "19th-century Swedish non-fiction writers": "كتاب غير روائيين سويديون في القرن 19",
    "21st-century Swedish non-fiction writers": "كتاب غير روائيين سويديون في القرن 21",
    "20th-century Chinese non-fiction writers": "كتاب غير روائيين صينيون في القرن 20",
    "21st-century Chinese non-fiction writers": "كتاب غير روائيين صينيون في القرن 21",
    "20th-century Finnish non-fiction writers": "كتاب غير روائيين فنلنديون في القرن 20",
    "21st-century South Korean non-fiction writers": "كتاب غير روائيين كوريون جنوبيون في القرن 21",
    "21st-century Lithuanian non-fiction writers": "كتاب غير روائيين ليتوانيون في القرن 21",
    "20th-century Egyptian non-fiction writers": "كتاب غير روائيين مصريون في القرن 20",
    "21st-century Egyptian non-fiction writers": "كتاب غير روائيين مصريون في القرن 21",
    "19th-century Mexican non-fiction writers": "كتاب غير روائيين مكسيكيون في القرن 19",
    "20th-century Mexican non-fiction writers": "كتاب غير روائيين مكسيكيون في القرن 20",
    "21st-century Mexican non-fiction writers": "كتاب غير روائيين مكسيكيون في القرن 21",
    "21st-century Norwegian non-fiction writers": "كتاب غير روائيين نرويجيون في القرن 21",
    "20th-century Austrian non-fiction writers": "كتاب غير روائيين نمساويون في القرن 20",
    "21st-century Austrian non-fiction writers": "كتاب غير روائيين نمساويون في القرن 21",
    "17th-century Dutch non-fiction writers": "كتاب غير روائيين هولنديون في القرن 17",
    "18th-century Dutch non-fiction writers": "كتاب غير روائيين هولنديون في القرن 18",
    "19th-century Dutch non-fiction writers": "كتاب غير روائيين هولنديون في القرن 19",
    "20th-century Welsh non-fiction writers": "كتاب غير روائيين ويلزيون في القرن 20",
    "21st-century Welsh non-fiction writers": "كتاب غير روائيين ويلزيون في القرن 21",
    "20th-century Japanese non-fiction writers": "كتاب غير روائيين يابانيون في القرن 20",
    "21st-century Japanese non-fiction writers": "كتاب غير روائيين يابانيون في القرن 21",
    "19th-century Greek non-fiction writers": "كتاب غير روائيين يونانيون في القرن 19",
    "20th-century Greek non-fiction writers": "كتاب غير روائيين يونانيون في القرن 20",
    "21st-century Greek non-fiction writers": "كتاب غير روائيين يونانيون في القرن 21",
}

to_test = [
    ("test_non_fiction_data_by", non_fiction_data_by),
    ("test_non_fiction_data_from", non_fiction_data_from),
    ("test_non_fiction_data_nats", non_fiction_data_nats),
    ("test_non_fiction_data_male", non_fiction_data_male),
    ("test_non_fiction_data_nat_with_time", non_fiction_data_nat_with_time),
]

non_fiction_data_all = {
    **non_fiction_data_by,
    **non_fiction_data_from,
    **non_fiction_data_nats,
    **non_fiction_data_male,
    **non_fiction_data_nat_with_time,
}


@pytest.mark.parametrize("category, expected", non_fiction_data_all.items(), ids=non_fiction_data_all.keys())
@pytest.mark.slow
def test_non_fiction_writers(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
