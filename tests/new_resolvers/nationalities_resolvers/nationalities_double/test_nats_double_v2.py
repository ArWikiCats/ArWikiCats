"""

tests related to nationalities_double_v2 resolver

"""

import pytest
from load_one_data import dump_diff, one_dump_test, dump_same_and_not_same

from ArWikiCats import resolve_label_ar

male_tests = {
    "Category:Argentine people of French-Jewish descent": "تصنيف:أرجنتينيون من أصل فرنسي يهودي",
    "Category:French people of Polish-Jewish descent": "تصنيف:فرنسيون من أصل بولندي يهودي",
    "Category:French people of Syrian-Jewish descent": "تصنيف:فرنسيون من أصل سوري يهودي",
    "Category:German people of Lithuanian-Jewish descent": "تصنيف:ألمان من أصل ليتواني يهودي",
    "Category:Indian people of Iraqi-Jewish descent": "تصنيف:هنود من أصل عراقي يهودي",
    "Category:People of Argentine-Jewish descent": "تصنيف:أشخاص من أصل أرجنتيني يهودي",
    "Category:Russian people of Austrian-Jewish descent": "تصنيف:روس من أصل نمساوي يهودي",
    "Category:Colombian people of Spanish-Jewish descent": "تصنيف:كولومبيون من أصل إسباني يهودي",
    "Category:Ethnic groups in Dutch Caribbean": "تصنيف:مجموعات عرقية في كاريبيون هولنديون",
    "Category:Football competitions in Dutch Caribbean": "تصنيف:منافسات كرة قدم في كاريبيون هولنديون",
    "Category:Gender in Dutch Caribbean": "تصنيف:الجنس في كاريبيون هولنديون",
    "Category:Lithuanian-Jewish culture in United States by state": "تصنيف:ثقافة ليتوانية يهودية في الولايات المتحدة حسب الولاية",
    "Category:Men from Dutch Caribbean": "تصنيف:رجال من كاريبيون هولنديون",
    "Category:Men in Dutch Caribbean": "تصنيف:رجال في كاريبيون هولنديون",
    "Category:Peruvian people of Hungarian-Jewish descent": "تصنيف:بيرويون من أصل مجري يهودي",
    "Category:Sports competitions in Dutch Caribbean": "تصنيف:منافسات رياضية في كاريبيون هولنديون",
    "Category:Women from Dutch Caribbean": "تصنيف:نساء من كاريبيون هولنديون",
    "Category:Women in Dutch Caribbean": "تصنيف:المرأة في كاريبيون هولنديون",
    "Category:Romanian people of Hungarian-Jewish descent": "تصنيف:رومان من أصل مجري يهودي",
    "Category:Churches in Dutch Caribbean": "تصنيف:كنائس في كاريبيون هولنديون",
    "Category:Populated places in Dutch Caribbean": "تصنيف:أماكن مأهولة في كاريبيون هولنديون"
}


@pytest.mark.parametrize("category, expected_key", male_tests.items(), ids=male_tests.keys())
@pytest.mark.fast
def test_male_tests(category: str, expected_key: str) -> None:
    label2 = resolve_label_ar(category)
    assert label2 == expected_key


to_test = [
    ("test_male_tests", male_tests, resolve_label_ar),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_non_dump(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
