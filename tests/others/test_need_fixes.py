"""
Tests
"""
import pytest
from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

test_data_0 = {
    "Slaves from the Mamluk Sultanate": "عبيد من مماليك مصر",
    "Philosophers of technology": "فلاسفة تقنية (تكنولوجيا)",
}

test_data_1 = {
    "1988 war films": "أفلام حربية في 1988",
    "2011 in film by country": "الأفلام في 2011 حسب البلد",
    "20th-century Danish sportsmen": "رياضيون رجال دنماركيون في القرن 20",
    "21st-century Indian murderers": "قتلة هنود في القرن 21",
    "African pan-Africanists": "وحدويون أفارقة أفارقة",
    "American expatriate actresses in India": "ممثلات مغتربات أمريكيات في الهند",
    "American scholars of ancient Greek philosophy": "دارسون أمريكيون في فلسفة يونانية قديمة",
    "Asian Games footballers for Chinese Taipei": "لاعبو كرة قدم في الألعاب الآسيوية في تايبيه الصينية",
    "Australian expatriate actresses in India": "ممثلات مغتربات أستراليات في الهند",
    "Candidates in the 2025 Canadian federal election": "مرشحون في الانتخابات الفيدرالية الكندية 2025",
    "Children's crime films": "أفلام أطفال جريمة",
    "Constituencies of the National Assembly (South Korea)": "دوائر إنتخابية في الجمعية الوطنية (كوريا الجنوبية)",
    "Fantasy adventure novels": "روايات فانتازيا مغامرات",
    "Film characters introduced in 1999": "شخصيات أفلام عرضت في 1999",
    "Judges in Canadian reality television series": "قضاة في مسلسلات تلفزيونية واقعية كندية",
    "Male adult models": "عارضون بالغون ذكور",
    "Members of the Democratic Socialists of America from New York (state)": "أعضاء اشتراكيون ديمقراطيون من أمريكا من ولاية نيويورك",
    "Members of the Democratic Socialists of America from Pennsylvania": "أعضاء اشتراكيون ديمقراطيون من أمريكا من بنسلفانيا",
    "People from the Province of Huesca": "أشخاص من وشقة (مقاطعة)",
    "Poetry of Georgia (country)": "شعر في جورجيا",
    "Polish sportspeople by voivodeship and populated place": "رياضيون بولنديون حسب الفويفود والمكان المأهول",
    "Prisoners sentenced to death by the British military": "مسجونون حكم عليهم بالإعدام بواسطة الجيش البريطاني",
    "Prisoners sentenced to death by the United Kingdom": "مسجونون حكم عليهم بالإعدام بواسطة المملكة المتحدة",
    "Scholars of ancient Greek history": "دارسون من تاريخ يوناني قديم",
    "Scholars of ancient Greek philosophy by nationality": "دارسون من فلسفة يونانية قديمة حسب الجنسية",
    "YouTubers with disabilities": "مشاهير يوتيوب بإعاقات",
    "12th-century deaths from infectious disease": "وفيات بسبب أمراض معدية في القرن 12",
    "14th-century writers from the Crown of Aragon": "كتاب من تاج أرغون في القرن 14",
    "17th-century women from the Republic of Venice": "نساء من جمهورية البندقية في القرن 17",
    "18th-century clergy from the Republic of Geneva": "رجال دين من جمهورية جنيف في القرن 18",
    "2010s supernatural thriller films": "أفلام إثارة خارقة للطبيعة في عقد 2010",
    "2022 Women's Africa Cup of Nations": "كأس الأمم الإفريقية للسيدات 2022",
    "Accidental deaths from falls in the United Kingdom": "وفيات عرضية نتيجة السقوط في المملكة المتحدة",
    "American people executed for robbery": "أمريكيون أعدموا بتهمة السرقة",
    "Environment and climate change ministers of Qatar": "وزراء بيئة وتغير المناخ قطر",
    "Haitian people with disabilities": "هايتيون بإعاقات",
    "Lists of American reality television series episodes": "قوائم حلقات مسلسلات تلفزيونية واقعية أمريكية",
    "Members of the National Council (Switzerland) 1999–2003": "أعضاء المجلس الوطني (سويسرا) 1999–2003",
    "October 1970 in sports": "ألعاب رياضية في أكتوبر 1970",
    "Pan American Games bronze medalists for Canada in athletics (track and field)": "فائزون بميداليات برونزية في دورة الألعاب الأمريكية من كندا في ألعاب قوى المضمار والميدان",
    "Pan American Games gold medalists for Canada in athletics (track and field)": "فائزون بميداليات ذهبية في دورة الألعاب الأمريكية من كندا في ألعاب قوى المضمار والميدان",
    "Pan American Games silver medalists for Canada in athletics (track and field)": "فائزون بميداليات فضية في دورة الألعاب الأمريكية من كندا في ألعاب قوى المضمار والميدان",
    "Relationships of Jeffrey Epstein": "علاقات جيفري إبستين",
    "Secretaries of health of the Philippines": "وزراء صحة فلبينيون",
    "Secretaries of state of France": "وزراء خارجية فرنسيون",
    "Secretaries of the Australian Department of Defence": "وزراء دفاع أستراليون",
    "Somalian people with disabilities": "صوماليون بإعاقات",
    "Supernatural slasher films": "أفلام تقطيع خارقة للطبيعة",
    "United States under secretaries of agriculture": "نواب وزير الزراعة الأمريكي للشؤون المتخصصة",
    "Women's handball players": "لاعبات كرة يد",
    "Women's National Basketball Association players from Belgium": "لاعبات الاتحاد الوطني لكرة السلة للسيدات من بلجيكا",
    "11th-century people from the Republic of Venice": "أشخاص من جمهورية البندقية في القرن 11",
}


@pytest.mark.parametrize("category,expected", test_data_1.items(), ids=test_data_1.keys())
@pytest.mark.fast
def test_move_by_in(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_data", test_data_1),
]

test_dump_all = make_dump_test_name_data(TEMPORAL_CASES, callback=resolve_label_ar, run_same=True)
