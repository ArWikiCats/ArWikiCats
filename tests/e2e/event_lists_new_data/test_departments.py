#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

data_0 = {
    "Children's clothing designers": "x",
    "Children's clothing retailers": "x",
    "Defunct department stores based in Downtown Los Angeles": "x",
    "Defunct department stores based in Greater Los Angeles": "x",
    "Defunct department stores based in North Hollywood": "x",
    "Defunct department stores based in Southeast Los Angeles County, California": "x",
    "Defunct department stores based in the Miracle Mile": "x",
    "Defunct department stores based in the San Fernando Valley": "x",
    "Defunct department stores based in the San Gabriel Valley": "x",
    "Defunct department stores based in the South Bay, Los Angeles County": "x",
    "Defunct department stores based in the Westside, Los Angeles": "x",
    "Department stores in Southend-on-Sea (town)": "x",
}

data_1 = {
    "Companies that have filed for bankruptcy in Canada": "شركات أعلنت إفلاسها في كندا",
    "Clothing retailers of the United States": "متاجر ملابس بالتجزئة في الولايات المتحدة",
    "Department stores of the United States": "متاجر متعددة الأقسام في الولايات المتحدة",
    "Department stores of Canada": "متاجر متعددة الأقسام في كندا",
}

data_2 = {
    "Companies that have filed for bankruptcy in Brazil": "شركات أعلنت إفلاسها في البرازيل",
    "Companies that have filed for bankruptcy in Canada": "شركات أعلنت إفلاسها في كندا",
    "Companies that have filed for bankruptcy in Japan": "شركات أعلنت إفلاسها في اليابان",
    "Companies that have filed for bankruptcy in South Korea": "شركات أعلنت إفلاسها في كوريا الجنوبية",
    "Companies that have filed for bankruptcy in the People's Republic of China": "شركات أعلنت إفلاسها في جمهورية الصين الشعبية",
    "Companies that have filed for bankruptcy in the United States": "شركات أعلنت إفلاسها في الولايات المتحدة",
    "Clothing retailers": "متاجر ملابس بالتجزئة",
    "Clothing retailers by country": "متاجر ملابس بالتجزئة حسب البلد",
    "Clothing retailers of Australia": "متاجر ملابس بالتجزئة في أستراليا",
    "Clothing retailers of Brazil": "متاجر ملابس بالتجزئة في البرازيل",
    "Clothing retailers of Canada": "متاجر ملابس بالتجزئة في كندا",
    "Clothing retailers of China": "متاجر ملابس بالتجزئة في الصين",
    "Clothing retailers of Denmark": "متاجر ملابس بالتجزئة في الدنمارك",
    "Clothing retailers of England": "متاجر ملابس بالتجزئة في إنجلترا",
    "Clothing retailers of France": "متاجر ملابس بالتجزئة في فرنسا",
    "Clothing retailers of Germany": "متاجر ملابس بالتجزئة في ألمانيا",
    "Clothing retailers of Greece": "متاجر ملابس بالتجزئة في اليونان",
    "Clothing retailers of Greenland": "متاجر ملابس بالتجزئة في جرينلاند",
    "Clothing retailers of Hong Kong": "متاجر ملابس بالتجزئة في هونغ كونغ",
    "Clothing retailers of Iceland": "متاجر ملابس بالتجزئة في آيسلندا",
    "Clothing retailers of India": "متاجر ملابس بالتجزئة في الهند",
    "Clothing retailers of Ireland": "متاجر ملابس بالتجزئة في أيرلندا",
    "Clothing retailers of Israel": "متاجر ملابس بالتجزئة في إسرائيل",
    "Clothing retailers of Italy": "متاجر ملابس بالتجزئة في إيطاليا",
    "Clothing retailers of Japan": "متاجر ملابس بالتجزئة في اليابان",
    "Clothing retailers of Lithuania": "متاجر ملابس بالتجزئة في ليتوانيا",
    "Clothing retailers of Mexico": "متاجر ملابس بالتجزئة في المكسيك",
    "Clothing retailers of New Zealand": "متاجر ملابس بالتجزئة في نيوزيلندا",
    "Clothing retailers of Nigeria": "متاجر ملابس بالتجزئة في نيجيريا",
    "Clothing retailers of Pakistan": "متاجر ملابس بالتجزئة في باكستان",
    "Clothing retailers of Scotland": "متاجر ملابس بالتجزئة في إسكتلندا",
    "Clothing retailers of Spain": "متاجر ملابس بالتجزئة في إسبانيا",
    "Clothing retailers of Sweden": "متاجر ملابس بالتجزئة في السويد",
    "Clothing retailers of Switzerland": "متاجر ملابس بالتجزئة في سويسرا",
    "Clothing retailers of the United Kingdom": "متاجر ملابس بالتجزئة في المملكة المتحدة",
    "Clothing retailers of the United States": "متاجر ملابس بالتجزئة في الولايات المتحدة",
    "Clothing retailers of Tunisia": "متاجر ملابس بالتجزئة في تونس",
    "Clothing retailers of Wales": "متاجر ملابس بالتجزئة في ويلز",
    "Department stores": "متاجر متعددة الأقسام",
    "Department stores by country": "متاجر متعددة الأقسام حسب البلد",
    "Department stores of Andorra": "متاجر متعددة الأقسام في أندورا",
    "Department stores of Australia": "متاجر متعددة الأقسام في أستراليا",
    "Department stores of Austria": "متاجر متعددة الأقسام في النمسا",
    "Department stores of Brazil": "متاجر متعددة الأقسام في البرازيل",
    "Department stores of Brunei": "متاجر متعددة الأقسام في بروناي",
    "Department stores of Bulgaria": "متاجر متعددة الأقسام في بلغاريا",
    "Department stores of Canada": "متاجر متعددة الأقسام في كندا",
    "Department stores of Central America": "متاجر متعددة الأقسام في أمريكا الوسطى",
    "Department stores of Chile": "متاجر متعددة الأقسام في تشيلي",
    "Department stores of China": "متاجر متعددة الأقسام في الصين",
    "Department stores of Denmark": "متاجر متعددة الأقسام في الدنمارك",
    "Department stores of El Salvador": "متاجر متعددة الأقسام في السلفادور",
    "Department stores of Finland": "متاجر متعددة الأقسام في فنلندا",
    "Department stores of France": "متاجر متعددة الأقسام في فرنسا",
    "Department stores of Germany": "متاجر متعددة الأقسام في ألمانيا",
    "Department stores of Hong Kong": "متاجر متعددة الأقسام في هونغ كونغ",
    "Department stores of India": "متاجر متعددة الأقسام في الهند",
    "Department stores of Indonesia": "متاجر متعددة الأقسام في إندونيسيا",
    "Department stores of Ireland": "متاجر متعددة الأقسام في أيرلندا",
    "Department stores of Israel": "متاجر متعددة الأقسام في إسرائيل",
    "Department stores of Italy": "متاجر متعددة الأقسام في إيطاليا",
    "Department stores of Japan": "متاجر متعددة الأقسام في اليابان",
    "Department stores of Kazakhstan": "متاجر متعددة الأقسام في كازاخستان",
    "Department stores of Kuwait": "متاجر متعددة الأقسام في الكويت",
    "Department stores of Lebanon": "متاجر متعددة الأقسام في لبنان",
    "Department stores of Malaysia": "متاجر متعددة الأقسام في ماليزيا",
    "Department stores of Mexico": "متاجر متعددة الأقسام في المكسيك",
    "Department stores of New Zealand": "متاجر متعددة الأقسام في نيوزيلندا",
    "Department stores of North Korea": "متاجر متعددة الأقسام في كوريا الشمالية",
    "Department stores of Norway": "متاجر متعددة الأقسام في النرويج",
    "Department stores of Pakistan": "متاجر متعددة الأقسام في باكستان",
    "Department stores of Poland": "متاجر متعددة الأقسام في بولندا",
    "Department stores of Portugal": "متاجر متعددة الأقسام في البرتغال",
    "Department stores of Russia": "متاجر متعددة الأقسام في روسيا",
    "Department stores of Serbia": "متاجر متعددة الأقسام في صربيا",
    "Department stores of Singapore": "متاجر متعددة الأقسام في سنغافورة",
    "Department stores of Slovenia": "متاجر متعددة الأقسام في سلوفينيا",
    "Department stores of South Korea": "متاجر متعددة الأقسام في كوريا الجنوبية",
    "Department stores of Spain": "متاجر متعددة الأقسام في إسبانيا",
    "Department stores of Sri Lanka": "متاجر متعددة الأقسام في سريلانكا",
    "Department stores of Sweden": "متاجر متعددة الأقسام في السويد",
    "Department stores of Switzerland": "متاجر متعددة الأقسام في سويسرا",
    "Department stores of Taiwan": "متاجر متعددة الأقسام في تايوان",
    "Department stores of Thailand": "متاجر متعددة الأقسام في تايلاند",
    "Department stores of the Netherlands": "متاجر متعددة الأقسام في هولندا",
    "Department stores of the Philippines": "متاجر متعددة الأقسام في الفلبين",
    "Department stores of the Soviet Union": "متاجر متعددة الأقسام في الاتحاد السوفيتي",
    "Department stores of the United Arab Emirates": "متاجر متعددة الأقسام في الإمارات العربية المتحدة",
    "Department stores of the United Kingdom": "متاجر متعددة الأقسام في المملكة المتحدة",
    "Department stores of the United States": "متاجر متعددة الأقسام في الولايات المتحدة",
    "Department stores of Turkey": "متاجر متعددة الأقسام في تركيا",
    "Department stores of Zimbabwe": "متاجر متعددة الأقسام في زيمبابوي",
    "Department stores on the National Register of Historic Places": "متاجر متعددة الأقسام في السجل الوطني للأماكن التاريخية",
    "Disasters in department stores": "كوارث في متاجر متعددة الأقسام",
    "Works set in department stores": "أعمال تقع أحداثها في متاجر متعددة الأقسام",
    "Television shows set in department stores": "عروض تلفزيونية تقع أحداثها في متاجر متعددة الأقسام",
    "Films set in department stores": "أفلام تقع أحداثها في متاجر متعددة الأقسام",
    "Fiction about department stores": "الخيال عن متاجر متعددة الأقسام",
}

data_3 = {
    "Defunct department stores based in New York State": "متاجر متعددة الأقسام سابقة مقرها في ولاية نيويورك",
    "Defunct department stores based in Washington State": "متاجر متعددة الأقسام سابقة مقرها في ولاية واشنطن",
    "Online clothing retailers": "متاجر ملابس بالتجزئة عبر الإنترنت",
    "Online clothing retailers of Canada": "متاجر ملابس بالتجزئة عبر الإنترنت في كندا",
    "Online clothing retailers of Germany": "متاجر ملابس بالتجزئة عبر الإنترنت في ألمانيا",
    "Online clothing retailers of India": "متاجر ملابس بالتجزئة عبر الإنترنت في الهند",
    "Online clothing retailers of Italy": "متاجر ملابس بالتجزئة عبر الإنترنت في إيطاليا",
    "Online clothing retailers of Singapore": "متاجر ملابس بالتجزئة عبر الإنترنت في سنغافورة",
    "Online clothing retailers of Spain": "متاجر ملابس بالتجزئة عبر الإنترنت في إسبانيا",
    "Online clothing retailers of the United Kingdom": "متاجر ملابس بالتجزئة عبر الإنترنت في المملكة المتحدة",
    "Online clothing retailers of the United States": "متاجر ملابس بالتجزئة عبر الإنترنت في الولايات المتحدة",
    "Defunct clothing retailers of the United States": "متاجر ملابس بالتجزئة سابقة في الولايات المتحدة",
    "Defunct department stores": "متاجر متعددة الأقسام سابقة",
    "Defunct department stores based in Alabama": "متاجر متعددة الأقسام سابقة مقرها في ألاباما",
    "Defunct department stores based in Arizona": "متاجر متعددة الأقسام سابقة مقرها في أريزونا",
    "Defunct department stores based in Arkansas": "متاجر متعددة الأقسام سابقة مقرها في أركنساس",
    "Defunct department stores based in Atlanta": "متاجر متعددة الأقسام سابقة مقرها في أتلانتا (جورجيا)",
    "Defunct department stores based in California": "متاجر متعددة الأقسام سابقة مقرها في كاليفورنيا",
    "Defunct department stores based in Chicago": "متاجر متعددة الأقسام سابقة مقرها في شيكاغو",
    "Defunct department stores based in Cincinnati": "متاجر متعددة الأقسام سابقة مقرها في سينسيناتي",
    "Defunct department stores based in Cleveland": "متاجر متعددة الأقسام سابقة مقرها في كليفلاند",
    "Defunct department stores based in Colorado": "متاجر متعددة الأقسام سابقة مقرها في كولورادو",
    "Defunct department stores based in Columbus, Ohio": "متاجر متعددة الأقسام سابقة مقرها في كولومبوس (أوهايو)",
    "Defunct department stores based in Connecticut": "متاجر متعددة الأقسام سابقة مقرها في كونيتيكت",
    "Defunct department stores based in Dayton, Ohio": "متاجر متعددة الأقسام سابقة مقرها في دايتون (أوهايو)",
    "Defunct department stores based in Florida": "متاجر متعددة الأقسام سابقة مقرها في فلوريدا",
    "Defunct department stores based in Georgia (U.S. state)": "متاجر متعددة الأقسام سابقة مقرها في ولاية جورجيا",
    "Defunct department stores based in Hawaii": "متاجر متعددة الأقسام سابقة مقرها في هاواي",
    "Defunct department stores based in Hollywood": "متاجر متعددة الأقسام سابقة مقرها في هوليوود",
    "Defunct department stores based in Illinois": "متاجر متعددة الأقسام سابقة مقرها في إلينوي",
    "Defunct department stores based in Indiana": "متاجر متعددة الأقسام سابقة مقرها في إنديانا",
    "Defunct department stores based in Iowa": "متاجر متعددة الأقسام سابقة مقرها في آيوا",
    "Defunct department stores based in Kentucky": "متاجر متعددة الأقسام سابقة مقرها في كنتاكي",
    "Defunct department stores based in Long Beach, California": "متاجر متعددة الأقسام سابقة مقرها في لونغ بيتش (كاليفورنيا)",
    "Defunct department stores based in Louisiana": "متاجر متعددة الأقسام سابقة مقرها في لويزيانا",
    "Defunct department stores based in Maine": "متاجر متعددة الأقسام سابقة مقرها في مين",
    "Defunct department stores based in Maryland": "متاجر متعددة الأقسام سابقة مقرها في ماريلند",
    "Defunct department stores based in Massachusetts": "متاجر متعددة الأقسام سابقة مقرها في ماساتشوستس",
    "Defunct department stores based in Michigan": "متاجر متعددة الأقسام سابقة مقرها في ميشيغان",
    "Defunct department stores based in Minnesota": "متاجر متعددة الأقسام سابقة مقرها في منيسوتا",
    "Defunct department stores based in Mississippi": "متاجر متعددة الأقسام سابقة مقرها في مسيسيبي",
    "Defunct department stores based in Missouri": "متاجر متعددة الأقسام سابقة مقرها في ميزوري",
    "Defunct department stores based in Nebraska": "متاجر متعددة الأقسام سابقة مقرها في نبراسكا",
    "Defunct department stores based in Nevada": "متاجر متعددة الأقسام سابقة مقرها في نيفادا",
    "Defunct department stores based in New Jersey": "متاجر متعددة الأقسام سابقة مقرها في نيوجيرسي",
    "Defunct department stores based in New York City": "متاجر متعددة الأقسام سابقة مقرها في مدينة نيويورك",
    "Defunct department stores based in North Carolina": "متاجر متعددة الأقسام سابقة مقرها في كارولاينا الشمالية",
    "Defunct department stores based in North Dakota": "متاجر متعددة الأقسام سابقة مقرها في داكوتا الشمالية",
    "Defunct department stores based in Ohio": "متاجر متعددة الأقسام سابقة مقرها في أوهايو",
    "Defunct department stores based in Oklahoma": "متاجر متعددة الأقسام سابقة مقرها في أوكلاهوما",
    "Defunct department stores based in Orange County, California": "متاجر متعددة الأقسام سابقة مقرها في مقاطعة أورانج (كاليفورنيا)",
    "Defunct department stores based in Oregon": "متاجر متعددة الأقسام سابقة مقرها في أوريغن",
    "Defunct department stores based in Pennsylvania": "متاجر متعددة الأقسام سابقة مقرها في بنسلفانيا",
    "Defunct department stores based in Philadelphia": "متاجر متعددة الأقسام سابقة مقرها في فيلادلفيا",
    "Defunct department stores based in Pittsburgh": "متاجر متعددة الأقسام سابقة مقرها في بيتسبرغ",
    "Defunct department stores based in Sacramento": "متاجر متعددة الأقسام سابقة مقرها في ساكرامينتو",
    "Defunct department stores based in San Bernardino County, California": "متاجر متعددة الأقسام سابقة مقرها في مقاطعه سان بيرناردينو (كاليفورنيا)",
    "Defunct department stores based in San Diego": "متاجر متعددة الأقسام سابقة مقرها في سان دييغو",
    "Defunct department stores based in South Carolina": "متاجر متعددة الأقسام سابقة مقرها في كارولاينا الجنوبية",
    "Defunct department stores based in Tennessee": "متاجر متعددة الأقسام سابقة مقرها في تينيسي",
    "Defunct department stores based in Texas": "متاجر متعددة الأقسام سابقة مقرها في تكساس",
    "Defunct department stores based in the City of Los Angeles": "متاجر متعددة الأقسام سابقة مقرها في مدينة لوس أنجلوس",
    "Defunct department stores based in the San Francisco Bay Area": "متاجر متعددة الأقسام سابقة مقرها في منطقة خليج سان فرانسيسكو",
    "Defunct department stores based in Toledo, Ohio": "متاجر متعددة الأقسام سابقة مقرها في توليدو (أوهايو)",
    "Defunct department stores based in Utah": "متاجر متعددة الأقسام سابقة مقرها في يوتا",
    "Defunct department stores based in Virginia": "متاجر متعددة الأقسام سابقة مقرها في فرجينيا",
    "Defunct department stores based in Washington, D.C.": "متاجر متعددة الأقسام سابقة مقرها في واشنطن العاصمة",
    "Defunct department stores based in West Virginia": "متاجر متعددة الأقسام سابقة مقرها في فرجينيا الغربية",
    "Defunct department stores based in Wisconsin": "متاجر متعددة الأقسام سابقة مقرها في ويسكونسن",
    "Defunct department stores by country": "متاجر متعددة الأقسام سابقة حسب البلد",
    "Defunct department stores of Australia": "متاجر متعددة الأقسام سابقة في أستراليا",
    "Defunct department stores of Mexico": "متاجر متعددة الأقسام سابقة في المكسيك",
    "Defunct department stores of Thailand": "متاجر متعددة الأقسام سابقة في تايلاند",
    "Defunct department stores of the United Kingdom": "متاجر متعددة الأقسام سابقة في المملكة المتحدة",
    "Defunct department stores of the United States": "متاجر متعددة الأقسام سابقة في الولايات المتحدة",
    "Defunct department stores of the United States by city": "متاجر متعددة الأقسام سابقة في الولايات المتحدة حسب المدينة",
    "Defunct department stores of the United States by state": "متاجر متعددة الأقسام سابقة في الولايات المتحدة حسب الولاية",
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_departments_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_departments_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
@pytest.mark.fast
def test_departments_3(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_departments_1", data_1),
    ("test_departments_2", data_2),
    ("test_departments_3", data_3),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
