#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data0 = {
    "russian empire-united states relations": "العلاقات بين الإمبراطورية الروسية والولايات المتحدة",
    "south korean presidential election, 2017": "الانتخابات الرئاسية الكورية الجنوبية 2017",
    "republic of ireland women's national football team": "منتخب جمهورية أيرلندا لكرة القدم للسيدات",
}

data1 = {
    "ivorian people": "تصنيف:أعلام إيفواريون",
    "japanese lgbtq people": "تصنيف:أعلام إل جي بي تي كيو يابانيون",
    "chinese lgbtq people": "تصنيف:أعلام إل جي بي تي كيو صينيون",
    "arab lgbtq people": "تصنيف:أعلام إل جي بي تي كيو عرب",
    "rwandan political people": "تصنيف:ساسة روانديون",
    "maldivian people": "تصنيف:أعلام مالديفيون",
    "malian people": "تصنيف:أعلام ماليون",
    "maltese lgbtq people": "تصنيف:أعلام إل جي بي تي كيو مالطيون",
    "namibia–russia relations": "تصنيف:العلاقات الروسية الناميبية",
    "morocco–netherlands relations": "تصنيف:العلاقات المغربية الهولندية",
    "morocco–pakistan relations": "تصنيف:العلاقات الباكستانية المغربية",
    "morocco–qatar relations": "تصنيف:العلاقات القطرية المغربية",
    "morocco–russia relations": "تصنيف:العلاقات الروسية المغربية",
    "morocco–united kingdom relations": "تصنيف:العلاقات البريطانية المغربية",
    "mongolia–russia relations": "تصنيف:العلاقات الروسية المنغولية",
    "mauritania–morocco relations": "تصنيف:العلاقات المغربية الموريتانية",
    "mauritania–russia relations": "تصنيف:العلاقات الروسية الموريتانية",
    "south korea–united states relations": "تصنيف:العلاقات الأمريكية الكورية الجنوبية",
    "somalia–turkey relations": "تصنيف:العلاقات التركية الصومالية",
    "russia–sudan relations": "تصنيف:العلاقات الروسية السودانية",
    "russia–tunisia relations": "تصنيف:العلاقات التونسية الروسية",
    "russia–united arab emirates relations": "تصنيف:العلاقات الإماراتية الروسية",
    "russia–uzbekistan relations": "تصنيف:العلاقات الأوزبكستانية الروسية",
    "philippine–american war": "تصنيف:الحرب الأمريكية الفلبينية",
    "philippines–saudi arabia relations": "تصنيف:العلاقات السعودية الفلبينية",
    "palestine national basketball team": "تصنيف:منتخب فلسطين لكرة السلة",
    "russia men's national ice hockey team": "تصنيف:منتخب روسيا لهوكي الجليد للرجال",
    "palestine–united arab emirates relations": "تصنيف:العلاقات الإماراتية الفلسطينية",
    "palestine–united kingdom relations": "تصنيف:العلاقات البريطانية الفلسطينية",
    "palestine–uruguay relations": "تصنيف:العلاقات الأوروغويانية الفلسطينية",
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
    "taekwondo in the 2004 summer olympics": "تصنيف:التايكوندو في الألعاب الأولمبية الصيفية 2004",
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
    "saudi arabia–ukraine relations": "تصنيف:العلاقات الأوكرانية السعودية",
    "china–sudan relations": "تصنيف:العلاقات السودانية الصينية",
    "china-sudan relations": "تصنيف:العلاقات السودانية الصينية",
    "saudi arabia-ukraine relations": "تصنيف:العلاقات الأوكرانية السعودية",
    "mauritania-morocco relations": "تصنيف:العلاقات المغربية الموريتانية",
    "mauritania-russia relations": "تصنيف:العلاقات الروسية الموريتانية",
    "mongolia-russia relations": "تصنيف:العلاقات الروسية المنغولية",
    "morocco-netherlands relations": "تصنيف:العلاقات المغربية الهولندية",
    "morocco-pakistan relations": "تصنيف:العلاقات الباكستانية المغربية",
    "morocco-qatar relations": "تصنيف:العلاقات القطرية المغربية",
    "morocco-russia relations": "تصنيف:العلاقات الروسية المغربية",
    "morocco-united kingdom relations": "تصنيف:العلاقات البريطانية المغربية",
    "namibia-russia relations": "تصنيف:العلاقات الروسية الناميبية",
    "palestine-united arab emirates relations": "تصنيف:العلاقات الإماراتية الفلسطينية",
    "palestine-united kingdom relations": "تصنيف:العلاقات البريطانية الفلسطينية",
    "palestine-uruguay relations": "تصنيف:العلاقات الأوروغويانية الفلسطينية",
    "philippines-saudi arabia relations": "تصنيف:العلاقات السعودية الفلبينية",
    "russia-sudan relations": "تصنيف:العلاقات الروسية السودانية",
    "russia-tunisia relations": "تصنيف:العلاقات التونسية الروسية",
    "russia-united arab emirates relations": "تصنيف:العلاقات الإماراتية الروسية",
    "russia-uzbekistan relations": "تصنيف:العلاقات الأوزبكستانية الروسية",
    "somalia-turkey relations": "تصنيف:العلاقات التركية الصومالية",
    "south korea-united states relations": "تصنيف:العلاقات الأمريكية الكورية الجنوبية",
    "lists of populated places in the united states": "تصنيف:قوائم أماكن مأهولة في الولايات المتحدة",
    "populated places in the british virgin islands": "تصنيف:أماكن مأهولة في جزر العذراء البريطانية",
    "soccer in australia": "تصنيف:كرة القدم في أستراليا",
    "soccer in the united states": "تصنيف:كرة القدم في الولايات المتحدة",
    "football in spain": "تصنيف:كرة القدم في إسبانيا",
    "water polo in the world aquatics championships": "تصنيف:كرة الماء في بطولة العالم للرياضات المائية",
    "populated places in tokelau": "تصنيف:أماكن مأهولة في توكيلاو",
    "townships in michigan": "تصنيف:ضواحي مدن في ميشيغان",
    "populated places in christmas island": "تصنيف:أماكن مأهولة في جزيرة عيد الميلاد",
    "cities and towns in india": "تصنيف:مدن وبلدات في الهند",
    "neighbourhoods in rio de janeiro (city)": "تصنيف:أحياء في ريو دي جانيرو",
    "populated places in the cocos (keeling) islands": "تصنيف:أماكن مأهولة في جزر كوكوس",
    "populated places in puebla": "تصنيف:أماكن مأهولة في ولاية بويبلا",
    "populated places in the cook islands": "تصنيف:أماكن مأهولة في جزر كوك",
    "populated places in norfolk island": "تصنيف:أماكن مأهولة في جزيرة نورفولك",
    "cities and towns in moscow oblast": "تصنيف:مدن وبلدات في محافظة موسكو",

    "wheelchair basketball world championship": "تصنيف:بطولة العالم لكرة السلة على الكراسي المتحركة",
    "water polo at the world aquatics championships": "تصنيف:كرة الماء في بطولة العالم للرياضات المائية",
    "portugal national rugby league team": "تصنيف:منتخب البرتغال لدوري الرجبي",
    "new zealand women's national ice hockey team": "تصنيف:منتخب نيوزيلندا لهوكي الجليد للسيدات",
    "new zealand women's national rugby league team": "تصنيف:منتخب نيوزيلندا لدوري الرجبي للسيدات",
    "kazakhstan women's national ice hockey team": "تصنيف:منتخب كازاخستان لهوكي الجليد للسيدات",
    "georgia national rugby union team": "تصنيف:منتخب جورجيا لاتحاد الرجبي",
    "england women's national rugby league team": "تصنيف:منتخب إنجلترا لدوري الرجبي للسيدات",
    "chile national rugby union team": "تصنيف:منتخب تشيلي لاتحاد الرجبي",
    "australia national rugby union team": "تصنيف:منتخب أستراليا لاتحاد الرجبي",
    "algeria national rugby union team": "تصنيف:منتخب الجزائر لاتحاد الرجبي",
    "united states national rugby union team": "تصنيف:منتخب الولايات المتحدة لاتحاد الرجبي",
    "greece national rugby league team": "تصنيف:منتخب اليونان لدوري الرجبي",
    "archery at the 2004 summer olympics": "تصنيف:النبالة في الألعاب الأولمبية الصيفية 2004",
    "wrestling at the 2004 summer olympics": "تصنيف:المصارعة في الألعاب الأولمبية الصيفية 2004",
    "triathlon at the 2004 summer olympics": "تصنيف:السباق الثلاثي في الألعاب الأولمبية الصيفية 2004",
    "synchronized swimming at the 2004 summer olympics": "تصنيف:السباحة المتزامنة في الألعاب الأولمبية الصيفية 2004",
    "united states national futsal team": "تصنيف:منتخب الولايات المتحدة لكرة الصالات",
    "thailand women's national basketball team": "تصنيف:منتخب تايلاند لكرة السلة للسيدات",
    "sweden national bandy team": "تصنيف:منتخب السويد للباندي",
    "slovenia women's national football team": "تصنيف:منتخب سلوفينيا لكرة القدم للسيدات",
    "papua new guinea women's national football team": "تصنيف:منتخب بابوا غينيا الجديدة لكرة القدم للسيدات",
    "netherlands men's national basketball team": "تصنيف:منتخب هولندا لكرة السلة للرجال",
    "taekwondo at the 2004 summer olympics": "تصنيف:التايكوندو في الألعاب الأولمبية الصيفية 2004",
    "namibia women's national football team": "تصنيف:منتخب ناميبيا لكرة القدم للسيدات",
    "myanmar women's national football team": "تصنيف:منتخب ميانمار لكرة القدم للسيدات",
    "montenegro women's national football team": "تصنيف:منتخب الجبل الأسود لكرة القدم للسيدات",
    "moldova national rugby league team": "تصنيف:منتخب مولدافيا لدوري الرجبي",
    "moldova women's national football team": "تصنيف:منتخب مولدافيا لكرة القدم للسيدات",
    "bosnia and herzegovina national under-21 football team": "تصنيف:منتخب البوسنة والهرسك لكرة القدم تحت 21 سنة",
    "philippine football federation": "تصنيف:الاتحاد الفلبيني لكرة القدم",
    "iraq national football team results": "تصنيف:نتائج منتخب العراق لكرة القدم",
    "austria women's national football team": "تصنيف:منتخب النمسا لكرة القدم للسيدات",
    "algeria women's national football team": "تصنيف:منتخب الجزائر لكرة القدم للسيدات",
    "thailand women's national football team": "تصنيف:منتخب تايلاند لكرة القدم للسيدات",
    "switzerland women's national football team": "تصنيف:منتخب سويسرا لكرة القدم للسيدات",
    "south korea national under-17 football team": "تصنيف:منتخب كوريا الجنوبية لكرة القدم تحت 17 سنة",
    "south korea national under-20 football team": "تصنيف:منتخب كوريا الجنوبية لكرة القدم تحت 20 سنة",
    "south korea national under-23 football team": "تصنيف:منتخب كوريا الجنوبية لكرة القدم تحت 23 سنة",
    "portugal women's national football team": "تصنيف:منتخب البرتغال لكرة القدم للسيدات",
    "vietnam national basketball team": "تصنيف:منتخب فيتنام لكرة السلة",
    "uruguay national football team": "تصنيف:منتخب الأوروغواي لكرة القدم",
    "bolivia national soccer team": "تصنيف:منتخب بوليفيا لكرة القدم",

}

data_2 = {

}

to_test = [
    ("test_1", data1),
    ("test_2", data_2),
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
