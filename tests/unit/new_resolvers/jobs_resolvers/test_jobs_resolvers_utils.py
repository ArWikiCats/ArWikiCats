"""
Tests
"""

from ArWikiCats.new_resolvers.jobs_resolvers.utils import nat_and_gender_keys


def test_nat_and_gender_keys_male():
    data = nat_and_gender_keys("{en_nat}", "emigrants", "male", "{ar_nat} مهاجرون ذكور")

    assert data == {
        "{en_nat} male emigrants": "{ar_nat} مهاجرون ذكور",
        "{en_nat} emigrants male": "{ar_nat} مهاجرون ذكور",
        "male {en_nat} emigrants": "{ar_nat} مهاجرون ذكور",
    }, f"Unexpected result: {data}"


def test_nat_and_gender_keys_female():
    data = nat_and_gender_keys("{en_nat}", "expatriate", "{women}", "{ar_nat} مغتربات")

    assert data == {
        "{en_nat} {women} expatriate": "{ar_nat} مغتربات",
        "{en_nat} expatriate {women}": "{ar_nat} مغتربات",
        "{women} {en_nat} expatriate": "{ar_nat} مغتربات",
    }, f"Unexpected result: {data}"


def test_nat_and_gender_keys_2():
    data = nat_and_gender_keys("{en_job}", "emigrants", "male", "{ar_job} مهاجرون ذكور")

    assert data == {
        'male {en_job} emigrants': '{ar_job} مهاجرون ذكور',
        '{en_job} emigrants male': '{ar_job} مهاجرون ذكور',
        '{en_job} male emigrants': '{ar_job} مهاجرون ذكور',
    }, f"Unexpected result: {data}"
