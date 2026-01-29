#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

national_championships_data = {
    "dutch national track cycling championships": "بطولات سباق الدراجات على المضمار وطنية هولندية",
    "asian national weightlifting championships": "بطولات رفع أثقال وطنية آسيوية",
}

championships_data = {
    "asian weightlifting championships": "بطولة آسيا لرفع الأثقال",
    "asian wushu championships": "بطولة آسيا للووشو",
    "australian netball championships": "بطولة أستراليا لكرة الشبكة",
    "bulgarian athletics championships": "بطولة بلغاريا لألعاب القوى",
    "czech figure skating championships": "بطولة التشيك للتزلج الفني",
    "czechoslovak athletics championships": "بطولة تشيكوسلوفاكيا لألعاب القوى",
    "european cross country championships": "بطولة أوروبا للعدو الريفي",
    "european diving championships": "بطولة أوروبا للغطس",
    "european table tennis championships": "بطولة أوروبا لكرة الطاولة",
    "european taekwondo championships": "بطولة أوروبا للتايكوندو",
    "european wrestling championships": "بطولة أوروبا للمصارعة",
    "french athletics championships": "بطولة فرنسا لألعاب القوى",
    "lithuanian athletics championships": "بطولة ليتوانيا لألعاب القوى",
    "lithuanian swimming championships": "بطولة ليتوانيا للسباحة",
    "paraguayan athletics championships": "بطولة باراغواي لألعاب القوى",
    "slovak figure skating championships": "بطولة سلوفاكيا للتزلج الفني",
    "south american gymnastics championships": "بطولة أمريكا الجنوبية للجمباز",
    "turkish figure skating championships": "بطولة تركيا للتزلج الفني",
    "african judo championships": "بطولة إفريقيا للجودو",
    "african swimming championships": "بطولة إفريقيا للسباحة",
    "asian athletics championships": "بطولة آسيا لألعاب القوى",
    "asian swimming championships": "بطولة آسيا للسباحة",
    "asian wrestling championships": "بطولة آسيا للمصارعة",
    "canadian wheelchair curling championships": "بطولة كندا للكيرلنغ على الكراسي المتحركة",
    "european amateur boxing championships": "بطولة أوروبا للبوكسينغ للهواة",
    "european beach volleyball championships": "بطولة أوروبا لكرة الطائرة الشاطئية",
    "european fencing championships": "بطولة أوروبا لمبارزة سيف الشيش",
    "european judo championships": "بطولة أوروبا للجودو",
    "european karate championships": "بطولة أوروبا للكاراتيه",
    "european speed skating championships": "بطولة أوروبا لتزلج السريع",
    "south american swimming championships": "بطولة أمريكا الجنوبية للسباحة",
    "world karate championships": "بطولة العالم للكاراتيه",
}


@pytest.mark.parametrize(
    "category, expected", national_championships_data.items(), ids=national_championships_data.keys()
)
def test_national_championships_data(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


@pytest.mark.parametrize("category, expected", championships_data.items(), ids=championships_data.keys())
def test_championships_data(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


to_test = [
    ("test_national_championships_data", national_championships_data),
    ("test_championships_data", championships_data),
]


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
