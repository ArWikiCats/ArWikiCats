"""
Tests
"""
import pytest
from ArWikiCats import resolve_label_ar
# from utils.dump_runner import s
from load_one_data import one_dump_test, dump_same_and_not_same, dump_diff_text

test_data = {
    "12th-century deaths from infectious disease": "وفيات القرن 12 من أمراض معدية",
    "14th-century writers from the Crown of Aragon": "كتاب من تاج أرغون القرن 14",
    "17th-century women from the Republic of Venice": "نساء من جمهورية البندقية القرن 17",
    "18th-century clergy from the Republic of Geneva": "رجال دين من جمهورية جنيف القرن 18",
    "1966 British Empire and Commonwealth Games venues": "الإمبراطورية البريطانية وملاعب ألعاب الكومنولث 1966",
    "1988 war films": "أفلام حربية في 1988",
    "2010s supernatural thriller films": "أفلام خارقة للطبيعة إثارة عقد 2010",
    "2011 in film by country": "الأفلام في 2011 حسب البلد",
    "2022 Women's Africa Cup of Nations": "كأس إفريقيا نسائية في بلدان 2022",
    "20th-century Danish sportsmen": "رياضيون رجال دنماركيون في القرن 20",
    "21st-century Canadian federal election candidates": "مرشحو الانتخابات الفيدرالية الكندية القرن 21",
    "21st-century Indian murderers": "قتلة هنود في القرن 21",
    "21st-century Ohio politicians": "سياسيو أوهايو القرن 21",
    "Accidental deaths from falls in the United Kingdom": "وفيات عرضية من فالز في المملكة المتحدة",
    "African pan-Africanists": "وحدويون أفارقة أفارقة",
    "American expatriate actresses in India": "ممثلات مغتربات أمريكيات في الهند",
    "American people executed for robbery": "أعلام أمريكيون أعدموا بتهمة السرقة",
    "American scholars of ancient Greek philosophy": "دارسون أمريكيون في فلسفة يونانية قديمة",
    "Asian Games footballers for Chinese Taipei": "لاعبو كرة قدم في الألعاب الآسيوية في تايبيه الصينية",
    "Australian expatriate actresses in India": "ممثلات مغتربات أستراليات في الهند",
    "British people executed for theft": "أعلام بريطانيون أعدموا بتهمة سرقة",
    "Candidates in the 2025 Canadian federal election": "مرشحون في الانتخابات الفيدرالية الكندية 2025",
    "Caribbean Series managers": "مدربو مسلسلات كاريبية",
    "Chancellors of the University of the Witwatersrand": "مستشاري من جامعة ويتواترسراند",
    "Children's crime films": "أفلام أطفال جريمة",
    "Constituencies of the National Assembly (South Korea)": "دوائر إنتخابية في الجمعية الوطنية (كوريا الجنوبية)",
    "Environment and climate change ministers of Qatar": "البيئة ووزراء تغير المناخ في قطر",
    "Executed people from Gansu": "أشخاص أعدموا من قانسو",
    "Fantasy adventure novels": "روايات فانتازيا مغامرات",
    "Film characters introduced in 1999": "شخصيات أفلام عرضت في 1999",
    "Games and sports introduced in 2026": "ألعاب وألعاب رياضية عرضت في 2026",
    "Haitian people with disabilities": "أعلام هايتيون",
    "Judges in Canadian reality television series": "قضاة في مسلسلات تلفزيونية واقعية كندية",
    "Lists of American reality television series episodes": "حلقات قوائم مسلسلات تلفزيونية واقعية أمريكية",
    "Male adult models": "عارضون بالغون ذكور",
    "Members of the Democratic Socialists of America from New York (state)": "أعضاء اشتراكيون ديمقراطيون من أمريكا من ولاية نيويورك",
    "Members of the Democratic Socialists of America from Pennsylvania": "أعضاء اشتراكيون ديمقراطيون من أمريكا من بنسلفانيا",
    "Members of the National Council (Switzerland) 1999–2003": "أعضاء المجلس الوطني (سويسرا) 2000–2003",
    "October 1970 in sports": "أحداث ألعاب رياضية أكتوبر 1970",
    "Pan American Games bronze medalists for Canada in athletics (track and field)": "فائزون بميداليات برونزية دورة الألعاب الأمريكية من كندا في ألعاب قوى المضمار والميدان",
    "Pan American Games gold medalists for Canada in athletics (track and field)": "فائزون بميداليات ذهبية دورة الألعاب الأمريكية من كندا في ألعاب قوى المضمار والميدان",
    "Pan American Games silver medalists for Canada in athletics (track and field)": "فائزون بميداليات فضية دورة الألعاب الأمريكية من كندا في ألعاب قوى المضمار والميدان",
    "People from the Province of Huesca": "أشخاص من وشقة (مقاطعة)",
    "Philosophers of technology": "فلاسفة تقنية (تكنولوجيا)",
    "Poetry of Georgia (country)": "شعر في جورجيا",
    "Polish sportspeople by voivodeship and populated place": "رياضيون بولنديون حسب الفويفود والمكان المأهول",
    "Prisoners sentenced to death by the British military": "مسجونون حكم عليهم بالإعدام بواسطة الجيش البريطاني",
    "Prisoners sentenced to death by the United Kingdom": "مسجونون حكم عليهم بالإعدام بواسطة المملكة المتحدة",
    "Relationships of Jeffrey Epstein": "علاقات في جيفري إبستاين",
    "Scholars of ancient Greek history": "دارسون من تاريخ يوناني قديم",
    "Scholars of ancient Greek philosophy by nationality": "دارسون من فلسفة يونانية قديمة حسب الجنسية",
    "Secretaries of health of the Philippines": "أمناء من الصحة في الفلبين",
    "Secretaries of state of France": "وزير خارجية فرنسا",
    "Secretaries of the Australian Department of Defence": "وزراء في وزارة الدفاع الأسترالية",
    "Slaves from the Mamluk Sultanate": "العبيد من مماليك مصر",
    "Somalian people with disabilities": "أعلام صوماليون",
    "Songs from The Sound of Music": "أغان من ناطق في موسيقى",
    "Speculative crime and thriller fiction novels": "جريمة تأملية وروايات إثارة خيالية",
    "Supernatural slasher films": "أفلام خارقة للطبيعة تقطيع",
    "United States under secretaries of agriculture": "الولايات المتحدة تحت وزراء زراعة",
    "Women's handball players": "لاعبو كرة يد نسائية",
    "Women's National Basketball Association players from Belgium": "لاعبو الاتحاد الوطني لكرة السلة النسائية من بلجيكا",
    "YouTubers with disabilities": "مشاهير يوتيوب بإعاقات",
    "11th-century people from the Republic of Venice": "أشخاص من جمهورية البندقية القرن 11",
}


@pytest.mark.parametrize("category,expected", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_move_by_in(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


# test_dump_all = make_dump_test_name_data([("test_data", test_data)], callback=resolve_label_ar, run_same=True)

TEMPORAL_CASES = [
    ("test_data", test_data, resolve_label_ar),
]


@pytest.mark.parametrize("name,data,callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback: callable) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff_text(expected, diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
