#
from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset, dump_diff

data = {
    "Category:Gymnastics organizations": "تصنيف:منظمات جمباز",
    "Category:Publications by format": "تصنيف:منشورات حسب التنسيق",
    "Category:Publications disestablished in 1946": "تصنيف:منشورات انحلت في 1946",
    "Category:Subfields by academic discipline": "تصنيف:حقول فرعية حسب التخصص الأكاديمي",
    "Category:Women's organizations based in Cuba": "تصنيف:منظمات نسائية مقرها في كوبا",
    "Category:Women's universities and colleges in India": "تصنيف:جامعات نسائية وكليات في الهند"
}


def test_institutions():
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_institutions")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
