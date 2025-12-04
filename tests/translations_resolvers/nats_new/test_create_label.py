import pytest

from ArWikiCats.translations_resolvers.nats_new import nats_new_create_label, create_nat_label

data = {
    "british softball championshipszz": "بطولة المملكة المتحدة للكرة اللينة",
    "ladies british softball tour": "بطولة المملكة المتحدة للكرة اللينة للسيدات",
    "british football tour": "بطولة المملكة المتحدة لكرة القدم",
    "Yemeni football championships": "بطولة اليمن لكرة القدم",
    "german figure skating championships": "بطولة ألمانيا للتزلج الفني",
    "british figure skating championships": "بطولة المملكة المتحدة للتزلج الفني",
    "dominican republic national sports teams ": "منتخبات للرياضة وطنية جمهورية الدومينيكان",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_create_label(key: str, expected: str) -> None:
    template_label = nats_new_create_label(key)
    assert template_label != ""
    assert template_label == expected


data2 = {
    "yemeni {sport_en} championships": "بطولة اليمن {sport_ar}",
}


@pytest.mark.parametrize("key,expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_create_nat_label(key: str, expected: str) -> None:
    template_label = create_nat_label(key)
    assert template_label != ""
    assert template_label == expected
