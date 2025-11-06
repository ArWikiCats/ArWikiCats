#
import pytest

from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset, dump_diff

data = {
    "Category:Action anime and manga": "تصنيف:أنمي ومانغا حركة",
    "Category:Action films by genre": "تصنيف:أفلام حركة حسب النوع الفني",
    "Category:Adventure anime and manga": "تصنيف:أنمي ومانغا مغامرات",
    "Category:Adventure films by genre": "تصنيف:أفلام مغامرات حسب النوع الفني",
    "Category:American Cinema Editors": "تصنيف:محررون سينمائون أمريكيون",
    "Category:American television episodes": "تصنيف:حلقات تلفزيونية أمريكية",
    "Category:American television series based on British television series": "تصنيف:مسلسلات تلفزيونية أمريكية مبنية على مسلسلات تلفزيونية بريطانية",
    "Category:Apocalyptic anime and manga": "تصنيف:أنمي ومانغا نهاية العالم",
    "Category:Argentine songwriters": "تصنيف:كتاب أغان أرجنتينيون",
    "Category:Books about automobiles": "تصنيف:كتب عن سيارات",
    "Category:British editorial cartoonists": "تصنيف:محررون كارتونيون بريطانيون",
    "Category:British television chefs": "تصنيف:طباخو تلفاز بريطانيون",
    "Category:Cartoonists by publication": "تصنيف:رسامو كارتون حسب المؤسسة",
    "Category:Characters in children's literature": "تصنيف:شخصيات في أدب الأطفال",
    "Category:Comedy anime and manga": "تصنيف:أنمي ومانغا كوميدية",
    "Category:Comedy films by genre": "تصنيف:أفلام كوميدية حسب النوع الفني",
    "Category:Comics adapted into films": "تصنيف:قصص مصورة تم تحويلها إلى أفلام",
    "Category:Comics based on films": "تصنيف:قصص مصورة مبنية على أفلام",
    "Category:Crime anime and manga": "تصنيف:أنمي ومانغا جريمة",
    "Category:Crime films by genre": "تصنيف:أفلام جريمة حسب النوع الفني",
    "Category:Dark fantasy video games": "تصنيف:ألعاب فيديو فانتازيا مظلمة",
    "Category:Dinosaurs in fiction": "تصنيف:ديناصورات في الخيال",
    "Category:Dinosaurs in video games": "تصنيف:ديناصورات في ألعاب فيديو",
    "Category:Disney animated films": "تصنيف:أفلام رسوم متحركة ديزني",
    "Category:Documentary films by genre": "تصنيف:أفلام وثائقية حسب النوع الفني",
    "Category:Drama anime and manga": "تصنيف:أنمي ومانغا درامية",
    "Category:Drama films by genre": "تصنيف:أفلام درامية حسب النوع الفني",
    "Category:Editorial cartoonists from Northern Ireland": "تصنيف:محررون كارتونيون من أيرلندا الشمالية",
    "Category:Erotic films by genre": "تصنيف:أفلام إغرائية حسب النوع الفني",
    "Category:Fantasy anime and manga": "تصنيف:أنمي ومانغا فانتازيا",
    "Category:Fantasy films by genre": "تصنيف:أفلام فانتازيا حسب النوع الفني",
    "Category:Fantasy video games": "تصنيف:ألعاب فيديو فانتازيا",
    "Category:Female comics writers": "تصنيف:كاتبات قصص مصورة",
    "Category:Figure skating films": "تصنيف:أفلام تزلج فني",
    "Category:Figure skating media": "تصنيف:إعلام تزلج فني",
    "Category:Figure skating on television": "تصنيف:التزلج الفني على التلفاز",
    "Category:Films about Olympic boxing": "تصنيف:أفلام عن بوكسينغ أولمبي",
    "Category:Films about Olympic figure skating": "تصنيف:أفلام عن تزلج فني أولمبي",
    "Category:Films about Olympic gymnastics": "تصنيف:أفلام عن جمباز أولمبي",
    "Category:Films about Olympic skiing": "تصنيف:أفلام عن تزلج أولمبي",
    "Category:Films about Olympic swimming and diving": "تصنيف:أفلام عن سباحة أولمبية والغطس",
    "Category:Films about Olympic track and field": "تصنيف:أفلام عن سباقات مضمار وميدان أولمبي",
    "Category:Films about automobiles": "تصنيف:أفلام عن سيارات",
    "Category:Films about the Olympic Games by athletic event": "تصنيف:أفلام عن الألعاب الأولمبية حسب حدث ألعاب القوى",
    "Category:Films based on American comics": "تصنيف:أفلام مبنية على قصص مصورة أمريكية",
    "Category:Films based on comics": "تصنيف:أفلام مبنية على قصص مصورة",
    "Category:Films based on television series": "تصنيف:أفلام مبنية على مسلسلات تلفزيونية",
    "Category:Films by audience": "تصنيف:أفلام حسب الجمهور",
    "Category:Films by continent": "تصنيف:أفلام حسب القارة",
    "Category:Films by culture": "تصنيف:أفلام حسب الثقافة",
    "Category:Films by date": "تصنيف:أفلام حسب التاريخ",
    "Category:Films by director": "تصنيف:أفلام حسب المخرج",
    "Category:Films by genre": "تصنيف:أفلام حسب النوع الفني",
    "Category:Films by language": "تصنيف:أفلام حسب اللغة",
    "Category:Films by movement": "تصنيف:أفلام حسب الحركة",
    "Category:Films by producer": "تصنيف:أفلام حسب المنتج",
    "Category:Films by setting": "تصنيف:أفلام حسب موقع الأحداث",
    "Category:Films by shooting location": "تصنيف:أفلام حسب موقع التصوير",
    "Category:Films by source": "تصنيف:أفلام حسب المصدر",
    "Category:Films by studio": "تصنيف:أفلام حسب استوديو الإنتاج",
    "Category:Films by technology": "تصنيف:أفلام حسب التكنولوجيا",
    "Category:Films by topic": "تصنيف:أفلام حسب الموضوع",
    "Category:Films by type": "تصنيف:أفلام حسب الفئة",
    "Category:Films set in national parks": "تصنيف:أفلام تقع أحداثها في متنزهات وطنية",
    "Category:French comic strips": "تصنيف:شرائط مصورة فرنسية",
    "Category:French comic": "تصنيف:قصص مصورة فرنسية",
    "Category:Historical anime and manga": "تصنيف:أنمي ومانغا تاريخية",
    "Category:Historical comics": "تصنيف:قصص مصورة تاريخية",
    "Category:Historical fiction by setting": "تصنيف:خيال تاريخي حسب موقع الأحداث",
    "Category:Historical television series": "تصنيف:مسلسلات تلفزيونية تاريخية",
    "Category:Horror anime and manga": "تصنيف:أنمي ومانغا رعب",
    "Category:Horror films by genre": "تصنيف:أفلام رعب حسب النوع الفني",
    "Category:LGBT-related films by genre": "تصنيف:أفلام متعلقة بإل جي بي تي حسب النوع الفني",
    "Category:Lists of British television series characters by series": "تصنيف:قوائم شخصيات مسلسلات تلفزيونية بريطانية حسب السلسلة",
    "Category:Lists of television characters by series": "تصنيف:قوائم شخصيات تلفزيونية حسب السلسلة",
    "Category:Magical girl anime and manga": "تصنيف:أنمي ومانغا فتاة ساحرة",
    "Category:Martial arts anime and manga": "تصنيف:أنمي ومانغا فنون قتالية",
    "Category:Mecha anime and manga": "تصنيف:أنمي ميكا",
    "Category:Musical films by genre": "تصنيف:أفلام موسيقية حسب النوع الفني",
    "Category:Mystery anime and manga": "تصنيف:أنمي ومانغا غموض",
    "Category:Mystery films by genre": "تصنيف:أفلام غموض حسب النوع الفني",
    "Category:Participants in British reality television series": "تصنيف:مشاركون في مسلسلات تلفزيونية واقعية بريطانية",
    "Category:Peruvian television actors": "تصنيف:ممثلو تلفزيون بيرويون",
    "Category:Philippine films by subgenre": "تصنيف:أفلام فلبينية حسب النوع الفرعي",
    "Category:Political films by genre": "تصنيف:أفلام سياسية حسب النوع الفني",
    "Category:Pornographic films by genre": "تصنيف:أفلام إباحية حسب النوع الفني",
    "Category:Romance anime and manga": "تصنيف:أنمي ومانغا رومانسية",
    "Category:Romance films by genre": "تصنيف:أفلام رومانسية حسب النوع الفني",
    "Category:Science fiction anime and manga": "تصنيف:أنمي ومانغا خيال علمي",
    "Category:Science fiction films by genre": "تصنيف:أفلام خيال علمي حسب النوع الفني",
    "Category:Songs about automobiles": "تصنيف:أغاني عن سيارات",
    "Category:South Korean television series by production location": "تصنيف:مسلسلات تلفزيونية كورية جنوبية حسب موقع الإنتاج",
    "Category:Sports anime and manga": "تصنيف:أنمي ومانغا رياضية",
    "Category:Sports films by genre": "تصنيف:أفلام رياضية حسب النوع الفني",
    "Category:Spy anime and manga": "تصنيف:أنمي ومانغا تجسسية",
    "Category:Spy films by genre": "تصنيف:أفلام تجسسية حسب النوع الفني",
    "Category:Superhero anime and manga": "تصنيف:أنمي ومانغا خارقة",
    "Category:Supernatural anime and manga": "تصنيف:أنمي ومانغا خارقة للطبيعة",
    "Category:Teen films by genre": "تصنيف:أفلام مراهقة حسب النوع الفني",
    "Category:Television characters by series": "تصنيف:شخصيات تلفزيونية حسب السلسلة",
    "Category:Television programs by geographic setting": "تصنيف:برامج تلفزيونية حسب الموقع الجغرافي للأحداث",
    "Category:Television series produced in Alberta": "تصنيف:مسلسلات تلفزيونية أنتجت في ألبرتا",
    "Category:Television series produced in Seoul": "تصنيف:مسلسلات تلفزيونية أنتجت في سول",
    "Category:Television shows filmed in Algeria": "تصنيف:عروض تلفزيونية صورت في الجزائر",
    "Category:Thriller anime and manga": "تصنيف:أنمي ومانغا إثارة",
    "Category:Thriller films by genre": "تصنيف:أفلام إثارة حسب النوع الفني",
    "Category:Video games about diseases": "تصنيف:ألعاب فيديو عن الأمراض",
    "Category:Video games about slavery": "تصنيف:ألعاب فيديو عن العبودية",
    "Category:Video games based on Egyptian mythology": "تصنيف:ألعاب فيديو مبنية على أساطير مصرية",
    "Category:Video games based on mythology": "تصنيف:ألعاب فيديو مبنية على أساطير",
    "Category:Video games set in prehistory": "تصنيف:ألعاب فيديو تقع أحداثها في ما قبل التاريخ",
    "Category:Video games set in the Byzantine Empire": "تصنيف:ألعاب فيديو تقع أحداثها في الإمبراطورية البيزنطية",
    "Category:War anime and manga": "تصنيف:أنمي ومانغا حربية",
    "Category:War films by genre": "تصنيف:أفلام حربية حسب النوع الفني",
    "Category:Works about automobiles": "تصنيف:أعمال عن سيارات",
    "Category:Works adapted for other media": "تصنيف:أعمال تم تحويلها إلى وسائط أخرى",
    "Category:songs about busan": "تصنيف:أغاني عن بوسان",
}


def test_entertainment():
    print(f"len of data: {len(data)}")
    org, diff = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff, "entertainment")

    assert diff == org, f"Differences found: {len(diff)}"


@pytest.mark.skip("Need to fix")
def test_entertainment_2():
    data2 = {
        "Category:documentary filmmakers by nationality": "تصنيف:صانعو أفلام وثائقية حسب الجنسية",
        "Category:yemeni war filmmakers": "تصنيف:صانعو أفلام حربية يمنيون",
        "Category:Peruvian documentary film directors": "تصنيف:مخرجو أفلام وثائقية بيروفيون",
        "Category:Lists of action television characters by series": "تصنيف:قوائم شخصيات تلفزيونية حركة حسب السلسلة",
        "Category:Holocaust literature": "تصنيف:أدب هولوكوست",
        "Category:Drama television characters by series": "تصنيف:شخصيات تلفزيونية درامية حسب السلسلة",
        "Category:Fantasy television characters by series": "تصنيف:شخصيات تلفزيونية فانتازيا حسب السلسلة"
    }

    print(f"len of data: {len(data2)}")
    org, diff = ye_test_one_dataset(data2, new_func_lab_final_label)

    dump_diff(diff, "entertainment2")

    assert diff == org, f"Differences found: {len(diff)}"
