"""
from .test_4_list import replace_labels_2022, en_is_P17_ar_is_mens, en_is_P17_ar_is_P17, en_is_nat_ar_is_P17, en_is_nat_ar_is_al_mens, baston_men, en_is_nat_ar_is_man, en_is_nat_ar_is_al_women, baston_women, en_is_nat_ar_is_women, Wo_priffix, Me_priffix, change_male_to_female, people_priffix, Mens_suffix, priffix_lab_for_2018, Mens_priffix, Women_s_priffix, en_is_nat_ar_is_women_2, Main_priffix, Main_priffix_to, ttk, ttk2, Multi_sport_for_Jobs


"""
import copy
from .keys_23 import afc_keys
from .all_keys3 import businesspeoples
from ..geo.games_labs import summer_winter_games

from ..sports import (
    sport_formts_new_kkk,
    sport_formts_male_nat,
    sport_formts_female_nat,
)
from .all_keys2 import Books_table, Books_type
from .Newkey import pop_final6

# ---
replace_labels_2022 = {
    "مجندون أطفال": "أطفال مجندون",
}
# ---
# الإنجليزية اسم البلد والعربية نساء
# tab[Category:United States navy] = "تصنيف:البحرية الأمريكية"
# tab[Category:syria air force] = "تصنيف:القوات الجوية السورية
# ---
en_is_P17_ar_is_al_women = {
    "civil war": "الحرب الأهلية {}",
    "royal air force": "القوات الجوية الملكية {}",
    "air force": "القوات الجوية {}",
    "royal defence force": "قوات الدفاع الملكية {}",
    "navy": "البحرية {}",
    "royal navy": "البحرية الملكية {}",
    "naval force": "البحرية {}",
    "naval forces": "البحرية {}",
}
# ---
# الإنجليزية اسم البلد والعربية رجال
# tab[Category:United States government officials] = "تصنيف:مسؤولون حكوميون أمريكيون"
# ---
en_is_P17_ar_is_mens = {
    "government officials": "مسؤولون حكوميون {}",
}
# ---
# الإنجليزية والعربية اسم البلد
# tab[Category:United States board members] = "تصنيف:أعضاء مجلس الولايات المتحدة"
# ---
en_is_P17_ar_is_P17 = {
    "board members": "أعضاء مجلس {}",
    "afc women's asian cup squad": "تشكيلات {} في كأس آسيا للسيدات",
    "afc asian cup squad": "تشكيلات {} في كأس آسيا",
    "fifa world cup squad": "تشكيلات {} في كأس العالم",
    "fifa futsal world cup squad": "تشكيلات {} في كأس العالم لكرة الصالات",
    "summer olympics squad": "تشكيلات {} في الألعاب الأولمبية الصيفية",
    "winter olympics squad": "تشكيلات {} في الألعاب الأولمبية الشتوية",
    "olympics squad": "تشكيلات {} في الألعاب الأولمبية",
    "summer olympics": " {} في الألعاب الأولمبية الصيفية",
    "winter olympics": " {} في الألعاب الأولمبية الشتوية",
    "elections": "انتخابات {}",
    "government personnel": "موظفي حكومة {}",
    "executive cabinet": "مجلس وزراء {} التنفيذي",
    "political leader": "قادة {} السياسيون",
    "government": "حكومة {}",
    "cup": "كأس {}",
    "presidents": "رؤساء {}",
    "territorial officials": "مسؤولو أقاليم {}",
    "territorial judges": "قضاة أقاليم {}",
    "conflict": "نزاع {}",
    "war": "حرب {}",
    "responses": "استجابات {}",
    #    "courts" : "محاكم {}"
}
# ---
# الإنجليزي جنسية والعربي اسم البلد
# tab[Category:Bahraini King's Cup] = "تصنيف:كأس ملك البحرين"
en_is_nat_ar_is_P17 = {
    "king's cup": "كأس ملك {}",  # Bahraini King's Cup
    "cup": "كأس {}",
    "independence": "استقلال {}",
    "open": "{} المفتوحة",
    "ladies open": "{} المفتوحة للسيدات",
    "grand prix": "جائزة {} الكبرى",
    "national university": "جامعة {} الوطنية",
    "national university alumni": "خريجو جامعة {} الوطنية",
    # "open (tennis)" : "{} المفتوحة للتنس",
}
# ---
for hy in sport_formts_new_kkk.keys():
    en_is_nat_ar_is_P17[hy] = sport_formts_new_kkk[hy]
# ---
# الانجليزية جنسية
# رجالية بألف ولام التعريف
# tab[Category:Yemeni president cup] = "تصنيف:كأس الرئيس اليمني"
# ---
en_is_nat_ar_is_al_mens = {
    "president cup": "كأس الرئيس {}",
    "federation cup": "كأس الاتحاد {}",
    "fa cup": "كأس الاتحاد {}",
    "occupation": "الاحتلال {}",
    "super cup": "كأس السوبر {}",
    "elite cup": "كأس النخبة {}",
    "referendum": "الاستفتاء {}",
    "involvement": "التدخل {}",
    "census": "التعداد {}",
    # "professional football league": "الدوري {} لكرة القدم للمحترفين",
    "professional football league": "دوري كرة القدم {} للمحترفين",
    "premier football league": "الدوري {} الممتاز لكرة القدم",
    "national super league": "دوري السوبر {}",
    "super league": "دوري السوبر {}",
    "premier league": "الدوري {} الممتاز",
    "premier division": "الدوري {} الممتاز",
    "amateur football league": "الدوري {} لكرة القدم للهواة",
    "football league": "الدوري {} لكرة القدم",
    "population census": "التعداد السكاني {}",
    "population and housing census": "التعداد {} للسكان والمساكن",
    "national party": "الحزب الوطني {}",
    "criminal law": "القانون الجنائي {}",
    "family law": "قانون الأسرة {}",
    "labour law": "قانون العمل {}",
    "abortion law": "قانون الإجهاض {}",
    "rugby union leagues": "اتحاد دوري الرجبي {}",
    "women's rugby union": "اتحاد الرجبي {} للنساء",
    "rugby union": "اتحاد الرجبي {}",
    "presidential pardons": "العفو الرئاسي {}",
    "pardons": "العفو {}",
}
# ---
# العربي جنسية مثل : Yemeni > اليمني
# tab[Category:syrian invasion] = "تصنيف:الغزو السوري"
# ---
baston_men = {
    "solidarity movement": "حركة التضامن",
    "invasion": "الغزو",
    "league": "الدوري",
    "professional league": "دوري المحترفين",
    "professional league managers": "مدربو دوري المحترفين",
    "military": "الجيش",
    "army": "الجيش",
}
# ---
# Russian Professional Football League
# دوري كرة القدم الروسي للمحترفين
# ---
for er in sport_formts_male_nat:
    en_is_nat_ar_is_al_mens[er] = sport_formts_male_nat[er]
# ---
for cdc in baston_men:
    en_is_nat_ar_is_al_mens[cdc.lower()] = "%s {}" % baston_men[cdc]
# ---
# رجالية بدون ألف ولام التعريف
# tab[Category:syrian descent] = "تصنيف:أصل سوري"
# ---
en_is_nat_ar_is_man = {
    "descent": "أصل {}",
    "military occupations": "احتلال عسكري {}",
    "integration": "تكامل {}",
    "innovation": "ابتكار {}",
    "design": "تصميم {}",
    "contemporary art": "فن معاصر {}",
    "art": "فن {}",
    "cuisine": "مطبخ {}",
    "calendar": "تقويم {}",
    "literature": "أدب {}",
    "caste system": "نظام طبقي {}",
    "law": "قانون {}",
    "military equipment": "عتاد عسكري {}",
    "wine": "نبيذ {}",
    "history": "تاريخ {}",
    "nuclear history": "تاريخ نووي {}",
    "military history": "تاريخ عسكري {}",
    "diaspora": "شتات {}",
    "traditions": "تراث {}",
    "folklore": "فلكور {}",
    # "literary critics" : "نقد أدبي {}",
    "television": "تلفاز {}",
}
# ---
# نسائية بألف ولام التعريف
# الانجليزية والعربية جنسية
# tab[Category:Yemeni navy] = "تصنيف:البحرية اليمنية"
# tab[Category:syrian air force] = "تصنيف:القوات الجوية السورية"
en_is_nat_ar_is_al_women = {
    "royal air force": "القوات الجوية الملكية {}",
    "air force": "القوات الجوية {}",
    "royal defence force": "قوات الدفاع الملكية {}",
    "royal navy": "البحرية {}",
    "naval force": "البحرية {}",
    "naval forces": "البحرية {}",
    "navy": "البحرية {}",
    "airways accidents and incidents": "حوادث الخطوط الجوية {}",
    "airways accidents-and-incidents": "حوادث الخطوط الجوية {}",
    "airways": "الخطوط الجوية {}",
    "youth games": "الألعاب {} الشبابية",
    "financial crisis": "الأزمة المالية {}",
    "presidential crisis": "الأزمة الرئاسية {}",
    # "society" : "الجمعية {}",
    "military academy": "الأكاديمية العسكرية {}",
    "military college": "الكلية العسكرية {}",
    "crisis": "الأزمة {}",
    "energy crisis": "أزمة الطاقة {}",
    "constitutional crisis": "الأزمة الدستورية {}",
    "games competitors": "منافسون في الألعاب {}",
    "games medalists": "فائزون بميداليات في الألعاب {}",
    "games gold medalists": "فائزون بميداليات ذهبية في الألعاب {}",
    "games silver medalists": "فائزون بميداليات فضية في الألعاب {}",
    "games bronze medalists": "فائزون بميداليات برونزية في الألعاب {}",
    "television people": "شخصيات التلفزة {}",
    # ---
    "presidential primaries": "الانتخابات الرئاسية التمهيدية {}",
    "legislative election": "الانتخابات التشريعية {}",
    "parliamentary election": "الانتخابات البرلمانية {}",
    "general election": "الانتخابات العامة {}",
    "regional election": "انتخابات الإقليمية {}",
    "vice-presidential election": "انتخابات نائب الرئاسة {}",
    "presidential primarie": "الانتخابات الرئاسية التمهيدية {nat}",
    "presidential election": "انتخابات الرئاسة {}",
    # ---
}
# ---
for uuy, oio in sport_formts_female_nat.items():
    # if uuy in ["road cycling"] : continue
    en_is_nat_ar_is_al_women[uuy] = oio
# ---
# [Category:myanmarian movement] = "تصنيف:الحركة الميانمارية"
baston_women = {
    "movement": "الحركة",
    "unity cup": "كأس الوحدة",
    "rail": "السكك الحديدية",
    # "grand prix" : "الجائزة الكبرى",
    "television": "التلفزة",
    "revolution": "الثورة",
    "war": "الحرب",
    "civil war": "الحرب الأهلية",
    "detention": "المعتقلات",
    "para games": "الألعاب البارالمبية",
    "games": "الألعاب",
    "medical association": "الجمعية الطبية",
    "football": "كرة القدم",
    "soccer": "كرة القدم",
    "cinema": "السينما",
    "politics": "السياسة",
    # "sports" : "الرياضة",
}
# ---
for cdc in baston_women:
    en_is_nat_ar_is_al_women[cdc.lower()] = "%s {}" % baston_women[cdc]
# ---
# جنسية عربي وإنجليزي
# نسائية بدون ألف ولام التعريف
# tab[Category:myanmarian crimes] = "تصنيف:جرائم ميانمارية"
en_is_nat_ar_is_women = {
    "phonologies": "تصريفات صوتية {}",
    "crimes": "جرائم {}",
    "crimes against humanity": "جرائم ضد الإنسانية {}",
    "war crimes": "جرائم حرب {}",
    "airstrikes": "ضربات جوية {}",
    "archipelagoes": "أرخبيلات {}",
    "architecture": "عمارة {}",
    "autobiographies": "ترجمة ذاتية {}",
    "automotive": "سيارات {}",
    "awards and decorations": "جوائز وأوسمة {}",
    "awards": "جوائز {}",
    "ballot measures": "إجراءات اقتراع {}",
    "ballot propositions": "اقتراحات اقتراع {}",
    "border crossings": "معابر حدودية {}",
    "border": "حدود {}",
    "brands": "ماركات {}",
    "budgets": "موازنات {}",
    "buildings": "مباني {}",
    "business culture": "ثقافة مالية {}",
    "businesspeople": "شخصيات أعمال {}",
    "cantons": "كانتونات {}",
    "casualties": "خسائر {}",
    "cathedrals": "كاتدرائيات {}",
    "championships": "بطولات {}",
    "civil awards and decorations": "جوائز وأوسمة مدنية {}",
    "classical albums": "ألبومات كلاسيكية {}",
    "classical music": "موسيقى كلاسيكية {}",
    "clothing": "ملابس {}",
    "clubs": "أندية {}",
    "coats of arms": "شعارات نبالة {}",
    "colonial": "مستعمرات {}",
    "comedy albums": "ألبومات كوميدية {}",
    "comedy music": "موسيقى كوميدية {}",
    "comedy": "كوميديا {}",
    "companies": "شركات {}",
    "competitions": "منافسات {}",
    "compilation albums": "ألبومات تجميعية {}",
    "countries": "بلدان {}",
    "culture": "ثقافة {}",
    "decorations": "أوسمة {}",
    "diplomatic missions": "بعثات دبلوماسية {}",
    "discoveries": "اكتشافات {}",
    "drink": "مشروبات {}",
    "elections": "انتخابات {}",
    "encyclopedias": "موسوعات {}",
    "executions": "إعدامات {}",
    "explosions": "انفجارات {}",
    "families": "عائلات {}",
    "fauna": "حيوانات {}",
    "festivals": "مهرجانات {}",
    "folk albums": "ألبومات فلكلورية {}",
    "folk music": "موسيقى فلكلورية {}",
    "folklore characters": "شخصيات فلكلورية {}",
    "football club matches": "مباريات أندية كرة قدم {}",
    "football club seasons": "مواسم أندية كرة قدم {}",
    "forests": "غابات {}",
    "gangs": "عصابات {}",
    "given names": "أسماء شخصية {}",
    "heraldry": "نبالة {}",
    "heritage sites": "موقع تراث عالمي {}",
    "inscriptionss": "نقوش وكتابات {}",
    "introductions": "استحداثات {}",
    "inventions": "اختراعات {}",
    "islands": "جزر {}",
    "issues": "قضايا {}",
    "jewellery": "مجوهرات {}",
    "journalism": "صحافة {}",
    "lakes": "بحيرات {}",
    "learned and professional societies": "جمعيات علمية ومهنية {}",
    "learned societies": "جمعيات علمية {}",
    "literary awards": "جوائز أدبية {}",
    "magazines": "مجلات {}",
    # "magazines": "مجلة {}",
    "mascots": "تمائم {}",
    "masculine given names": "أسماء ذكور {}",
    "media personalities": "شخصيات إعلامية {}",
    "media": "وسائل إعلام {}",
    "memoirs": "مذكرات {}",
    "memorials and cemeteries": "نصب تذكارية ومقابر {}",
    "military equipment": "معدات عسكرية {}",
    "military terminology": "مصطلحات عسكرية {}",
    "military-equipment": "معدات عسكرية {}",
    "military-terminology": "مصطلحات عسكرية {}",
    "mixtape albums": "ألبومات ميكستايب {}",
    "mixtape music": "موسيقى ميكستايب {}",
    "monarchy": "ملكية {}",
    "motorsport": "رياضة محركات {}",
    "mountains": "جبال {}",
    "movies": "أفلام {}",
    "music people": "شخصيات موسيقية {}",
    "music personalities": "شخصيات موسيقية {}",
    "music": "موسيقى {}",
    "musical duos": "فرق موسيقية ثنائية {}",
    "musical groups": "فرق موسيقية {}",
    "musical instruments": "آلات موسيقية {}",
    "mythology": "أساطير {}",
    "phonology": "نطقيات {}",
    "names": "أسماء {}",
    "nationalism": "قومية {}",
    "newspapers": "صحف {}",
    "non-profit organizations": "منظمات غير ربحية {}",
    "non-profit publishers": "ناشرون غير ربحيون {}",
    "novels": "روايات {}",
    "online journalism": "صحافة إنترنت {}",
    "operas": "أوبيرات {}",
    "organisations": "منظمات {}",
    "organizations": "منظمات {}",
    "parishes": "أبرشيات {}",
    "parks": "متنزهات {}",
    "peoples": "شعوب {}",
    "philosophy": "فلسفة {}",
    "plays": "مسرحيات {}",
    "poems": "قصائد {}",
    "political philosophy": "فلسفة سياسية {}",
    "popular culture": "ثقافة شعبية {}",
    "professional societies": "جمعيات مهنية {}",
    "provinces": "مقاطعات {}",
    "publications": "منشورات {}",
    "radio networks": "شبكات مذياع {}",
    "radio stations": "محطات إذاعية {}",
    "radio": "راديو {}",
    "rebellions": "تمردات {}",
    "rectors": "عمدات {}",
    "referendums": "استفتاءات {}",
    "religions": "ديانات {}",
    "resorts": "منتجعات {}",
    "restaurants": "مطاعم {}",
    "revolutions": "ثورات {}",
    "riots": "أعمال شغب {}",
    "road cycling": "سباقات دراجات على الطريق {}",
    "roads": "طرقات {}",
    "royal families": "عائلات ملكية {}",
    "schools and colleges": "مدارس وكليات {}",
    "sculptures": "منحوتات {}",
    "sea temples": "معابد بحرية {}",
    "short stories": "قصص قصيرة {}",
    "societies": "جمعيات {}",
    "songs": "أغاني {}",
    "sorts events": "أحداث رياضية {}",
    "sorts-events": "أحداث رياضية {}",
    "soundtracks": "موسيقى تصويرية {}",
    "sport": "رياضة {}",
    "sports competitions": "منافسات رياضية {}",
    "sports events": "أحداث رياضية {}",
    "sports": "رياضة {}",
    "surnames": "ألقاب {}",
    "swamps": "مستنقعات {}",
    "telenovelas": "تيلينوفيلا {}",
    "television commercials": "إعلانات تجارية تلفزيونية {}",
    "television films": "أفلام تلفزيونية {}",
    "television miniseries": "مسلسلات قصيرة {}",
    "television networks": "شبكات تلفزيونية {}",
    "television news": "أخبار تلفزيونية {}",
    "television personalities": "شخصيات تلفزيونية {}",
    "television programme-debuts": "برامج تلفزيونية {} بدأ عرضها في",
    "television programmes": "برامج تلفزيونية {}",
    "television programs": "برامج تلفزيونية {}",
    "television series": "مسلسلات تلفزيونية {}",
    "film series": "سلاسل أفلام {}",
    "television series-debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
    "television series-endings": "مسلسلات تلفزيونية {} انتهت في",
    "television stations": "محطات تلفزيونية {}",
    "television-seasons": "مواسم تلفزيونية {}",
    "temples": "معابد {}",
    "tennis": "كرة مضرب {}",
    "terminology": "مصطلحات {}",
    "titles": "ألقاب {}",
    "tour": "بطولات {}",
    "towns": "بلدات {}",
    "trains": "قطارات {}",
    "trials": "محاكمات {}",
    "tribes": "قبائل {}",
    "underground culture": "ثقافة باطنية {}",
    "universities": "جامعات {}",
    "verbs": "أفعال {}",
    "video game businesspeople": "شخصيات أعمال {} في ألعاب الفيديو",
    "video games": "ألعاب فيديو {}",
    "volcanoes": "براكين {}",
    "wars": "حروب {}",
    "waterfalls": "شلالات {}",
    "webcomic": "ويب كومكس {}",
    "webcomics": "ويب كومكس {}",
    "websites": "مواقع ويب {}",
    "women's sport": "رياضة {} نسائية",
    "works": "أعمال {}",
    "youth competitions": "منافسات شبابية {}",
    "youth music competitions": "منافسات موسيقية شبابية {}",
    "youth sports competitions": "منافسات رياضية شبابية {}",
    # "athletic conference schools" : "كرة مضرب {}",
    # "ballot measures":"استفتاءات عامة {}",
    # "books" : "كتب {}",
    # "cinema" : "سينما {}",
    # "dukes" : "دوقات {}",
    # ---
}
# ---
# for sx in singers_tab.keys():
#     en_is_nat_ar_is_man[sx] = "%s {}" % singers_tab[sx]
#     en_is_nat_ar_is_women[f"{sx} groups"] = "فرق %s {}" % singers_tab[sx]
#     en_is_nat_ar_is_women[f"{sx} musical groups"] = "فرق موسيقى %s {}" % singers_tab[sx]
# ---
for iu in businesspeoples:
    en_is_nat_ar_is_women[f"{iu} businesspeople"] = "شخصيات أعمال {} في %s" % businesspeoples[iu]
    en_is_nat_ar_is_women[f"{iu} industry businesspeople"] = "شخصيات أعمال {} في صناعة %s" % businesspeoples[iu]
# ---
en_is_nat_ar_is_women_2 = copy.deepcopy(en_is_nat_ar_is_women)
# ---
for bo, bo_la in Books_table.items():
    en_is_nat_ar_is_women[bo.lower()] = "%s {}" % bo_la
    # ---
    for fyy in Books_type:
        kk = f"{fyy.lower()} {bo.lower()}"
        en_is_nat_ar_is_women[kk] = f"{bo_la} {Books_type[fyy]} {{}}"
    # ---
    en_is_nat_ar_is_women[f"non fiction {bo.lower()}"] = "%s {} غير خيالية" % bo_la
    en_is_nat_ar_is_women[f"non-fiction {bo.lower()}"] = "%s {} غير خيالية" % bo_la
    en_is_nat_ar_is_women[f"online {bo.lower()}"] = "%s إنترنت {}" % bo_la
# ---
for bo in pop_final6:
    en_is_nat_ar_is_women[bo.lower()] = "%s {}" % pop_final6[bo]
# ---
Women_s_priffix = {}
Wo_priffix = {
    # "women of" : "{}",
    # "non-" : "غير {}",
    "women": "{}",
    "female": "{}",
    "women's": "{}",
    "blind": "{} مكفوفات",
    "deafblind": "{} صم ومكفوفات",
    "deaf": "{} صم",
    # "expatriate women's" : "{} مغتربات",
    # "expatriate female" : "{} مغتربات",
    # "expatriate women" : "{} مغتربات",
}
for wom in Wo_priffix:
    Women_s_priffix[wom] = Wo_priffix[wom]
    Women_s_priffix[f"expatriate {wom}"] = f"{Wo_priffix[wom]} مغتربات"
    # Women_s_priffix["executed {}".format(wom)] = "%s معدومات" % Wo_priffix[wom]
    Women_s_priffix[f"kidnapped {wom}"] = f"{Wo_priffix[wom]} مختطفات"
# Women_s_priffix["executed"] = "معدومات"
# ---
Mens_priffix = {}  # ,"kidnapped":  {"mens":"مختطفون", "womens":"مختطفات"}
# ---
Me_priffix = {
    "amputee": "{} مبتورو أحد الأطراف",
    "blind": "{} مكفوفون",
    "child": "{} أطفال",
    "children": "{} أطفال",
    "contemporary": "{} معاصرون",
    "deaf": "{} صم",
    "deafblind": "{} صم ومكفوفون",
    "disabled": "{} معاقون",
    "executed": "{} معدمون",
    "fictional": "{} خياليون",
    "latin": "{} لاتينيون",
    "lgbt male": "{} مثليون ذكور",
    "lgbt": "{} مثليون",
    "male child": "{} أطفال ذكور",
    "male deaf": "{} صم ذكور",
    "male": "{} ذكور",
    "men": "{} رجال",
    "military": "{} عسكريون",
    "mythological": "{} أسطوريون",
    "nautical": "{} بحريون",
    "political": "{} سياسيون",
    "religious": "{} دينيون",
    "romantic": "{} رومانسيون",
    # "male" : "ذكور {}",
}
# ---
change_male_to_female = {
    "{} مغتربون": "{} مغتربات",
    "{} مختطفون": "{} مختطفات",
    "{} معدمون": "{} معدمات",
    "{} معاقون": "{} معاقات",
    "{} مثليون": "{} مثليات",
    "{} أصليون": "{} أصليات",
    "{} أسطوريون": "{} أسطوريات",
    "{} خياليون": "{} خياليات",
    "{} بحريون": "{} بحريات",
    "{} سياسيون": "{} سياسيات",
    "{} معاصرون": "{} معاصرات",
    "{} عسكريون": "{} عسكريات",
    "{} لاتينيون": "{} لاتينيات",
    "{} رومانسيون": "{} رومانسيات",
    "{} دينيون": "{} دينيات",
}
# ---
for me in Me_priffix:
    Mens_priffix[me] = Me_priffix[me]
    Mens_priffix[f"expatriate {me}"] = f"{Me_priffix[me]} مغتربون"
# ---
Years_List = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
# ---
for year in Years_List:
    Mens_priffix[f"under-{year}"] = "{} تحت %d سنة" % year
    Mens_priffix[f"under–{year}"] = "{} تحت %d سنة" % year
# ---
Mens_priffix["kidnapped"] = "{} مختطفون"
Mens_priffix["expatriate"] = "{} مغتربون"
Mens_priffix["renaissance"] = "{} عصر النهضة"
Mens_priffix["murdered"] = "{} قتلوا"
Mens_priffix["under-19"] = "{} تحت 19 سنة"
Mens_priffix["assassinated"] = "{} مغتالون"
Mens_priffix["sunni muslim"] = "{} مسلمون سنة"
# ---
people_priffix = {
    # ---
    "assassinated": "{} مغتالون",
    "fictional": "{} خياليون",
    "native": "{} أصليون",
    "murdered": "{} قتلوا",
    "killed": "{} قتلوا",
    "contemporary": "{} معاصرون",
    "ancient": "{} قدماء",
}
# ---
Mens_suffix = {
    "male deaf": "{} صم ذكور",
    "blind": "{} مكفوفون",
    "deafblind": "{} صم ومكفوفون",
    "deaf": "{} صم",
    "missing-in-action": "{} فقدوا في عمليات قتالية",
    "missing in action": "{} فقدوا في عمليات قتالية",
    "killed-in-action": "{} قتلوا في عمليات قتالية",
    "killed in action": "{} قتلوا في عمليات قتالية",
    "murdered abroad": "{} قتلوا في الخارج",
}
# ---
priffix_lab_for_2018 = {
    # ---
    "fictional": {"men": "{} خيالي", "women": "{} خيالية"},
    "native": {"men": "{} أصلي", "women": "{} أصلية"},
    "contemporary": {"men": "{} معاصر", "women": "{} معاصرة"},
    "ancient": {"men": "{} قديم", "women": "{} قديمة"},
}
# ---
Main_priffix = {
    # ---
    "assassinated": "{} مغتالون",
    "fictional": "{} خياليون",
    "native": "{} أصليون",
    "murdered": "{} قتلوا",
    "killed": "{} قتلوا",
    "contemporary": "{} معاصرون",
    "ancient": "{} قدماء",
    # ---
    "cultural depictions of": "تصوير ثقافي عن {}",
    "fictional depictions of": "تصوير خيالي عن {}",
    "depictions of": "تصوير عن {}",
    # "medieval" : "{} من العصور الوسطى",
    "non": "{} غير",
    # "non" : "غير {}",
}
Main_priffix_to = {
    "non": "{t} غير {nat}",
}

ttk = {
    "cultural depictions of": "التصوير الثقافي ل{}",
    "fictional depictions of": "التصوير الخيالي ل{}",
    "depictions of": "تصوير عن {}",
}

ttk2 = {
    "cultural depictions of": "تصوير ثقافي عن {}",
    "fictional depictions of": "تصوير خيالي عن {}",
    "depictions of": "تصوير عن {}",
}

Multi_sport_for_Jobs = {
    "afc asian cup": "كأس آسيا",
    "afc cup": "كأس الاتحاد الآسيوي",
    "fifa futsal world cup": "كأس العالم لكرة الصالات",
}

Multi_sport_for_Jobs.update(summer_winter_games)
Multi_sport_for_Jobs.update(afc_keys)
