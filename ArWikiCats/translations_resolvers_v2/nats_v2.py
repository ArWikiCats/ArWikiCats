#!/usr/bin/python3
"""
TODO: use this instead of for_me.py and nats_women.py
"""
import functools

from ..helps import logger
from ..translations_resolvers_v2.nats_as_country_names import nats_keys_as_country_names, nats_keys_as_country_names_bad_keys
from ..translations_formats import FormatDataV2
from ..translations import all_country_with_nat_ar
from .data import country_names_and_nats_data

peoples_nats_not_jobs_males = {
    "{en} expatriates": "{males} مغتربون",
    "{en} emigrants": "{males} مهاجرون",
    # "Category:Indonesian women singers": "تصنيف:مغنيات إندونيسيات",
    "{en} singers": "مغنون {males}",
    "{en} women singers": "مغنيات {females}",
}

males_data = {
    # en_is_nat_ar_is_mens
    "{en} non profit publishers": "ناشرون غير ربحيون {males}",
    "{en} non-profit publishers": "ناشرون غير ربحيون {males}",
    "{en} government officials": "مسؤولون حكوميون {males}",
}

males_data.update(peoples_nats_not_jobs_males)

ar_data = {
    # ar - en_is_nat_ar_is_P17
    "{en} grand prix": "جائزة {ar} الكبرى",
    "{en} king's cup": "كأس ملك {ar}",  # Bahraini King's Cup
    "{en} cup": "كأس {ar}",
    "{en} independence": "استقلال {ar}",
    "{en} open": "{ar} المفتوحة",
    "{en} ladies open": "{ar} المفتوحة للسيدات",
    "{en} national university": "جامعة {ar} الوطنية",
    "{en} national university alumni": "خريجو جامعة {ar} الوطنية",
    "{en} national women's motorsports racing team": "منتخب {ar} لسباق رياضة المحركات للسيدات",

}

the_male_data = {
    "{en} nationality law": "قانون الجنسية {the_male}",
    "{en} executive council": "المجلس التنفيذي {the_male}",
    "{en} executive council positions": "مناصب في المجلس التنفيذي {the_male}",
    "former {en} executive council positions": "مناصب سابقة في المجلس التنفيذي {the_male}",

    # the_male - en_is_nat_ar_is_al_mens
    "{en} president cup": "كأس الرئيس {the_male}",
    "{en} federation cup": "كأس الاتحاد {the_male}",
    "{en} fa cup": "كأس الاتحاد {the_male}",
    "{en} occupation": "الاحتلال {the_male}",
    "{en} super cup": "كأس السوبر {the_male}",
    "{en} elite cup": "كأس النخبة {the_male}",
    "{en} referendum": "الاستفتاء {the_male}",
    "{en} involvement": "التدخل {the_male}",
    "{en} census": "التعداد {the_male}",
    "{en} professional football league": "دوري كرة القدم {the_male} للمحترفين",
    "{en} premier football league": "الدوري {the_male} الممتاز لكرة القدم",
    "{en} national super league": "دوري السوبر {the_male}",
    "{en} super league": "دوري السوبر {the_male}",
    "{en} premier league": "الدوري {the_male} الممتاز",
    "{en} premier division": "الدوري {the_male} الممتاز",
    "{en} amateur football league": "الدوري {the_male} لكرة القدم للهواة",
    "{en} football league": "الدوري {the_male} لكرة القدم",
    "{en} population census": "التعداد السكاني {the_male}",
    "{en} population and housing census": "التعداد {the_male} للسكان والمساكن",
    "{en} national party": "الحزب الوطني {the_male}",
    "{en} criminal law": "القانون الجنائي {the_male}",
    "{en} family law": "قانون الأسرة {the_male}",
    "{en} labour law": "قانون العمل {the_male}",
    "{en} abortion law": "قانون الإجهاض {the_male}",
    "{en} rugby union leagues": "اتحاد دوري الرجبي {the_male}",
    "{en} women's rugby union": "اتحاد الرجبي {the_male} للنساء",
    "{en} rugby union": "اتحاد الرجبي {the_male}",
    "{en} presidential pardons": "العفو الرئاسي {the_male}",
    "{en} pardons": "العفو {the_male}",
}

male_data = {
    # male - en_is_nat_ar_is_man
    # "{en} television": "تلفاز {male}",

    "{en} diaspora": "شتات {male}",
    "{en} descent": "أصل {male}",
    "{en} military occupations": "احتلال عسكري {male}",
    "{en} integration": "تكامل {male}",
    "{en} innovation": "ابتكار {male}",
    "{en} design": "تصميم {male}",
    "{en} contemporary art": "فن معاصر {male}",
    "{en} art": "فن {male}",
    "{en} cuisine": "مطبخ {male}",
    "{en} calendar": "تقويم {male}",
    "{en} non fiction literature": "أدب غير خيالي {male}",
    "{en} non-fiction literature": "أدب غير خيالي {male}",
    "{en} literature": "أدب {male}",
    "{en} caste system": "نظام طبقي {male}",
    "{en} law": "قانون {male}",
    "{en} wine": "نبيذ {male}",
    "{en} history": "تاريخ {male}",
    "{en} nuclear history": "تاريخ نووي {male}",
    "{en} military history": "تاريخ عسكري {male}",
    "{en} traditions": "تراث {male}",
    "{en} folklore": "فلكور {male}",
}

female_data = {
    "{en} entertainment industry businesspeople": "شخصيات أعمال {female} في صناعة الترفيه",
    "{en} non-fiction comic strips": "شرائط مصورة {female} غير خيالية",
    "{en} non-fiction comic": "قصص مصورة {female} غير خيالية",
    "{en} non-fiction comics": "قصص مصورة {female} غير خيالية",
    "{en} non-fiction crime": "جريمة {female} غير خيالية",
    "{en} non-fiction graphic novels": "روايات مصورة {female} غير خيالية",
    "{en} non-fiction novels": "روايات {female} غير خيالية",

    # female - en_is_nat_ar_is_women
    "{en} non-fiction books": "كتب {female} غير خيالية",
    "{en} non fiction books": "كتب {female} غير خيالية",
    "{en} books": "كتب {female}",
    "{en} phonologies": "تصريفات صوتية {female}",
    "{en} crimes": "جرائم {female}",
    "{en} crimes against humanity": "جرائم ضد الإنسانية {female}",
    "{en} war crimes": "جرائم حرب {female}",
    "{en} airstrikes": "ضربات جوية {female}",
    "{en} archipelagoes": "أرخبيلات {female}",
    "{en} architecture": "عمارة {female}",
    "{en} autobiographies": "ترجمة ذاتية {female}",
    "{en} automotive": "سيارات {female}",
    "{en} awards and decorations": "جوائز وأوسمة {female}",
    "{en} awards": "جوائز {female}",
    "{en} ballot measures": "إجراءات اقتراع {female}",
    "{en} ballot propositions": "اقتراحات اقتراع {female}",
    "{en} border crossings": "معابر حدودية {female}",
    "{en} border": "حدود {female}",
    "{en} brands": "ماركات {female}",
    "{en} budgets": "موازنات {female}",
    "{en} buildings": "مباني {female}",
    "{en} business culture": "ثقافة مالية {female}",
    "{en} businesspeople": "شخصيات أعمال {female}",
    "{en} cantons": "كانتونات {female}",
    "{en} casualties": "خسائر {female}",
    "{en} cathedrals": "كاتدرائيات {female}",
    "{en} championships": "بطولات {female}",
    "{en} civil awards and decorations": "جوائز وأوسمة مدنية {female}",
    "{en} classical albums": "ألبومات كلاسيكية {female}",
    "{en} classical music": "موسيقى كلاسيكية {female}",
    "{en} clothing": "ملابس {female}",
    "{en} clubs": "أندية {female}",
    "{en} coats of arms": "شعارات نبالة {female}",
    "{en} colonial": "مستعمرات {female}",
    "{en} comedy albums": "ألبومات كوميدية {female}",
    "{en} comedy music": "موسيقى كوميدية {female}",
    "{en} comedy": "كوميديا {female}",
    "{en} companies": "شركات {female}",
    "{en} competitions": "منافسات {female}",
    "{en} compilation albums": "ألبومات تجميعية {female}",
    "{en} countries": "بلدان {female}",
    "{en} culture": "ثقافة {female}",
    "{en} decorations": "أوسمة {female}",
    "{en} diplomatic missions": "بعثات دبلوماسية {female}",
    "{en} discoveries": "اكتشافات {female}",
    "{en} drink": "مشروبات {female}",
    "{en} elections": "انتخابات {female}",
    "{en} encyclopedias": "موسوعات {female}",
    "{en} executions": "إعدامات {female}",
    "{en} explosions": "انفجارات {female}",
    "{en} families": "عائلات {female}",
    "{en} fauna": "حيوانات {female}",
    "{en} festivals": "مهرجانات {female}",
    "{en} folk albums": "ألبومات فلكلورية {female}",
    "{en} folk music": "موسيقى فلكلورية {female}",
    "{en} folklore characters": "شخصيات فلكلورية {female}",
    "{en} football club matches": "مباريات أندية كرة قدم {female}",
    "{en} football club seasons": "مواسم أندية كرة قدم {female}",
    "{en} forests": "غابات {female}",
    "{en} gangs": "عصابات {female}",
    "{en} given names": "أسماء شخصية {female}",
    "{en} heraldry": "نبالة {female}",
    "{en} heritage sites": "موقع تراث عالمي {female}",
    "{en} inscriptions": "نقوش {female}",
    "{en} introductions": "استحداثات {female}",
    "{en} inventions": "اختراعات {female}",
    "{en} islands": "جزر {female}",
    "{en} issues": "قضايا {female}",
    "{en} jewellery": "مجوهرات {female}",
    "{en} journalism": "صحافة {female}",
    "{en} lakes": "بحيرات {female}",
    "{en} learned and professional societies": "جمعيات علمية ومهنية {female}",
    "{en} learned societies": "جمعيات علمية {female}",
    "{en} literary awards": "جوائز أدبية {female}",
    "{en} magazines": "مجلات {female}",
    "{en} mascots": "تمائم {female}",
    "{en} masculine given names": "أسماء ذكور {female}",
    "{en} media personalities": "شخصيات إعلامية {female}",
    "{en} media": "وسائل إعلام {female}",
    "{en} memoirs": "مذكرات {female}",
    "{en} memorials and cemeteries": "نصب تذكارية ومقابر {female}",
    "{en} military equipment": "معدات عسكرية {female}",
    "{en} military terminology": "مصطلحات عسكرية {female}",
    "{en} military-equipment": "معدات عسكرية {female}",
    "{en} military-terminology": "مصطلحات عسكرية {female}",
    "{en} mixtape albums": "ألبومات ميكستايب {female}",
    "{en} mixtape music": "موسيقى ميكستايب {female}",
    "{en} monarchy": "ملكية {female}",
    "{en} motorsport": "رياضة محركات {female}",
    "{en} mountains": "جبال {female}",
    "{en} movies": "أفلام {female}",
    "{en} music people": "شخصيات موسيقية {female}",
    "{en} music personalities": "شخصيات موسيقية {female}",
    "{en} music": "موسيقى {female}",
    "{en} musical duos": "فرق موسيقية ثنائية {female}",
    "{en} musical groups": "فرق موسيقية {female}",
    "{en} musical instruments": "آلات موسيقية {female}",
    "{en} mythology": "أساطير {female}",
    "{en} phonology": "نطقيات {female}",
    "{en} names": "أسماء {female}",
    "{en} nationalism": "قومية {female}",
    "{en} newspapers": "صحف {female}",
    "{en} non-profit organizations": "منظمات غير ربحية {female}",
    "{en} non profit organizations": "منظمات غير ربحية {female}",
    "{en} novels": "روايات {female}",
    "{en} online journalism": "صحافة إنترنت {female}",
    "{en} operas": "أوبيرات {female}",
    "{en} organisations": "منظمات {female}",
    "{en} organizations": "منظمات {female}",
    "{en} parishes": "أبرشيات {female}",
    "{en} parks": "متنزهات {female}",
    "{en} peoples": "شعوب {female}",
    "{en} philosophy": "فلسفة {female}",
    "{en} plays": "مسرحيات {female}",
    "{en} poems": "قصائد {female}",
    "{en} political philosophy": "فلسفة سياسية {female}",
    "{en} popular culture": "ثقافة شعبية {female}",
    "{en} professional societies": "جمعيات مهنية {female}",
    "{en} provinces": "مقاطعات {female}",
    "{en} publications": "منشورات {female}",
    "{en} radio networks": "شبكات مذياع {female}",
    "{en} radio stations": "محطات إذاعية {female}",
    "{en} radio": "راديو {female}",
    "{en} rebellions": "تمردات {female}",
    "{en} occupations": "مهن {female}",
    "{en} religious occupations": "مهن دينية {female}",
    "{en} rectors": "عمدات {female}",
    "{en} referendums": "استفتاءات {female}",
    "{en} religions": "ديانات {female}",
    "{en} resorts": "منتجعات {female}",
    "{en} restaurants": "مطاعم {female}",
    "{en} revolutions": "ثورات {female}",
    "{en} riots": "أعمال شغب {female}",
    "{en} road cycling": "سباقات دراجات على الطريق {female}",
    "{en} roads": "طرقات {female}",
    "{en} royal families": "عائلات ملكية {female}",
    "{en} schools and colleges": "مدارس وكليات {female}",
    "{en} sculptures": "منحوتات {female}",
    "{en} sea temples": "معابد بحرية {female}",
    "{en} short stories": "قصص قصيرة {female}",
    "{en} societies": "جمعيات {female}",
    "{en} songs": "أغاني {female}",
    "{en} sorts events": "أحداث رياضية {female}",
    "{en} sports-events": "أحداث رياضية {female}",
    "{en} soundtracks": "موسيقى تصويرية {female}",
    "{en} sport": "رياضة {female}",
    "{en} sports competitions": "منافسات رياضية {female}",
    "{en} sports events": "أحداث رياضية {female}",
    "{en} sports": "رياضة {female}",
    "{en} surnames": "ألقاب {female}",
    "{en} swamps": "مستنقعات {female}",
    "{en} telenovelas": "تيلينوفيلا {female}",
    "{en} television commercials": "إعلانات تجارية تلفزيونية {female}",
    "{en} television films": "أفلام تلفزيونية {female}",
    "{en} television miniseries": "مسلسلات قصيرة {female}",
    "{en} television networks": "شبكات تلفزيونية {female}",
    "{en} television news": "أخبار تلفزيونية {female}",
    "{en} television personalities": "شخصيات تلفزيونية {female}",
    "{en} television programmes": "برامج تلفزيونية {female}",
    "{en} television programs": "برامج تلفزيونية {female}",
    "{en} television series": "مسلسلات تلفزيونية {female}",
    "non {en} television series": "مسلسلات تلفزيونية غير {female}",
    "non-{en} television series": "مسلسلات تلفزيونية غير {female}",
    "{en} film series": "سلاسل أفلام {female}",
    "{en} television series-debuts": "مسلسلات تلفزيونية {female} بدأ عرضها في",
    "{en} television series-endings": "مسلسلات تلفزيونية {female} انتهت في",
    "{en} television stations": "محطات تلفزيونية {female}",
    "{en} television-seasons": "مواسم تلفزيونية {female}",
    "{en} temples": "معابد {female}",
    "{en} tennis": "كرة مضرب {female}",
    "{en} terminology": "مصطلحات {female}",
    "{en} titles": "ألقاب {female}",
    "{en} tour": "بطولات {female}",
    "{en} towns": "بلدات {female}",
    "{en} trains": "قطارات {female}",
    "{en} trials": "محاكمات {female}",
    "{en} tribes": "قبائل {female}",
    "{en} underground culture": "ثقافة باطنية {female}",
    "{en} universities": "جامعات {female}",
    "{en} verbs": "أفعال {female}",
    "{en} video games": "ألعاب فيديو {female}",
    "{en} volcanoes": "براكين {female}",
    "{en} wars": "حروب {female}",
    "{en} waterfalls": "شلالات {female}",
    "{en} webcomic": "ويب كومكس {female}",
    "{en} webcomics": "ويب كومكس {female}",
    "{en} websites": "مواقع ويب {female}",
    "{en} women's sport": "رياضة {female} نسائية",
    "{en} works": "أعمال {female}",
    "{en} youth competitions": "منافسات شبابية {female}",
    "{en} youth music competitions": "منافسات موسيقية شبابية {female}",
    "{en} youth sports competitions": "منافسات رياضية شبابية {female}",
}

the_female_data = {
    "{en} film awards": "جوائز الأفلام {the_female}",
    "{en} film award": "جوائز الأفلام {the_female}",
    "{en} film award winners": "فائزون بجائزة الأفلام {the_female}",
    "{en} short film awards": "جوائز الأفلام القصيرة {the_female}",

    "{en} airways accidents and incidents": "حوادث الخطوط الجوية {the_female}",
    "{en} airways accidents-and-incidents": "حوادث الخطوط الجوية {the_female}",
    "{en} airways": "الخطوط الجوية {the_female}",
    "{en} youth games": "الألعاب {the_female} الشبابية",
    "{en} financial crisis": "الأزمة المالية {the_female}",
    "{en} presidential crisis": "الأزمة الرئاسية {the_female}",
    "{en} military academy": "الأكاديمية العسكرية {the_female}",
    "{en} military college": "الكلية العسكرية {the_female}",
    "{en} crisis": "الأزمة {the_female}",
    "{en} energy crisis": "أزمة الطاقة {the_female}",
    "{en} constitutional crisis": "الأزمة الدستورية {the_female}",
    "{en} games competitors": "منافسون في الألعاب {the_female}",
    "{en} games medalists": "فائزون بميداليات في الألعاب {the_female}",
    "{en} games gold medalists": "فائزون بميداليات ذهبية في الألعاب {the_female}",
    "{en} games silver medalists": "فائزون بميداليات فضية في الألعاب {the_female}",
    "{en} games bronze medalists": "فائزون بميداليات برونزية في الألعاب {the_female}",
    "{en} television people": "شخصيات التلفزة {the_female}",
    "{en} legislative election": "الانتخابات التشريعية {the_female}",
    "{en} parliamentary election": "الانتخابات البرلمانية {the_female}",
    "{en} regional election": "انتخابات الإقليمية {the_female}",
    "{en} vice-presidential election": "انتخابات نائب الرئاسة {the_female}",

    # baston_women: dict[str, str] = {
    "{en} movement": "الحركة {the_female}",
    "{en} unity cup": "كأس الوحدة {the_female}",
    "{en} rail": "السكك الحديدية {the_female}",
    "{en} television": "التلفزة {the_female}",
    "{en} revolution": "الثورة {the_female}",
    "{en} war": "الحرب {the_female}",
    "{en} border war": "حرب الحدود {the_female}",
    "{en} detention": "المعتقلات {the_female}",
    "{en} para games": "الألعاب البارالمبية {the_female}",
    "{en} games": "الألعاب {the_female}",
    "{en} medical association": "الجمعية الطبية {the_female}",
    "{en} soccer": "كرة القدم {the_female}",
    "{en} cinema": "السينما {the_female}",
    "{en} politics": "السياسة {the_female}",

    # female - military_format_women_without_al
    "{en} federal legislation": "تشريعات فيدرالية {female}",
    "{en} courts": "محاكم {female}",
    "{en} sports templates": "قوالب رياضة {female}",
    "{en} political party": "أحزاب سياسية {female}",
}

all_formatted_data = males_data | ar_data | the_male_data | female_data | male_data | the_female_data | country_names_and_nats_data


@functools.lru_cache(maxsize=1)
def _load_bot() -> FormatDataV2:
    nats_data = {
        x: v
        for x, v in all_country_with_nat_ar.items()
        if v.get("ar")
    }
    nats_data.update({
        x: v
        for x, v in nats_keys_as_country_names.items()
        if v.get("ar")
    })
    return FormatDataV2(
        formatted_data=all_formatted_data,
        data_list=nats_data,
        key_placeholder="{en}",
        text_before="the ",
    )


@functools.lru_cache(maxsize=10000)
def resolve_by_nats(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_by_nats: {category=}")

    if category in nats_keys_as_country_names_bad_keys:
        logger.debug(f"<<yellow>> end resolve_by_nats: {category=}, [result=]")
        return ""

    nat_bot = _load_bot()
    result = nat_bot.search_all_category(category)
    logger.debug(f"<<yellow>> end resolve_by_nats: {category=}, {result=}")
    return result


__all__ = [
    "resolve_by_nats",
]
