#
import pytest

from ArWikiCats import resolve_arabic_category_label

data = {
    "Category:Gymnastics organizations": "تصنيف:منظمات جمباز",
    "Category:Publications by format": "تصنيف:منشورات حسب التنسيق",
    "Category:Publications disestablished in 1946": "تصنيف:منشورات انحلت في 1946",
    "Category:Subfields by academic discipline": "تصنيف:حقول فرعية حسب التخصص الأكاديمي",
    "Category:Women's organizations based in Cuba": "تصنيف:منظمات نسائية مقرها في كوبا",
    "Category:Women's universities and colleges in India": "تصنيف:جامعات نسائية وكليات في الهند",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=list(data.keys()))
@pytest.mark.fast
def test_institutions(category, expected) -> None:
    label = resolve_arabic_category_label(category)
    assert label.strip() == expected
