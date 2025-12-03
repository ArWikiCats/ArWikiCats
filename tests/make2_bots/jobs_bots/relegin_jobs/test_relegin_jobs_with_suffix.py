""" """

import pytest

from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.jobs_bots.relegin_jobs_new import new_relegins_jobs_with_suffix
from ArWikiCats.make_bots.jobs_bots.jobs_mainbot import create_country_lab
from ArWikiCats.make_bots.jobs_bots.relegin_jobs import try_relegins_jobs_with_suffix
from ArWikiCats.translations import RELIGIOUS_KEYS_PP

# new dict with only 10 items from RELIGIOUS_KEYS_PP
RELIGIOUS_KEYS_10 = {k: RELIGIOUS_KEYS_PP[k] for k in list(RELIGIOUS_KEYS_PP.keys())[:10]}

jobs_mens_data = {
    "scholars of islam": "باحثون عن الإسلام",
    "women's rights activists": "ناشطون في حقوق المرأة",
    "convicted-of-murder": "أدينوا بالقتل",
    "classical europop cheerleaders": "قادة تشجيع يوروبوب كلاسيكيون",
    "classical europop composers": "ملحنو يوروبوب كلاسيكيون",
    "abidat rma pianists": "عازفو بيانو عبيدات الرما",
    "abidat rma record producers": "منتجو تسجيلات عبيدات الرما",
    "historical objectivists": "موضوعيون تاريخيون",
    "historical opera authors": "مؤلفو أوبرا تاريخيون",
    "men's sailing (sport) power forwards": "مهاجمون أقوياء الجسم رياضة إبحار رجالية",
    "men's sailing (sport) quarterbacks": "أظهرة رباعيون رياضة إبحار رجالية",
    "men's sailing (sport) racing centers": "لاعبو وسط سباق رياضة إبحار رجالية",
    "ski-orienteering quarterbacks": "أظهرة رباعيون سباق تزلج موجه",
    "abidat rma saxophonists": "عازفو سكسفون عبيدات الرما",
    "abidat rma singer-songwriters": "مغنون وكتاب أغاني عبيدات الرما",
    "expatriates": "مغتربون",
}

expatriates_data = {}
for key, data in RELIGIOUS_KEYS_10.items():
    mens_label = data.get("mens", "")
    if mens_label:
        for job_key, job_label in jobs_mens_data.items():
            label = create_country_lab(job_label, mens_label, job_key)
            expatriates_data[f"{key} {job_key}"] = label


# new dict with only 20 items from RELIGIOUS_KEYS_PP
RELIGIOUS_KEYS_20 = {k: RELIGIOUS_KEYS_PP[k] for k in list(RELIGIOUS_KEYS_PP.keys())[:20]}


@pytest.mark.parametrize(
    "key,data",
    RELIGIOUS_KEYS_20.items(),
    ids=[x for x in RELIGIOUS_KEYS_20],
)
def test_with_suffix(key: str, data: dict[str, str]) -> None:
    input2 = f"{key} historical house music bloggers"
    expected2 = f"مدونو هاوس تاريخيون {data['mens']}"

    result2 = try_relegins_jobs_with_suffix(input2)
    assert result2 == expected2, f"{expected2=}, {result2=}, {input2=}"


@pytest.mark.parametrize(
    "input_text,expected",
    expatriates_data.items(),
    ids=[x for x in expatriates_data],
)
@pytest.mark.slow
def test_with_suffix_expatriates(input_text: str, expected: str) -> None:
    result = try_relegins_jobs_with_suffix(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"


def test_one() -> None:
    # {"cate": "bahá'ís classical europop composers", "country_prefix": "bahá'ís", "category_suffix": "classical europop composers", "mens": "بهائيون", "womens": "بهائيات", "country_lab": "ملحنو يوروبوب كلاسيكيون بهائيون"}
    input_text = "bahá'ís classical europop composers"
    expected = "ملحنو يوروبوب كلاسيكيون بهائيون"

    result = try_relegins_jobs_with_suffix(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"


test_data_2 = {
    "anglican expatriates": "أنجليكيون مغتربون",
    "buddhist expatriates": "بوذيون مغتربون",
    "buddhist scholars of islam": "بوذيون باحثون عن الإسلام",
    "christian convicted-of-murder": "مسيحيون أدينوا بالقتل",
    "christian expatriates": "مسيحيون مغتربون",
    "nazi expatriates": "نازيون مغتربون",
    "nazi bloggers": "مدونون نازيون",
    "nazi scholars of islam": "نازيون باحثون عن الإسلام"
}


@pytest.mark.parametrize("input_text,expected", test_data_2.items(), ids=test_data_2.keys())
def test_get_suffix_prefix(input_text: str, expected: tuple[str, str]) -> None:
    result = try_relegins_jobs_with_suffix(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"


TEMPORAL_CASES = [
    ("test_get_suffix_prefix", test_data_2, try_relegins_jobs_with_suffix),
    ("new_relegins_jobs_with_suffix", test_data_2, new_relegins_jobs_with_suffix),
]


@pytest.mark.parametrize("name,data,callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
