#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data1 = {
    "african championships in athletics": "تصنيف:بطولات إفريقية في ألعاب القوى",
    "automotive industry in italy": "تصنيف:صناعة سيارات في إيطاليا",
    "bahrain in the asian para games": "تصنيف:البحرين في دورة الألعاب الآسيوية البارالمبية",
    "field hockey in the 2004 summer olympics": "تصنيف:هوكي الميدان في الألعاب الأولمبية الصيفية 2004",
    "gymnastics in the 2004 summer olympics": "تصنيف:الجمباز في الألعاب الأولمبية الصيفية 2004",
    "history of the petroleum industry in canada": "تصنيف:تاريخ صناعة بترولية في كندا",
    "internet in bahrain": "تصنيف:إنترنت في البحرين",
    "islam in bermuda": "تصنيف:الإسلام في برمودا",
    "kingdom of hungary in the middle ages": "تصنيف:مملكة المجر في العصور الوسطى",
    "kurds in syria": "تصنيف:الأكراد في سوريا",
    "kurds in turkey": "تصنيف:الأكراد في تركيا",
    "protestantism in morocco": "تصنيف:البروتستانتية في المغرب",
    "protestantism in yemen": "تصنيف:البروتستانتية في اليمن",
    "same-sex marriage in the netherlands": "تصنيف:زواج مثلي في هولندا",
    "shia islam in afghanistan": "تصنيف:الشيعة في أفغانستان",
    "shooting in the 2004 summer olympics": "تصنيف:الرماية في الألعاب الأولمبية الصيفية 2004",
    "silver mining in the united states": "تصنيف:التنقيب عن الفضة في الولايات المتحدة",
    "swimming in the 2004 summer olympics": "تصنيف:السباحة في الألعاب الأولمبية الصيفية 2004",
    "synchronized swimming in the 2004 summer olympics": "تصنيف:السباحة المتزامنة في الألعاب الأولمبية الصيفية 2004",
    "taekwondo in the 2004 summer olympics": "تصنيف:تايكوندو في الألعاب الأولمبية الصيفية 2004",
    "time in azerbaijan": "تصنيف:الزمن في أذربيجان",
    "time in cyprus": "تصنيف:الزمن في قبرص",
    "triathlon in the 2004 summer olympics": "تصنيف:السباق الثلاثي في الألعاب الأولمبية الصيفية 2004",
    "video gaming in south africa": "تصنيف:ألعاب الفيديو في جنوب إفريقيا",
    "women in niue": "تصنيف:المرأة في نييوي",
    "women in pala": "تصنيف:المرأة في بالاو",
    "women in the cook islands": "تصنيف:المرأة في جزر كوك",
    "women in the federated states of micronesia": "تصنيف:المرأة في ولايات ميكرونيسيا المتحدة",
    "women in the federated states-of micronesia": "تصنيف:المرأة في ولايات ميكرونيسيا المتحدة",
    "wrestling in the 2004 summer olympics": "تصنيف:المصارعة في الألعاب الأولمبية الصيفية 2004",
    "wrestling in the 2016 summer olympics": "تصنيف:المصارعة في الألعاب الأولمبية الصيفية 2016",
}
data_2 = {
    "al-qaeda in the arabian peninsula": "تنظيم القاعدة في جزيرة العرب",
    "anti-jewish pogroms in the russian empire": "برنامج إبادة اليهود في روسيا القيصرية",
    "catholic church in algeria": "المسيحية في الجزائر",
    "enlightenment in spain": "التنوير في إسبانيا",
    "feminism in japan": "الحركة النسائية في اليابان",
    "french mandate for syria and the lebanon": "الانتداب الفرنسي على سوريا ولبنان",
    "french protectorate in morocco": "الحماية الفرنسية على المغرب",
    "ghost in the shell": "شبح في الهيكل",
    "government shutdowns in the united states": "تعطل الحكومة عن العمل",
    "irreligion in egypt": "اللادين في مصر",
    "jack in the box": "جاك إن ذا بوكس",
    "kazakhs in china": "كازاخ الصين",
    "orthodox church in america": "الكنيسة الأرثوذكسية في أمريكا",
    "palestinians in syria": "فلسطينيو سوريا",
    "refugee olympic team in the 2016 summer olympics": "فريق الرياضيين الأولمبيين اللاجئين في الألعاب الأولمبية الصيفية 2016",
    "spanish protectorate in morocco": "حماية إسبانيا في المغرب",
    "territory of the military commander in serbia": "إقليم القائد العسكري في صربيا",
    "water supply and sanitation in egypt": "سياسة مصر المائية",
    "world junior championships in athletics": "بطولة العالم للناشئين لألعاب القوى",
}
to_test = [
    ("test_1", data1),
    # ("test_2", data_2),
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
