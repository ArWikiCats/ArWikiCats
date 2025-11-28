#!/usr/bin/python3
"""Integration tests for :mod:`teamsnew_bot` lazy resolver."""

import re

import pytest

from ArWikiCats.translations_formats.format_data import FormatData


@pytest.fixture
def sample_data():
    formatted_data = {
        "men's {en} world cup": "كأس العالم للرجال في {ar}",
        "women's {en} championship": "بطولة السيدات في {ar}",
        "{en} records": "سجلات {ar}",
        "{en} league": "دوري {ar}",
        "{en} alaskan independence partys": "أعضاء حزب استقلال ألاسكا في {ar}",
        "{en} alaskan independences": "أعضاء حزب استقلال ألاسكا في {ar}",
        "{en} anti administration partys": "أعضاء حزب معاداة الإدارة في {ar}",
        "{en} anti administrations": "أعضاء حزب معاداة الإدارة في {ar}",
        "{en} anti masonic partys": "أعضاء حزب مناهضة الماسونية في {ar}",
        "{en} anti masonics": "أعضاء حزب مناهضة الماسونية في {ar}",
        "{en} anti-administration partys": "أعضاء حزب معاداة الإدارة في {ar}",
        "{en} anti-administrations": "أعضاء حزب معاداة الإدارة في {ar}",
        "{en} anti-masonic partys": "أعضاء حزب مناهضة الماسونية في {ar}",
        "{en} anti-masonics": "أعضاء حزب مناهضة الماسونية في {ar}",
        "{en} anti-monopoly partys": "أعضاء حزب مكافحة الاحتكار في {ar}",
        "{en} anti-monopolys": "أعضاء حزب مكافحة الاحتكار في {ar}",
        "{en} appellate court judges": "قضاة محكمة استئناف {ar}",
        "{en} attorneys general": "مدعي {ar} العام",
        "{en} ballot measures": "إجراءات اقتراع {ar}",
        "{en} ballot propositions": "اقتراحات اقتراع {ar}",
        "{en} board of education": "مجلس التعليم في ولاية {ar}",
        "{en} board of health": "مجلس الصحة في ولاية {ar}",
        "{en} citizens partys": "أعضاء حزب المواطنين في {ar}",
        "{en} citizenss": "أعضاء حزب المواطنين في {ar}",
        "{en} city councils": "مجالس مدن {ar}",
        "{en} conditional union partys": "أعضاء حزب الاتحاد المشروط في {ar}",
        "{en} conditional unions": "أعضاء حزب الاتحاد المشروط في {ar}",
        "{en} constitutional union partys": "أعضاء حزب الاتحاد الدستوري في {ar}",
        "{en} constitutional unions": "أعضاء حزب الاتحاد الدستوري في {ar}",
        "{en} court judges": "قضاة محكمة {ar}",
        "{en} court of appeals": "محكمة استئناف {ar}",
        "{en} court of appeals judges‎": "قضاة محكمة استئناف {ar}",
        "{en} democratic partys": "أعضاء الحزب الديمقراطي في {ar}",
        "{en} democratic republicans": "أعضاء الحزب الديمقراطي الجمهوري في {ar}",
        "{en} democratic-republican partys": "أعضاء الحزب الديمقراطي الجمهوري في {ar}",
        "{en} democratic-republicans": "أعضاء الحزب الديمقراطي الجمهوري في {ar}",
        "{en} democratics": "أعضاء الحزب الديمقراطي في {ar}",
        "{en} democrats": "ديمقراطيون من ولاية {ar}",
        "{en} farmer labor partys": "أعضاء حزب العمال المزارعين في {ar}",
        "{en} farmer labors": "أعضاء حزب العمال المزارعين في {ar}",
        "{en} farmer–labor partys": "أعضاء حزب العمال المزارعين في {ar}",
        "{en} farmer–labors": "أعضاء حزب العمال المزارعين في {ar}",
        "{en} federalist partys": "أعضاء الحزب الفيدرالي الأمريكي في {ar}",
        "{en} federalists": "أعضاء الحزب الفيدرالي الأمريكي في {ar}",
        "{en} free soil partys": "أعضاء حزب التربة الحرة في {ar}",
        "{en} free soils": "أعضاء حزب التربة الحرة في {ar}",
        "{en} general assembly": "جمعية {ar} العامة",
        "{en} green partys": "أعضاء حزب الخضر في {ar}",
        "{en} greenback partys": "أعضاء حزب الدولار الأمريكي في {ar}",
        "{en} greenbacks": "أعضاء حزب الدولار الأمريكي في {ar}",
        "{en} greens": "أعضاء حزب الخضر في {ar}",
        "{en} gubernatorial elections": "انتخابات حاكم {ar}",
        "{en} house of representatives": "مجلس نواب ولاية {ar}",
        "{en} house-of-representatives": "مجلس نواب ولاية {ar}",
        "{en} house-of-representatives elections": "انتخابات مجلس نواب ولاية {ar}",
        "{en} in the War of 1812": "{ar} في حرب 1812",
        "{en} independent voters associations": "أعضاء رابطة الناخبين المستقلين في {ar}",
        "{en} independents": "مستقلون من ولاية {ar}",
        "{en} know nothings": "أعضاء حزب لا أدري في {ar}",
        "{en} know-nothings": "أعضاء حزب لا أدري في {ar}",
        "{en} law": "قانون {ar}",
        "{en} law and order of rhode islands": "أعضاء حزب القانون والنظام في رود آيلاند في {ar}",
        "{en} law and order party of rhode islands": "أعضاء حزب القانون والنظام في رود آيلاند في {ar}",
        "{en} lawyers": "محامون من ولاية {ar}",
        "{en} legislative assembly": "هيئة {ar} التشريعية",
        "{en} legislature": "هيئة {ar} التشريعية",
        "{en} liberal republican partys": "أعضاء الحزب الجمهوري الليبرالي في {ar}",
        "{en} liberal republicans": "أعضاء الحزب الجمهوري الليبرالي في {ar}",
        "{en} liberty (1840)s": "أعضاء حزب الحرية 1840 في {ar}",
        "{en} liberty party (1840)s": "أعضاء حزب الحرية 1840 في {ar}",
        "{en} liberty union partys": "أعضاء حزب الحرية المتحد في {ar}",
        "{en} liberty unions": "أعضاء حزب الحرية المتحد في {ar}",
        "{en} local politicians": "سياسيون محليون في {ar}",
        "{en} national republican partys": "أعضاء الحزب الجمهوري الوطني في {ar}",
        "{en} national republicans": "أعضاء الحزب الجمهوري الوطني في {ar}",
        "{en} nonpartisan league states": "أعضاء الرابطة غير الحزبية في {ar}",
        "{en} nullifier partys": "أعضاء حزب الرفض في {ar}",
        "{en} nullifiers": "أعضاء حزب الرفض في {ar}",
        "{en} opposition partys": "أعضاء أوبوسيشن بارتي في {ar}",
        "{en} oppositions": "أعضاء أوبوسيشن بارتي في {ar}",
        "{en} people's partys": "أعضاء حزب الشعب في {ar}",
        "{en} people'ss": "أعضاء حزب الشعب في {ar}",
        "{en} peoples partys": "أعضاء حزب الشعب في {ar}",
        "{en} peopless": "أعضاء حزب الشعب في {ar}",
        "{en} politicians": "سياسيو {ar}",
        "{en} politics": "سياسة {ar}",
        "{en} pro administration partys": "أعضاء حزب دعم الإدارة في {ar}",
        "{en} pro administrations": "أعضاء حزب دعم الإدارة في {ar}",
        "{en} pro-administration partys": "أعضاء حزب دعم الإدارة في {ar}",
        "{en} pro-administrations": "أعضاء حزب دعم الإدارة في {ar}",
        "{en} readjuster partys": "أعضاء ريدجوستر بارتي في {ar}",
        "{en} readjusters": "أعضاء ريدجوستر بارتي في {ar}",
        "{en} referendums": "استفتاءات {ar}",
        "{en} republican partys": "أعضاء الحزب الجمهوري في {ar}",
        "{en} republicans": "أعضاء الحزب الجمهوري في {ar}",
        "{en} senate": "مجلس شيوخ ولاية {ar}",
        "{en} senators": "أعضاء مجلس شيوخ ولاية {ar}",
        "{en} sheriffs": "مأمورو {ar}",
        "{en} silver partys": "أعضاء الحزب الفضي في {ar}",
        "{en} silver republican partys": "أعضاء الحزب الجمهوري الفضي في {ar}",
        "{en} silver republicans": "أعضاء الحزب الجمهوري الفضي في {ar}",
        "{en} silvers": "أعضاء الحزب الفضي في {ar}",
        "{en} socialist party usas": "أعضاء الحزب الاشتراكي في {ar}",
        "{en} socialist partys": "أعضاء الحزب الاشتراكي في {ar}",
        "{en} socialist usas": "أعضاء الحزب الاشتراكي في {ar}",
        "{en} socialists": "أعضاء الحزب الاشتراكي في {ar}",
        "{en} solidaritys": "أعضاء حزب التضامن في {ar}",
        "{en} state assembly": "جمعية ولاية {ar}",
        "{en} state attorneys general": "مدعي ولاية {ar} العام",
        "{en} state court judges": "قضاة محكمة ولاية {ar}",
        "{en} state courts": "محكمة ولاية {ar}",
        "{en} state legislature": "هيئة ولاية {ar} التشريعية",
        "{en} state politics": "سياسة ولاية {ar}",
        "{en} state senators": "أعضاء مجلس شيوخ ولاية {ar}",
        "{en} state superior court judges": "قضاة محكمة ولاية {ar} العليا",
        "{en} superior court judges": "قضاة محكمة {ar} العليا",
        "{en} supreme court": "محكمة {ar} العليا",
        "{en} supreme court justices": "قضاة محكمة {ar} العليا",
        "{en} territorial legislature": "هيئة {ar} التشريعية الإقليمية",
        "{en} territory": "إقليم {ar}",
        "{en} territory judges": "قضاة إقليم {ar}",
        "{en} territory officials": "مسؤولو إقليم {ar}",
        "{en} unconditional union partys": "أعضاء حزب الاتحاد غير المشروط في {ar}",
        "{en} unconditional unions": "أعضاء حزب الاتحاد غير المشروط في {ar}",
        "{en} unionist partys": "أعضاء الحزب الوحدوي في {ar}",
        "{en} unionists": "أعضاء الحزب الوحدوي في {ar}",
        "{en} whig partys": "أعضاء حزب اليمين في {ar}",
        "{en} whigs": "أعضاء حزب اليمين في {ar}"
    }

    data_list = {
        "georgia (u.s. state)": "ولاية جورجيا",
        "georgia": "جورجيا",
        "new york (state)": "ولاية نيويورك",
        "new york": "نيويورك",
        "virginia": "فرجينيا",
        "washington (state)": "ولاية واشنطن",
        "washington": "واشنطن",
        "washington, d.c.": "واشنطن العاصمة",
        "west virginia": "فيرجينيا الغربية",
    }

    return formatted_data, data_list


def test_keys_to_pattern(sample_data):
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, "{en}", "{ar}")
    pattern = bot.keys_to_pattern()
    assert isinstance(pattern, re.Pattern)
    assert pattern.search("football") is not None
    assert pattern.search("snooker") is not None


@pytest.mark.parametrize(
    "category,expected",
    [
        ("men's football world cup", "football"),
        ("women's basketball championship", "basketball"),
        ("women's rugby league championship", "rugby league"),
        ("random text", ""),
    ],
)
def test_match_key(category, expected, sample_data):
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, "{en}", "{ar}")
    assert bot.match_key(category) == expected


@pytest.mark.parametrize(
    "template_label,ar,expected",
    [
        ("كأس العالم في xoxo", "كرة القدم", "كأس العالم في كرة القدم"),
        ("xoxo بطولة", "كرة السلة", "كرة السلة بطولة"),
        ("", "كرة الطائرة", ""),  # placeholder not found
    ],
    ids=[k for k in range(3)],
)
def test_apply_pattern_replacement(template_label, ar, expected, sample_data):
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, value_placeholder="xoxo")
    assert bot.apply_pattern_replacement(template_label, ar) == expected


@pytest.mark.parametrize(
    "category,sport_key,expected",
    [
        ("men's football world cup", "football", "men's xoxo world cup"),
        ("women's basketball championship", "basketball", "women's xoxo championship"),
    ],
)
def test_normalize_category(category, sport_key, expected, sample_data):
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list)
    result = bot.normalize_category(category, sport_key)
    assert result.lower() == expected.lower()


@pytest.mark.parametrize(
    "category,expected",
    [
        ("men's football world cup", "كأس العالم للرجال في كرة القدم"),
        ("women's basketball championship", "بطولة السيدات في كرة السلة"),
        ("women's Rugby championship", "بطولة السيدات في الرجبي"),
        ("women's Rugby League championship", "بطولة السيدات في دوري الرجبي"),
        ("snooker records", "سجلات سنوكر"),
        ("unknown category", ""),
    ],
    ids=[k for k in range(6)],
)
def test_search(sample_data, category, expected):
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, key_placeholder="{en}", value_placeholder="{ar}")
    assert bot.search(category) == expected


def test_search_no_sport_match(sample_data):
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list)
    assert bot.search("unrelated topic") == ""


def test_search_no_template_label(sample_data):
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list)
    bot.formatted_data = {}  # remove templates
    assert bot.search("men's football world cup") == ""


def test_case(sample_data):
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, key_placeholder="{en}", value_placeholder="{ar}")
    result = bot.search("men's football world cup")
    assert result == "كأس العالم للرجال في كرة القدم"


def test_get_template(sample_data):
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, key_placeholder="{en}", value_placeholder="{ar}")
    normalized = bot.normalize_category("men's football world cup", "football")
    assert normalized == "men's {en} world cup"
    template_label = bot.get_template("football", "men's football world cup")
    assert template_label == "كأس العالم للرجال في {ar}"


def test_empty_data_lists():
    bot = FormatData({}, {}, key_placeholder="{k}", value_placeholder="{v}")
    assert bot.match_key("any") == ""
    assert bot.search("text") == ""
    assert bot.keys_to_pattern() is None


def test_case_insensitivity(sample_data):
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, key_placeholder="{en}", value_placeholder="{ar}")
    result = bot.search("MEN'S FOOTBALL WORLD CUP")
    assert result == "كأس العالم للرجال في كرة القدم"
