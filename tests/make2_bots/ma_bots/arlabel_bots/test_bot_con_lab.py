"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.arlabel_bots.bot_con_lab import get_con_lab

data = [
    {"tito2": "about", "country": "busan", "output": "بوسان"},
    {"tito2": "about", "country": "chefs", "output": "طباخون"},
    {"tito2": "about", "country": "chinese canadians", "output": "كنديون صينيون"},
    {"tito2": "about", "country": "slavery", "output": "العبودية"},
    {"tito2": "about", "country": "south carolina", "output": "كارولاينا الجنوبية"},
    {"tito2": "about", "country": "south dakota", "output": "داكوتا الجنوبية"},
    {"tito2": "about", "country": "the american civil war", "output": "الحرب الأهلية الأمريكية"},
    {"tito2": "about", "country": "the united states navy", "output": "البحرية الأمريكية"},
    {"tito2": "about", "country": "the vietnam war", "output": "حرب فيتنام"},
    {"tito2": "about", "country": "weather", "output": "الطقس"},
    {"tito2": "adapted for", "country": "other media", "output": "وسائط أخرى"},
    {"tito2": "adapted into", "country": "films", "output": "أفلام"},
    {"tito2": "against", "country": "the united states", "output": "الولايات المتحدة"},
    {"tito2": "and", "country": "architecture", "output": "هندسة معمارية"},
    {"tito2": "and", "country": "united states treaties", "output": "معاهدات الولايات المتحدة"},
    {"tito2": "and", "country": "värmland county", "output": "محافظة ورملاند"},
    {"tito2": "at", "country": "yemen", "output": "اليمن"},
    {"tito2": "based in", "country": "aomori prefecture", "output": "محافظة آوموري"},
    {"tito2": "based in", "country": "belarus", "output": "روسيا البيضاء"},
    {"tito2": "based in", "country": "illinois by populated place", "output": "إلينوي حسب المكان المأهول"},
    {"tito2": "basedon", "country": "american comics", "output": "قصص مصورة أمريكية"},
    {"tito2": "basedon", "country": "british television series", "output": "مسلسلات تلفزيونية بريطانية"},
    {"tito2": "basedon", "country": "comics", "output": "قصص مصورة"},
    {"tito2": "basedon", "country": "egyptian mythology", "output": "أساطير مصرية"},
    {"tito2": "between", "country": "national teams", "output": "منتخبات وطنية"},
    {"tito2": "built-in", "country": "montreal", "output": "مونتريال"},
    {"tito2": "built-in", "country": "poland", "output": "بولندا"},
    {"tito2": "by", "country": "by academic discipline", "output": "حسب التخصص الأكاديمي"},
    {"tito2": "by", "country": "by american artists", "output": "بواسطة فنانون أمريكيون"},
    {"tito2": "by", "country": "by andy warhol", "output": "بواسطة آندي وارهول"},
    {"tito2": "by", "country": "by athletic event", "output": "حسب حدث ألعاب القوى"},
    {"tito2": "by", "country": "by under-20 national team", "output": "حسب المنتخب الوطني تحت 20 سنة"},
    {"tito2": "by", "country": "by year templates", "output": "قوالب حسب السنة"},
    {"tito2": "by-car-bomb", "country": "in the united kingdom", "output": "في المملكة المتحدة"},
    {"tito2": "closed in", "country": "1420", "output": "1420"},
    {"tito2": "closed in", "country": "20th century", "output": "القرن 20"},
    {"tito2": "completed in", "country": "1420s", "output": "عقد 1420"},
    {"tito2": "completed in", "country": "2nd century", "output": "القرن 2"},
    {"tito2": "concerning", "country": "eritrea", "output": "إريتريا"},
    {"tito2": "convicted of", "country": "crimes", "output": "جرائم"},
    {"tito2": "convicted of", "country": "kidnapping", "output": "الخطف"},
    {"tito2": "created in", "country": "1420", "output": "1420"},
    {"tito2": "demolished in", "country": "1420", "output": "1420"},
    {"tito2": "described in", "country": "1420", "output": "1420"},
    {"tito2": "described in", "country": "20th century", "output": "القرن 20"},
    {"tito2": "directed by", "country": "christopher doyle", "output": "كريستوفر دويل"},
    {"tito2": "discovered in", "country": "1420", "output": "1420"},
    {"tito2": "disestablished in", "country": "1420 by country", "output": "1420 حسب البلد"},
    {"tito2": "disestablished in", "country": "14th century bc", "output": "القرن 14 ق م"},
    {"tito2": "during", "country": "world-war-ii by nationality", "output": "الحرب العالمية الثانية حسب الجنسية"},
    {"tito2": "during", "country": "world-war-ii", "output": "الحرب العالمية الثانية"},
    {"tito2": "established in", "country": "1420s", "output": "عقد 1420"},
    {"tito2": "established in", "country": "14th century", "output": "القرن 14"},
    {"tito2": "executed by", "country": "jamaica", "output": "جامايكا"},
    {"tito2": "executed by", "country": "nazi germany", "output": "ألمانيا النازية"},
    {"tito2": "executed by", "country": "new spain", "output": "إسبانيا الجديدة"},
    {"tito2": "executed by", "country": "utah by firing squad", "output": "يوتا رميا بالرصاص"},
    {"tito2": "extended to", "country": "curaçao", "output": "كوراساو"},
    {"tito2": "filmed in", "country": "algeria", "output": "الجزائر"},
    {"tito2": "filmed in", "country": "jiangsu", "output": "جيانغسو"},
    {"tito2": "for", "country": "for argentina", "output": "الأرجنتين"},
    {"tito2": "for", "country": "for australia", "output": "أستراليا"},
    {"tito2": "for", "country": "for german-language films", "output": "أفلام باللغة الألمانية"},
    {"tito2": "for", "country": "for germany", "output": "ألمانيا"},
    {"tito2": "for", "country": "for national teams", "output": "للمنتخبات الوطنية"},
    {"tito2": "for", "country": "for women's football", "output": "كرة القدم للسيدات"},
    {"tito2": "from", "country": "aden", "output": "عدن"},
    {"tito2": "from", "country": "ahrweiler (district)", "output": "أرفيلر"},
    {"tito2": "from", "country": "georgia (country)", "output": "جورجيا"},
    {"tito2": "from", "country": "georgia (u.s. state)", "output": "ولاية جورجيا"},
    {"tito2": "from", "country": "northern ireland of canadian descent", "output": "أيرلندا الشمالية من أصل كندي"},
    {"tito2": "hosted by", "country": "argentina", "output": "الأرجنتين"},
    {"tito2": "imprisoned-in", "country": "germany", "output": "ألمانيا"},
    {"tito2": "in", "country": "1420 all-africa games", "output": "ألعاب عموم إفريقيا 1420"},
    {"tito2": "in", "country": "1420 world games", "output": "الألعاب العالمية 1420"},
    {"tito2": "in", "country": "1420–51", "output": "1420–51"},
    {"tito2": "in", "country": "abkhazia", "output": "أبخازيا"},
    {"tito2": "in", "country": "afghanistan", "output": "أفغانستان"},
    {"tito2": "in", "country": "german novels of 20th century", "output": "روايات ألمانية في القرن 20"},
    {"tito2": "in", "country": "mandatory syria", "output": "الانتداب الفرنسي على سوريا ولبنان"},
    {"tito2": "in", "country": "the socialist republic-of macedonia", "output": "جمهورية مقدونيا الاشتراكية"},
    {"tito2": "in", "country": "the universiade navigational boxes", "output": "صناديق تصفح الألعاب الجامعية"},
    {"tito2": "in-sports-in", "country": "california", "output": "كاليفورنيا"},
    {"tito2": "in-sports-in", "country": "delaware", "output": "ديلاوير"},
    {"tito2": "introduced in", "country": "21st century", "output": "القرن 21"},
    {"tito2": "involving", "country": "north macedonia", "output": "مقدونيا الشمالية"},
    {"tito2": "involving the", "country": "united states", "output": "الولايات المتحدة"},
    {"tito2": "killed in", "country": "the second italo-ethiopian war", "output": "الحرب الإيطالية الإثيوبية الثانية"},
    {"tito2": "murdered in", "country": "1420", "output": "1420"},
    {"tito2": "murdered in", "country": "india by state or union territory", "output": "الهند حسب الولاية أو الإقليم الاتحادي"},
    {"tito2": "named after", "country": "american explorers", "output": "مستكشفون أمريكيون"},
    {"tito2": "named after", "country": "american novelists", "output": "روائيون أمريكيون"},
    {"tito2": "named after", "country": "canadian awards", "output": "جوائز كندية"},
    {"tito2": "named after", "country": "indian politicians", "output": "سياسيون هنود"},
    {"tito2": "named after", "country": "populated places in latvia", "output": "أماكن مأهولة في لاتفيا"},
    {"tito2": "named after", "country": "populated places in portugal", "output": "أماكن مأهولة في البرتغال"},
    {"tito2": "named after", "country": "religious organizations", "output": "منظمات دينية"},
    {"tito2": "named after", "country": "slovak musicians", "output": "موسيقيون سلوفاكيون"},
    {"tito2": "named by", "country": "theodosius dobzhansky", "output": "ثيودوسيوس دوبجانسكي"},
    {"tito2": "of", "country": "11th government of turkey", "output": "حكومة تركيا"},
    {"tito2": "of", "country": "1420 films", "output": "أفلام 1420"},
    {"tito2": "of", "country": "british television series characters", "output": "شخصيات مسلسلات تلفزيونية بريطانية"},
    {"tito2": "of", "country": "ottoman–persian wars", "output": "الحروب العثمانية الفارسية"},
    {"tito2": "of", "country": "prime ministers of malaysia", "output": "رؤساء وزراء ماليزيا"},
    {"tito2": "of", "country": "westchester county, new york", "output": "مقاطعة ويستتشستر (نيويورك)"},
    {"tito2": "on", "country": "buildings and structures", "output": "مبان ومنشآت"},
    {"tito2": "on", "country": "diplomatic missions", "output": "بعثات دبلوماسية"},
    {"tito2": "on", "country": "the moon", "output": "القمر"},
    {"tito2": "on", "country": "the-national-register-of-historic-places", "output": "السجل الوطني للأماكن التاريخية"},
    {"tito2": "opened in", "country": "19th century", "output": "القرن 19"},
    {"tito2": "originating in", "country": "turkey", "output": "تركيا"},
    {"tito2": "produced by", "country": "brian wilson", "output": "بريان ويلسون"},
    {"tito2": "produced in", "country": "alberta", "output": "ألبرتا"},
    {"tito2": "published in", "country": "finland", "output": "فنلندا"},
    {"tito2": "published in", "country": "western australia", "output": "أستراليا الغربية"},
    {"tito2": "related to", "country": "the future", "output": "المستقبل"},
    {"tito2": "remadein", "country": "other languages", "output": "لغات أخرى"},
    {"tito2": "scored by", "country": "spanish composers", "output": "ملحنون إسبان"},
    {"tito2": "sentenced to", "country": "death", "output": "الموت"},
    {"tito2": "set in", "country": "10th century", "output": "القرن 10"},
    {"tito2": "set in", "country": "australia by city", "output": "أستراليا حسب المدينة"},
    {"tito2": "shot in", "country": "china by city", "output": "الصين حسب المدينة"},
    {"tito2": "to", "country": "american samoa", "output": "ساموا الأمريكية"},
    {"tito2": "to", "country": "north korea", "output": "كوريا الشمالية"},
    {"tito2": "to", "country": "the united states house-of-representatives from missouri territory", "output": "مجلس النواب الأمريكي من إقليم ميزوري"},
    {"tito2": "to", "country": "the united states", "output": "الولايات المتحدة"},
    {"tito2": "to", "country": "togo", "output": "توغو"},
    {"tito2": "to", "country": "venezuela", "output": "فنزويلا"},
    {"tito2": "to", "country": "zimbabwe", "output": "زيمبابوي"},
    {"tito2": "who died in", "country": "prison custody", "output": "السجن"},
    {"tito2": "with screenplays by", "country": "matt damon", "output": "مات ديمون"},
    {"tito2": "written by", "country": "lady gaga", "output": "ليدي غاغا"},
]


@pytest.mark.parametrize("tab", data, ids=lambda x: f"{x['tito2']} {x['country']}")
@pytest.mark.fast
def test_event_Lab_seoo_data(tab) -> None:

    label = get_con_lab(
        preposition=f" {tab['tito2']} ",
        tito2=tab["tito2"],
        country=tab["country"],
        country_lower=tab["country"].lower(),
        start_get_country2=True
    )
    assert label.strip() == tab["output"]


def test_get_con_lab():
    # Test with basic inputs
    result = get_con_lab("from", "from", "test country", "test country", True)
    assert isinstance(result, str)

    # Test with different parameters
    result_various = get_con_lab("in", "in", "us", "us", False)
    assert isinstance(result_various, str)

    # Test with empty strings
    result_empty = get_con_lab("", "", "", "", False)
    assert isinstance(result_empty, str)
