"""
TODO: write code relegin_jobs_nats_jobs.py
"""

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers.relegin_jobs_nats_jobs import resolve_nats_jobs

# from ArWikiCats.new_resolvers.jobs_resolvers.relegin_jobs_new import new_religions_jobs_with_suffix as resolve_nats_jobs
# from ArWikiCats.new_resolvers.reslove_all import all_new_resolvers as resolve_nats_jobs
# from ArWikiCats.make_bots.jobs_mainbot import jobs_with_nat_prefix_label as resolve_nats_jobs


# from ArWikiCats import resolve_label_ar as resolve_nats_jobs
# from ArWikiCats.make_bots.relegin_jobs_new import new_religions_jobs_with_suffix

data_without_nats = {
    "painters shi'a muslims": "رسامون مسلمون شيعة",
    "painters shia muslims": "رسامون مسلمون شيعة",
    "painters male muslims": "رسامون ذكور مسلمون",
    "muslims painters": "رسامون مسلمون",
    "painters muslims": "رسامون مسلمون",
    "female painters shi'a muslims": "رسامات مسلمات شيعيات",
    "painters female shia muslims": "رسامات مسلمات شيعيات",
    "painters women's muslims": "رسامات مسلمات",
    "painters female muslims": "رسامات مسلمات",
    "women's painters muslims": "رسامات مسلمات",
    "women's muslims": "مسلمات",
    "muslims": "مسلمون",
}

test_data_error = {
    "Ancient Roman saints": "رومان قدماء قديسون",
    "Yemeni muslims male": "يمنيون مسلمون ذكور",
    "muslims Yemeni": "يمنيون مسلمون",
    "female Yemeni shi'a muslims": "مسلمات شيعيات يمنيات",
    "women's Yemeni muslims": "مسلمات يمنيات",
}

test_data = {
    "Turkish Cypriot Sufis": "قبرصيون شماليون صوفيون",
    "Turkish Cypriot Sunni Muslims": "قبرصيون شماليون مسلمون سنة",
    "Afghan Christians": "أفغان مسيحيون",
    "American Episcopalians": "أمريكيون أسقفيون",
    "American Hindus": "أمريكيون هندوس",
    "American saints": "أمريكيون قديسون",
    "American Sufis": "أمريكيون صوفيون",
    "American Sunni Muslims": "أمريكيون مسلمون سنة",
    "Angolan Anglicans": "أنغوليون أنجليكيون",
    "Angolan Christians": "أنغوليون مسيحيون",
    "Arab Christians": "عرب مسيحيون",
    "Argentine Anglicans": "أرجنتينيون أنجليكيون",
    "Argentine Christians": "أرجنتينيون مسيحيون",
    "Argentine saints": "أرجنتينيون قديسون",
    "Armenian Christians": "أرمن مسيحيون",
    "Armenian saints": "أرمن قديسون",
    "Armenian Yazidis": "أرمن يزيديون",
    "Aruban Christians": "أروبيون مسيحيون",
    "Asian Christians": "آسيويون مسيحيون",
    "Asian Hindus": "آسيويون هندوس",
    "Asian Sufis": "آسيويون صوفيون",
    "Assyrian saints": "آشوريون قديسون",
    "Australian Anglicans": "أستراليون أنجليكيون",
    "Australian Christians": "أستراليون مسيحيون",
    "Australian Hindus": "أستراليون هندوس",
    "Australian saints": "أستراليون قديسون",
    "Australian Sufis": "أستراليون صوفيون",
    "Australian Sunni Muslims": "أستراليون مسلمون سنة",
    "Austrian Christians": "نمساويون مسيحيون",
    "Austrian saints": "نمساويون قديسون",
    "Austrian Sunni Muslims": "نمساويون مسلمون سنة",
    "Azerbaijani Christians": "أذربيجانيون مسيحيون",
    "Bahamian Anglicans": "بهاميون أنجليكيون",
    "Bahamian Christians": "بهاميون مسيحيون",
    "Bahraini Christians": "بحرينيون مسيحيون",
    "Bahraini Sufis": "بحرينيون صوفيون",
    "Bahraini Sunni Muslims": "بحرينيون مسلمون سنة",
    "Bangladeshi Anglicans": "بنغلاديشيون أنجليكيون",
    "Bangladeshi Christians": "بنغلاديشيون مسيحيون",
    "Bangladeshi Hindus": "بنغلاديشيون هندوس",
    "Bangladeshi Sufis": "بنغلاديشيون صوفيون",
    "Bangladeshi Sunni Muslims": "بنغلاديشيون مسلمون سنة",
    "Barbadian Anglicans": "بربادوسيون أنجليكيون",
    "Barbadian Christians": "بربادوسيون مسيحيون",
    "Barbadian Hindus": "بربادوسيون هندوس",
    "Belarusian Christians": "بيلاروسيون مسيحيون",
    "Belgian Christians": "بلجيكيون مسيحيون",
    "Belgian Hindus": "بلجيكيون هندوس",
    "Belgian saints": "بلجيكيون قديسون",
    "Belgian Sunni Muslims": "بلجيكيون مسلمون سنة",
    "Belizean Anglicans": "بليزيون أنجليكيون",
    "Belizean Christians": "بليزيون مسيحيون",
    "Trinidad and Tobago Anglicans": "ترنيداديون أنجليكيون",
    "Trinidad and Tobago Christians": "ترنيداديون مسيحيون",
    "Trinidad and Tobago Hindus": "ترنيداديون هندوس",
    "Tunisian Christians": "تونسيون مسيحيون",
    "Tunisian Sufis": "تونسيون صوفيون",
    "Tunisian Sunni Muslims": "تونسيون مسلمون سنة",
    "Turkish Christians": "أتراك مسيحيون",
    "Turkish Sufis": "أتراك صوفيون",
    "Turkish Sunni Muslims": "أتراك مسلمون سنة",
    "Turkish Yazidis": "أتراك يزيديون",
    "Turkmenistan Sufis": "تركمانيون صوفيون",
    "Tuvaluan Christians": "توفاليون مسيحيون",
    "Ugandan Anglicans": "أوغنديون أنجليكيون",
    "Ugandan Christians": "أوغنديون مسيحيون",
    "Ugandan saints": "أوغنديون قديسون",
    "Ukrainian Christians": "أوكرانيون مسيحيون",
    "Ukrainian saints": "أوكرانيون قديسون",
    "Ukrainian Sunni Muslims": "أوكرانيون مسلمون سنة",
    "Uruguayan Christians": "أوروغويانيون مسيحيون",
    "Uruguayan saints": "أوروغويانيون قديسون",
    "Uzbek Sufis": "أوزبكيون صوفيون",
    "Uzbekistani Christians": "أوزبكستانيون مسيحيون",
    "Uzbekistani Hindus": "أوزبكستانيون هندوس",
    "Uzbekistani Sunni Muslims": "أوزبكستانيون مسلمون سنة",
    "Vanuatuan Anglicans": "فانواتيون أنجليكيون",
    "Vanuatuan Christians": "فانواتيون مسيحيون",
    "Venezuelan Christians": "فنزويليون مسيحيون",
    "Venezuelan Hindus": "فنزويليون هندوس",
    "Vietnamese Christians": "فيتناميون مسيحيون",
    "Vietnamese Hindus": "فيتناميون هندوس",
    "Vietnamese saints": "فيتناميون قديسون",
    "Welsh Anglicans": "ويلزيون أنجليكيون",
    "Welsh Christians": "ويلزيون مسيحيون",
    "Welsh Hindus": "ويلزيون هندوس",
    "Welsh saints": "ويلزيون قديسون",
    "Yemeni Christians": "يمنيون مسيحيون",
    "Yemeni Sufis": "يمنيون صوفيون",
    "Yemeni Sunni Muslims": "يمنيون مسلمون سنة",
    "Yemeni Zaydis": "يمنيون زيود",
    "Yugoslav Christians": "يوغسلافيون مسيحيون",
    "Zambian Anglicans": "زامبيون أنجليكيون",
    "Zambian Christians": "زامبيون مسيحيون",
    "Zimbabwean Anglicans": "زيمبابويون أنجليكيون",
    "Zimbabwean Christians": "زيمبابويون مسيحيون",
    "Zimbabwean Hindus": "زيمبابويون هندوس",
    "Zimbabwean Sunni Muslims": "زيمبابويون مسلمون سنة",
}

test_religions_data = {
    "Yemeni shi'a muslims": "يمنيون مسلمون شيعة",
    "Yemeni shia muslims": "يمنيون مسلمون شيعة",
    "Yemeni male muslims": "مسلمون ذكور يمنيون",
    "Yemeni muslims": "يمنيون مسلمون",
    "Yemeni people muslims": "يمنيون مسلمون",
}

test_religions_female_data = {
    "Yemeni female shia muslims": "مسلمات شيعيات يمنيات",
    "Yemeni women's muslims": "مسلمات يمنيات",
    "Yemeni female muslims": "مسلمات يمنيات",
}


@pytest.mark.parametrize("input_text,expected", test_data_error.items(), ids=test_data_error.keys())
def test_relegin_jobs(input_text: str, expected: str) -> None:
    result = resolve_nats_jobs(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"


@pytest.mark.parametrize("input_text,expected", data_without_nats.items(), ids=data_without_nats.keys())
def test_data_without_nats(input_text: str, expected: str) -> None:
    result = resolve_nats_jobs(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"


@pytest.mark.parametrize("input_text,expected", test_data.items(), ids=test_data.keys())
def test_relegin_nats_jobs(input_text: str, expected: str) -> None:
    result = resolve_nats_jobs(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"


@pytest.mark.parametrize("category,expected", test_religions_data.items(), ids=test_religions_data.keys())
def test_religions_jobs_1(category: str, expected: str) -> None:
    result = resolve_nats_jobs(category)
    assert result == expected


@pytest.mark.parametrize("category,expected", test_religions_female_data.items(), ids=test_religions_female_data.keys())
def test_religions_females(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = resolve_nats_jobs(category)
    assert result == expected
