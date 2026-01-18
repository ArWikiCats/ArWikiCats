""" """

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers.relegin_jobs_new import new_religions_jobs_with_suffix, womens_result
from ArWikiCats.translations import RELIGIOUS_KEYS_PP

# new dict with only 20 items from RELIGIOUS_KEYS_PP
RELIGIOUS_KEYS_20 = {k: RELIGIOUS_KEYS_PP[k] for k in list(RELIGIOUS_KEYS_PP.keys())[:20]}


@pytest.mark.parametrize("key,data", RELIGIOUS_KEYS_20.items(), ids=RELIGIOUS_KEYS_20.keys())
def test_with_womens(key: str, data: dict[str, str]) -> None:
    input_text = f"female {key}"
    expected = data["females"]

    result = new_religions_jobs_with_suffix(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"


@pytest.mark.parametrize("key,data", RELIGIOUS_KEYS_20.items(), ids=RELIGIOUS_KEYS_20.keys())
def test_with_mens(key: str, data: dict[str, str]) -> None:
    expected_mens = data["males"]
    result_mens = new_religions_jobs_with_suffix(key)
    assert result_mens == expected_mens, f"{expected_mens=}, {result_mens=}, {key=}"


@pytest.mark.parametrize("key,data", RELIGIOUS_KEYS_20.items(), ids=RELIGIOUS_KEYS_20.keys())
def test_with_male(key: str, data: dict[str, str]) -> None:
    input_text = f"male {key}"
    expected = f"{data['males']} ذكور"
    result_mens = new_religions_jobs_with_suffix(input_text)
    assert result_mens == expected, f"{expected=}, {result_mens=}, {key=}"


test_data = {
    "anglican": "أنجليكيون",
    "anglicans": "أنجليكيون",
    "bahá'ís": "بهائيون",
    "baháís": "بهائيون",
    "buddhist": "بوذيون",
    "christian": "مسيحيون",
    "christians": "مسيحيون",
    "coptic": "أقباط",
    "episcopalians": "أسقفيون",
    "female anglican": "أنجليكيات",
    "female anglicans": "أنجليكيات",
    "female bahá'ís": "بهائيات",
    "female baháís": "بهائيات",
    "female buddhist": "بوذيات",
    "womens christian": "مسيحيات",
    "womens christians": "مسيحيات",
    "womens coptic": "قبطيات",
    "womens episcopalians": "أسقفيات",
    "womens hindu": "هندوسيات",
    "female hindus": "هندوسيات",
    "female islamic": "إسلاميات",
    "female jewish": "يهوديات",
    "female jews": "يهوديات",
    "female methodist": "ميثوديات لاهوتيات",
    "female muslim": "مسلمات",
    "women's nazi": "نازيات",
    "women's protestant": "بروتستانتيات",
    "women's shi'a muslims": "مسلمات شيعيات",
    "female sufis": "صوفيات",
    "female yazidis": "يزيديات",
    "female zaydi": "زيديات",
    "female zaydis": "زيديات",
    "hindu": "هندوس",
    "hindus": "هندوس",
    "islamic": "إسلاميون",
    "jewish": "يهود",
    "jews": "يهود",
    "methodist": "ميثوديون لاهوتيون",
    "muslim": "مسلمون",
    "nazi": "نازيون",
    "protestant": "بروتستانتيون",
    "shi'a muslims": "مسلمون شيعة",
    "sufis": "صوفيون",
    "yazidis": "يزيديون",
    "zaydi": "زيود",
    "zaydis": "زيود",
}


test_data_2 = {
    "actors Episcopalians": "ممثلون أسقفيون",
    "actors Sunni Muslims": "ممثلون مسلمون سنة",
    "hindu philosophers and theologians": "فلاسفة ولاهوتيون هندوس",
    "hindu philosophers": "فلاسفة هندوس",
}


test_female_2 = {
    # "Muslims actresses": "ممثلات مسلمات",
    "muslims female singers": "مغنيات مسلمات",
    "female muslims singers": "مغنيات مسلمات",
    "female singers muslims": "مغنيات مسلمات",
}


@pytest.mark.parametrize("input_text,expected", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_new_religions_jobs_with_suffix(input_text: str, expected: str) -> None:
    result = new_religions_jobs_with_suffix(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"

    input2 = f"people {input_text}"
    result2 = new_religions_jobs_with_suffix(input2)
    assert result2 == expected, f"{expected=}, {result2=}, {input2=}"


@pytest.mark.parametrize("input_text,expected", test_data_2.items(), ids=test_data_2.keys())
@pytest.mark.fast
def test_religions_with_jobs(input_text: str, expected: str) -> None:
    result = new_religions_jobs_with_suffix(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"


@pytest.mark.parametrize("input_text,expected", test_female_2.items(), ids=test_female_2.keys())
@pytest.mark.fast
def test_females(input_text: str, expected: str) -> None:
    result = womens_result(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"
