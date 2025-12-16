#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data0 = {
}

data_1 = {
    "Category:Zimbabwean film posters": "",
    "Category:1890s French film templates": "",
    "Category:Asian Film Awards ceremonies": "",
    "Category:Canadian women film score composers": ""
}

data_2 = {
    "Category:Asian Film Award winners": "تصنيف:فائزون بجائزة الأفلام الآسيوية",
    "Category:Zimbabwean film people": "تصنيف:أعلام أفلام زيمبابويون",
    "Category:Zimbabwean film actors": "تصنيف:ممثلو أفلام زيمبابويون",
    "Category:Zimbabwean film actresses": "تصنيف:ممثلات أفلام زيمبابويات",
    "Category:Zimbabwean film directors": "تصنيف:مخرجو أفلام زيمبابويون",
    "Category:Zimbabwean filmmakers": "تصنيف:صانعو أفلام زيمبابويون",
    "Category:Zimbabwean male film actors": "تصنيف:ممثلو أفلام ذكور زيمبابويون",
    "Category:Zimbabwean women film directors": "تصنيف:مخرجات أفلام زيمبابويات",
    "Category:Zombie film series": "تصنيف:سلاسل أفلام زومبي",
    "Category:Zombie film series navigational boxes": "تصنيف:صناديق تصفح سلاسل أفلام زومبي",
    "Category:1880s in film by country": "تصنيف:أفلام في عقد 1880 حسب البلد",
    "Category:Asian film awards": "تصنيف:جوائز الأفلام الآسيوية",
    "Category:Asian Film Awards": "تصنيف:جوائز الأفلام الآسيوية",
    "Category:Asian Film Awards navigational boxes": "تصنيف:صناديق تصفح جوائز الأفلام الآسيوية",
    "Category:Canadian women film critics": "تصنيف:ناقدات أفلام كنديات",
    "Category:Canadian women film directors": "تصنيف:مخرجات أفلام كنديات",
    "Category:Canadian women film editors": "تصنيف:محررات أفلام كنديات",
    "Category:Canadian women film producers": "تصنيف:منتجات أفلام كنديات",
}

to_test = [
    ("test_film_keys_1", data_1),
    ("test_film_keys_2", data_2),
]


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_film_keys_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:

    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
