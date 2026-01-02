#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

national_championships_data = {
    "dutch national track cycling championships": "تصنيف:بطولات سباق الدراجات على المضمار وطنية هولندية",
    "asian national weightlifting championships": "تصنيف:بطولات رفع أثقال وطنية آسيوية",
}

championships_data = {
    "asian weightlifting championships": "تصنيف:بطولة آسيا لرفع الأثقال",
    "asian wushu championships": "تصنيف:بطولة آسيا للووشو",
    "australian netball championships": "تصنيف:بطولة أستراليا لكرة الشبكة",
    "bulgarian athletics championships": "تصنيف:بطولة بلغاريا لألعاب القوى",
    "czech figure skating championships": "تصنيف:بطولة التشيك للتزلج الفني",
    "czechoslovak athletics championships": "تصنيف:بطولة تشيكوسلوفاكيا لألعاب القوى",
    "european cross country championships": "تصنيف:بطولة أوروبا للعدو الريفي",
    "european diving championships": "تصنيف:بطولة أوروبا للغطس",
    "european table tennis championships": "تصنيف:بطولة أوروبا لكرة الطاولة",
    "european taekwondo championships": "تصنيف:بطولة أوروبا للتايكوندو",
    "european wrestling championships": "تصنيف:بطولة أوروبا للمصارعة",
    "french athletics championships": "تصنيف:بطولة فرنسا لألعاب القوى",
    "lithuanian athletics championships": "تصنيف:بطولة ليتوانيا لألعاب القوى",
    "lithuanian swimming championships": "تصنيف:بطولة ليتوانيا للسباحة",
    "paraguayan athletics championships": "تصنيف:بطولة باراغواي لألعاب القوى",
    "slovak figure skating championships": "تصنيف:بطولة سلوفاكيا للتزلج الفني",
    "south american gymnastics championships": "تصنيف:بطولة أمريكا الجنوبية للجمباز",
    "turkish figure skating championships": "تصنيف:بطولة تركيا للتزلج الفني",
    "african judo championships": "تصنيف:بطولة إفريقيا للجودو",
    "african swimming championships": "تصنيف:بطولة إفريقيا للسباحة",
    "asian athletics championships": "تصنيف:بطولة آسيا لألعاب القوى",
    "asian swimming championships": "تصنيف:بطولة آسيا للسباحة",
    "asian wrestling championships": "تصنيف:بطولة آسيا للمصارعة",
    "canadian wheelchair curling championships": "تصنيف:بطولة كندا للكيرلنغ على الكراسي المتحركة",
    "european amateur boxing championships": "تصنيف:بطولة أوروبا للبوكسينغ للهواة",
    "european beach volleyball championships": "تصنيف:بطولة أوروبا لكرة الطائرة الشاطئية",
    "european fencing championships": "تصنيف:بطولة أوروبا لمبارزة سيف الشيش",
    "european judo championships": "تصنيف:بطولة أوروبا للجودو",
    "european karate championships": "تصنيف:بطولة أوروبا للكاراتيه",
    "european speed skating championships": "تصنيف:بطولة أوروبا لتزلج السريع",
    "south american swimming championships": "تصنيف:بطولة أمريكا الجنوبية للسباحة",
    "world karate championships": "تصنيف:بطولة العالم للكاراتيه",
}


@pytest.mark.parametrize(
    "category, expected", national_championships_data.items(), ids=national_championships_data.keys()
)
def test_national_championships_data(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("category, expected", championships_data.items(), ids=championships_data.keys())
def test_championships_data(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


to_test = [
    ("test_national_championships_data", national_championships_data),
    ("test_championships_data", championships_data),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    add_result = {x: v for x, v in data.items() if x in diff_result and "" == diff_result.get(x)}
    dump_diff(add_result, f"{name}_add")
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
