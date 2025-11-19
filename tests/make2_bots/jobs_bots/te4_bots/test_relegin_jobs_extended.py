""" """

import pytest

from src.make2_bots.jobs_bots.jobs_mainbot import create_country_lab
from src.make2_bots.jobs_bots.te4_bots.relegin_jobs import try_relegins_jobs_with_suffix
from src.translations import RELIGIOUS_KEYS_PP

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


@pytest.mark.parametrize(
    "input,expected",
    expatriates_data.items(),
    ids=[x for x in expatriates_data],
)
@pytest.mark.slow
def test_with_suffix_expatriates(input, expected):
    result = try_relegins_jobs_with_suffix(input)
    assert result == expected, f"{expected=}, {result=}, {input=}"
