#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar


data0 = {
    "Buddhist comics": "تصنيف:قصص مصورة بوذيون",
    "Buddhist media in Taiwan": "تصنيف:إعلام بوذيون في تايوان",
    "Buddhist media": "تصنيف:إعلام بوذيون",
    "Buddhist music": "تصنيف:موسيقى بوذيون",
    "Buddhist video games": "تصنيف:ألعاب فيديو بوذيون",
    "Hindu music": "تصنيف:موسيقى هندوس",
    "Islamic media in India": "تصنيف:إعلام إسلاميون في الهند",
    "Islamic media": "تصنيف:إعلام إسلاميون",
    "Islamic music": "تصنيف:موسيقى إسلاميون",
    "Jewish music genres": "تصنيف:أنواع موسيقى يهود",
    "Nazi culture": "تصنيف:ثقافة نازيون",
    "Nazi songs": "تصنيف:أغاني نازيون",
    "Saints and Soldiers films": "تصنيف:قديسون وأفلام مجندون",
    "muslim people templates": "تصنيف:قوالب أعلام مسلمون",
    "deaf culture": "ثقافة صم",
    "Category:Canadian football players in Edmonton": "تصنيف:لاعبو كرة قدم كندية في إدمونتون",
    "christian saints": "قديسون",
    "electro musicians": "موسيقيو موسيقى كهربائية",
    "film editors": "محررو أفلام",
    "gardeners": "مزارعو حدائق",
    "music journalists": "صحفيون موسيقيون",
    "olympic beach volleyball players": "لاعبو كرة طائرة شاطئية أولمبيون",
    "olympic divers": "غواصون أولمبيون",
    "olympic handball players": "لاعبو كرة يد أولمبيون",
    "olympic judoka": "لاعبو جودو أولمبيون",
    "olympic nordic combined skiers": "متزحلقو تزلج نوردي مزدوج أولمبيون",
    "polo players": "لاعبو بولو",
    "traditional pop music singers": "مغنو موسيقى بوب تقليدية",
    "voice actresses": "ممثلات أداء صوتي",
    "singaporean blind people": "أعلام سنغافوريون مكفوفون",
    "ukrainian deaf people": "أعلام أوكرانيون صم",
    "slovenian deaf people": "أعلام سلوفينيون صم",
    "russian blind people": "أعلام روس مكفوفون",
    "czech deaf people": "أعلام تشيكيون صم",
    "male models": "عارضو أزياء ذكور",
    "male sport shooters": "لاعبو رماية ذكور",
    "by benjamin britten": "بواسطة بنجامين بريتن",
    "by james cameron": "بواسطة جيمس كاميرون",
    "by raphael": "بواسطة رافاييل",
    "by vaikom muhammad basheer": "بواسطة محمد بشير",
    "assassinated politicians": "سياسيون مغتالون",
    "expatriate men's footballers": "لاعبو كرة قدم رجالية مغتربون",
    "expatriate men's soccer players": "لاعبو كرة قدم رجالية مغتربون",
    "Icelandic deaf people": "أعلام آيسلنديون صم",
    "Romantic composers": "ملحنون رومانسيون",
    "Category:Expatriate men's footballers in Papua New Guinea": "تصنيف:لاعبو كرة قدم رجالية مغتربون في بابوا غينيا الجديدة",
    "18th-century Dutch explorers": "مستكشفون هولنديون في القرن 18",
    "Category:1650s crimes": "تصنيف:جرائم عقد 1650",
    "1650s controversies": "خلافات عقد 1650",
    "20th century women musicians": "موسيقيات في القرن 20",
    "20th century canadian violinists": "عازفو كمان كنديون في القرن 20",
    "20th century russian dramatists": "دراميون روس في القرن 20",
    "20th century polish dramatists": "دراميون بولنديون في القرن 20",
    "20th century chinese dramatists": "دراميون صينيون في القرن 20",
    "20th century dramatists": "دراميون في القرن 20",
    "20th century english dramatists": "دراميون إنجليز في القرن 20",
    "20th century israeli dramatists": "دراميون إسرائيليون في القرن 20",
    "works by gotthold ephraim lessing": "أعمال بواسطة إفرايم ليسينغ",
    "works by leo tolstoy": "أعمال بواسطة ليو تولستوي",
    "works by osamu tezuka": "أعمال بواسطة أوسامو تزوكا",
    "italian defectors to soviet union": "إيطاليون منشقون إلى الاتحاد السوفيتي",
    "zambian emigrants to sweden": "زامبيون مهاجرون إلى السويد",
    "sri lankan emigrants to india": "سريلانكيون مهاجرون إلى الهند",
    "taiwanese emigrants to argentina": "تايوانيون مهاجرون إلى الأرجنتين",
    "polish emigrants to brazil": "بولنديون مهاجرون إلى البرازيل",
    "italian emigrants to finland": "إيطاليون مهاجرون إلى فنلندا",
    "icelandic emigrants to new zealand": "آيسلنديون مهاجرون إلى نيوزيلندا",
    "german emigrants to scotland": "ألمان مهاجرون إلى إسكتلندا",
    "croatian emigrants to netherlands": "كروات مهاجرون إلى هولندا",
    "cypriot emigrants to israel": "قبرصيون مهاجرون إلى إسرائيل",
    "chinese emigrants to thailand": "صينيون مهاجرون إلى تايلاند",
    "british emigrants to switzerland": "بريطانيون مهاجرون إلى سويسرا",
    "british emigrants to zimbabwe": "بريطانيون مهاجرون إلى زيمبابوي",
    "American child classical musicians": "موسيقيون كلاسيكيون أمريكيون أطفال",
    "Canadian child singers": "مغنون كنديون أطفال",
    "Native American people in American Revolution": "أمريكيون أصليون في الثورة الأمريكية",
    "Yugoslav disabled sports-people": "رياضيون يوغسلافيون معاقون",
    "American women in politics by descent": "أمريكيات في السياسة حسب الأصل",
    "Native American people from Minnesota": "أمريكيون أصليون من منيسوتا",
    "Native American people from North Dakota": "أمريكيون أصليون من داكوتا الشمالية",
    "Native American people from South Dakota": "أمريكيون أصليون من داكوتا الجنوبية",
    "Native American people from Washington (state)": "أمريكيون أصليون من ولاية واشنطن",
    "Somalian disabled sports-people": "رياضيون صوماليون معاقون",
    "American expatriate men's soccer players": "لاعبو كرة قدم أمريكيون مغتربون",
    "Byzantine female saints": "قديسات بيزنطيات",
    "Canarian Jews": "يهود كناريون",
    "Ancient Christian saints": "مسيحيون قديسون قدماء",
    "Ancient Jews by occupation": "يهود قدماء حسب المهنة",
    "Ancient Christians": "مسيحيون قدماء",
    "Ancient Jews": "يهود قدماء",
    "2017 sports events": "أحداث 2017 الرياضية",
    "bengali-language romantic comedy films": "أفلام كوميدية رومانسية باللغة البنغالية",
    "cantonese-language speculative fiction films": "أفلام خيال تأملي باللغة الكانتونية",
    "Ancient Christian female saints": "قديسات مسيحيات قدماء",
    "Ancient Egyptian Jews": "مصريون يهود قدماء",
    "Ancient Jewish physicians": "أطباء يهود قدماء",
    "Ancient Jewish scholars": "دارسون يهود قدماء",
    "Ancient Jewish women": "يهوديات قدماء",
    "Ancient Jewish writers": "كتاب يهود قدماء",
    "Fictional American Jews in comics": "أمريكيون يهود خياليون في قصص مصورة",
    "Fictional American Jews": "أمريكيون يهود خياليون",
    "Fictional Argentine Jews": "أرجنتينيون يهود خياليون",
    "Fictional British Jews": "بريطانيون يهود خياليون",
    "Fictional Canadian Jews": "كنديون يهود خياليون",
    "Fictional English Jews": "إنجليز يهود خياليون",
    "Fictional German Jews": "ألمان يهود خياليون",
    "Fictional Israeli Jews": "إسرائيليون يهود خياليون",
    "Fictional Italian Jews": "إيطاليون يهود خياليون",
    "Fictional Polish Jews": "بولنديون يهود خياليون",
    "Fictional Russian Jews": "روس يهود خياليون",
    "Fictional Serbian Jews": "صرب يهود خياليون",
    "Murdered American Jews": "أمريكيون يهود قتلوا"
}

data1 = {
    # "American expatriate men's soccer players in Canada": "",
    "West German men sprinters": "عداؤون سريعون ألمانيون غربيون",
    "Emirati men's footballers": "لاعبو كرة قدم إماراتيون",
    "2015 American television": "التلفزة الأمريكية 2015",
    # "yemeni presidential elections": "انتخابات اليمن الرئاسية",
    "ambassadors of federated states of micronesia in yemen by year": "سفراء ولايات ميكرونيسيا المتحدة في اليمن حسب السنة",
    "Adaptations of works by Greek writers": "أعمال مقتبسة عن أعمال كتاب يونانيون",
    "Adaptations of works by Irish writers": "أعمال مقتبسة عن أعمال كتاب أيرلنديون",
    "Adaptations of works by Italian writers": "أعمال مقتبسة عن أعمال كتاب إيطاليون",
    "sieges of french invasion of egypt and syria": "حصارات الغزو الفرنسي لمصر وسوريا",
    "1330 in men's international football": "كرة قدم دولية للرجال في 1330",
    "2017 American television series": "مسلسلات تلفزيونية أمريكية في 2017",
    "Cross-country skiers at 1992 Winter Paralympics": "متزحلقون ريفيون في الألعاب البارالمبية الشتوية 1992",
    "2017 American television episodes": "حلقات تلفزيونية أمريكية في 2017",
    "2017 American television seasons": "مواسم تلفزيونية أمريكية في 2017",
    "Roller skaters at 2003 Pan American Games": "متزلجون بالعجلات في دورة الألعاب الأمريكية 2003",
    "Ski jumpers at 2007 Winter Universiade": "متزلجو قفز في الألعاب الجامعية الشتوية 2007",
    "Figure skaters at 2002 Winter Olympics": "متزلجون فنيون في الألعاب الأولمبية الشتوية 2002",
    "Figure skaters at 2003 Asian Winter Games": "متزلجون فنيون في الألعاب الآسيوية الشتوية 2003",
    "Figure skaters at 2007 Winter Universiade": "متزلجون فنيون في الألعاب الجامعية الشتوية 2007",
    "Nations at 2010 Summer Youth Olympics": "بلدان في الألعاب الأولمبية الشبابية الصيفية 2010",
    "military personnel of republic-of china": "أفراد عسكريون من جمهورية الصين",
    "children of prime ministers of ukraine": "أبناء رؤساء وزراء أوكرانيا",
    # "roman catholic bishops of fulda": "",
    "men of poseidon": "رجال من بوسيدون",
    "Olympic shooters of Egypt": "رماة أولمبيون من مصر",
    "Olympic short track speed skaters of Japan": "متزلجون على مسار قصير أولمبيون من اليابان",
    "Olympic figure skaters of Argentina": "متزلجون فنيون أولمبيون من الأرجنتين",
    "Olympic figure skaters of Armenia": "متزلجون فنيون أولمبيون من أرمينيا",
    "Olympic figure skaters of Australia": "متزلجون فنيون أولمبيون من أستراليا",
    # "communists of bosnia and herzegovina politicians": "أحداث أكتوبر 1550 الرياضية في أوقيانوسيا",
}

data_test2 = {
    "Schools for deaf in New York (state)": "مدارس للصم في ولاية نيويورك",
    "Cabinets involving Liberal Party (Norway)": "",
    "Television plays directed by William Sterling (director)": "",
    "Television plays filmed in Brisbane": "مسرحيات تلفزيونية صورت في بريزبان",
    "Television personalities from Yorkshire": "شخصيات تلفزيون من يوركشاير",
    "Cabinets involving Progress Party (Norway)": "مجالس وزراء تشمل حزب التقدم (النرويج)",
    "100 metres at African Championships in Athletics": "",
    "100 metres at IAAF World Youth Championships in Athletics": "",
    "100 metres at World Para Athletics Championships": "",
    "Documentary films about 2011 Tōhoku earthquake and tsunami": "",
    "People accused of lèse majesté in Thailand": "",
    "People accused of lèse majesté in Thailand since 2020": "",
    "People associated with former colleges of University of London": "",
    "People associated with Nazarene universities and colleges": "",
}


data_list_bad = {
    # "20th century roman catholic archbishops in colombia": "رؤساء أساقفة رومان كاثوليك في كولومبيا القرن 20",
    # "20th century disasters in afghanistan": "كوارث القرن 20 في أفغانستان",
    # "20th century churches in ethiopia": "كنائس في إثيوبيا القرن 20",
    # "20th century churches in nigeria": "كنائس في نيجيريا القرن 20",
    "Paralympic competitors for Cape Verde": "منافسون بارالمبيون من الرأس الأخضر",
    "20th century american people by occupation": "أمريكيون في القرن 20 حسب المهنة",
    "20th century people from al-andalus": "أشخاص من الأندلس في القرن 20",
    "september 1550 sports-events in germany": "أحداث سبتمبر 1550 الرياضية في ألمانيا",
    "1550s disestablishments in yugoslavia": "انحلالات عقد 1550 في يوغسلافيا",
    "20th century disestablishments in united kingdom": "انحلالات القرن 20 في المملكة المتحدة",
    "november 1550 sports-events in north america": "أحداث نوفمبر 1550 الرياضية في أمريكا الشمالية",
    "1550s establishments in wisconsin": "تأسيسات عقد 1550 في ويسكونسن",
    "20th century disestablishments in sri lanka": "انحلالات القرن 20 في سريلانكا",
    "3rd millennium disestablishments in england": "انحلالات الألفية 3 في إنجلترا",
    "may 1550 sports-events in united states": "أحداث مايو 1550 الرياضية في الولايات المتحدة",
    "december 1550 sports-events in united states": "أحداث ديسمبر 1550 الرياضية في الولايات المتحدة",
    "1550s crimes in pakistan": "جرائم عقد 1550 في باكستان",
    "2nd millennium establishments in rhode island": "تأسيسات الألفية 2 في رود آيلاند",
    "1550s establishments in chile": "تأسيسات عقد 1550 في تشيلي",
    "1550s disestablishments in southeast asia": "انحلالات عقد 1550 في جنوب شرق آسيا",
    "december 1550 sports-events in united kingdom": "أحداث ديسمبر 1550 الرياضية في المملكة المتحدة",
    "1550s establishments in jamaica": "تأسيسات عقد 1550 في جامايكا",
    "march 1550 sports-events in belgium": "أحداث مارس 1550 الرياضية في بلجيكا",
    "april 1550 sports-events in united kingdom": "أحداث أبريل 1550 الرياضية في المملكة المتحدة",
    "1550s disestablishments in mississippi": "انحلالات عقد 1550 في مسيسيبي",
    "1550s establishments in maine": "تأسيسات عقد 1550 في مين",
    "1550s establishments in sweden": "تأسيسات عقد 1550 في السويد",
    "20th century disestablishments in newfoundland and labrador": "انحلالات القرن 20 في نيوفاوندلاند واللابرادور",
    "20th century disestablishments in danish colonial empire": "انحلالات القرن 20 في الإمبراطورية الاستعمارية الدنماركية",
    "20th century establishments in french guiana": "تأسيسات القرن 20 في غويانا الفرنسية",
    "20th century establishments in ireland": "تأسيسات القرن 20 في أيرلندا",
    "20th century monarchs by country": "ملكيون في القرن 20 حسب البلد",
    "august 1550 sports-events in france": "أحداث أغسطس 1550 الرياضية في فرنسا",
    "february 1550 sports-events in germany": "أحداث فبراير 1550 الرياضية في ألمانيا",
    "july 1550 crimes by continent": "جرائم يوليو 1550 حسب القارة",
    "july 1550 sports-events in north america": "أحداث يوليو 1550 الرياضية في أمريكا الشمالية",
    "june 1550 sports-events in malaysia": "أحداث يونيو 1550 الرياضية في ماليزيا",
    "march 1550 sports-events in thailand": "أحداث مارس 1550 الرياضية في تايلاند",
    "november 1550 sports-events in europe": "أحداث نوفمبر 1550 الرياضية في أوروبا",
    "november 1550 sports-events in united kingdom": "أحداث نوفمبر 1550 الرياضية في المملكة المتحدة",
    "october 1550 sports-events in oceania": "أحداث أكتوبر 1550 الرياضية في أوقيانوسيا",
}


to_test = [
    ("test_1", data1),
    ("test_2", data_test2),
    ("test_2_new_bug_check", data_list_bad),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
@pytest.mark.skip2
def test_0(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_test2.items(), ids=data_test2.keys())
@pytest.mark.fast
def test_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_list_bad.items(), ids=data_list_bad.keys())
@pytest.mark.fast
def test_2_new_bug_check(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
