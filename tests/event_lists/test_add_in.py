#
import pytest

from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset, dump_diff

examples = {
    'Category:18th-century Dutch explorers': 'تصنيف:مستكشفون هولنديون في القرن 18',
    "Category:20th-century Albanian sports coaches": "تصنيف:مدربو رياضة ألبان في القرن 20",

    'Category:00s establishments in the Roman Empire': 'تصنيف:تأسيسات عقد 00 في الإمبراطورية الرومانية',
    'Category:1000 disestablishments by country': 'تصنيف:انحلالات سنة 1000 حسب البلد',
    'Category:1000 disestablishments in Europe': 'تصنيف:انحلالات سنة 1000 في أوروبا',
    'Category:1000s disestablishments in Asia': 'تصنيف:انحلالات عقد 1000 في آسيا',
    'Category:10th-century BC architecture': 'تصنيف:عمارة القرن 10 ق م',
    'Category:1370s conflicts': 'تصنيف:نزاعات عقد 1370',
    'Category:13th century establishments in the Roman Empire': 'تصنيف:تأسيسات القرن 13 في الإمبراطورية الرومانية',
    'Category:14th-century establishments in India': 'تصنيف:تأسيسات القرن 14 في الهند',
    'Category:1902 films': 'تصنيف:أفلام إنتاج 1902',
    'Category:1950s criminal comedy films': 'تصنيف:أفلام كوميديا الجريمة عقد 1950',
    'Category:1960s black comedy films': 'تصنيف:أفلام كوميدية سوداء عقد 1960',
    'Category:1960s criminal comedy films': 'تصنيف:أفلام كوميديا الجريمة عقد 1960',
    'Category:1970s black comedy films': 'تصنيف:أفلام كوميدية سوداء عقد 1970',
    'Category:1970s criminal comedy films': 'تصنيف:أفلام كوميديا الجريمة عقد 1970',
    'Category:1980 sports events in Europe': 'تصنيف:أحداث 1980 الرياضية في أوروبا',
    'Category:1980s black comedy films': 'تصنيف:أفلام كوميدية سوداء عقد 1980',
    'Category:1980s criminal comedy films': 'تصنيف:أفلام كوميديا الجريمة عقد 1980',
    'Category:1990s BC disestablishments in Asia': 'تصنيف:انحلالات عقد 1990 ق م في آسيا',
    'Category:1990s disestablishments in Europe': 'تصنيف:انحلالات عقد 1990 في أوروبا',
    'Category:1994–95 in European rugby union by country': 'تصنيف:اتحاد الرجبي الأوروبي في 1994–95 حسب البلد',
    'Category:19th-century actors': 'تصنيف:ممثلون في القرن 19',
    'Category:19th-century publications': 'تصنيف:منشورات القرن 19',
    'Category:1st century BC': 'تصنيف:القرن 1 ق م',
    'Category:1st-century architecture': 'تصنيف:عمارة القرن 1',
    'Category:1st-millennium architecture': 'تصنيف:عمارة الألفية 1',
    'Category:1st-millennium literature': 'تصنيف:أدب الألفية 1',
    'Category:2000s American films': 'تصنيف:أفلام أمريكية في عقد 2000',
    'Category:2000s films': 'تصنيف:أفلام إنتاج عقد 2000',
    'Category:2000s in American cinema': 'تصنيف:السينما الأمريكية في عقد 2000',
    'Category:2000s in film': 'تصنيف:عقد 2000 في الأفلام',
    'Category:2006 Winter Paralympics events': 'تصنيف:أحداث الألعاب البارالمبية الشتوية 2006',
    'Category:2006 establishments by country': 'تصنيف:تأسيسات سنة 2006 حسب البلد',
    'Category:2006 in Northern Ireland sport': 'تصنيف:رياضة أيرلندية شمالية في 2006',
    'Category:2006 in north korean sport': 'تصنيف:رياضة كورية شمالية في 2006',
    'Category:2017 American television series debuts': 'تصنيف:مسلسلات تلفزيونية أمريكية بدأ عرضها في 2017',
    'Category:2017 American television series endings': 'تصنيف:مسلسلات تلفزيونية أمريكية انتهت في 2017',
    'Category:2017 events by country': 'تصنيف:أحداث 2017 حسب البلد',
    'Category:2017 events': 'تصنيف:أحداث 2017',
    'Category:2017 in Emirati football': 'تصنيف:كرة القدم الإماراتية في 2017',
    'Category:2017–18 in Emirati football': 'تصنيف:كرة القدم الإماراتية في 2017–18',
    'Category:2018 Summer Youth Olympics events': 'تصنيف:أحداث الألعاب الأولمبية الشبابية الصيفية 2018',
    'Category:20th-century disestablishments in India': 'تصنيف:انحلالات القرن 20 في الهند',
    'Category:21st century in film': 'تصنيف:القرن 21 في الأفلام',
    'Category:21st-century films': 'تصنيف:أفلام القرن 21',
    'Category:440s bc': 'تصنيف:عقد 440 ق م',
    'Category:440s': 'تصنيف:عقد 440',
    'Category:977 by country': 'تصنيف:977 حسب البلد',
    'Category:Airlines by year of establishment': 'تصنيف:شركات طيران حسب سنة التأسيس',
    'Category:American cinema by decade': 'تصنيف:السينما الأمريكية حسب العقد',
    'Category:Animals by year of formal description': 'تصنيف:حيوانات حسب سنة الوصف',
    'Category:April 1983 events in Europe': 'تصنيف:أحداث أبريل 1983 في أوروبا',
    'Category:Comics set in the 1st century BC': 'تصنيف:قصص مصورة تقع أحداثها في القرن 1 ق م',
    'Category:Decades by country': 'تصنيف:عقود حسب البلد',
    'Category:Decades in Oklahoma': 'تصنيف:عقود في أوكلاهوما',
    'Category:Decades in the United States by state': 'تصنيف:عقود في الولايات المتحدة حسب الولاية',
    'Category:Films set in the 21st century': 'تصنيف:أفلام تقع أحداثها في القرن 21',
    'Category:Historical webcomics': 'تصنيف:ويب كومكس تاريخية',
    'Category:July 2018 events by continent': 'تصنيف:أحداث يوليو 2018 حسب القارة',
    'Category:Mammals by century of formal description': 'تصنيف:ثدييات حسب قرن الوصف',
    'Category:Multi-sport events in the Soviet Union': 'تصنيف:أحداث رياضية متعددة في الاتحاد السوفيتي',
    'Category:November 2006 in Yemen': 'تصنيف:نوفمبر 2006 في اليمن',
    'Category:Olympic figure skaters by year': 'تصنيف:متزلجون فنيون أولمبيون حسب السنة',
    'Category:Publications by year of disestablishment': 'تصنيف:منشورات حسب سنة الانحلال',
    'Category:Publications by year of establishment': 'تصنيف:منشورات حسب سنة التأسيس',
    'Category:Sports organisations by decade of establishment': 'تصنيف:منظمات رياضية حسب عقد التأسيس',
    'Category:Television series endings by year': 'تصنيف:مسلسلات تلفزيونية حسب سنة انتهاء العرض',
    'Category:Tetrapods by century of formal description': 'تصنيف:رباعيات الأطراف حسب قرن الوصف',
    'Category:Vertebrates described in the 20th century': 'تصنيف:فقاريات وصفت في القرن 20',
    'Category:Years in north korean television': 'تصنيف:سنوات في التلفزة الكورية الشمالية',
    'Category:Years in the United States by state': 'تصنيف:سنوات في الولايات المتحدة حسب الولاية',
    'Category:multi-sport events at Yemen': 'تصنيف:أحداث رياضية متعددة في اليمن',
}

TEMPORAL_CASES = [
    ("temporal_1", examples),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
def _test_temporal(name, data):
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.parametrize(
    "category, expected",
    examples.items(),
    ids=[k for k in examples],
)
def test_add_in(category: str, expected: str) -> None:

    assert new_func_lab_final_label(category) == expected
