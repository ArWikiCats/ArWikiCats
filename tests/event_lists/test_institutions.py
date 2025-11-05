#
from src import new_func_lab

data = {
    "Category:Gymnastics organizations": "تصنيف:منظمات جمباز",
    "Category:Publications by format": "تصنيف:منشورات حسب التنسيق",
    "Category:Publications disestablished in 1946": "تصنيف:منشورات انحلت في 1946",
    "Category:Subfields by academic discipline": "تصنيف:حقول فرعية حسب التخصص الأكاديمي",
    "Category:Women's organizations based in Cuba": "تصنيف:منظمات نسائية مقرها في كوبا",
    "Category:Women's universities and colleges in India": "تصنيف:جامعات نسائية وكليات في الهند"
}


def ye_test_one_dataset(dataset):
    print(f"len of dataset: {len(dataset)}")
    org = {}
    diff = {}
    data = {x: v for x, v in dataset.items() if v}
    for cat, ar in data.items():
        result = new_func_lab(cat)
        if result == ar:
            assert result == ar
        else:
            org[cat] = ar
            diff[cat] = result

    assert org == diff
