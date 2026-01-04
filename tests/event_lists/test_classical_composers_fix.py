#
import pytest
from load_one_data import dump_diff, one_dump_test, dump_same_and_not_same, dump_diff_text

from ArWikiCats import resolve_label_ar

test_to_fix_0 = {
    "Film score composers by nationality": "مؤلفو موسيقى أفلام حسب الجنسية",
    "Film score composers": "مؤلفو موسيقى تصويرية",
    "French film score composers": "مؤلفو موسيقى أفلام فرنسيون",
    "German film score composers": "مؤلفو موسيقى أفلام ألمان",
    "Indian film score composers": "مؤلفو موسيقى أفلام هنود",
    "Israeli film score composers": "مؤلفو موسيقى أفلام إسرائيليون",
    "Italian film score composers": "مؤلفو موسيقى أفلام إيطاليون",
    "Classical-period composers": "مؤلفو موسيقى في الفترة الكلاسيكية",
    "English film score composers": "مؤلفو موسيقى أفلام إنجليز",
    "Brazilian film score composers": "مؤلفو موسيقى أفلام برازيليون",
    "British film score composers": "مؤلفو موسيقى أفلام بريطانيون",
    "Canadian film score composers": "مؤلفو موسيقى أفلام كنديون",
    "Ballet composers": "مؤلفو موسيقى الباليه",
    "Australian film score composers": "مؤلفو موسيقى أفلام أستراليون",
    "Argentine film score composers": "مؤلفو موسيقى أفلام أرجنتينيون",
    "American film score composers": "مؤلفو موسيقى أفلام أمريكيون",
    "American male film score composers": "مؤلفو موسيقى أفلام أمريكيون ذكور",
    "Japanese film score composers": "مؤلفو موسيقى أفلام يابانيون",
    "Minimalist composers": "مؤلفون موسيقيون في الحركة المنيمالية",
    "Medieval composers": "مؤلفون موسيقيون من العصور الوسطى",
    "Male film score composers": "مؤلفو موسيقى أفلام",
    "Russian film score composers": "مؤلفو موسيقى أفلام روس",
    "South Korean film score composers": "مؤلفو موسيقى أفلام كوريون جنوبيون",
    "Turkish film score composers": "مؤلفو موسيقى أفلام أتراك",
}

test_to_fix_1 = {
    "19th-century classical composers": "مؤلفون موسيقيون في القرن ال19",
    "20th-century classical composers": "مؤلفون موسيقيون في القرن ال20",
    "21st-century classical composers": "مؤلفون موسيقيون في القرن 21",
    "African-American opera composers": "مؤلفو الأوبرا أفارقة أمريكيون",
    "American opera composers": "مؤلفو أوبرا أمريكيون",
    "Argentine opera composers": "مؤلفو أوبرا أرجنتينيون",
    "Armenian opera composers": "مؤلفو الأوبرا أرمن",
    "Australian opera composers": "مؤلفو أوبرا أستراليون",
    "Azerbaijani opera composers": "مؤلفو أوبرا أذربيجانيون",
    "Belgian opera composers": "مؤلفو أوبرا بلجيكيون",
    "Brazilian opera composers": "مؤلفو أوبرا برازيليون",
    "British opera composers": "مؤلفو أوبرا بريطانيون",
    "Canadian opera composers": "مؤلفو أوبرا كنديون",
    "Chilean opera composers": "مؤلفو أوبرا تشيليون",
    "Chinese opera composers": "مؤلفو أوبرا صينيون",
    "Classical composers": "مؤلفو موسيقى كلاسيكية",
    "Classical composers by nationality": "مؤلفو موسيقى كلاسيكية حسب الجنسية",
    "Cuban opera composers": "مؤلفو أوبرا كوبيون",
    "Czech opera composers": "مؤلفو أوبرا تشيكيون",
    "Danish classical composers": "مؤلفو موسيقى كلاسيكية دنماركيون",
    "Danish opera composers": "مؤلفو أوبرا دنماركيون",
    "Dutch opera composers": "مؤلفو الأوبرا هولنديون",
    "English opera composers": "مؤلفو الأوبرا إنجليز",
    "Estonian opera composers": "مؤلفو الأوبرا إستونيون",
    "Finnish opera composers": "مؤلفو الأوبرا فنلنديون",
    "French opera composers": "مؤلفو أوبرا فرنسيون",
    "German composers": "مؤلفون موسيقيون ألمان",
    "Greek opera composers": "مؤلفو الأوبرا يونانيون",
    "Guatemalan opera composers": "مؤلفو الأوبرا غواتيماليون",
    "Hungarian opera composers": "مؤلفو أوبرا مجريون",
    "Irish opera composers": "مؤلفو أوبرا أيرلنديون",
    "Israeli opera composers": "مؤلفو الأوبرا إسرائيليون",
    "Italian opera composers": "مؤلفو الأوبرا إيطاليون",

    "Japanese opera composers": "مؤلفو أوبرا يابانيون",
    "Jewish opera composers": "مؤلفو الأوبرا يهود",
    "Lebanese opera composers": "مؤلفو الأوبرا لبنانيون",
    "Male opera composers": "مؤلفو أوبرات",
    "Maltese opera composers": "مؤلفو الأوبرا مالطيون",
    "Mexican opera composers": "مؤلفو الأوبرا مكسيكيون",
    "New-age composers": "مؤلفو موسيقى العصر الجديد",
    "New Zealand opera composers": "مؤلفو الأوبرا نيوزيلنديون",
    "Norwegian opera composers": "مؤلفو الأوبرا نرويجيون",
    "Opera composers": "مؤلفو الأوبرا",
    "Opera composers by nationality": "مؤلفو الأوبرا حسب الجنسية",
    "Opera composers from Georgia (country)": "مؤلفو الأوبرا من جورجيا",
    "Opera composers from Northern Ireland": "مؤلفو الأوبرا من أيرلندا الشمالية",
    "Peruvian opera composers": "مؤلفو الأوبرا بيرويون",
    "Polish opera composers": "مؤلفو أوبرا بولنديون",
    "Portuguese opera composers": "مؤلفو الأوبرا برتغاليون",
    "Romanian opera composers": "مؤلفو أوبرا رومانيون",
    "Romantic composers": "مؤلفون موسيقيون من العصر الرومانسي",
    "Russian opera composers": "مؤلفو أوبرا روس",
    "Scottish opera composers": "مؤلفو الأوبرا إسكتلنديون",
    "Serbian opera composers": "مؤلفو أوبرا صرب",
    "Slovak opera composers": "مؤلفو الأوبرا سلوفاكيون",
    "Soviet opera composers": "مؤلفو أوبرا سوفيت",
    "Spanish opera composers": "مؤلفو أوبرا إسبان",
    "Swedish opera composers": "مؤلفو الأوبرا سويديون",
    "Swiss opera composers": "مؤلفو أوبرا سويسريون",
    "Turkish opera composers": "مؤلفو الأوبرا أتراك",
    "Venezuelan opera composers": "مؤلفو الأوبرا فنزويليون",
    "Women opera composers": "مؤلفات الأوبرا",
}

to_test = [
    # ("test_classical_composers_to_fix1", test_to_fix_0),
    ("test_classical_composers_to_fix2", test_to_fix_1),
]


@pytest.mark.parametrize("category, expected", test_to_fix_1.items(), ids=test_to_fix_1.keys())
@pytest.mark.fast
def test_classical_composers_to_fix1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    dump_diff_text(expected, diff_result, name)
    # dump_same_and_not_same(data, diff_result, name, True)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
