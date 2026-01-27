#!/usr/bin/python3
"""Integration tests for v3i translations resolvers validating country, year, and combined formatters."""

import pytest

from ArWikiCats.new_resolvers.time_and_jobs_resolvers.year_job_origin_resolver import get_job_label
from utils.dump_runner import make_dump_test_name_data

test_0 = {}

test_data_standard = {
    "sports-people": "رياضيون",
    "sportspeople": "رياضيون",
    "botanists": "علماء نباتات",
    "actors": "ممثلون",
    "actresses": "ممثلات",
    "architects": "معماريون",
    "artisans": "حرفيون",
    "artists": "فنانون",
    "astronomers": "فلكيون",
    "autobiographers": "كتاب سيرة ذاتية",
    "ballet dancers": "راقصو باليه",
    "bass guitarists": "عازفو غيتار باس",
    "biographers": "كتاب سيرة",
    "biologists": "علماء أحياء",
    "businesspeople": "شخصيات أعمال",
    "businesswomen": "سيدات أعمال",
    "chemists": "كيميائيون",
    "chess players": "لاعبو شطرنج",
    "civil servants": "موظفو خدمة مدنية",
    "classical composers": "ملحنون كلاسيكيون",
    "classical musicians": "موسيقيون كلاسيكيون",
    "classical pianists": "عازفو بيانو كلاسيكيون",
    "clergy": "رجال دين",
    "comedians": "كوميديون",
    "composers": "ملحنون",
    "criminals": "مجرمون",
    "dancers": "راقصون",
    "deaths": "وفيات",
    "diarists": "كتاب يوميات",
    "diplomats": "دبلوماسيون",
    "dramatists and playwrights": "كتاب دراما ومسرح",
    "drummers": "طبالون",
    "educators": "معلمون",
    "engineers": "مهندسون",
    "engravers": "نقاشون",
    "explorers": "مستكشفون",
    "folk musicians": "موسيقيو فولك",
    "guitarists": "عازفو قيثارة",
    "historians": "مؤرخون",
    "illustrators": "رسامون توضيحيون",
    "Jews": "يهود",
    "journalists": "صحفيون",
    "jurists": "حقوقيون",
    "landowners": "حائزو أراضي",
    "lawyers": "محامون",
    "LGBTQ people": "أعلام إل جي بي تي كيو",
    "male actors": "ممثلون ذكور",
    "male artists": "فنانون ذكور",
    "male composers": "ملحنون ذكور",
    "male musicians": "موسيقيون ذكور",
    "male singers": "مغنون ذكور",
    "male writers": "كتاب ذكور",
    "mathematicians": "رياضياتيون",
    "medical doctors": "أطباء",
    "memoirists": "كتاب مذكرات",
    "military personnel": "أفراد عسكريون",
    "musicians": "موسيقيون",
    "naturalists": "علماء طبيعة",
    "nobility": "نبلاء",
    "non-fiction writers": "كتاب غير روائيين",
    "novelists": "روائيون",
    "opera singers": "مغنو أوبرا",
    "painters": "رسامون",
    "philosophers": "فلاسفة",
    "photographers": "مصورون",
    "physicians": "أطباء",
    "physicists": "فيزيائيون",
    "pianists": "عازفو بيانو",
    "poets": "شعراء",
    "politicians": "سياسيون",
    "princes": "أمراء",
    "publishers (people)": "ناشرون",
    "rabbis": "حاخامات",
    "scholars": "دارسون",
    "scientists": "علماء",
    "screenwriters": "كتاب سيناريو",
    "sculptors": "نحاتون",
    "short story writers": "كتاب قصة قصيرة",
    "singer-songwriters": "مغنون وكتاب أغاني",
    "singers": "مغنون",
    "songwriters": "كتاب أغان",
    "sportsmen": "رياضيون رجال",
    "sportswomen": "رياضيات",
    "translators": "مترجمون",
    "violinists": "عازفو كمان",
    "women artists": "فنانات",
    "women composers": "ملحنات",
    "women educators": "معلمات",
    "women journalists": "صحفيات",
    "women lawyers": "محاميات",
    "women medical doctors": "طبيبات",
    "women musicians": "موسيقيات",
    "women opera singers": "مغنيات أوبرا",
    "women painters": "رسامات",
    "women politicians": "سياسيات",
    "women scientists": "عالمات",
    "women singers": "مغنيات",
    "women writers": "كاتبات",
    "women": "نساء",
    "writers": "كتاب",
    "zoologists": "علماء حيوانات",
}


@pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
def test_get_job_label_1(category: str, expected: str) -> None:
    """
    Test
    """
    result = get_job_label(category)
    assert result == expected


to_test = [
    ("test_get_job_label_1", test_data_standard),
]


test_dump_all = make_dump_test_name_data(to_test, get_job_label, run_same=False)
