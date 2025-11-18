"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.country2_bots.cn_lab import make_cnt_lab

make_cnt_lab_data = {
    "jerusalem": "القدس",
    "georgia": "جورجيا",
    "naples": "نابولي",
    "sicily": "صقلية",
    "sardinia": "سردينيا",
    "lagos": "ولاية لاغوس",
    "hanover": "هانوفر",
    "saxony": "ساكسونيا",
    "morocco": "المغرب",
    "galicia": "منطقة غاليسيا",
}


@pytest.mark.parametrize("category, ar", make_cnt_lab_data.items(), ids=list(make_cnt_lab_data.keys()))
@pytest.mark.fast
def test_make_cnt_lab_data(category, ar) -> None:

    label = make_cnt_lab(
        tat_o="-of ",
        country2=f"kingdom-of {category}",
        c_2_l=ar,
        c_1_l="مملكة",
        cona_1="kingdom of",
        cona_2=category,
        sps=" "
    )
    assert label.strip() == f"مملكة {ar}"


party_data = {
    "vietnam": ("communist party-of vietnam", "فيتنام", "الحزب الشيوعي في فيتنام"),
    "bosnia and herzegovina": ("communist party-of bosnia and herzegovina", "البوسنة والهرسك", "الحزب الشيوعي في البوسنة والهرسك"),
    "cuba": ("communist party-of cuba", "كوبا", "الحزب الشيوعي في كوبا"),
    "soviet union": ("communist party-of soviet union", "الاتحاد السوفيتي", "الحزب الشيوعي في الاتحاد السوفيتي"),
    "yugoslavia": ("communist party-of yugoslavia", "يوغوسلافيا", "الحزب الشيوعي في يوغوسلافيا"),
}


@pytest.mark.parametrize(
    "country2, c_2_l, expected",
    party_data.values(),
    ids=list(party_data.keys())
)
@pytest.mark.fast
def test_make_cnt_lab_communist_party(country2, c_2_l, expected):

    label = make_cnt_lab(
        tat_o="-of ",
        country2=country2,
        c_2_l=c_2_l,
        c_1_l="الحزب الشيوعي في ",
        cona_1="communist party of",
        cona_2=country2.replace("communist party-of ", ""),
        sps=" "
    )

    assert label.strip() == expected


def test_make_cnt_lab():
    result1 = make_cnt_lab(
        tat_o=" in ",
        country2="university of arts in belgrade",
        c_2_l="بلغراد",
        c_1_l="جامعة {} للفنون في",
        cona_1="university of arts",
        cona_2="belgrade",
        sps=" في "
    )
    assert isinstance(result1, str)
    assert result1 == "جامعة بلغراد للفنون"

    result1 = make_cnt_lab(
        tat_o=" of ",
        country2="by medium from insular areas of united states",
        c_2_l="الولايات المتحدة",
        c_1_l="حسب الوسط من المناطق المعزولة في ",
        cona_1="by medium from insular areas of",
        cona_2="united states",
        sps=" "
    )
    assert isinstance(result1, str)
    assert result1 == "حسب الوسط من المناطق المعزولة في الولايات المتحدة"

    # Test with basic inputs
    result = make_cnt_lab("in", "test in country", "country label", "test label", "test", "country", " ")
    assert isinstance(result, str)

    # Test with different parameters
    result_various = make_cnt_lab("from", "test from country", "country label2", "test label2", "test2", "country2", " من ")
    assert isinstance(result_various, str)

    # Test with empty strings
    result_empty = make_cnt_lab("", "", "", "", "", "", "")
    assert isinstance(result_empty, str)

    # Test with empty strings


congress_data = {
    "103rd": "الثالث بعد المئة",
    "104th": "الرابع بعد المئة"
}


@pytest.mark.parametrize("category, ar", party_data.items(), ids=list(party_data.keys()))
@pytest.mark.fast
def test_congress_data(category, ar):
    label = f"الكونغرس الأمريكي {ar}"
    result = make_cnt_lab(
        tat_o=" of ",
        country2=f"acts of {category} united states congress",
        c_2_l=label,
        c_1_l="أفعال",
        cona_1="acts of",
        cona_2=f"{category} united states congress",
        sps=" "
    )

    assert result == f"أفعال {label}"


universities_data = [
    {
        "tat_o": " of ",
        "country2": "azerbaijan university of architecture and construction",
        "c_2_l": "هندسة معمارية وبناء",
        "c_1_l": "جامعة أذربيجان",
        "cona_1": "azerbaijan university of",
        "cona_2": "architecture and construction",
        "output": "جامعة أذربيجان هندسة معمارية وبناء"
    },
    {
        "tat_o": " of ",
        "country2": "bangladesh university of engineering and technology",
        "c_2_l": "هندسة والتقانة",
        "c_1_l": "جامعة بنغلاديش",
        "cona_1": "bangladesh university of",
        "cona_2": "engineering and technology",
        "output": "جامعة بنغلاديش هندسة والتقانة"
    },
    {
        "tat_o": " of ",
        "country2": "university of koblenz and landau",
        "c_2_l": "كوبلنتس ولانداو إن در بفالتس",
        "c_1_l": "جامعة {}",
        "cona_1": "university of",
        "cona_2": "koblenz and landau",
        "output": "جامعة كوبلنتس ولانداو إن در بفالتس"
    },
    {
        "tat_o": " of ",
        "country2": "university of modena and reggio emilia",
        "c_2_l": "مودينا وريدجو إميليا",
        "c_1_l": "جامعة {}",
        "cona_1": "university of",
        "cona_2": "modena and reggio emilia",
        "output": "جامعة مودينا وريدجو إميليا"
    },
    {
        "tat_o": " of ",
        "country2": "china university of mining and technology",
        "c_2_l": "تعدين والتقانة",
        "c_1_l": "جامعة الصين",
        "cona_1": "china university of",
        "cona_2": "mining and technology",
        "output": "جامعة الصين تعدين والتقانة"
    },
]
