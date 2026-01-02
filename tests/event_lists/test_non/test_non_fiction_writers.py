#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

non_fiction_data_by = {
    "Category:Turkish non-fiction writers by century": "تصنيف:كتاب غير روائيين أتراك حسب القرن",
    "Category:Australian non-fiction writers by century": "تصنيف:كتاب غير روائيين أستراليون حسب القرن",
    "Category:Brazilian non-fiction writers by century": "تصنيف:كتاب غير روائيين برازيليون حسب القرن",
    "Category:Portuguese non-fiction writers by century": "تصنيف:كتاب غير روائيين برتغاليون حسب القرن",
    "Category:Puerto Rican non-fiction writers by century": "تصنيف:كتاب غير روائيين بورتوريكيون حسب القرن",
    "Category:Czech non-fiction writers by century": "تصنيف:كتاب غير روائيين تشيكيون حسب القرن",
    "Category:Welsh non-fiction writers by century": "تصنيف:كتاب غير روائيين ويلزيون حسب القرن",
    "Category:Jewish non-fiction writers by nationality": "تصنيف:كتاب غير روائيين يهود حسب الجنسية",
    "Category:Greek non-fiction writers by century": "تصنيف:كتاب غير روائيين يونانيون حسب القرن",
    "Category:Mexican non-fiction writers by century": "تصنيف:كتاب غير روائيين مكسيكيون حسب القرن",
    "Category:Non-fiction writers from Northern Ireland by century": "تصنيف:كتاب غير روائيين من أيرلندا الشمالية حسب القرن",
    "Category:Non-fiction writers by ethnicity": "تصنيف:كتاب غير روائيين حسب المجموعة العرقية",
    "Category:17th-century non-fiction writers by nationality": "تصنيف:كتاب غير روائيين في القرن 17 حسب الجنسية",
    "Category:18th-century non-fiction writers by nationality": "تصنيف:كتاب غير روائيين في القرن 18 حسب الجنسية",
}

non_fiction_data_from = {
    "Category:20th-century non-fiction writers from Northern Ireland": "تصنيف:كتاب غير روائيين من أيرلندا الشمالية في القرن 20",
    "Category:18th-century non-fiction writers from the Russian Empire": "تصنيف:كتاب غير روائيين من الإمبراطورية الروسية في القرن 18",
}

non_fiction_data_nats = {
    "Category:Salvadoran non-fiction writers": "تصنيف:كتاب غير روائيين سلفادوريون",
    "Category:Non-fiction writers about the United States": "تصنيف:كتاب غير روائيين عن الولايات المتحدة",
    "Category:Non-fiction writers about organized crime": "تصنيف:كتاب غير روائيين عن جريمة منظمة",
    "Category:Non-fiction writers about California": "تصنيف:كتاب غير روائيين عن كاليفورنيا",
    "Category:Croatian non-fiction writers": "تصنيف:كتاب غير روائيين كروات",
    "Category:Moldovan non-fiction writers": "تصنيف:كتاب غير روائيين مولدوفيون",
    "Category:Nepalese non-fiction writers": "تصنيف:كتاب غير روائيين نيباليون",
    "Category:Nicaraguan non-fiction writers": "تصنيف:كتاب غير روائيين نيكاراغويون",
    "Category:British non-fiction environmental writers": "تصنيف:كتاب بيئة غير روائيين بريطانيون",
    "Category:Jordanian non-fiction writers": "تصنيف:كتاب غير روائيين أردنيون",
    "Category:Bahraini non-fiction writers": "تصنيف:كتاب غير روائيين بحرينيون",
    "Category:Bulgarian non-fiction writers": "تصنيف:كتاب غير روائيين بلغاريون",
    "Category:Panamanian non-fiction writers": "تصنيف:كتاب غير روائيين بنميون",
    "Category:Burundian non-fiction writers": "تصنيف:كتاب غير روائيين بورونديون",
    "Category:Gibraltarian non-fiction writers": "تصنيف:كتاب غير روائيين جبل طارقيون",
    "Category:Algerian non-fiction writers": "تصنيف:كتاب غير روائيين جزائريون",
}

non_fiction_data_male = {
    # "Category:New Zealand male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور نيوزيلنديون",
    "Category:Turkish male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور أتراك",
    "Category:Argentine male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور أرجنتينيون",
    "Category:Albanian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور ألبان",
    "Category:Estonian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور إستونيون",
    "Category:Israeli male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور إسرائيليون",
    "Category:Scottish male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور إسكتلنديون",
    "Category:Pakistani male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور باكستانيون",
    "Category:Brazilian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور برازيليون",
    "Category:Portuguese male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور برتغاليون",
    "Category:Puerto Rican male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور بورتوريكيون",
    "Category:Bolivian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور بوليفيون",
    "Category:Peruvian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور بيرويون",
    "Category:Trinidad and Tobago male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور ترنيداديون",
    "Category:Czech male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور تشيكيون",
    "Category:Chilean male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور تشيليون",
    "Category:Jamaican male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور جامايكيون",
    "Category:Russian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور روس",
    "Category:Romanian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور رومان",
    "Category:Soviet male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور سوفيت",
    "Category:Swiss male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور سويسريون",
    "Category:Serbian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور صرب",
    "Category:Chinese male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور صينيون",
    "Category:Palestinian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور فلسطينيون",
    "Category:Venezuelan male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور فنزويليون",
    "Category:Finnish male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور فنلنديون",
    "Category:Cuban male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور كوبيون",
    "Category:Colombian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور كولومبيون",
    "Category:Luxembourgian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور لوكسمبورغيون",
    "Category:Lithuanian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور ليتوانيون",
    "Category:Hungarian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور مجريون",
    "Category:Egyptian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور مصريون",
    "Category:Mexican male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور مكسيكيون",
    "Category:Moldovan male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور مولدوفيون",
    "Category:Norwegian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور نرويجيون",
    "Category:Austrian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور نمساويون",
    "Category:Haitian male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور هايتيون",
    "Category:Dutch male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور هولنديون",
    "Category:Welsh male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور ويلزيون",
    "Category:Japanese male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور يابانيون",
    "Category:Greek male non-fiction writers": "تصنيف:كتاب غير روائيين ذكور يونانيون",
}

non_fiction_data_nat_with_time = {
    "Category:20th-century Turkish non-fiction writers": "تصنيف:كتاب غير روائيين أتراك في القرن 20",
    "Category:21st-century Turkish non-fiction writers": "تصنيف:كتاب غير روائيين أتراك في القرن 21",
    "Category:19th-century Australian non-fiction writers": "تصنيف:كتاب غير روائيين أستراليون في القرن 19",
    "Category:17th-century Irish non-fiction writers": "تصنيف:كتاب غير روائيين أيرلنديون في القرن 17",
    "Category:18th-century Irish non-fiction writers": "تصنيف:كتاب غير روائيين أيرلنديون في القرن 18",
    "Category:19th-century Spanish non-fiction writers": "تصنيف:كتاب غير روائيين إسبان في القرن 19",
    "Category:20th-century Spanish non-fiction writers": "تصنيف:كتاب غير روائيين إسبان في القرن 20",
    "Category:17th-century Scottish non-fiction writers": "تصنيف:كتاب غير روائيين إسكتلنديون في القرن 17",
    "Category:18th-century Scottish non-fiction writers": "تصنيف:كتاب غير روائيين إسكتلنديون في القرن 18",
    "Category:19th-century Scottish non-fiction writers": "تصنيف:كتاب غير روائيين إسكتلنديون في القرن 19",
    "Category:20th-century Scottish non-fiction writers": "تصنيف:كتاب غير روائيين إسكتلنديون في القرن 20",
    "Category:19th-century Italian non-fiction writers": "تصنيف:كتاب غير روائيين إيطاليون في القرن 19",
    "Category:19th-century Brazilian non-fiction writers": "تصنيف:كتاب غير روائيين برازيليون في القرن 19",
    "Category:20th-century Brazilian non-fiction writers": "تصنيف:كتاب غير روائيين برازيليون في القرن 20",
    "Category:21st-century Brazilian non-fiction writers": "تصنيف:كتاب غير روائيين برازيليون في القرن 21",
    "Category:20th-century Portuguese non-fiction writers": "تصنيف:كتاب غير روائيين برتغاليون في القرن 20",
    "Category:21st-century Portuguese non-fiction writers": "تصنيف:كتاب غير روائيين برتغاليون في القرن 21",
    "Category:19th-century Belgian non-fiction writers": "تصنيف:كتاب غير روائيين بلجيكيون في القرن 19",
    "Category:20th-century Bangladeshi non-fiction writers": "تصنيف:كتاب غير روائيين بنغلاديشيون في القرن 20",
    "Category:21st-century Bangladeshi non-fiction writers": "تصنيف:كتاب غير روائيين بنغلاديشيون في القرن 21",
    "Category:19th-century Puerto Rican non-fiction writers": "تصنيف:كتاب غير روائيين بورتوريكيون في القرن 19",
    "Category:20th-century Puerto Rican non-fiction writers": "تصنيف:كتاب غير روائيين بورتوريكيون في القرن 20",
    "Category:21st-century Puerto Rican non-fiction writers": "تصنيف:كتاب غير روائيين بورتوريكيون في القرن 21",
    "Category:19th-century Czech non-fiction writers": "تصنيف:كتاب غير روائيين تشيكيون في القرن 19",
    "Category:20th-century Czech non-fiction writers": "تصنيف:كتاب غير روائيين تشيكيون في القرن 20",
    "Category:21st-century Czech non-fiction writers": "تصنيف:كتاب غير روائيين تشيكيون في القرن 21",
    "Category:18th-century Danish non-fiction writers": "تصنيف:كتاب غير روائيين دنماركيون في القرن 18",
    "Category:19th-century Danish non-fiction writers": "تصنيف:كتاب غير روائيين دنماركيون في القرن 19",
    "Category:19th-century Swedish non-fiction writers": "تصنيف:كتاب غير روائيين سويديون في القرن 19",
    "Category:21st-century Swedish non-fiction writers": "تصنيف:كتاب غير روائيين سويديون في القرن 21",
    "Category:20th-century Chinese non-fiction writers": "تصنيف:كتاب غير روائيين صينيون في القرن 20",
    "Category:21st-century Chinese non-fiction writers": "تصنيف:كتاب غير روائيين صينيون في القرن 21",
    "Category:20th-century Finnish non-fiction writers": "تصنيف:كتاب غير روائيين فنلنديون في القرن 20",
    "Category:21st-century South Korean non-fiction writers": "تصنيف:كتاب غير روائيين كوريون جنوبيون في القرن 21",
    "Category:21st-century Lithuanian non-fiction writers": "تصنيف:كتاب غير روائيين ليتوانيون في القرن 21",
    "Category:20th-century Egyptian non-fiction writers": "تصنيف:كتاب غير روائيين مصريون في القرن 20",
    "Category:21st-century Egyptian non-fiction writers": "تصنيف:كتاب غير روائيين مصريون في القرن 21",
    "Category:19th-century Mexican non-fiction writers": "تصنيف:كتاب غير روائيين مكسيكيون في القرن 19",
    "Category:20th-century Mexican non-fiction writers": "تصنيف:كتاب غير روائيين مكسيكيون في القرن 20",
    "Category:21st-century Mexican non-fiction writers": "تصنيف:كتاب غير روائيين مكسيكيون في القرن 21",
    "Category:21st-century Norwegian non-fiction writers": "تصنيف:كتاب غير روائيين نرويجيون في القرن 21",
    "Category:20th-century Austrian non-fiction writers": "تصنيف:كتاب غير روائيين نمساويون في القرن 20",
    "Category:21st-century Austrian non-fiction writers": "تصنيف:كتاب غير روائيين نمساويون في القرن 21",
    "Category:17th-century Dutch non-fiction writers": "تصنيف:كتاب غير روائيين هولنديون في القرن 17",
    "Category:18th-century Dutch non-fiction writers": "تصنيف:كتاب غير روائيين هولنديون في القرن 18",
    "Category:19th-century Dutch non-fiction writers": "تصنيف:كتاب غير روائيين هولنديون في القرن 19",
    "Category:20th-century Welsh non-fiction writers": "تصنيف:كتاب غير روائيين ويلزيون في القرن 20",
    "Category:21st-century Welsh non-fiction writers": "تصنيف:كتاب غير روائيين ويلزيون في القرن 21",
    "Category:20th-century Japanese non-fiction writers": "تصنيف:كتاب غير روائيين يابانيون في القرن 20",
    "Category:21st-century Japanese non-fiction writers": "تصنيف:كتاب غير روائيين يابانيون في القرن 21",
    "Category:19th-century Greek non-fiction writers": "تصنيف:كتاب غير روائيين يونانيون في القرن 19",
    "Category:20th-century Greek non-fiction writers": "تصنيف:كتاب غير روائيين يونانيون في القرن 20",
    "Category:21st-century Greek non-fiction writers": "تصنيف:كتاب غير روائيين يونانيون في القرن 21",
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
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_non_dump(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
