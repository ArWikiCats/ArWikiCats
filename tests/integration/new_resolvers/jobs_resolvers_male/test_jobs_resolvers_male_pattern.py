"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers_male.mens import males_resolver_labels
from utils.dump_runner import make_dump_test_name_data_callback

male_test_data = {
    # {en_nat} men
    "czechoslovak men": "رجال تشيكوسلوفاكيون",
    "bosnia and herzegovina men": "رجال بوسنيون",
    # {en_nat} sportsmen
    "anglo-irish sportsmen": "رياضيون رجال أنجلو إيرلنديون",
    "ancient-romans sportsmen": "رياضيون رجال رومان قدماء",
    # {en_nat} men by occupation
    "federated states-of micronesia men by occupation": "رجال ميكرونيزيون حسب المهنة",
    "equatorial guinean men by occupation": "رجال غينيون استوائيون حسب المهنة",

    # males with ذكور - {en_nat} male swimmers
    "east timorese male swimmers": "سباحون ذكور تيموريون شرقيون",
    "federated states-of micronesia male swimmers": "سباحون ذكور ميكرونيزيون",
    # {en_nat} male freestyle swimmers
    "bissau-guinean male freestyle swimmers": "سباحو تزلج حر ذكور غينيون بيساويون",
    "anglo-irish male freestyle swimmers": "سباحو تزلج حر ذكور أنجلو إيرلنديون",
    # {en_nat} male sprinters
    "czechoslovak male sprinters": "عداؤون سريعون ذكور تشيكوسلوفاكيون",
    "east german male sprinters": "عداؤون سريعون ذكور ألمانيون شرقيون",
    # males without ذكور - {en_nat} male martial artists
    "bosnia and herzegovina male martial artists": "ممارسو فنون قتالية ذكور بوسنيون",
    "chinese taipei male martial artists": "ممارسو فنون قتالية ذكور تايبيون صينيون",
    # {en_nat} male boxers
    "democratic-republic-of-congo male boxers": "ملاكمون ذكور كونغويون ديمقراطيون",
    "dominican republic male boxers": "ملاكمون ذكور دومينيكانيون",
    # {en_nat} male athletes
    "eastern asian male athletes": "لاعبو قوى ذكور آسيويون شرقيون",
    "equatoguinean male athletes": "لاعبو قوى ذكور غينيون استوائيون",
    # {en_nat} male actors
    "central african republic male actors": "ممثلون ذكور أفارقة أوسطيون",
    "equatorial guinean male actors": "ممثلون ذكور غينيون استوائيون",
    # {en_nat} male singers
    "ancient-romans male singers": "مغنون ذكور رومان قدماء",
    "eastern european male singers": "مغنون ذكور أوروبيون شرقيون",
    # {en_nat} male writers
    "central american male writers": "كتاب ذكور أمريكيون أوسطيون",
    "central asian male writers": "كتاب ذكور آسيويون أوسطيون",
    # {en_nat} male film actors
    "east timorese male film actors": "ممثلو أفلام ذكور تيموريون شرقيون",
    "federated states-of micronesia male film actors": "ممثلو أفلام ذكور ميكرونيزيون",
}


@pytest.mark.parametrize("category, expected", male_test_data.items(), ids=male_test_data.keys())
@pytest.mark.fast
def test_male_test_data(category: str, expected: str) -> None:
    label = males_resolver_labels(category)
    assert label == expected


to_test = [
    ("test_male_test_data", male_test_data, males_resolver_labels),
]

test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
