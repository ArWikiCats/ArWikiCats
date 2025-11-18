"""
{"cate": "shi'a muslims expatriates", "country_prefix": "shi'a muslims", "category_suffix": "expatriates", "mens": "مسلمون شيعة", "womens": "مسلمات شيعيات", "country_lab": "مسلمون شيعة مغتربون"}

"""
import pytest

from src.make2_bots.jobs_bots.te4_bots.relegin_jobs import relegins_jobs, try_relegins_jobs_with_suffix
from src.translations import RELIGIOUS_KEYS_PP

# new dict with only 20 items from RELIGIOUS_KEYS_PP
RELIGIOUS_KEYS_20 = {k: RELIGIOUS_KEYS_PP[k] for k in list(RELIGIOUS_KEYS_PP.keys())[:20]}

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

expatriates_data = {
    f"{key} expatriates": f"{data['mens']} مغتربون"
    for key, data in RELIGIOUS_KEYS_20.items()
    if data.get("mens")
}
for key, data in RELIGIOUS_KEYS_20.items():
    mens_label = data.get("mens", "")
    if mens_label:
        for job_key, job_label in jobs_mens_data.items():
            expatriates_data[f"{key} {job_key}"] = f"{job_label} {mens_label}"


@pytest.mark.parametrize(
    "input,expected",
    expatriates_data.items(),
    ids=[x for x in expatriates_data],
)
def _test_with_suffix_expatriates(input, expected):
    result = try_relegins_jobs_with_suffix(input)
    assert result == expected, f"{expected=}, {result=}, {input=}"


@pytest.mark.parametrize(
    "key,data",
    RELIGIOUS_KEYS_20.items(),
    ids=[x for x in RELIGIOUS_KEYS_20],
)
def test_with_suffix(key, data):
    input2 = f"{key} historical house music bloggers"
    expected2 = f"مدونو هاوس تاريخيون {data['mens']}"

    result2 = try_relegins_jobs_with_suffix(input2)
    assert result2 == expected2, f"{expected2=}, {result2=}, {input2=}"


@pytest.mark.parametrize(
    "key,data",
    RELIGIOUS_KEYS_20.items(),
    ids=[x for x in RELIGIOUS_KEYS_20],
)
def test_no_suffix_female(key, data):
    input = f"female {key}"
    expected = data['womens']

    result = relegins_jobs(input)
    assert result == expected, f"{expected=}, {result=}, {input=}"

    expected_mens = data['mens']
    result_mens = relegins_jobs(key)
    assert result_mens == expected_mens, f"{expected_mens=}, {result_mens=}, {key=}"


data = [
    ("sufis", "صوفيون"),
    ("female sufis", "صوفيات"),
    ("shi'a muslims", "مسلمون شيعة"),
    ("female shi'a muslims", "مسلمات شيعيات"),
]


@pytest.mark.parametrize(
    "input,expected",
    data,
    ids=[x[0] for x in data],
)
def test_no_suffix(input, expected):
    result = relegins_jobs(input)
    assert result == expected, f"{expected=}, {result=}, {input=}"

    input2 = f"people {input}"
    result2 = relegins_jobs(input)
    assert result2 == expected, f"{expected=}, {result2=}, {input2=}"
