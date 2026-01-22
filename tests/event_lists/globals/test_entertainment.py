#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

entertainment_1 = {
    "Action anime and manga": "أنمي ومانغا حركة",
    "Action films by genre": "أفلام حركة حسب النوع الفني",
    "Adventure anime and manga": "أنمي ومانغا مغامرات",
    "Adventure films by genre": "أفلام مغامرات حسب النوع الفني",
    "American Cinema Editors": "محررون سينمائون أمريكيون",
    "American television episodes": "حلقات تلفزيونية أمريكية",
    "American television series based on British television series": "مسلسلات تلفزيونية أمريكية مبنية على مسلسلات تلفزيونية بريطانية",
    "Apocalyptic anime and manga": "أنمي ومانغا نهاية العالم",
    "Argentine songwriters": "كتاب أغان أرجنتينيون",
    "Books about automobiles": "كتب عن سيارات",
    "British editorial cartoonists": "محررون كارتونيون بريطانيون",
    "British television chefs": "طباخو تلفاز بريطانيون",
    "Cartoonists by publication": "رسامو كارتون حسب المؤسسة",
    # "Characters in children's literature": "شخصيات في أدب الأطفال",
    "Comedy anime and manga": "أنمي ومانغا كوميدية",
    "Comedy films by genre": "أفلام كوميدية حسب النوع الفني",
    "Comics adapted into films": "قصص مصورة تم تحويلها إلى أفلام",
    "Comics based on films": "قصص مصورة مبنية على أفلام",
    "Crime anime and manga": "أنمي ومانغا جريمة",
    "Crime films by genre": "أفلام جريمة حسب النوع الفني",
    "Dark fantasy video games": "ألعاب فيديو فانتازيا مظلمة",
    "Dinosaurs in fiction": "ديناصورات في الخيال",
    "Dinosaurs in video games": "ديناصورات في ألعاب فيديو",
    "Disney animated films": "أفلام رسوم متحركة ديزني",
    "Documentary films by genre": "أفلام وثائقية حسب النوع الفني",
}

entertainment_2 = {
    "Drama anime and manga": "أنمي ومانغا درامية",
    "Drama films by genre": "أفلام درامية حسب النوع الفني",
    "Editorial cartoonists from Northern Ireland": "محررون كارتونيون من أيرلندا الشمالية",
    "Erotic films by genre": "أفلام إغرائية حسب النوع الفني",
    "Fantasy anime and manga": "أنمي ومانغا فانتازيا",
    "Fantasy films by genre": "أفلام فانتازيا حسب النوع الفني",
    "Fantasy video games": "ألعاب فيديو فانتازيا",
    "Female comics writers": "كاتبات قصص مصورة",
    "Figure skating films": "أفلام تزلج فني",
    "Figure skating media": "إعلام تزلج فني",
    "Films about Olympic boxing": "أفلام عن بوكسينغ أولمبي",
    "Films about Olympic figure skating": "أفلام عن تزلج فني أولمبي",
    "Films about Olympic gymnastics": "أفلام عن جمباز أولمبي",
    "Films about Olympic skiing": "أفلام عن تزلج أولمبي",
    "Films about Olympic track and field": "أفلام عن سباقات مضمار وميدان أولمبي",
    "Films about automobiles": "أفلام عن سيارات",
    "Films about the Olympic Games by athletic event": "أفلام عن الألعاب الأولمبية حسب حدث ألعاب القوى",
    "Films based on American comics": "أفلام مبنية على قصص مصورة أمريكية",
    "Films based on comics": "أفلام مبنية على قصص مصورة",
    "Films based on television series": "أفلام مبنية على مسلسلات تلفزيونية",
    "Films by audience": "أفلام حسب الجمهور",
    "Films by continent": "أفلام حسب القارة",
    "Films by culture": "أفلام حسب الثقافة",
    "Films by date": "أفلام حسب التاريخ",
    "Films by director": "أفلام حسب المخرج",
    "Films by genre": "أفلام حسب النوع الفني",
    "Films by language": "أفلام حسب اللغة",
    "Films by movement": "أفلام حسب الحركة",
    "Films by producer": "أفلام حسب المنتج",
    "Films by setting location": "أفلام حسب موقع الأحداث",
    "Films by shooting location": "أفلام حسب موقع التصوير",
    "Films by source": "أفلام حسب المصدر",
    "Films by studio": "أفلام حسب استوديو الإنتاج",
    "Films by technology": "أفلام حسب التقانة",
    "Films by topic": "أفلام حسب الموضوع",
    "Films by type": "أفلام حسب الفئة",
    "Films set in national parks": "أفلام تقع أحداثها في متنزهات وطنية",
    "French comic strips": "شرائط كومكس فرنسية",
    "Historical anime and manga": "أنمي ومانغا تاريخية",
    "Historical comics": "قصص مصورة تاريخية",
    "Historical fiction by setting location": "خيال تاريخي حسب موقع الأحداث",
    "Historical television series": "مسلسلات تلفزيونية تاريخية",
    "Horror anime and manga": "أنمي ومانغا رعب",
    "Horror films by genre": "أفلام رعب حسب النوع الفني",
    "LGBTQ-related films by genre": "أفلام متعلقة بإل جي بي تي كيو حسب النوع الفني",
    "Lists of British television series characters by series": "قوائم شخصيات مسلسلات تلفزيونية بريطانية حسب السلسلة",
    "Lists of television characters by series": "قوائم شخصيات تلفزيونية حسب السلسلة",
}

entertainment_3 = {
    "Magical girl anime and manga": "أنمي ومانغا فتاة ساحرة",
    "Mecha anime and manga": "أنمي ميكا",
    "Musical films by genre": "أفلام موسيقية حسب النوع الفني",
    "Mystery anime and manga": "أنمي ومانغا غموض",
    "Mystery films by genre": "أفلام غموض حسب النوع الفني",
    "Participants in British reality television series": "مشاركون في مسلسلات تلفزيونية واقعية بريطانية",
    "Peruvian television actors": "ممثلو تلفزيون بيرويون",
    "Philippine films by subgenre": "أفلام فلبينية حسب النوع الفرعي",
    "Political films by genre": "أفلام سياسية حسب النوع الفني",
    "Pornographic films by genre": "أفلام إباحية حسب النوع الفني",
    "Romance anime and manga": "أنمي ومانغا رومانسية",
    "Romance films by genre": "أفلام رومانسية حسب النوع الفني",
    "Science fiction anime and manga": "أنمي ومانغا خيال علمي",
    "Science fiction films by genre": "أفلام خيال علمي حسب النوع الفني",
    "Songs about automobiles": "أغاني عن سيارات",
    "South Korean television series by production location": "مسلسلات تلفزيونية كورية جنوبية حسب موقع الإنتاج",
    "Sports anime and manga": "أنمي ومانغا رياضية",
    "Sports films by genre": "أفلام رياضية حسب النوع الفني",
    "Spy anime and manga": "أنمي ومانغا تجسسية",
    "Spy films by genre": "أفلام تجسسية حسب النوع الفني",
    "Supernatural anime and manga": "أنمي ومانغا خارقة للطبيعة",
    "Teen films by genre": "أفلام مراهقة حسب النوع الفني",
    "Television characters by series": "شخصيات تلفزيونية حسب السلسلة",
    "Television programs by geographic setting": "برامج تلفزيونية حسب الموقع الجغرافي للأحداث",
    "Television series produced in Alberta": "مسلسلات تلفزيونية أنتجت في ألبرتا",
    "Television series produced in Seoul": "مسلسلات تلفزيونية أنتجت في سول",
    "Television shows filmed in Algeria": "عروض تلفزيونية صورت في الجزائر",
    "Thriller anime and manga": "أنمي ومانغا إثارة",
    "Thriller films by genre": "أفلام إثارة حسب النوع الفني",
    "Video games about diseases": "ألعاب فيديو عن الأمراض",
    "Video games about slavery": "ألعاب فيديو عن العبودية",
    "Video games based on Egyptian mythology": "ألعاب فيديو مبنية على أساطير مصرية",
    "Video games based on mythology": "ألعاب فيديو مبنية على أساطير",
    "Video games set in prehistory": "ألعاب فيديو تقع أحداثها في ما قبل التاريخ",
    "Video games set in the Byzantine Empire": "ألعاب فيديو تقع أحداثها في الإمبراطورية البيزنطية",
    "War anime and manga": "أنمي ومانغا حربية",
    "War films by genre": "أفلام حربية حسب النوع الفني",
    "Works about automobiles": "أعمال عن سيارات",
    "Works adapted for other media": "أعمال تم تحويلها إلى وسائط أخرى",
    "songs about busan": "أغاني عن بوسان",
}

data2 = {
    "documentary filmmakers by nationality": "صانعو أفلام وثائقية حسب الجنسية",
    "yemeni war filmmakers": "صانعو أفلام حربية يمنيون",
    "Peruvian documentary film directors": "مخرجو أفلام وثائقية بيرويون",
    "Lists of action television characters by series": "قوائم شخصيات تلفزيونية حركة حسب السلسلة",
    "Drama television characters by series": "شخصيات تلفزيونية درامية حسب السلسلة",
    "Fantasy television characters by series": "شخصيات تلفزيونية فانتازيا حسب السلسلة",
}


ENTERTAINMENT_CASES = [
    ("entertainment_1", entertainment_1),
    ("entertainment_2", entertainment_2),
    ("entertainment_3", entertainment_3),
    ("entertainment_data2", data2),
]


@pytest.mark.parametrize("category, expected", entertainment_1.items(), ids=entertainment_1.keys())
@pytest.mark.fast
def test_entertainment_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", entertainment_2.items(), ids=entertainment_2.keys())
@pytest.mark.fast
def test_entertainment_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", entertainment_3.items(), ids=entertainment_3.keys())
@pytest.mark.fast
def test_entertainment_3(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", ENTERTAINMENT_CASES)
@pytest.mark.dump
def test_entertainment(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
