#!/usr/bin/python3


"""
SELECT DISTINCT #?item ?humanLabel
#?ar
#?page_en ?page_ar
(concat('   "' , ?page_en , '":"' , ?page_ar  , '",')  as ?itemscds)
WHERE {
  ?human wdt:P31 ?cc.
  #?cc wdt:P31 wd:Q31629. # رياضة
  ?cc wdt:P31 wd:Q151885.#مفهووم
 FILTER NOT EXISTS{ ?human wdt:P31 wd:Q28640. } #مهن
  FILTER NOT EXISTS { ?human wdt:P31 wd:Q12737077.}#مهنة
  FILTER NOT EXISTS {?human wdt:P31 wd:Q31629. }
  FILTER NOT EXISTS {?human wdt:P31 wd:Q188451. }
  FILTER NOT EXISTS {?human wdt:P31 wd:Q1968435. }
  ?human wdt:P910 ?item .
  ?item wdt:P301 ?human.
  ?article schema:about ?item ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?page_en .
  ?article2 schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> ; schema:name ?page_ar .
  #FILTER NOT EXISTS {?article schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> . }.
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "ar,en" .
  }
  ?item rdfs:label ?ar .  FILTER((LANG(?ar)) = "ar")

    }
#LIMIT 100
"""

# from .all_keys5 import Clubs_key_2, pop_final_5
# ---
import sys

from .utils.json_dir import open_json_file

from .male_keys import New_male_keys
from ..helps import len_print

# ---
clubs_query = """
    # تصانيف الأندية
    SELECT DISTINCT #?cat
    #?ar  ?humanLabel
    #?page_en ?page_ar
    #(concat('   "' , ?page_en , '":"' , ?ar  , '",')  as ?itemscds)
    (concat('   "' , ?page_en , '":"' , ?page_ar  , '",')  as ?itemscds)
    WHERE {
    #?human wdt:P31 wd:Q5.#
    ?human wdt:P31 wd:Q476028.
    #?human wdt:P31/wdt:P279* wd:Q515.#
    #?human wdt:P31/wdt:P279* wd:Q486972.
    ?human wdt:P910 ?cat .
    #?cat wdt:P301 ?human.
    {?cat rdfs:label ?page_ar .  FILTER((LANG(?page_ar)) = "ar") } UNION
    { ?article2 schema:about ?cat ; schema:isPartOf <https://ar.wikipedia.org/> ; schema:name ?page_ar . }
    #OPTIONAL { ?sitelink schema:about ?cat . ?sitelink schema:isPartOf <https://ar.wikipedia.org/> }
    #OPTIONAL { ?sitelink schema:about ?cat . ?sitelink schema:inLanguage "ar" }
    # but select items with no such article
    #FILTER (!BOUND(?sitelink))
    ?article schema:about ?cat ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?page_en .
    SERVICE wikibase:label {
        bd:serviceParam wikibase:language "ar,en" .
    }
        }
    LIMIT 1000
"""
# ---
opvf = """
    # فرق غير كرة القدم وغير المنتخبات
    SELECT DISTINCT #?cat
    (concat('   "' , ?page_en , '":"' , ?page_ar  , '",')  as ?itemscds)
    WHERE {
    ?human wdt:P31/wdt:P279* wd:Q847017.
    FILTER NOT EXISTS {?human wdt:P31 wd:Q476028.} .
    FILTER NOT EXISTS {?human wdt:P31/wdt:P279* wd:Q1194951.} .

    ?human wdt:P910 ?cat .
    {?cat rdfs:label ?page_ar .  FILTER((LANG(?page_ar)) = "ar") } UNION
    { ?article2 schema:about ?cat ; schema:isPartOf <https://ar.wikipedia.org/> ; schema:name ?page_ar . }
    ?article schema:about ?cat ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?page_en .
        }
    #LIMIT 10
"""
# ---
Clubs_key = {}
# ---
Clubs_key = open_json_file("Clubs_key") or {}
# ---
# "christian saints":"قديسون",
# ---
pop_final_5 = {
    "trustees of": "أمناء",
    "members of": "أعضاء",
    "independent members": "أعضاء مستقلون",
    "jacksonian members": "أعضاء جاكسونيون",
    "members": "أعضاء",
    "secession": "الانفصالية",
    "separatism": "الانفصالية",
    "military of": "عسكرية",
    "tanks of": "دبابات",
    "relationships": "علاقات",
    "mass media": "وسائل الإعلام",
    "denominations": "طوائف",
    "equipment of": "معدات",
    "radars of": "رادارات",
    "cargo ships of": "سفن بضائع",
    "ships of": "سفن",
    "satellites of": "أقمار صناعية تتبع",
    "military aviation": "طيران عسكري",
    "wind farms": "مزارع الرياح",
    "aviation": "طيران",
    "equipment": "معدات",
    "military-equipment of": "عتاد عسكري",
    "military equipment of": "عتاد عسكري",
    "barracks": "ثكنات",
    "deuterostomes": "ثانويات الفم",
    "order of gold star (ukraine)": "وسام النجمة الذهبية الأوكراني",
    "order of the holy sepulchre": "فرسان القبر المقدس",
    "behistun inscription": "نقش بيستون",
    "macaronic language": "تلميع",
    "binding energy": "طاقة الارتباط",
    "dumping (pricing policy)": "إغراق تجاري",
    "cosmopolitanism": "كوسموبوليتية",
    "lakshmi": "لاكشمي",
    "medical privacy": "خصوصية صحية",
    "kinetic energy": "طاقة حركية",
    "prohibition": "منع الكحول",
    "chemnitz": "كيمنتس",
    "glucose": "غلوكوز",
    "weimar": "فايمار",
    "kempten": "كمبتن",
    "bottrop": "بوتروب",
    "greifswald": "غرايفسفالت",
    "schweinfurt": "شفاينفورت",
    "wilhelmshaven": "فيلهلمسهافن",
    "hof, bavaria": "هوف",
    "wolfsburg": "فولفسبورغ",
    "baden-baden": "بادن بادن",
    "patriotism": "وطنية",
    "memmingen": "ميمينجين",
    "rostock": "روستوك",
    "salzgitter": "زالتسغيتر",
    "zwickau": "تسفيكاو",
    "dortmund": "دورتموند",
    "ingolstadt": "إنغولشتات",
    "rosenheim": "روزنهايم",
    "economic indicators": "مؤشرات اقتصادية",
    "scientific skepticism": "شكوكية علمية",
    "tropes": "مجازات",
    "theism": "الإيمان بالله",
    "chemical energy": "طاقة كيميائية",
    "setting": "مواقع الأحداث",
    "fictional characters": "شخصيات خيالية",
    "economic systems": "أنظمة اقتصادية",
    "platonism": "أفلاطونية",
    "electric power": "طاقة كهربائية",
    "fifa": "فيفا",
    "determinism": "حتمية",
    "european system of central banks": "النظام الأوروبي للبنوك المركزية",
    "homeostasis": "استتباب",
    "irony": "سخرية",
    "rationalism": "عقلانية",
    "plot (narrative)": "حبكة (سرد)",
    "injection (medicine)": "حقن طبي",
    "ointments": "مراهم",
    "cardiac arrhythmia": "اضطراب النظم القلبي",
    "economic bubbles": "فقاعات اقتصادية",
    "euphemisms": "تسميل",
    "onomatopoeia": "محاكاة صوتية",
    "synecdoche": "مجاز مرسل",
    "flora of azerbaijan": "نباتات أذربيجان",
    "oligopoly": "احتكار القلة",
    "aphorisms": "حكمة",
    "dehydration": "تجفاف",
    "traffic management": "إدارة الحركة",
    "walking": "مشي",
    "types of soil": "أنواع التربة",
    "gnosticism": "غنوصية",
    "humanism": "إنسانية",
    "dresden": "درسدن",
    "metonymy": "كناية",
    "monopoly (economics)": "احتكار",
    "monopoly": "الاحتكار",
    "prayer": "صلاة",
    "tübingen": "توبينغن",
    "leipzig": "لايبزيغ",
    "nuclear power": "طاقة نووية",
    "bonn": "بون",
    "wiesbaden": "فيسبادن",
    "kassel": "كاسل",
    "communism": "شيوعية",
    "gera": "غيرا",
    "plauen": "بلاوين",
    "religious fundamentalism": "أصولية دينية",
    "mannheim": "مانهايم",
    "lüneburg": "لونبورغ",
    "eisenach": "أيسناخ",
    "death": "موت",
    "do it yourself": "افعلها بنفسك",
    "duisburg": "دويسبورغ",
    "erfurt": "إرفورت",
    "bamberg": "بامبرغ",
    "bochum": "بوخوم",
    "darmstadt": "دارمشتات",
    "göttingen": "غوتنغن",
    "offenbach am main": "أوفنباخ أم ماين",
    "karlsruhe": "كارلسروه",
    "heilbronn": "هايلبرون",
    "force": "قوى",
    "pforzheim": "بفورتسهايم",
    "atheism": "إلحاد",
    "osnabrück": "أوسنابروك",
    "schwerin": "شفيرين",
    "materialism": "مادية",
    "bremerhaven": "بريمرهافن",
    "würzburg": "فورتسبورغ",
    "erlangen": "إرلنغن",
    "fables": "حكاية رمزية",
    "fürth": "فورت",
    "idealism": "مثالية",
    "jena": "يينا",
    "regensburg": "ريغنسبورغ",
    "global warming": "احترار عالمي",
    "ulm": "أولم",
    "amberg": "آمبرغ",
    "metaphors": "استعارات",
    # ---
}
# ---
"""
    # تصانيف الأندية
    SELECT DISTINCT #?cat
    #?ar  ?humanLabel
    #?page_en ?page_ar
    #(concat('   "' , ?page_en , '":"' , ?ar  , '",')  as ?itemscds)
    (concat('   "' , ?page_en , '":"' , ?page_ar  , '",')  as ?itemscds)
    WHERE {
    #?human wdt:P31 wd:Q5.#
    ?human wdt:P31 wd:Q476028.
    #?human wdt:P31/wdt:P279* wd:Q515.#
    #?human wdt:P31/wdt:P279* wd:Q486972.
    ?human wdt:P910 ?cat .
    #?cat wdt:P301 ?human.
    {?cat rdfs:label ?page_ar .  FILTER((LANG(?page_ar)) = "ar") } UNION
    { ?article2 schema:about ?cat ; schema:isPartOf <https://ar.wikipedia.org/> ; schema:name ?page_ar . }
    #OPTIONAL { ?sitelink schema:about ?cat . ?sitelink schema:isPartOf <https://ar.wikipedia.org/> }
    #OPTIONAL { ?sitelink schema:about ?cat . ?sitelink schema:inLanguage "ar" }
    # but select items with no such article
    #FILTER (!BOUND(?sitelink))
    ?article schema:about ?cat ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?page_en .
    SERVICE wikibase:label {
        bd:serviceParam wikibase:language "ar,en" .
    }
        }
    LIMIT 1000
"""
opvf = """
    # فرق غير كرة القدم وغير المنتخبات
    SELECT DISTINCT #?cat
    (concat('   "' , ?page_en , '":"' , ?page_ar  , '",')  as ?itemscds)
    WHERE {
    ?human wdt:P31/wdt:P279* wd:Q847017.
    FILTER NOT EXISTS {?human wdt:P31 wd:Q476028.} .
    FILTER NOT EXISTS {?human wdt:P31/wdt:P279* wd:Q1194951.} .

    ?human wdt:P910 ?cat .
    {?cat rdfs:label ?page_ar .  FILTER((LANG(?page_ar)) = "ar") } UNION
    { ?article2 schema:about ?cat ; schema:isPartOf <https://ar.wikipedia.org/> ; schema:name ?page_ar . }
    ?article schema:about ?cat ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?page_en .
        }
    #LIMIT 10
"""
# ---
Clubs_key_2 = {}
# ---
for club, lab in Clubs_key.items():
    # ---
    club2 = club.lower()
    # ---
    """
    pop_final_5[f"{club2} players"] = f"لاعبو {lab}"
    pop_final_5[f"{club2} seasons"] = f"مواسم {lab}"
    pop_final_5[f"{club2} songs"] = f"أغاني {lab}"
    pop_final_5[f"{club2} chairmen and investors"] = f"رؤساء ومسيرو {lab}"
    pop_final_5[f"{club2} non-playing staff"] = "طاقم %s غير اللاعبين" % lab
    pop_final_5[f"{club2} matches"] = f"مباريات {lab}"
    pop_final_5[f"{club2} managers"] = f"مدربو {lab}"
    pop_final_5[f"{club2} templates"] = f"قوالب {lab}"
    """
    # ---
    if club and lab:
        pop_final_5[club2] = lab
        Clubs_key_2[club2] = lab
# ---
# pop_final_5[so % "buildings on the national register of historic places in"] = "مباني {} في السجل الوطني للأماكن التاريخية في".format(lab)
# pop_final_5[so % "buildings on the national register of historic places"] = "مباني {} في السجل الوطني للأماكن التاريخية".format(lab)
# ---
# "illegal logging":"",
# "people associated with":"أشخاص مرتبطين مع",
OPOPOP = {
    "bauxite": "البوكسيت",
    "coal gas-fired power stations": "محطات توليد الطاقة تعمل بغاز الفحم",
    "coal": "الفحم",
    "coal-fired power stations": "محطات توليد الطاقة تعمل بالفحم",
    "computer companies": "شركات حوسبة",
    "copper": "النحاس",
    "dragon boat": "قوارب التنين",
    "electric power generation": "توليد الكهرباء",
    "electric power transmission": "نقل الكهرباء",
    "electric power": "القدرة الكهربائية",
    "electricity sector": "قطاع الكهرباء",
    "former power stations": "محطات طاقة سابقة",
    "fossil fuel": "وقود أحفوري",
    "fossil fuels": "وقود أحفوري",
    "gas-fired power plants": "محطات طاقة وقود أحفوري",
    "gold": "الذهب",
    "hydraulic fracturing": "تصديع مائي",
    "hydroelectric power stations": "محطات طاقة كهرمائية",
    "hydroelectricity": "الطاقة الكهرومائية",
    "hydroelectrics": "كهرمائية",
    "industries": "صناعات",
    "influence (social and political)": "تأثير اجتماعي وسياسي",
    "man-made disasters": "كوارث من صنع الإنسان",
    "mines": "مناجم",
    "mining": "التعدين",
    "natural gas fields": "خطوط غاز طبيعي",
    "natural gas pipelines": "خطوط أنابيب غاز",
    "natural gas": "غاز طبيعي",
    "natural gas-fired power stations": "محطات توليد الطاقة تعمل بالغاز الطبيعي",
    "nuclear power stations": "محطات طاقة نووية",
    "nuclear power": "طاقة نووية",
    "nuclear weapons testing": "اختبار الأسلحة النووية",
    "oil and gas": "النفط والغاز",
    "oil fields": "حقول نفط",
    "oil shale": "صخر زيتي",
    "oil shale-fired power stations": "محطات توليد الطاقة تعمل بالصخر الزيتي",
    "oil": "نفط",
    "oil-fired power stations": "محطات توليد الطاقة تعمل بزيت الوقود",
    "peat-fired power stations": "محطات توليد الطاقة تعمل بالخث",
    "petroleum": "بترول",
    "photovoltaic power stations": "محطات طاقة كهروضوئية",
    "photovoltaics": "خلايا كهروضوئية",
    "pollution": "تلوث",
    "power (social and political)": "نفوذ اجتماعي وسياسي",
    "power companies": "شركات طاقة",
    "power stations": "محطات طاقة",
    "proposed power stations": "محطات طاقة مقترحة",
    "sedimentary rocks": "صخور رسوبية",
    "service industries": "صناعات خدمية",
    "shipping": "النقل البحري",
    "solar eclipses": "كسوفات شمسية",
    "solar power stations": "محطات طاقة شمسية",
    "solar power": "طاقة شمسية",
    "solid fuel": "وقود صلب",
    "solid fuels": "وقود صلب",
    "trucking": "النقل بالشاحنات",
    "water resource management in": "إدارة الموارد المائية في",
    "water transportation": "النقل المائي",
    "wind power": "طاقة الرياح",
}
# ---
for key in OPOPOP:
    key2 = key.lower()
    pop_final_5[key2] = OPOPOP[key]
# ---
for cdf in New_male_keys:
    pop_final_5[cdf] = New_male_keys[cdf]
# ---
Lenth1 = {"pop_final_5": sys.getsizeof(pop_final_5)}
# ---
len_print.lenth_pri("all_keys5.py", Lenth1)
# ---
del Clubs_key
