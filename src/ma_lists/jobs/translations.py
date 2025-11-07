"""A consolidated module for job title translations.

This module contains dictionaries that map English job titles to their Arabic translations,
including gender-specific variations. The data is organized into logical groups, such as
by profession, sport, or artistic domain.

The main dictionary, `ARABIC_TRANSLATIONS`, is populated dynamically by merging all
the individual job-related dictionaries. This provides a single, comprehensive source
for all job title translations.
"""

from typing import Dict, List

# --- Type Aliases ---

GenderTranslations = Dict[str, str]
"""A dictionary containing gender-specific translations for a job title."""

# --- Main Dictionary ---

ARABIC_TRANSLATIONS: Dict[str, GenderTranslations] = {}
"""A comprehensive dictionary of all job title translations."""

# --- Religious Roles ---

RELIGIOUS_GROUPS: Dict[str, GenderTranslations] = {
    "bahá'ís": {"mens": "بهائيون", "womens": "بهائيات"},
    "yazidis": {"mens": "يزيديون", "womens": "يزيديات"},
    "christians": {"mens": "مسيحيون", "womens": "مسيحيات"},
    "anglican": {"mens": "أنجليكيون", "womens": "أنجليكيات"},
    "anglicans": {"mens": "أنجليكيون", "womens": "أنجليكيات"},
    "episcopalians": {"mens": "أسقفيون", "womens": "أسقفيات"},
    "christian": {"mens": "مسيحيون", "womens": "مسيحيات"},
    "buddhist": {"mens": "بوذيون", "womens": "بوذيات"},
    "nazi": {"mens": "نازيون", "womens": "نازيات"},
    "muslim": {"mens": "مسلمون", "womens": "مسلمات"},
    "coptic": {"mens": "أقباط", "womens": "قبطيات"},
    "islamic": {"mens": "إسلاميون", "womens": "إسلاميات"},
    "hindus": {"mens": "هندوس", "womens": "هندوسيات"},
    "hindu": {"mens": "هندوس", "womens": "هندوسيات"},
    "protestant": {"mens": "بروتستانتيون", "womens": "بروتستانتيات"},
    "methodist": {"mens": "ميثوديون لاهوتيون", "womens": "ميثوديات لاهوتيات"},
    "jewish": {"mens": "يهود", "womens": "يهوديات"},
    "jews": {"mens": "يهود", "womens": "يهوديات"},
    "zaydis": {"mens": "زيود", "womens": "زيديات"},
    "zaydi": {"mens": "زيود", "womens": "زيديات"},
    "sufis": {"mens": "صوفيون", "womens": "صوفيات"},
    "religious": {"mens": "دينيون", "womens": "دينيات"},
    "muslims": {"mens": "مسلمون", "womens": "مسلمات"},
    "shia muslims": {"mens": "مسلمون شيعة", "womens": "مسلمات شيعيات"},
    "shi'a muslims": {"mens": "مسلمون شيعة", "womens": "مسلمات شيعيات"},
    "sunni muslims": {"mens": "مسلمون سنة", "womens": "مسلمات سنيات"},
    "shia muslim": {"mens": "مسلمون شيعة", "womens": "مسلمات شيعيات"},
    "shi'a muslim": {"mens": "مسلمون شيعة", "womens": "مسلمات شيعيات"},
    "sunni muslim": {"mens": "مسلمون سنة", "womens": "مسلمات سنيات"},
    "evangelical": {"mens": "إنجيليون", "womens": "إنجيليات"},
    "venerated": {"mens": "مبجلون", "womens": "مبجلات"},
    "saints": {"mens": "قديسون", "womens": "قديسات"},
}
"""Translations for various religious groups."""

RELIGIOUS_TITLES: Dict[str, GenderTranslations] = {
    "christians": {"mens": "مسيحيون", "womens": "مسيحيات"},
    "venerated": {"mens": "مبجلون", "womens": "مبجلات"},
    "missionaries": {"mens": "مبشرون", "womens": "مبشرات"},
    "evangelical": {"mens": "إنجيليون", "womens": "إنجيليات"},
    "monks": {"mens": "رهبان", "womens": "راهبات"},
    "nuns": {"mens": "", "womens": "راهبات"},
    "saints": {"mens": "قديسون", "womens": "قديسات"},
    "astrologers": {"mens": "منجمون", "womens": "منجمات"},
    "leaders": {"mens": "قادة", "womens": "قائدات"},
    "bishops": {"mens": "أساقفة", "womens": ""},
    "actors": {"mens": "ممثلون", "womens": "ممثلات"},
    "theologians": {"mens": "لاهوتيون", "womens": "لاهوتيات"},
    "clergy": {"mens": "رجال دين", "womens": "سيدات دين"},
    "religious leaders": {"mens": "قادة دينيون", "womens": "قائدات دينيات"},
}
"""Translations for various religious titles and roles."""

# --- Artistic Professions ---

PAINTER_STYLES: Dict[str, GenderTranslations] = {
    "symbolist": {"mens": "رمزيون", "womens": "رمزيات"},
    "history": {"mens": "تاريخيون", "womens": "تاريخيات"},
    "romantic": {"mens": "رومانسيون", "womens": "رومانسيات"},
    "neoclassical": {"mens": "كلاسيكيون حديثون", "womens": "كلاسيكيات حديثات"},
    "religious": {"mens": "دينيون", "womens": "دينيات"},
}
"""Translations for different styles of painters."""

ARTIST_ROLES: Dict[str, GenderTranslations] = {
    "painters": {"mens": "رسامون", "womens": "رسامات"},
    "artists": {"mens": "فنانون", "womens": "فنانات"},
}
"""Translations for general artistic roles."""

PAINTER_CATEGORIES: Dict[str, str] = {
    "make-up": "مكياج",
    "comics": "قصص مصورة",
    "marvel comics": "مارفال كومكس",
    "manga": "مانغا",
    "landscape": "مناظر طبيعية",
    "wildlife": "حياة برية",
    "portrait": "بورتريه",
    "animal": "حيوانات",
    "genre": "نوع",
    "still life": "طبيعة صامتة",
}
"""Translations for different categories of painters."""

FILM_AND_THEATER_ROLES: Dict[str, GenderTranslations] = {
    "film": {"mens": "أفلام", "womens": "أفلام"},
    "silent film": {"mens": "أفلام صامتة", "womens": "أفلام صامتة"},
    "pornographic film": {"mens": "أفلام إباحية", "womens": "أفلام إباحية"},
    "television": {"mens": "تلفزيون", "womens": "تلفزيون"},
    "musical theatre": {"mens": "مسرحيات موسيقية", "womens": "مسرحيات موسيقية"},
    "stage": {"mens": "مسرح", "womens": "مسرح"},
    "radio": {"mens": "راديو", "womens": "راديو"},
    "voice": {"mens": "أداء صوتي", "womens": "أداء صوتي"},
    "video game": {"mens": "ألعاب فيديو", "womens": "ألعاب فيديو"},
}
"""Translations for roles in film, theater, and other media."""

MUSIC_GENRES: Dict[str, str] = {
    "song": "أغاني",
    "albums": "ألبومات",
    "comedy": "كوميديا",
    "music": "موسيقى",
    "country": "كانتري",
    "light": "خفيفة",
    "house": "الهاوس",
    "chamber": "الحجرة",
    "children's songs": "أغاني أطفال",
    "children's": "أطفال",
    "classical": "كلاسيكية",
    "electronic": "إلكترونية",
    "electronica": "إلكترونيكا",
}
"""Translations for various music genres."""

MUSICIAN_ROLES: Dict[str, GenderTranslations] = {
    "record producers": {"mens": "منتجو تسجيلات", "womens": "منتجات تسجيلات"},
    "musicians": {"mens": "موسيقيو", "womens": "موسيقيات"},
    "singers": {"mens": "مغنو", "womens": "مغنيات"},
    "singer-songwriters": {"mens": "مغنون وكتاب أغاني", "womens": "مغنيات وكاتبات أغاني"},
    "songwriters": {"mens": "كتاب أغان", "womens": "كاتبات أغان"},
    "critics": {"mens": "نقاد", "womens": "ناقدات"},
    "educators": {"mens": "معلمو", "womens": "معلمات"},
    "historians": {"mens": "مؤرخو", "womens": "مؤرخات"},
    "bloggers": {"mens": "مدونو", "womens": "مدونات"},
    "drummers": {"mens": "طبالو", "womens": "طبالات"},
    "violinists": {"mens": "عازفو كمان", "womens": "عازفات كمان"},
    "trumpeters": {"mens": "عازفو بوق", "womens": "عازفات بوق"},
    "bassoonists": {"mens": "عازفو باسون", "womens": "عازفات باسون"},
    "trombonists": {"mens": "عازفو ترومبون", "womens": "عازفات ترومبون"},
    "composers": {"mens": "ملحنو", "womens": "ملحنات"},
    "flautists": {"mens": "عازفو فولت", "womens": "عازفات فولت"},
    "writers": {"mens": "كتاب", "womens": "كاتبات"},
    "guitarists": {"mens": "عازفو قيثارة", "womens": "عازفات قيثارة"},
    "pianists": {"mens": "عازفو بيانو", "womens": "عازفات بيانو"},
    "saxophonists": {"mens": "عازفو سكسفون", "womens": "عازفات سكسفون"},
    "authors": {"mens": "مؤلفو", "womens": "مؤلفات"},
    "journalists": {"mens": "صحفيو", "womens": "صحفيات"},
    "bandleaders": {"mens": "قادة فرق", "womens": "قائدات فرق"},
    "cheerleaders": {"mens": "قادة تشجيع", "womens": "قائدات تشجيع"},
}
"""Translations for various musician roles."""

# --- Military and Political Roles ---

MILITARY_AND_POLITICAL_GROUPS: Dict[str, GenderTranslations] = {
    "military": {"mens": "عسكريون", "womens": "عسكريات"},
    "politicians": {"mens": "سياسيون", "womens": "سياسيات"},
    "nazi": {"mens": "نازيون", "womens": "نازيات"},
    "literary": {"mens": "أدبيون", "womens": "أدبيات"},
    "organizational": {"mens": "تنظيميون", "womens": "تنظيميات"},
}
"""Translations for military and political groups."""

MILITARY_AND_POLITICAL_TITLES: Dict[str, GenderTranslations] = {
    "theorists": {"mens": "منظرون", "womens": "منظرات"},
    "musicians": {"mens": "موسيقيون", "womens": "موسيقيات"},
    "engineers": {"mens": "مهندسون", "womens": "مهندسات"},
    "leaders": {"mens": "قادة", "womens": "قائدات"},
    "officers": {"mens": "ضباط", "womens": "ضابطات"},
    "historians": {"mens": "مؤرخون", "womens": "مؤرخات"},
    "strategists": {"mens": "استراتيجيون", "womens": "استراتيجيات"},
    "nurses": {"mens": "ممرضون", "womens": "ممرضات"},
}
"""Translations for military and political titles."""

# --- Sports ---

SPORTS_PLAYER_ROLES: Dict[str, GenderTranslations] = {"freestyle swimmers": {"mens": "سباحو تزلج حر", "womens": "سباحات تزلج حر"}}
"""Translations for various sports player roles."""

BOXING_WEIGHT_CLASSES: Dict[str, str] = {
    "bantamweight": "وزن بانتام",
    "featherweight": "وزن الريشة",
    "lightweight": "وزن خفيف",
    "light heavyweight": "وزن ثقيل خفيف",
    "light-heavyweight": "وزن ثقيل خفيف",
    "light middleweight": "وزن خفيف متوسط",
    "middleweight": "وزن متوسط",
    "super heavyweight": "وزن ثقيل سوبر",
    "heavyweight": "وزن ثقيل",
    "welterweight": "وزن الويلتر",
    "flyweight": "وزن الذبابة",
    "super middleweight": "وزن متوسط سوبر",
    "pinweight": "وزن الذرة",
    "super flyweight": "وزن الذبابة سوبر",
    "super featherweight": "وزن الريشة سوبر",
    "super bantamweight": "وزن البانتام سوبر",
    "light flyweight": "وزن ذبابة خفيف",
    "light welterweight": "وزن والتر خفيف",
    "cruiserweight": "وزن الطراد",
    "minimumwe": "",
    "inimumweight": "",
    "atomweight": "وزن الذرة",
    "super cruiserweight": "وزن الطراد سوبر",
}
"""Translations for boxing weight classes."""

SKATING_DISCIPLINES: Dict[str, GenderTranslations] = {
    "nordic combined": {"mens": "تزلج نوردي مزدوج", "womens": "تزلج نوردي مزدوج"},
    "speed": {"mens": "سرعة", "womens": "سرعة"},
    "roller": {"mens": "بالعجلات", "womens": "بالعجلات"},
    "alpine": {"mens": "منحدرات ثلجية", "womens": "منحدرات ثلجية"},
    "short track speed": {"mens": "مسار قصير", "womens": "مسار قصير"},
}
"""Translations for skating disciplines."""

TEAM_SPORTS: Dict[str, str] = {
    "croquet players": "",
    "badminton players": "تنس الريشة",
    "chess players": "شطرنج",
    "basketball players": "كرة السلة",
    "beach volleyball players": "",
    "fifa world cup players": "كأس العالم لكرة القدم",
    "fifa futsal world cup players": "كأس العالم لكرة الصالات",
    "polo players": "بولو",
    "racquets players": "",
    "real tennis players": "",
    "roque players": "",
    "rugby players": "الرجبي",
    "softball players": "سوفتبول",
    "floorball players": "كرة الأرض",
    "table tennis players": "كرة الطاولة",
    "volleyball players": "كرة الطائرة",
    "water polo players": "كرة الماء",
    "field hockey players": "هوكي الميدان",
    "handball players": "كرة يد",
    "tennis players": "كرة مضرب",
    "football referees": "حكام كرة قدم",
    "racing drivers": "سائقو سيارات سباق",
    "snooker players": "سنوكر",
    "baseball players": "كرة القاعدة",
    "players of american football": "كرة قدم أمريكية",
    "players of canadian football": "كرة قدم كندية",
    "association football players": "كرة قدم",
    "gaelic footballers": "كرة قدم غيلية",
    "australian rules footballers": "كرة قدم أسترالية",
    "rules footballers": "كرة قدم",
    "players of australian rules football": "كرة القدم الأسترالية",
    "kabaddi players": "كابادي",
    "poker players": "بوكر",
    "rugby league players": "دوري الرغبي",
    "rugby union players": "اتحاد الرغبي",
    "lacrosse players": "لاكروس",
}
"""Translations for team sports."""

SPORTS_ROLES: Dict[str, GenderTranslations] = {
    "managers": {"mens": "مدربون", "womens": "مدربات"},
    "competitors": {"mens": "منافسون", "womens": "منافسات"},
    "coaches": {"mens": "مدربون", "womens": "مدربات"},
}
"""Translations for general sports roles."""

OLYMPIC_AND_SPORTS_TERMS: Dict[str, GenderTranslations] = {
    "paralympic": {"mens": "بارالمبيون", "womens": "بارالمبيات"},
    "olympics": {"mens": "أولمبيون", "womens": "أولمبيات"},
    "sports": {"mens": "رياضيون", "womens": "رياضيات"},
}
"""Translations for Olympic and general sports terms."""

# --- Science and Academia ---

SCIENTIFIC_FIELDS: Dict[str, str] = {
    "anatomists": "تشريح",
    "anthropologists": "أنثروبولوجيا",
    "arachnologists": "عنكبوتيات",
    "archaeologists": "آثار",
    "assyriologists": "آشوريات",
    "atmospheric scientists": "غلاف جوي",
    "biblical scholars": "الكتاب المقدس",
    "biologists": "أحياء",
    "biotechnologists": "تكنولوجيا حيوية",
    "botanists": "نباتات",
    "cartographers": "رسم خرائط",
    "cell biologists": "أحياء خلوية",
    "computer scientists": "حاسوب",
    "cosmologists": "كون",
    "criminologists": "جريمة",
    "cryptographers": "تعمية",
    "crystallographers": "بلورات",
    "demographers": "سكان",
    "dialectologists": "لهجات",
    "earth scientists": "الأرض",
    "ecologists": "بيئة",
    "egyptologists": "مصريات",
    "entomologists": "حشرات",
    "epidemiologists": "وبائيات",
    "epigraphers": "نقائش",
    "evolutionary biologists": "أحياء تطورية",
    "experimental physicists": "فيزياء تجريبية",
    "forensic scientists": "أدلة جنائية",
    "geneticists": "وراثة",
    "herpetologists": "زواحف وبرمائيات",
    "hydrographers": "وصف المياه",
    "hygienists": "صحة",
    "ichthyologists": "أسماك",
    "immunologists": "مناعة",
    "iranologists": "إيرانيات",
    "malariologists": "ملاريا",
    "mammalogists": "ثدييات",
    "marine biologists": "أحياء بحرية",
    "mineralogists": "معادن",
    "molecular biologists": "أحياء جزيئية",
    "mongolists": "منغوليات",
    "musicologists": "موسيقى",
    "naturalists": "طبيعة",
    "neuroscientists": "أعصاب",
    "nuclear physicists": "ذرة",
    "oceanographers": "محيطات",
    "ornithologists": "طيور",
    "paleontologists": "حفريات",
    "parasitologists": "طفيليات",
    "philologists": "لغة",
    "phycologists": "طحالب",
    "physical chemists": "كيمياء فيزيائية",
    "planetary scientists": "كواكب",
    "prehistorians": "عصر ما قبل التاريخ",
    "primatologists": "رئيسيات",
    "pteridologists": "سرخسيات",
    "quantum physicists": "فيزياء الكم",
    "seismologists": "زلازل",
    "sexologists": "جنس",
    "sinologists": "صينيات",
    "sociologists": "اجتماع",
    "taxonomists": "تصنيف",
    "toxicologists": "سموم",
    "turkologists": "تركيات",
    "virologists": "فيروسات",
    "zoologists": "حيوانات",
}
"""Translations for scientific fields."""

ACADEMIC_STUDIES: Dict[str, str] = {
    "islamic studies": "دراسات إسلامية",
    "native american studies": "دراسات الأمريكيين الأصليين",
    "strategic studies": "دراسات إستراتيجية",
    "romance studies": "دراسات رومانسية",
    "black studies": "دراسات إفريقية",
    "literary studies": "دراسات أدبية",
}
"""Translations for academic studies."""

# --- Miscellaneous ---

GENERAL_JOBS: Dict[str, GenderTranslations] = {
    "lawn bowls players": {"mens": "", "womens": ""},
    "community activists": {"mens": "ناشطو مجتمع", "womens": "ناشطات مجتمع"},
    "ecosocialists": {"mens": "إيكولوجيون", "womens": "إيكولوجيات"},
    "ecosocialistes": {"mens": "إيكولوجيون", "womens": "إيكولوجيات"},
    "horse trainers": {"mens": "مدربو خيول", "womens": "مدربات خيول"},
    "bullfighters": {"mens": "مصارعو ثيران", "womens": "مصارعات ثيران"},
    "supremacists": {"mens": "عنصريون", "womens": "عنصريات"},
    "white supremacists": {"mens": "عنصريون بيض", "womens": "عنصريات بيضوات"},
    "ceramists": {"mens": "خزفيون", "womens": "خزفيات"},
    "bodybuilders": {"mens": "لاعبو كمال أجسام", "womens": "لاعبات كمال أجسام"},
    "bowlers": {"mens": "لاعبو بولينج", "womens": "لاعبات بولينج"},
    "dragon boat racers": {
        "mens": "متسابقو قوارب التنين",
        "womens": "متسابقات قوارب التنين",
    },
    "ju-jitsu practitioners": {"mens": "ممارسو جوجوتسو", "womens": "ممارسات جوجوتسو"},
    "kurash practitioners": {"mens": "ممارسو كوراش", "womens": "ممارسات كوراش"},
    "silat practitioners": {"mens": "ممارسو سيلات", "womens": "ممارسات سيلات"},
    "pencak silat practitioners": {
        "mens": "ممارسو بنكات سيلات",
        "womens": "ممارسات بنكات سيلات",
    },
    "sambo practitioners": {"mens": "ممارسو سامبو", "womens": "ممارسات سامبو"},
    "ski orienteers": {"mens": "متسابقو تزلج موجه", "womens": "متسابقات تزلج موجه"},
    "ski-orienteers": {"mens": "متسابقو تزلج موجه", "womens": "متسابقات تزلج موجه"},
    "artistic swimmers": {"mens": "سباحون فنيون", "womens": "سباحات فنيات"},
    "synchronised swimmers": {"mens": "سباحون متزامنون", "womens": "سباحات متزامنات"},
    "powerlifters": {"mens": "ممارسو رياضة القوة", "womens": "ممارسات رياضة القوة"},
    "rifle shooters": {"mens": "رماة بندقية", "womens": "راميات بندقية"},
    "wheelchair curlers": {
        "mens": "لاعبو كيرلنغ على الكراسي المتحركة",
        "womens": "لاعبات كيرلنغ على الكراسي المتحركة",
    },
    "wheelchair fencers": {
        "mens": "مبارزون على الكراسي المتحركة",
        "womens": "مبارزات على الكراسي المتحركة",
    },
    "sepak takraw players": {
        "mens": "لاعبو سيباك تاكرو",
        "womens": "لاعبات سيباك تاكرو",
    },
    "boccia players": {"mens": "لاعبو بوتشيا", "womens": "لاعبات بوتشيا"},
    "wheelchair rugby players": {
        "mens": "لاعبو رغبي على الكراسي المتحركة",
        "womens": "لاعبات رغبي على الكراسي المتحركة",
    },
    "wheelchair tennis players": {
        "mens": "لاعبو كرة مضرب على الكراسي المتحركة",
        "womens": "لاعبات كرة مضرب على الكراسي المتحركة",
    },
}
"""A collection of general job titles and their translations."""

FORMATTABLE_STRINGS: Dict[str, str] = {
    "{} people in health professions": "عاملون {} بمهن صحية",
    "{} eugenicists": "علماء {nato} متخصصون في تحسين النسل",
}
"""String templates for constructing complex job titles."""

NATO_RELATED_JOBS: Dict[str, GenderTranslations] = {
    "eugenicists": {
        "mens": "علماء {nato} متخصصون في تحسين النسل",
        "womens": "عالمات {nato} متخصصات في تحسين النسل",
    },
    "politicians who committed suicide": {
        "mens": "سياسيون {nato} أقدموا على الانتحار",
        "womens": "سياسيات {nato} أقدمن على الانتحار",
    },
    "contemporary artists": {
        "mens": "فنانون {nato} معاصرون",
        "womens": "فنانات {nato} معاصرات",
    },
}
"""Job titles that can be combined with nationalities."""

DISABILITY_RELATED_JOBS: Dict[str, GenderTranslations] = {
    "deaf": {"mens": "صم", "womens": "صم"},
    "blind": {"mens": "مكفوفون", "womens": "مكفوفات"},
    "deafblind": {"mens": "صم ومكفوفون", "womens": "صم ومكفوفات"},
}
"""Translations for job titles related to disabilities."""

EXECUTIVE_ROLES: Dict[str, str] = {
    "railroad": "سكك حديدية",
    "media": "وسائل إعلام",
    "public transportation": "نقل عام",
    "film studio": "استوديوهات أفلام",
    "advertising": "إعلانات",
    "music industry": "صناعة الموسيقى",
    "newspaper": "جرائد",
    "radio": "مذياع",
    "television": "تلفاز",
    "media5": "",
}
"""Translations for executive roles in various industries."""

NATIONALITY_FIRST_JOBS: List[str] = [
    "convicted-of-murder",
    "murdered abroad",
    "contemporary",
    "tour de france stage winners",
    "deafblind",
    "deaf",
    "blind",
    "jews",
    "women's rights activists",
    "human rights activists",
    "imprisoned",
    "imprisoned abroad",
    "conservationists",
    "expatriate",
    "defectors",
    "scholars of islam",
    "scholars-of-islam",
    "amputees",
    "expatriates",
    "scholars of",
    "executed abroad",
    "emigrants",
]
"""A list of job titles where the nationality should precede the title."""

# --- Data Initialization ---


def _initialize_arabic_translations():
    """
    Dynamically constructs the ARABIC_TRANSLATIONS dictionary by merging all
    the individual job-related dictionaries.
    """
    for religion_key, religion_labels in RELIGIOUS_GROUPS.items():
        label_template = f"{religion_key} %s"
        for job_key, job_labels in RELIGIOUS_TITLES.items():
            womens_label = f'{job_labels["womens"]} {religion_labels["womens"]}' if job_labels["womens"] else ""
            ARABIC_TRANSLATIONS[label_template % job_key] = {
                "mens": f'{job_labels["mens"]} {religion_labels["mens"]}',
                "womens": womens_label,
            }

    for painter_style, painter_style_labels in PAINTER_STYLES.items():
        if painter_style != "history":
            ARABIC_TRANSLATIONS[painter_style] = painter_style_labels

        for artist_role, artist_role_labels in ARTIST_ROLES.items():
            ARABIC_TRANSLATIONS[artist_role] = artist_role_labels
            composite_key = f"{painter_style} {artist_role}"
            ARABIC_TRANSLATIONS[composite_key] = {
                "mens": f"{artist_role_labels['mens']} {painter_style_labels['mens']}",
                "womens": f"{artist_role_labels['womens']} {painter_style_labels['womens']}",
            }

    for painter_category, category_label in PAINTER_CATEGORIES.items():
        ARABIC_TRANSLATIONS[f"{painter_category} painters"] = {
            "mens": f"رسامو {category_label}",
            "womens": f"رسامات {category_label}",
        }
        ARABIC_TRANSLATIONS[f"{painter_category} artists"] = {
            "mens": f"فنانو {category_label}",
            "womens": f"فنانات {category_label}",
        }

    for military_key, military_labels in MILITARY_AND_POLITICAL_GROUPS.items():
        if military_key not in ["military", "literary"]:
            ARABIC_TRANSLATIONS[military_key] = military_labels
        for role_key, role_labels in MILITARY_AND_POLITICAL_TITLES.items():
            composite_key = f"{military_key} {role_key}"
            ARABIC_TRANSLATIONS[role_key] = role_labels
            ARABIC_TRANSLATIONS[composite_key] = {
                "mens": f"{role_labels['mens']} {military_labels['mens']}",
                "womens": f"{role_labels['womens']} {military_labels['womens']}",
            }

    for sx, llab in MUSIC_GENRES.items():
        kjab = f"{sx} %s"
        for sim, sim_t in MUSICIAN_ROLES.items():
            lale = kjab % sim
            ARABIC_TRANSLATIONS[lale] = {
                "mens": f"{sim_t['mens']} {llab}",
                "womens": f"{sim_t['womens']} {llab}",
            }

    for fop, fop_a in FILM_AND_THEATER_ROLES.items():
        ARABIC_TRANSLATIONS[f"{fop} actors"] = {"mens": "ممثلو " + fop_a["mens"], "womens": ""}

    for bo, bo_lab in BOXING_WEIGHT_CLASSES.items():
        SPORTS_PLAYER_ROLES[f"{bo} boxers"] = {"mens": f"ملاكمو {bo_lab}", "womens": f"ملاكمات {bo_lab}"}
        SPORTS_PLAYER_ROLES[f"world {bo} boxing champions"] = {"mens": f"أبطال العالم للملاكمة فئة {bo_lab}", "womens": ""}

    for cc, cc_lab in SKATING_DISCIPLINES.items():
        mens = cc_lab["mens"]
        womens = cc_lab["womens"]
        ARABIC_TRANSLATIONS[f"{cc} skaters"] = {
            "mens": f"متزلجو {mens}",
            "womens": f"متزلجات {womens}",
        }
        ARABIC_TRANSLATIONS[f"{cc} skiers"] = {
            "mens": f"متزحلقو {mens}",
            "womens": f"متزحلقات {womens}",
        }

    for cc, cva in TEAM_SPORTS.items():
        if cva:
            ARABIC_TRANSLATIONS[cc] = {
                "mens": f"لاعبو {cva}",
                "womens": f"لاعبات {cva}",
            }

    for pla, pla_la in SPORTS_PLAYER_ROLES.items():
        pla2 = pla.lower()
        if pla_la:
            mens = pla_la["mens"]
            womens = pla_la["womens"]
            ARABIC_TRANSLATIONS[pla2] = pla_la
            ARABIC_TRANSLATIONS[f"olympic {pla2}"] = {
                "mens": f"{mens} أولمبيون",
                "womens": f"{womens} أولمبيات",
            }
            ARABIC_TRANSLATIONS[f"international {pla2}"] = {
                "mens": f"{mens} دوليون",
                "womens": f"دوليات {womens}",
            }

    ARABIC_TRANSLATIONS["national team coaches"] = {
        "mens": "مدربو فرق وطنية",
        "womens": "مدربات فرق وطنية",
    }
    ARABIC_TRANSLATIONS["national team managers"] = {
        "mens": "مدربو فرق وطنية",
        "womens": "مدربات فرق وطنية",
    }
    ARABIC_TRANSLATIONS["sports agents"] = {
        "mens": "وكلاء رياضات",
        "womens": "وكيلات رياضات",
    }
    ARABIC_TRANSLATIONS["expatriate sprtspeople"] = {
        "mens": "رياضيون مغتربون",
        "womens": "رياضيات مغتربات",
    }
    ARABIC_TRANSLATIONS["expatriate sportspeople"] = {
        "mens": "رياضيون مغتربون",
        "womens": "رياضيات مغتربات",
    }

    for ghj, ghj_tab in SPORTS_ROLES.items():
        for men, men_tab in OLYMPIC_AND_SPORTS_TERMS.items():
            kk = f"{men} {ghj}".lower()
            ARABIC_TRANSLATIONS[kk] = {
                "mens": f"{ghj_tab['mens']} {men_tab['mens']}",
                "womens": f"{ghj_tab['womens']} {men_tab['womens']}",
            }

    for sci, lab in SCIENTIFIC_FIELDS.items():
        ARABIC_TRANSLATIONS[sci.lower()] = {"mens": f"علماء {lab}", "womens": f"عالمات {lab}"}

    for sci, lab in ACADEMIC_STUDIES.items():
        ARABIC_TRANSLATIONS[f"{sci.lower()} scholars"] = {"mens": f"علماء {lab}", "womens": f"عالمات {lab}"}

    ARABIC_TRANSLATIONS.update(GENERAL_JOBS)


_initialize_arabic_translations()

__all__ = [
    "ARABIC_TRANSLATIONS",
    "FORMATTABLE_STRINGS",
    "NATO_RELATED_JOBS",
    "DISABILITY_RELATED_JOBS",
    "EXECUTIVE_ROLES",
    "NATIONALITY_FIRST_JOBS",
]
