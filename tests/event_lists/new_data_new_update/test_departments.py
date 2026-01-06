#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data_0 = {
    "Category:Children's clothing designers": "x",
    "Category:Children's clothing retailers": "x",
    "Category:Defunct department stores based in Downtown Los Angeles": "x",
    "Category:Defunct department stores based in Greater Los Angeles": "x",
    "Category:Defunct department stores based in North Hollywood": "x",
    "Category:Defunct department stores based in Southeast Los Angeles County, California": "x",
    "Category:Defunct department stores based in the Miracle Mile": "x",
    "Category:Defunct department stores based in the San Fernando Valley": "x",
    "Category:Defunct department stores based in the San Gabriel Valley": "x",
    "Category:Defunct department stores based in the South Bay, Los Angeles County": "x",
    "Category:Defunct department stores based in the Westside, Los Angeles": "x",
    "Category:Department stores in Southend-on-Sea (town)": "x",
}

data_1 = {
    "Category:Companies that have filed for bankruptcy in Canada": "تصنيف:شركات أعلنت إفلاسها في كندا",
    "Category:Clothing retailers of the United States": "تصنيف:متاجر ملابس بالتجزئة في الولايات المتحدة",
    "Category:Department stores of the United States": "تصنيف:متاجر متعددة الأقسام في الولايات المتحدة",
    "Category:Department stores of Canada": "تصنيف:متاجر متعددة الأقسام في كندا",
}

data_2 = {
    "Category:Companies that have filed for bankruptcy in Brazil": "تصنيف:شركات أعلنت إفلاسها في البرازيل",
    "Category:Companies that have filed for bankruptcy in Canada": "تصنيف:شركات أعلنت إفلاسها في كندا",
    "Category:Companies that have filed for bankruptcy in Japan": "تصنيف:شركات أعلنت إفلاسها في اليابان",
    "Category:Companies that have filed for bankruptcy in South Korea": "تصنيف:شركات أعلنت إفلاسها في كوريا الجنوبية",
    "Category:Companies that have filed for bankruptcy in the People's Republic of China": "تصنيف:شركات أعلنت إفلاسها في جمهورية الصين الشعبية",
    "Category:Companies that have filed for bankruptcy in the United States": "تصنيف:شركات أعلنت إفلاسها في الولايات المتحدة",
    "Category:Clothing retailers": "تصنيف:متاجر ملابس بالتجزئة",
    "Category:Clothing retailers by country": "تصنيف:متاجر ملابس بالتجزئة حسب البلد",
    "Category:Clothing retailers of Australia": "تصنيف:متاجر ملابس بالتجزئة في أستراليا",
    "Category:Clothing retailers of Brazil": "تصنيف:متاجر ملابس بالتجزئة في البرازيل",
    "Category:Clothing retailers of Canada": "تصنيف:متاجر ملابس بالتجزئة في كندا",
    "Category:Clothing retailers of China": "تصنيف:متاجر ملابس بالتجزئة في الصين",
    "Category:Clothing retailers of Denmark": "تصنيف:متاجر ملابس بالتجزئة في الدنمارك",
    "Category:Clothing retailers of England": "تصنيف:متاجر ملابس بالتجزئة في إنجلترا",
    "Category:Clothing retailers of France": "تصنيف:متاجر ملابس بالتجزئة في فرنسا",
    "Category:Clothing retailers of Germany": "تصنيف:متاجر ملابس بالتجزئة في ألمانيا",
    "Category:Clothing retailers of Greece": "تصنيف:متاجر ملابس بالتجزئة في اليونان",
    "Category:Clothing retailers of Greenland": "تصنيف:متاجر ملابس بالتجزئة في جرينلاند",
    "Category:Clothing retailers of Hong Kong": "تصنيف:متاجر ملابس بالتجزئة في هونغ كونغ",
    "Category:Clothing retailers of Iceland": "تصنيف:متاجر ملابس بالتجزئة في آيسلندا",
    "Category:Clothing retailers of India": "تصنيف:متاجر ملابس بالتجزئة في الهند",
    "Category:Clothing retailers of Ireland": "تصنيف:متاجر ملابس بالتجزئة في أيرلندا",
    "Category:Clothing retailers of Israel": "تصنيف:متاجر ملابس بالتجزئة في إسرائيل",
    "Category:Clothing retailers of Italy": "تصنيف:متاجر ملابس بالتجزئة في إيطاليا",
    "Category:Clothing retailers of Japan": "تصنيف:متاجر ملابس بالتجزئة في اليابان",
    "Category:Clothing retailers of Lithuania": "تصنيف:متاجر ملابس بالتجزئة في ليتوانيا",
    "Category:Clothing retailers of Mexico": "تصنيف:متاجر ملابس بالتجزئة في المكسيك",
    "Category:Clothing retailers of New Zealand": "تصنيف:متاجر ملابس بالتجزئة في نيوزيلندا",
    "Category:Clothing retailers of Nigeria": "تصنيف:متاجر ملابس بالتجزئة في نيجيريا",
    "Category:Clothing retailers of Pakistan": "تصنيف:متاجر ملابس بالتجزئة في باكستان",
    "Category:Clothing retailers of Scotland": "تصنيف:متاجر ملابس بالتجزئة في إسكتلندا",
    "Category:Clothing retailers of Spain": "تصنيف:متاجر ملابس بالتجزئة في إسبانيا",
    "Category:Clothing retailers of Sweden": "تصنيف:متاجر ملابس بالتجزئة في السويد",
    "Category:Clothing retailers of Switzerland": "تصنيف:متاجر ملابس بالتجزئة في سويسرا",
    "Category:Clothing retailers of the United Kingdom": "تصنيف:متاجر ملابس بالتجزئة في المملكة المتحدة",
    "Category:Clothing retailers of the United States": "تصنيف:متاجر ملابس بالتجزئة في الولايات المتحدة",
    "Category:Clothing retailers of Tunisia": "تصنيف:متاجر ملابس بالتجزئة في تونس",
    "Category:Clothing retailers of Wales": "تصنيف:متاجر ملابس بالتجزئة في ويلز",
    "Category:Department stores": "تصنيف:متاجر متعددة الأقسام",
    "Category:Department stores by country": "تصنيف:متاجر متعددة الأقسام حسب البلد",
    "Category:Department stores of Andorra": "تصنيف:متاجر متعددة الأقسام في أندورا",
    "Category:Department stores of Australia": "تصنيف:متاجر متعددة الأقسام في أستراليا",
    "Category:Department stores of Austria": "تصنيف:متاجر متعددة الأقسام في النمسا",
    "Category:Department stores of Brazil": "تصنيف:متاجر متعددة الأقسام في البرازيل",
    "Category:Department stores of Brunei": "تصنيف:متاجر متعددة الأقسام في بروناي",
    "Category:Department stores of Bulgaria": "تصنيف:متاجر متعددة الأقسام في بلغاريا",
    "Category:Department stores of Canada": "تصنيف:متاجر متعددة الأقسام في كندا",
    "Category:Department stores of Central America": "تصنيف:متاجر متعددة الأقسام في أمريكا الوسطى",
    "Category:Department stores of Chile": "تصنيف:متاجر متعددة الأقسام في تشيلي",
    "Category:Department stores of China": "تصنيف:متاجر متعددة الأقسام في الصين",
    "Category:Department stores of Denmark": "تصنيف:متاجر متعددة الأقسام في الدنمارك",
    "Category:Department stores of El Salvador": "تصنيف:متاجر متعددة الأقسام في السلفادور",
    "Category:Department stores of Finland": "تصنيف:متاجر متعددة الأقسام في فنلندا",
    "Category:Department stores of France": "تصنيف:متاجر متعددة الأقسام في فرنسا",
    "Category:Department stores of Germany": "تصنيف:متاجر متعددة الأقسام في ألمانيا",
    "Category:Department stores of Hong Kong": "تصنيف:متاجر متعددة الأقسام في هونغ كونغ",
    "Category:Department stores of India": "تصنيف:متاجر متعددة الأقسام في الهند",
    "Category:Department stores of Indonesia": "تصنيف:متاجر متعددة الأقسام في إندونيسيا",
    "Category:Department stores of Ireland": "تصنيف:متاجر متعددة الأقسام في أيرلندا",
    "Category:Department stores of Israel": "تصنيف:متاجر متعددة الأقسام في إسرائيل",
    "Category:Department stores of Italy": "تصنيف:متاجر متعددة الأقسام في إيطاليا",
    "Category:Department stores of Japan": "تصنيف:متاجر متعددة الأقسام في اليابان",
    "Category:Department stores of Kazakhstan": "تصنيف:متاجر متعددة الأقسام في كازاخستان",
    "Category:Department stores of Kuwait": "تصنيف:متاجر متعددة الأقسام في الكويت",
    "Category:Department stores of Lebanon": "تصنيف:متاجر متعددة الأقسام في لبنان",
    "Category:Department stores of Malaysia": "تصنيف:متاجر متعددة الأقسام في ماليزيا",
    "Category:Department stores of Mexico": "تصنيف:متاجر متعددة الأقسام في المكسيك",
    "Category:Department stores of New Zealand": "تصنيف:متاجر متعددة الأقسام في نيوزيلندا",
    "Category:Department stores of North Korea": "تصنيف:متاجر متعددة الأقسام في كوريا الشمالية",
    "Category:Department stores of Norway": "تصنيف:متاجر متعددة الأقسام في النرويج",
    "Category:Department stores of Pakistan": "تصنيف:متاجر متعددة الأقسام في باكستان",
    "Category:Department stores of Poland": "تصنيف:متاجر متعددة الأقسام في بولندا",
    "Category:Department stores of Portugal": "تصنيف:متاجر متعددة الأقسام في البرتغال",
    "Category:Department stores of Russia": "تصنيف:متاجر متعددة الأقسام في روسيا",
    "Category:Department stores of Serbia": "تصنيف:متاجر متعددة الأقسام في صربيا",
    "Category:Department stores of Singapore": "تصنيف:متاجر متعددة الأقسام في سنغافورة",
    "Category:Department stores of Slovenia": "تصنيف:متاجر متعددة الأقسام في سلوفينيا",
    "Category:Department stores of South Korea": "تصنيف:متاجر متعددة الأقسام في كوريا الجنوبية",
    "Category:Department stores of Spain": "تصنيف:متاجر متعددة الأقسام في إسبانيا",
    "Category:Department stores of Sri Lanka": "تصنيف:متاجر متعددة الأقسام في سريلانكا",
    "Category:Department stores of Sweden": "تصنيف:متاجر متعددة الأقسام في السويد",
    "Category:Department stores of Switzerland": "تصنيف:متاجر متعددة الأقسام في سويسرا",
    "Category:Department stores of Taiwan": "تصنيف:متاجر متعددة الأقسام في تايوان",
    "Category:Department stores of Thailand": "تصنيف:متاجر متعددة الأقسام في تايلاند",
    "Category:Department stores of the Netherlands": "تصنيف:متاجر متعددة الأقسام في هولندا",
    "Category:Department stores of the Philippines": "تصنيف:متاجر متعددة الأقسام في الفلبين",
    "Category:Department stores of the Soviet Union": "تصنيف:متاجر متعددة الأقسام في الاتحاد السوفيتي",
    "Category:Department stores of the United Arab Emirates": "تصنيف:متاجر متعددة الأقسام في الإمارات العربية المتحدة",
    "Category:Department stores of the United Kingdom": "تصنيف:متاجر متعددة الأقسام في المملكة المتحدة",
    "Category:Department stores of the United States": "تصنيف:متاجر متعددة الأقسام في الولايات المتحدة",
    "Category:Department stores of Turkey": "تصنيف:متاجر متعددة الأقسام في تركيا",
    "Category:Department stores of Zimbabwe": "تصنيف:متاجر متعددة الأقسام في زيمبابوي",
    "Category:Department stores on the National Register of Historic Places": "تصنيف:متاجر متعددة الأقسام في السجل الوطني للأماكن التاريخية",
    "Category:Disasters in department stores": "تصنيف:كوارث في متاجر متعددة الأقسام",
    "Category:Works set in department stores": "تصنيف:أعمال تقع أحداثها في متاجر متعددة الأقسام",
    "Category:Television shows set in department stores": "تصنيف:عروض تلفزيونية تقع أحداثها في متاجر متعددة الأقسام",
    "Category:Films set in department stores": "تصنيف:أفلام تقع أحداثها في متاجر متعددة الأقسام",
    "Category:Fiction about department stores": "تصنيف:الخيال عن متاجر متعددة الأقسام",
}

data_3 = {
    "Category:Defunct department stores based in New York State": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في ولاية نيويورك",
    "Category:Defunct department stores based in Washington State": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في ولاية واشنطن",
    "Category:Online clothing retailers": "تصنيف:متاجر ملابس بالتجزئة عبر الإنترنت",
    "Category:Online clothing retailers of Canada": "تصنيف:متاجر ملابس بالتجزئة عبر الإنترنت في كندا",
    "Category:Online clothing retailers of Germany": "تصنيف:متاجر ملابس بالتجزئة عبر الإنترنت في ألمانيا",
    "Category:Online clothing retailers of India": "تصنيف:متاجر ملابس بالتجزئة عبر الإنترنت في الهند",
    "Category:Online clothing retailers of Italy": "تصنيف:متاجر ملابس بالتجزئة عبر الإنترنت في إيطاليا",
    "Category:Online clothing retailers of Singapore": "تصنيف:متاجر ملابس بالتجزئة عبر الإنترنت في سنغافورة",
    "Category:Online clothing retailers of Spain": "تصنيف:متاجر ملابس بالتجزئة عبر الإنترنت في إسبانيا",
    "Category:Online clothing retailers of the United Kingdom": "تصنيف:متاجر ملابس بالتجزئة عبر الإنترنت في المملكة المتحدة",
    "Category:Online clothing retailers of the United States": "تصنيف:متاجر ملابس بالتجزئة عبر الإنترنت في الولايات المتحدة",
    "Category:Defunct clothing retailers of the United States": "تصنيف:متاجر ملابس بالتجزئة سابقة في الولايات المتحدة",
    "Category:Defunct department stores": "تصنيف:متاجر متعددة الأقسام سابقة",
    "Category:Defunct department stores based in Alabama": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في ألاباما",
    "Category:Defunct department stores based in Arizona": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في أريزونا",
    "Category:Defunct department stores based in Arkansas": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في أركنساس",
    "Category:Defunct department stores based in Atlanta": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في أتلانتا (جورجيا)",
    "Category:Defunct department stores based in California": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في كاليفورنيا",
    "Category:Defunct department stores based in Chicago": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في شيكاغو",
    "Category:Defunct department stores based in Cincinnati": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في سينسيناتي",
    "Category:Defunct department stores based in Cleveland": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في كليفلاند",
    "Category:Defunct department stores based in Colorado": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في كولورادو",
    "Category:Defunct department stores based in Columbus, Ohio": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في كولومبوس (أوهايو)",
    "Category:Defunct department stores based in Connecticut": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في كونيتيكت",
    "Category:Defunct department stores based in Dayton, Ohio": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في دايتون (أوهايو)",
    "Category:Defunct department stores based in Florida": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في فلوريدا",
    "Category:Defunct department stores based in Georgia (U.S. state)": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في ولاية جورجيا",
    "Category:Defunct department stores based in Hawaii": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في هاواي",
    "Category:Defunct department stores based in Hollywood": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في هوليوود",
    "Category:Defunct department stores based in Illinois": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في إلينوي",
    "Category:Defunct department stores based in Indiana": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في إنديانا",
    "Category:Defunct department stores based in Iowa": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في آيوا",
    "Category:Defunct department stores based in Kentucky": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في كنتاكي",
    "Category:Defunct department stores based in Long Beach, California": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في لونغ بيتش (كاليفورنيا)",
    "Category:Defunct department stores based in Louisiana": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في لويزيانا",
    "Category:Defunct department stores based in Maine": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في مين",
    "Category:Defunct department stores based in Maryland": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في ماريلند",
    "Category:Defunct department stores based in Massachusetts": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في ماساتشوستس",
    "Category:Defunct department stores based in Michigan": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في ميشيغان",
    "Category:Defunct department stores based in Minnesota": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في منيسوتا",
    "Category:Defunct department stores based in Mississippi": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في مسيسيبي",
    "Category:Defunct department stores based in Missouri": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في ميزوري",
    "Category:Defunct department stores based in Nebraska": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في نبراسكا",
    "Category:Defunct department stores based in Nevada": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في نيفادا",
    "Category:Defunct department stores based in New Jersey": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في نيوجيرسي",
    "Category:Defunct department stores based in New York City": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في مدينة نيويورك",
    "Category:Defunct department stores based in North Carolina": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في كارولاينا الشمالية",
    "Category:Defunct department stores based in North Dakota": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في داكوتا الشمالية",
    "Category:Defunct department stores based in Ohio": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في أوهايو",
    "Category:Defunct department stores based in Oklahoma": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في أوكلاهوما",
    "Category:Defunct department stores based in Orange County, California": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في مقاطعة أورانج (كاليفورنيا)",
    "Category:Defunct department stores based in Oregon": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في أوريغن",
    "Category:Defunct department stores based in Pennsylvania": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في بنسلفانيا",
    "Category:Defunct department stores based in Philadelphia": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في فيلادلفيا",
    "Category:Defunct department stores based in Pittsburgh": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في بيتسبرغ",
    "Category:Defunct department stores based in Sacramento": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في ساكرامينتو",
    "Category:Defunct department stores based in San Bernardino County, California": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في مقاطعه سان بيرناردينو (كاليفورنيا)",
    "Category:Defunct department stores based in San Diego": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في سان دييغو",
    "Category:Defunct department stores based in South Carolina": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في كارولاينا الجنوبية",
    "Category:Defunct department stores based in Tennessee": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في تينيسي",
    "Category:Defunct department stores based in Texas": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في تكساس",
    "Category:Defunct department stores based in the City of Los Angeles": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في مدينة لوس أنجلوس",
    "Category:Defunct department stores based in the San Francisco Bay Area": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في منطقة خليج سان فرانسيسكو",
    "Category:Defunct department stores based in Toledo, Ohio": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في توليدو (أوهايو)",
    "Category:Defunct department stores based in Utah": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في يوتا",
    "Category:Defunct department stores based in Virginia": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في فرجينيا",
    "Category:Defunct department stores based in Washington, D.C.": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في واشنطن العاصمة",
    "Category:Defunct department stores based in West Virginia": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في فرجينيا الغربية",
    "Category:Defunct department stores based in Wisconsin": "تصنيف:متاجر متعددة الأقسام سابقة مقرها في ويسكونسن",
    "Category:Defunct department stores by country": "تصنيف:متاجر متعددة الأقسام سابقة حسب البلد",
    "Category:Defunct department stores of Australia": "تصنيف:متاجر متعددة الأقسام سابقة في أستراليا",
    "Category:Defunct department stores of Mexico": "تصنيف:متاجر متعددة الأقسام سابقة في المكسيك",
    "Category:Defunct department stores of Thailand": "تصنيف:متاجر متعددة الأقسام سابقة في تايلاند",
    "Category:Defunct department stores of the United Kingdom": "تصنيف:متاجر متعددة الأقسام سابقة في المملكة المتحدة",
    "Category:Defunct department stores of the United States": "تصنيف:متاجر متعددة الأقسام سابقة في الولايات المتحدة",
    "Category:Defunct department stores of the United States by city": "تصنيف:متاجر متعددة الأقسام سابقة في الولايات المتحدة حسب المدينة",
    "Category:Defunct department stores of the United States by state": "تصنيف:متاجر متعددة الأقسام سابقة في الولايات المتحدة حسب الولاية",
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_departments_1(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_departments_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
@pytest.mark.fast
def test_departments_3(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_departments_1", data_1),
    ("test_departments_2", data_2),
    ("test_departments_3", data_3),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
