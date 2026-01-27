#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

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
    "19th-century classical composers": "ملحنون كلاسيكيون في القرن 19",
    "20th-century classical composers": "ملحنون كلاسيكيون في القرن 20",
    "21st-century classical composers": "ملحنون كلاسيكيون في القرن 21",
    "African-American opera composers": "ملحنو أوبرا أمريكيون أفارقة",
    "American opera composers": "ملحنو أوبرا أمريكيون",
    "Argentine opera composers": "ملحنو أوبرا أرجنتينيون",
    "Armenian opera composers": "ملحنو أوبرا أرمن",
    "Australian opera composers": "ملحنو أوبرا أستراليون",
    "Azerbaijani opera composers": "ملحنو أوبرا أذربيجانيون",
    "Belgian opera composers": "ملحنو أوبرا بلجيكيون",
    "Brazilian opera composers": "ملحنو أوبرا برازيليون",
    "British opera composers": "ملحنو أوبرا بريطانيون",
    "Canadian opera composers": "ملحنو أوبرا كنديون",
    "Chilean opera composers": "ملحنو أوبرا تشيليون",
    "Chinese opera composers": "ملحنو أوبرا صينيون",
    "Classical composers": "ملحنون كلاسيكيون",
    "Classical composers by nationality": "ملحنون كلاسيكيون حسب الجنسية",
    "Cuban opera composers": "ملحنو أوبرا كوبيون",
    "Czech opera composers": "ملحنو أوبرا تشيكيون",
    "Danish classical composers": "ملحنون كلاسيكيون دنماركيون",
    "Danish opera composers": "ملحنو أوبرا دنماركيون",
    "Dutch opera composers": "ملحنو أوبرا هولنديون",
    "English opera composers": "ملحنو أوبرا إنجليز",
    "Estonian opera composers": "ملحنو أوبرا إستونيون",
    "Finnish opera composers": "ملحنو أوبرا فنلنديون",
    "French opera composers": "ملحنو أوبرا فرنسيون",
    "German composers": "ملحنون ألمان",
    "Greek opera composers": "ملحنو أوبرا يونانيون",
    "Guatemalan opera composers": "ملحنو أوبرا غواتيماليون",
    "Hungarian opera composers": "ملحنو أوبرا مجريون",
    "Irish opera composers": "ملحنو أوبرا أيرلنديون",
    "Israeli opera composers": "ملحنو أوبرا إسرائيليون",
    "Italian opera composers": "ملحنو أوبرا إيطاليون",
    "Japanese opera composers": "ملحنو أوبرا يابانيون",
    "Jewish opera composers": "ملحنو أوبرا يهود",
    "Lebanese opera composers": "ملحنو أوبرا لبنانيون",
    "Male opera composers": "ملحنو أوبرا ذكور",
    "Maltese opera composers": "ملحنو أوبرا مالطيون",
    "Mexican opera composers": "ملحنو أوبرا مكسيكيون",
    "New-age composers": "ملحنو العصر الحديث",
    "New Zealand opera composers": "ملحنو أوبرا نيوزيلنديون",
    "Norwegian opera composers": "ملحنو أوبرا نرويجيون",
    "Opera composers": "ملحنو أوبرا",
    "Opera composers by nationality": "ملحنو أوبرا حسب الجنسية",
    "Opera composers from Georgia (country)": "ملحنو أوبرا من جورجيا",
    "Opera composers from Northern Ireland": "ملحنو أوبرا من أيرلندا الشمالية",
    "Peruvian opera composers": "ملحنو أوبرا بيرويون",
    "Polish opera composers": "ملحنو أوبرا بولنديون",
    "Portuguese opera composers": "ملحنو أوبرا برتغاليون",
    "Romanian opera composers": "ملحنو أوبرا رومان",
    "Russian opera composers": "ملحنو أوبرا روس",
    "Scottish opera composers": "ملحنو أوبرا إسكتلنديون",
    "Serbian opera composers": "ملحنو أوبرا صرب",
    "Slovak opera composers": "ملحنو أوبرا سلوفاكيون",
    "Soviet opera composers": "ملحنو أوبرا سوفيت",
    "Spanish opera composers": "ملحنو أوبرا إسبان",
    "Swedish opera composers": "ملحنو أوبرا سويديون",
    "Swiss opera composers": "ملحنو أوبرا سويسريون",
    "Turkish opera composers": "ملحنو أوبرا أتراك",
    "Venezuelan opera composers": "ملحنو أوبرا فنزويليون",
    "Women opera composers": "ملحنات أوبرا",
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


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
