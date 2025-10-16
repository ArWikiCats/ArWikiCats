#!/usr/bin/python3
"""
python3 core8/pwb.py make/m test Category:People executed by the International Military Tribunal in Nuremberg

"""


# from .helps import printe

import sys

#
# ---
pop_final6 = {
    # ---
    "gulf war": "حرب الخليج الثانية",
    # ---
    "robert award": "جائزة روبرت",
    "emmy award": "جائزة إيمي",
    "grammy award": "جائزة غرامي",
    "golden globe award": "جائزة غولدن غلوب",
    "independent spirit award": "جائزة الروح المستقلة",
    "national board of review award": "جائزة المجلس الوطني للمراجعة",
    "toronto international film festival award": "جائزة مهرجان تورونتو السينمائي الدولي",
    # ---
    "hollywood film awards": "جوائز هوليوود للأفلام",
    "hong kong film awards": "جوائز مهرجان هونج كونج السينمائي",
    "empire awards": "جوائز إمباير",
    "ptc punjabi film awards": "جوائز المهرجان البنجابي السينمائي",
    "european film awards": "جوائز الفيلم الأوروبي",
    "environmental media awards": "جوائز الإعلام البيئي",
    "jussi awards": "جائزة جوسي",
    "bodil awards": "جائزة بوديل",
    "teen choice awards": "جائزة اختيار المراهقين",
    "claude jutra award": "جائزة كلود جوترا",
    "robert-bresson award": "جائزة روبرت بريسون",
    "robert award": "جائزة روبرت",
    "golden reel award": "جائزة الذهبية بكرة",
    "first steps award": "جائزة الخطوات الأولى",
    "herbert strate award": "جائزة إستراتيجيات هربرت",
    "nastro d'argento": "ناسترو دي أرجنتو",
    "crystal simorgh": "كريستال سيمرغ",
    "mussolini cup": "كأس موسوليني",
    "georg büchner prize winners": "فائزون بجائزة جورج بوشنر",
    "georg büchner prize": "جائزة جورج بوشنر",
    "grand prix": "سباق الجائزة الكبرى",
    "special jury prize": "جائزة لجنة التحكيم الخاصة",
    "fénix award of iberoamerican cinema": "جائزة فينيكس من الأيبيرية السينما الأميركية",
    "prix romy schneider": "جائزة رومي شنايدر",
    "human rights award (sarajevo film festival)": "جائزة حقوق الانسان (مهرجان سراييفو السينمائي)",
    "prix jean gabin": "جائزة جان غبن",
    "risto jarva prize": "جائزة جارفا ريستو",
    "for best canadian first feature film": "لأفضل وأول فيلم كندي مميز",
    "for best canadian film": "لأفضل فيلم كندي",
    "tp de oro": "تي بي دي أورو",
    "bayard d'or": "بايارد الذهبية",
    "golden bear": "الدب الذهبي",
    # ---
    "for best male playback singer": "لأفضل مغني أفلام",
    "for best female playback singer": "لأفضل مغنية أفلام",
    "for best male singer": "لأفضل مغني",
    "for best female  singer": "لأفضل مغنية",
    # ---
    "for best first feature": "لأفضل أول فيلم",
    "for best historical album": "لأفضل ألبوم تاريخي",
    "for best rock album": "لأفضل ألبوم روك",
    "for best album": "لأفضل ألبوم",
    "for best film": "لأفضل فيلم",
    "for best original song": "لأفضل أغنية أصلية",
    "for best album for children": "لأفضل ألبوم للأطفال",
    "for best spoken word album": "لأفضل ألبوم محكي",
    "for best alternative music album": "لأفضل ألبوم موسيقى بديلة",
    "for best screenplay": "لأفضل سيناريو",
    "for best motion picture – drama": "لأفضل فيلم - دراما",
    "for best motion picture – musical or comedy": "لأفضل فيلم - موسيقي أو كوميدي",
    "for best english-language foreign film": "لأفضل فيلم أجنبي ناطق بالإنجليزية",
    "for best foreign language film": "لأفضل فيلم بلغة أجنبية",
    "for best animated feature film": "لأفضل فيلم رسوم متحركة",
    "for best documentary film": "لأفضل فيلم وثائقي",
    "for best director": "لأفضل مخرج",
    "for best television series – drama": "لأفضل مسلسل - دراما",
    "for best television series – musical or comedy": "لأفضل مسلسل - موسيقي أو كوميدي",
    "for best miniseries or television film": "لأفضل مسلسل قصير أو فلم تلفزيوني",
    "for rhythm and blues": "لريذم أند بلوز",
    "for best actor": "لأفضل ممثل",
    "for best actor – motion picture drama": "لأفضل ممثل - فيلم دراما",
    "for best actor – television series drama": "لأفضل ممثل - مسلسل تلفزيوني دراما",
    "for best actor – miniseries or television film": "لأفضل ممثل - مسلسل قصير أو فيلم تلفزيوني",
    "for best actor – motion picture musical or comedy": "لأفضل ممثل في فيلم - موسيقي أو كوميدي",
    "for best actor – television series musical or comedy": "لأفضل ممثل في مسلسل موسيقي أو كوميدي",
    "for best supporting actor – motion picture": "لأفضل ممثل مساعد - فيلم",
    "for best supporting actor – series, miniseries or television film": "لأفضل ممثل مساعد - مسلسل، أو مسلسل قصير أو فيلم تلفزيوني",
    "for best actress – motion picture drama": "لأفضل ممثلة - فيلم دراما",
    "for best actress – motion picture musical or comedy": "لأفضل ممثلة - فيلم موسيقي أو كوميدي",
    "for best actress – television series musical or comedy": "لأفضل ممثلة - مسلسل تلفزيوني موسيقي أو كوميدي",
    "for best actress – television series drama": "لأفضل ممثلة - مسلسل دراما",
    "for best actress – miniseries or television film": "لأفضل ممثلة - مسلسل قصير أو فيلم تلفزيوني",
    "golden globe for an actress in a television series": "لأفضل ممثلة في مسلسل تلفزيوني",
    "for best supporting actress – motion picture": "لأفضل ممثلة مساعدة - فيلم",
    "for best supporting actress – series, miniseries or television film": "لأفضل ممثلة مساعدة - مسلسل، أو مسلسل قصير أو فيلم تلفزيوني",
    "for best original score": "لأفضل موسيقى تصويرية",
    "for album of the year": "لألبوم السنة",
    "for new star of the year – actor": "للنجم الصاعد",
    "for new star of the year – actress": "للنجمة الصاعدة",
    # ---
}
# ---
male_types = {
    "science": "علم",
    "literature": "أدب",
    # ---
}
# ---
for ma in male_types:
    pop_final6[f"fictional {ma}"] = f"{male_types[ma]} خيالي"
    pop_final6[f"{ma} themes"] = f"مواضيع {male_types[ma]}"
# ---
Awards = {
    # ---
    "grammy": "غرامي",
    "golden globe": "غولدن غلوب",
    # ---
    "filmfare": "فيلم فير",
    # ---
    "robert": "روبرت",
    "emmy": "إيمي",
    "grammy": "غرامي",
    "golden globe": "غولدن غلوب",
    "independent spirit": "الروح المستقلة",
    "national board of review": "المجلس الوطني للمراجعة",
    "toronto international film festival": "مهرجان تورونتو السينمائي الدولي",
    # ---
    "hollywood film": "هوليوود للأفلام",
    "hong kong film": "مهرجان هونج كونج السينمائي",
    "empire": "إمباير",
    "ptc punjabi film": "المهرجان البنجابي السينمائي",
    "european film": "الفيلم الأوروبي",
    "environmental media": "الإعلام البيئي",
    "jussi": "جوسي",
    "bodil": "بوديل",
    "teen choice": "اختيار المراهقين",
    "claude jutra": "كلود جوترا",
    "robert-bresson": "روبرت بريسون",
    "robert": "روبرت",
    "golden reel": "الذهبية بكرة",
    "first steps": "الخطوات الأولى",
    "herbert strate": "إستراتيجيات هربرت",
}
# ---
for award in Awards:
    pop_final6[f"{award.lower()} award"] = f"جائزة {Awards[award]}"
    pop_final6[f"{award.lower()} awards"] = f"جوائز {Awards[award]}"
# ---
After_type_female = {
    # ---
    # "discipline" : "تخصص",
    # "literature" : "أدب",
    # ---
    "universities and colleges": "جامعات وكليات",
    "schools": "مدارس",
    "awards": "جوائز",
    "buildings": "مبان",
    "centers": "مراكز",
    "museums": "متاحف",
    "organisations": "منظمات",
    "organizations": "منظمات",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "groups": "مجموعات",
    "gangs": "عصابات",
    "associations": "جمعيات",
    "services": "خدمات",
    "consulting": "استشارات",
    "utilities": "مرافق",
    "parks": "متنزهات",
    "academies": "أكاديميات",
    "research": "أبحاث",
    "societies": "جمعيات",
    "learned societies": "جمعيات علمية",
    "professional societies": "جمعيات مهنية",
    "learned and professional societies": "جمعيات علمية ومهنية",
    "documents": "وثائق",
    "publishing": "منشورات",
    # ---
    "companies": "شركات",
    "disciplines": "تخصصات",
    "terrorist incidents": "حوادث إرهابية",
    # ---
    "parties": "أحزاب",
    "political parties": "أحزاب سياسية",
    "politics": "سياسة",
    # ---
    "crises": "أزمات",
}
# ---
# "cruise ships" : "سفن سياحية",
# ---
Frist_type_female = {
    # ---
    # ---
    "paleolibertarianism": "ليبرتارية أصلية",
    "libertarian": "ليبرتارية",
    # ---
    "liberal": "ليبرالية",
    "classical conservative": "ليبرالية كلاسيكية",
    "liberal conservative": "ليبرالية محافظة",
    # ---
    "structural": "هيكلية",
    "agricultural": "زراعية",
    "astronomical": "فلكية",
    "chemical": "كيميائية",
    "commercial": "تجارية",
    "economical": "اقتصادية",
    "educational": "تعليمية",
    "environmental": "بيئية",
    "experimental": "تجريبية",
    "historical": "تاريخية",
    "industrial": "صناعية",
    "internal": "داخلية",
    "international": "دولية",
    "legal": "قانونية",
    "magical": "سحرية",
    "medical": "طبية",
    "musical": "موسيقية",
    "nautical": "بحرية",
    "residential": "سكنية",
    # ---
    "environmental": "بيئية",
    "eurosceptic": "شكوكية أوروبية",
    "anti-revisionist": "مناهضة للتحريفية",
    "anti-capitalist": "مناهضة للرأسمالية",
    "socialist": "اشتراكية",
    "socialism": "اشتراكية",
    "ecosocialist": "اشتراكية بيئية",
    "biological": "بيولوجية",
    "cruise": "سياحية",
    "defunct": "سابقة",
    "chemical": "كيميائية",
    "military nuclear": "نووية عسكرية",
    "nuclear": "نووية",
    "military and war": "عسكرية وحربية",
    # ---
    # "library" : "مكتبات",
    "military": "عسكرية",
    "training": "تدريبية",
    "consultative": "إستشارية",
    "legislative": "تشريعية",
    "constitutional": "دستورية",
    "political": "سياسية",
    "warfare": "حربية",
    "diplomatic": "دبلوماسية",
    # ---
    "publicly traded": "تداول عام",
    "computer": "حوسبة",
    "multi-national": "متعددة الجنسيات",
    "multinational": "متعددة الجنسيات",
    "power": "طاقة",
    "office": "إدارية",
    # ---
    "international": "دولية",
    "sports": "رياضية",
    "music": "موسيقى",
    "private": "خاصة",
    "independent": "مستقلة",
    "drama": "درامية",
    "law": "قانون",
    "commercial": "تجارية",
    # "trade" : "تجارية",
    "bank": "بنوك",
    "academic": "أكاديمية",
    "academic and learned": "أكاديمية وعلمية",
    # ---
    "horticultural": "بستنة",
    "islamic": "إسلامية",
    "fictional": "خيالية",
    "criminal": "إجرامية",
    # ---
    "history": "تاريخ",
    "cycling": "ركوب الدراجات",
    "architecture": "عمارة",
    "transportation": "النقل",
    # ---
    "science": "علمية",
    "sports": "رياضية",
    "ethnic": "عرقية",
    "professional": "تخصصية",
    "financial": "مالية",
    "public": "عمومية",
    "archaeological": "أثرية",
    "historical": "تاريخية",
    # ---
    # ---
    # "provincial":"",
    "interventionist": "تدخلية",
    "non-interventionist": "غير تدخلية",
    "banned": "محظورة",
    "anti-islam": "معادية للإسلام",
    "zionist": "صهيونية",
    "anti-zionist": "معادية للصهيونية",
    "monarchist": "ملكية",
    "classical": "كلاسيكية",
    "defunct": "سابقة",
    "far-left": "يسارية متطرفة",
    "far-right": "يمينية متطرفة",
    "social": "اجتماعية",
    "conservative": "محافظة",
    "republican": "جمهورية",
    "radical": "راديكالية",
    "nationalist": "قومية",
    "fascist": "فاشية",
    "secularist": "علمانية",
    "freemasonry": "ماسونية",
    "communist": "شيوعية",
    "centrist": "وسطية",
    "muslim": "إسلامية",
    "right-wing": "يمينية",
    "left-wing": "يسارية",
    # ---
}
# ---
for first in Frist_type_female:
    # ---
    pop_final6[f"{first} parties"] = f"أحزاب {Frist_type_female[first]}"
    # ---
    for secound in After_type_female:
        keyy = f"{first.lower()} {secound.lower()}"
        opo = f"{After_type_female[secound]} {Frist_type_female[first]}"
        pop_final6[keyy] = opo
        # printe.output('pop_final6[%s] = "%s" ' % (keyy , opo))
# ---
Ta_s = {
    "arts": "فنية",
    "arts": "فنية",
}
# ---
for ta in Ta_s:
    pop_final6[f"{ta} occupations"] = f"مهن {Ta_s[ta]}"
# ---
lenthe = {"pop_final6": sys.getsizeof(pop_final6)}
# ---
from .helps import len_print

len_print.lenth_pri("newkey.py", lenthe)
# ---
# ---
