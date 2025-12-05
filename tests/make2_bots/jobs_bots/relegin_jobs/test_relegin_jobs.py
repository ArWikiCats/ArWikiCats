"""
"""

import pytest
from ArWikiCats.translations import RELIGIOUS_KEYS_PP
from ArWikiCats.make_bots.jobs_bots.relegin_jobs_new import new_relegins_jobs_with_suffix

# new dict with only 20 items from RELIGIOUS_KEYS_PP
RELIGIOUS_KEYS_20 = {k: RELIGIOUS_KEYS_PP[k] for k in list(RELIGIOUS_KEYS_PP.keys())[:20]}


@pytest.mark.parametrize("key,data", RELIGIOUS_KEYS_20.items(), ids=[x for x in RELIGIOUS_KEYS_20])
def test_with_womens(key: str, data: dict[str, str]) -> None:
    input_text = f"female {key}"
    expected = data["females"]

    result = new_relegins_jobs_with_suffix(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"


@pytest.mark.parametrize("key,data", RELIGIOUS_KEYS_20.items(), ids=[x for x in RELIGIOUS_KEYS_20])
def test_with_mens(key: str, data: dict[str, str]) -> None:
    expected_mens = data["mens"]
    result_mens = new_relegins_jobs_with_suffix(key)
    assert result_mens == expected_mens, f"{expected_mens=}, {result_mens=}, {key=}"


@pytest.mark.parametrize("key,data", RELIGIOUS_KEYS_20.items(), ids=[x for x in RELIGIOUS_KEYS_20])
def test_with_male(key: str, data: dict[str, str]) -> None:
    input_text = f"male {key}"
    expected = f"{data['mens']} ذكور"
    result_mens = new_relegins_jobs_with_suffix(input_text)
    assert result_mens == expected, f"{expected=}, {result_mens=}, {key=}"


test_data = {
    "anglican": "أنجليكيون",
    "anglicans": "أنجليكيون",
    "bahá'ís": "بهائيون",
    "buddhist": "بوذيون",
    "christian": "مسيحيون",
    "christians": "مسيحيون",
    "coptic": "أقباط",
    "episcopalians": "أسقفيون",
    "female anglican": "أنجليكيات",
    "female anglicans": "أنجليكيات",
    "female bahá'ís": "بهائيات",
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


@pytest.mark.parametrize("input_text,expected", test_data.items(), ids=test_data.keys())
def test_new_relegins_jobs_with_suffix(input_text: str, expected: str) -> None:
    result = new_relegins_jobs_with_suffix(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"

    input2 = f"people {input_text}"
    result2 = new_relegins_jobs_with_suffix(input2)
    assert result2 == expected, f"{expected=}, {result2=}, {input2=}"
