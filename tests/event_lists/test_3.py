#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data1 = {
    "african championships in athletics": "بطولة إفريقيا لألعاب القوى",
    "al-qaeda in the arabian peninsula": "تنظيم القاعدة في جزيرة العرب",
    "anti-jewish pogroms in the russian empire": "برنامج إبادة اليهود في روسيا القيصرية",
    "automotive industry in italy": "صناعة السيارات في إيطاليا",
    "bahrain in the asian para games": "البحرين في دورة الألعاب الآسيوية البارالمبية",
    "catholic church in algeria": "المسيحية في الجزائر",
    "enlightenment in spain": "التنوير في إسبانيا",
    "feminism in japan": "الحركة النسائية في اليابان",
    "field hockey in the 2004 summer olympics": "هوكي الساحة في أولمبياد 2004",
    "french mandate for syria and the lebanon": "الانتداب الفرنسي على سوريا ولبنان",
    "french protectorate in morocco": "الحماية الفرنسية على المغرب",
    "ghost in the shell": "شبح في الهيكل",
    "government shutdowns in the united states": "تعطل الحكومة عن العمل",
    "gymnastics in the 2004 summer olympics": "الجمباز في أولمبياد 2004",
    "history of the petroleum industry in canada": "تاريخ صناعة البترول في كندا",
    "internet in bahrain": "الإنترنت في البحرين",
    "irreligion in egypt": "اللادين في مصر",
    "islam in bermuda": "الإسلام في برمودا",
    "jack in the box": "جاك إن ذا بوكس",
    "kazakhs in china": "كازاخ الصين",
    "kingdom of hungary in the middle ages": "مملكة المجر في العصور الوسطى",
    "kurds in syria": "أكراد سوريا",
    "kurds in turkey": "أكراد تركيا",
    "orthodox church in america": "الكنيسة الأرثوذكسية في أمريكا",
    "palestinians in syria": "فلسطينيو سوريا",
    "protestantism in morocco": "البروتستانتية في المغرب",
    "protestantism in yemen": "البروتستانتية في اليمن",
    "refugee olympic team in the 2016 summer olympics": "فريق الرياضيين الأولمبيين اللاجئين في الألعاب الأولمبية الصيفية 2016",
    "same-sex marriage in the netherlands": "زواج المثليين في هولندا",
    "shia islam in afghanistan": "الشيعة في أفغانستان",
    "shooting in the 2004 summer olympics": "الرماية في أولمبياد 2004",
    "silver mining in the united states": "التنقيب عن الفضة في الولايات المتحدة",
    "spanish protectorate in morocco": "حماية إسبانيا في المغرب",
    "swimming in the 2004 summer olympics": "السباحة في أولمبياد 2004",
    "synchronized swimming in the 2004 summer olympics": "سباحة إيقاعية في أولمبياد 2004",
    "taekwondo in the 2004 summer olympics": "التايكواندو في أولمبياد 2004",
    "territory of the military commander in serbia": "إقليم القائد العسكري في صربيا",
    "time in azerbaijan": "توقيت أذربيجان",
    "time in cyprus": "توقيت قبرص",
    "triathlon in the 2004 summer olympics": "الألعاب الثلاثية في أولمبياد 2004",
    "video gaming in south africa": "ألعاب الفيديو في جنوب إفريقيا",
    "water supply and sanitation in egypt": "سياسة مصر المائية",
    "women in niue": "المرأة في نييوي",
    "women in pala": "المرأة في بالاو",
    "women in the cook islands": "المرأة في جزر كوك",
    "women in the federated states of micronesia": "المرأة في ولايات ميكرونيسيا المتحدة",
    "women in the federated states-of micronesia": "المرأة في ولايات ميكرونيسيا المتحدة",
    "world junior championships in athletics": "بطولة العالم للناشئين لألعاب القوى",
    "wrestling in the 2004 summer olympics": "المصارعة في أولمبياد 2004",
    "wrestling in the 2016 summer olympics": "المصارعة في الألعاب الأولمبية الصيفية 2016",

}

to_test = [
    ("test_1", data1),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=list(data1.keys()))
@pytest.mark.fast
def test_1(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:

    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
