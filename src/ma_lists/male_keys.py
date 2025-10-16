#!/usr/bin/python3

"""
from .male_keys import New_female_keys, New_male_keys, religious_female_keys, female_keys, All_pop3_keys, pop_key3_male, pop_key3_female, pop_key_4, New_Company
"""

import sys
from .. import printe
from .films_mslslat import Films_keys_male_female

# ---
New_female_keys = {}
New_male_keys = {}
# ---
religious_female_keys = {
    "masonic": "ماسونية",
    "islamic": "إسلامية",
    "neopagan religious": "وثنية جديدة",
    "political party": "أحزاب سياسية",
    "jain": "جاينية",
    "new thought": "فكر جديد",
    "jewish": "يهودية",
    "protestant": "بروتستانتية",
    "sikh": "سيخية",
    "scientology": "سينتولوجيا",
    "spiritualist": "روحانية",
    "taoist": "طاوية",
    "buddhist": "بوذية",
    "unitarian universalist": "توحيدية عالمية",
    "hindu": "هندوسية",
    "christian": "مسيحية",
    "religious": "دينية",
    "zoroastrian": "زرادشتية",
    # "creationist":"",
    "bahá'í": "بهائية",
}
# ---
female_keys = {
    "academies": "أكاديميات",
    "agencies": "وكالات",
    "associations": "جمعيات",
    "awards": "جوائز",
    "bridge": "جسور",
    "buildings": "مبان",
    "bunkers": "مخابئ",
    "centers": "مراكز",
    "charities": "جمعيات خيرية",
    "children's charities": "جمعيات خيرية للأطفال",
    "clubs": "نوادي",
    "communities": "مجتمعات",
    "companies": "شركات",
    "consulting": "استشارات",
    "corporations": "مؤسسات تجارية",
    "culture": "ثقافة",
    "denominations": "طوائف",
    "disciplines": "تخصصات",
    "educational establishments": "مؤسسات تعليمية",
    "educational institutions": "هيئات تعليمية",
    "educational": "تعليمية",
    "facilities": "مرافق",
    "federations": "اتحادات",
    "festivals": "مهرجانات",
    "genital integrity": "سلامة الأعضاء التناسلية",
    "groups": "مجموعات",
    "ideologies": "أيديولوجيات",
    "installations": "منشآت",
    "institutions": "مؤسسات",
    "issues": "قضايا",
    "learned and professional societies": "جمعيات علمية ومهنية",
    "learned societies": "جمعيات علمية",
    "men's organizations": "منظمات رجالية",
    "movements and organisations": "حركات ومنظمات",
    "movements and organizations": "حركات ومنظمات",
    "movements": "حركات",
    "museums": "متاحف",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "occupations": "مهن",
    "orders": "أخويات",
    "organisations": "منظمات",
    "organization": "منظمات",
    "organizations": "منظمات",
    "parks": "متنزهات",
    "pornography": "إباحية",
    "professional societies": "جمعيات مهنية",
    "religions": "ديانات",
    "religious orders": "أخويات دينية",
    "research": "أبحاث",
    "schools": "مدارس",
    "service organizations": "منظمات خدمية",
    "services": "خدمات",
    "societies": "جمعيات",
    "specialisms": "تخصصات",
    "student organizations": "منظمات طلابية",
    "utilities": "مرافق",
    "women's organizations": "منظمات نسائية",
    "youth organizations": "منظمات شبابية",
}
# ---
for key, lab in religious_female_keys.items():
    # ---
    keys2 = key.lower()
    # ---
    # so = f"{keys2} %s"
    # ---
    New_female_keys[f"{keys2} companies of"] = f"شركات {lab} في"
    # ---
    for dd in female_keys:
        ky2 = f"{keys2} {dd}"
        lb3 = f"{female_keys[dd]} {lab}"
        New_female_keys[ky2] = lb3
        # ---
        if dd.find("movements") > -1:
            New_female_keys[f"new {keys2} {dd}"] = lb3 + " جديدة"
        # ---
        # if lab == "دينية": print(f"[{ky2}]= '{lb3}'")
    # ---
    New_female_keys[f"{keys2} founders"] = f"مؤسسو {lab}"
    New_female_keys[f"{keys2} rights"] = f"حقوق {lab}"
    New_female_keys[f"{keys2} underground culture"] = f"ثقافة باطنية {lab}"
    New_female_keys[f"{keys2} culture"] = f"ثقافة {lab}"

    New_female_keys[f"{keys2} think tanks"] = f"مؤسسات فكر ورأي {lab}"

    New_female_keys[f"{keys2} temples"] = f"معابد {lab}"
    New_female_keys[f"{keys2} research"] = f"أبحاث {lab}"
    New_female_keys[f"{keys2} industry"] = f"صناعة {lab}"
    New_female_keys[f"{keys2} technology"] = f"تقنيات {lab}"

    New_female_keys[f"{keys2} disasters"] = f"كوارث {lab}"
    New_female_keys[f"{keys2} politics"] = f"سياسة {lab}"
    New_female_keys[f"{keys2} banks"] = f"بنوك {lab}"
    New_female_keys[f"{keys2} buildings"] = f"مبان {lab}"
    New_female_keys[f"{keys2} buildings and structures"] = f"مبان ومنشآت {lab}"
    New_female_keys[f"{keys2} building and structure"] = f"مبان ومنشآت {lab}"
# ---
All_pop3_keys = {
    "healthcare": {"male": "", "female": "رعاية صحية"},
    "school": {"male": "", "female": "مدارس"},
    "theatres": {"male": "", "female": "مسارح"},
    "towers": {"male": "", "female": "أبراج"},
    "windmills": {"male": "", "female": "طواحين الهواء"},
    "veterans": {"male": "", "female": "قدامى المحاربين"},
    "transport": {"male": "", "female": "النقل"},
    "hotel": {"male": "", "female": "فنادق"},
    "fire": {"male": "", "female": "الإطفاء"},
    "major league baseball": {"male": "", "female": "دوري كرة القاعدة الرئيسي"},
    "veterans and descendants": {"male": "", "female": "أحفاد وقدامى المحاربين"},
    "transportation": {"male": "", "female": "نقل"},
    "shopping malls": {"male": "", "female": "مراكز تسوق"},
    "law enforcement": {"male": "", "female": "تطبيق القانون"},
    "dams": {"male": "", "female": "سدود"},
    "educational": {"male": "تعليمي", "female": "تعليمية"},
    "masonic": {"male": "ماسوني", "female": "ماسونية"},
    "office": {"male": "إداري", "female": "إدارية"},
    "religious": {"male": "ديني", "female": "دينية"},
    "residential": {"male": "سكني", "female": "سكنية"},
    "agricultural": {"male": "زراعي", "female": "زراعية"},
    "air defence": {"male": "دفاع جوي", "female": "دفاع جوية"},
    "anarchism": {"male": "لاسلطوي", "female": "لاسلطوية"},
    "anarchist": {"male": "لاسلطوي", "female": "لاسلطوية"},
    "anti-revisionist": {"male": "مناهض للتحريف", "female": "مناهضة للتحريفية"},
    "arts": {"male": "فني", "female": "فنية"},
    "astronomical": {"male": "فلكي", "female": "فلكية"},
    "chemical": {"male": "كيميائي", "female": "كيميائية"},
    "christian": {"male": "مسيحي", "female": "مسيحية"},
    "commercial": {"male": "تجاري", "female": "تجارية"},
    "constitutional": {"male": "دستوري", "female": "دستورية"},
    "consultative": {"male": "إستشاري", "female": "إستشارية"},
    "cultural": {"male": "ثقافي", "female": "ثقافية"},
    "defense": {"male": "دفاعي", "female": "دفاعية"},
    "economic": {"male": "اقتصادي", "female": "اقتصادية"},
    "environmental": {"male": "بيئي", "female": "بيئية"},
    "fraternal": {"male": "أخوي", "female": "أخوية"},
    "government": {"male": "حكومي", "female": "حكومية"},
    "industrial": {"male": "صناعي", "female": "صناعية"},
    "legal": {"male": "قانوني", "female": "قانونية"},
    "legislative": {"male": "تشريعي", "female": "تشريعية"},
    "logistics": {"male": "لوجستي", "female": "لوجستية"},
    "maritime": {"male": "بحري", "female": "بحرية"},
    "medical and health": {"male": "طبي وصحي", "female": "طبية وصحية"},
    "medical": {"male": "طبي", "female": "طبية"},
    "military": {"male": "عسكري", "female": "عسكرية"},
    "naval": {"male": "عسكرية بحري", "female": "عسكرية بحرية"},
    "paramilitary": {"male": "شبه عسكري", "female": "شبه عسكرية"},
    "political": {"male": "سياسي", "female": "سياسية"},
    "realist": {"male": "واقعي", "female": "واقعية"},
    "research": {"male": "بحثي", "female": "بحثية"},
    "strategy": {"male": "استراتيجي", "female": "استراتيجية"},
    "student": {"male": "طلابي", "female": "طلابية"},
    "training": {"male": "تدريبي", "female": "تدريبية"},
    "warfare": {"male": "حربي", "female": "حربية"},
    "youth": {"male": "شبابي", "female": "شبابية"},
    "hospital": {"male": "", "female": "مستشفيات"},
    "airports": {"male": "", "female": "مطارات"},
    "casinos": {"male": "", "female": "كازينوهات"},
    "university and college": {"male": "", "female": "جامعات وكليات"},
    "colleges and universities": {"male": "", "female": "كليات وجامعات"},
    "university": {"male": "", "female": "جامعات"},
    "universities": {"male": "", "female": "جامعات"},
    "college": {"male": "", "female": "كليات"},
    "colleges": {"male": "", "female": "كليات"},
}
# ---
pop_key3_male = {}
pop_key3_female = {}
# ---
for ui, uu in All_pop3_keys.items():
    if uu["male"]:
        pop_key3_male[ui] = uu["male"]
    if uu["female"]:
        pop_key3_female[ui] = uu["female"]
# ---
# "military logistics":"لوجستية عسكرية",
# ---#
for keyt in pop_key3_male:
    key2c = keyt.lower()
    labe = pop_key3_male[keyt]
    sod = f"{key2c} %s"
    New_male_keys[sod % "riots"] = f"شغب {labe}"
    New_male_keys[sod % "food"] = f"طعام {labe}"
    New_male_keys[sod % "impact"] = f"أثر {labe}"
    New_male_keys[sod % "broadcasting"] = f"بث لاسلكي {labe}"
    New_male_keys[sod % "science"] = f"علم {labe}"
    New_male_keys[sod % "medicine"] = f"طب {labe}"
    New_male_keys[sod % "outbreaks"] = f"تفشي {labe}"
    New_male_keys[sod % "exchange"] = f"تبادل {labe}"
    New_male_keys[sod % "repression"] = f"قمع {labe}"
    New_male_keys[sod % "orientation"] = f"توجه {labe}"
    New_male_keys[sod % "fiction"] = f"خيال {labe}"
    New_male_keys[sod % "union"] = f"اتحاد {labe}"
    New_male_keys[sod % "violence"] = f"عنف {labe}"
# ---
for key in pop_key3_female:
    keys2 = key.lower()
    lab = pop_key3_female[key]
    # so = f"{keys2} %s"
    # ---
    New_female_keys[f"defunct {keys2} stations"] = f"محطات {lab} سابقة"
    New_female_keys[f"{keys2} ttelevision networks"] = f"شبكات تلفزيونية {lab}"
    New_female_keys[f"{keys2} television stations"] = f"محطات تلفزيونية {lab}"
    New_female_keys[f"{keys2} superfund sites"] = f"مواقع استجابة بيئية شاملة {lab}"
    New_female_keys[f"{keys2} stations"] = f"محطات {lab}"
    New_female_keys[f"{keys2} responses"] = f"استجابات {lab}"
    New_female_keys[f"{keys2} censorship"] = f"رقابة {lab}"
    New_female_keys[f"{keys2} communications"] = f"اتصالات {lab}"
    New_female_keys[f"{keys2} animals"] = f"حيوانات {lab}"
    # ---
    New_female_keys[f"{keys2} philosophy"] = f"فلسفة {lab}"
    New_female_keys[f"{keys2} migration"] = f"هجرة {lab}"
    # ---
    New_female_keys[f"{keys2} think tanks"] = f"مؤسسات فكر ورأي {lab}"
    New_female_keys[f"{keys2} positions"] = f"مراكز {lab}"
    # ---
    New_female_keys[f"{keys2} accidents-and-incidents"] = f"حوادث {lab}"
    New_female_keys[f"{keys2} accidents and incidents"] = f"حوادث {lab}"
    New_female_keys[f"{keys2} accidents or incidents"] = f"حوادث {lab}"
    New_female_keys[f"{keys2} accidents"] = f"حوادث {lab}"
    New_female_keys[f"{keys2} incidents"] = f"حوادث {lab}"
    New_female_keys[f"{keys2} software"] = f"برمجيات {lab}"
    New_female_keys[f"{keys2} databases"] = f"قواعد بيانات {lab}"
    # ---
    New_female_keys[f"{keys2} controversies"] = f"خلافات {lab}"
    New_female_keys[f"{keys2} agencies"] = f"وكالات {lab}"
    New_female_keys[f"{keys2} units and formations"] = f"وحدات وتشكيلات {lab}"
    New_female_keys[f"{keys2} squadrons‎"] = f"أسراب {lab}"
    New_female_keys[f"{keys2} ideologies"] = f"أيديولوجيات {lab}"
    New_female_keys[f"{keys2} occupations"] = f"مهن {lab}"
    New_female_keys[f"{keys2} organisations"] = f"منظمات {lab}"
    New_female_keys[f"{keys2} organizations"] = f"منظمات {lab}"
    New_female_keys[f"{keys2} organization"] = f"منظمات {lab}"
    New_female_keys[f"{keys2} facilities"] = f"مرافق {lab}"
    New_female_keys[f"{keys2} bunkers"] = f"مخابئ {lab}"
    # ---
    New_female_keys[f"{keys2} research facilities"] = f"مرافق بحثية {lab}"
    New_female_keys[f"{keys2} training facilities"] = f"مرافق تدريب {lab}"
    New_female_keys[f"{keys2} industrial facilities"] = f"مرافق صناعية {lab}"
    New_female_keys[f"{keys2} warfare facilities"] = f"مرافق حربية {lab}"
    # ---
    New_female_keys[f"{keys2} logistics"] = f"لوجستية {lab}"
    New_female_keys[f"{keys2} research"] = f"أبحاث {lab}"
    New_female_keys[f"{keys2} industry"] = f"صناعة {lab}"
    New_female_keys[f"{keys2} technology"] = f"تقنيات {lab}"

    New_female_keys[f"{keys2} disasters"] = f"كوارث {lab}"
    New_female_keys[f"{keys2} writing"] = f"كتابات {lab}"
    New_female_keys[f"{keys2} issues"] = f"قضايا {lab}"

    New_female_keys[f"{keys2} rights"] = f"حقوق {lab}"
    New_female_keys[f"{keys2} communities"] = f"مجتمعات {lab}"
    New_female_keys[f"{keys2} culture"] = f"ثقافة {lab}"
    New_female_keys[f"{keys2} underground culture"] = f"ثقافة باطنية {lab}"

    # New_male_keys[f"{keys2} economics"] = "اقتصاد {}".format(lab)
    # ---
    New_female_keys[f"{keys2} companies of"] = f"شركات {lab} في"
    New_female_keys[f"{keys2} companies"] = f"شركات {lab}"
    New_female_keys[f"{keys2} firms of"] = f"شركات {lab} في"
    New_female_keys[f"{keys2} firms"] = f"شركات {lab}"
    New_female_keys[f"{keys2} museums"] = f"متاحف {lab}"
    # ---
    New_female_keys[f"{keys2} politics"] = f"سياسة {lab}"
    New_female_keys[f"{keys2} banks"] = f"بنوك {lab}"
    New_female_keys[f"{keys2} buildings"] = f"مبان {lab}"
    New_female_keys[f"{keys2} structures"] = f"منشآت {lab}"
    New_female_keys[f"{keys2} installations"] = f"منشآت {lab}"
    New_female_keys[f"{keys2} building and structure"] = f"مبان ومنشآت {lab}"
    New_female_keys[f"{keys2} buildings and structures"] = f"مبان ومنشآت {lab}"
# ---
for ttt in Films_keys_male_female:
    # ---
    lab = Films_keys_male_female[ttt].get("female", "")
    # ---
    if lab:
        ttt2 = ttt.lower()
        # so = f"{ttt2} %s"
        # ---
        New_female_keys[f"{ttt2} agencies"] = f"وكالات {lab}"
        New_female_keys[f"{ttt2} occupations"] = f"مهن {lab}"
        New_female_keys[f"{ttt2} organisations"] = f"منظمات {lab}"
        New_female_keys[f"{ttt2} organizations"] = f"منظمات {lab}"
        New_female_keys[f"{ttt2} organization"] = f"منظمات {lab}"
        New_female_keys[f"{ttt2} research"] = f"أبحاث {lab}"
        New_female_keys[f"{ttt2} industry"] = f"صناعة {lab}"
        New_female_keys[f"{ttt2} technology"] = f"تقنيات {lab}"
        New_female_keys[f"{ttt2} disasters"] = f"كوارث {lab}"
        New_female_keys[f"{ttt2} issues"] = f"قضايا {lab}"
        New_female_keys[f"{ttt2} culture"] = f"ثقافة {lab}"
        New_female_keys[f"{ttt2} companies"] = f"شركات {lab}"
# ---
pop_key_4 = {
    # "lighthouses":"منارات",
    "non-renewable resource": "موارد غير متجددة",
    "oil shale": "صخر زيتي",
    "mobile phone": "هاتف محمول",
    "bauxite": "البوكسيت",
    "biofuel": "وقود حيوي",
    "chemical": "كيميائية",
    "coal gas": "غاز الفحم",
    "coal": "الفحم",
    "coals": "الفحم",
    "condiment": "توابل",
    "copper": "النحاس",
    "electric power": "طاقة كهربائية",
    "electric": "قدرة",
    "electrical engineering": "هندسة كهربائية",
    "energy": "طاقة",
    "fossil fuel": "وقود أحفوري",
    "fossil fuels": "وقود أحفوري",
    "gas": "غاز",
    "geothermal": "حرارية جوفية",
    "gold": "الذهب",
    "hydroelectric": "كهرمائية",
    "mining": "التعدين",
    "natural gas": "غاز طبيعي",
    "nuclear": "نووية",
    "oil and gas": "النفط والغاز",
    "oil": "نفطية",
    "petroleum": "بترولية",
    "photovoltaic": "كهروضوئية",
    "non-renewable energy": "طاقة غير متجددة",
    "renewable energy": "طاقة متجددة",
    "renewable resource": "موارد متجددة",
    "sedimentary rocks": "صخور رسوبية",
    "solar": "شمسية",
    "solid fuel": "وقود صلب",
    "solid fuels": "وقود صلب",
}
# ---
for key in pop_key_4:
    key2 = key.lower()
    lab = pop_key_4[key]
    # so = f"{key2} %s"
    New_female_keys[f"{key2} companies of"] = f"شركات {lab} في"
    New_female_keys[f"{key2} companies"] = f"شركات {lab}"
    New_female_keys[f"{key2} firms"] = f"شركات {lab}"
    New_female_keys[f"{key2} firms of"] = f"شركات {lab} في"

    New_female_keys[f"{key2} agencies"] = f"وكالات {lab}"
    New_female_keys[f"{key2} disciplines"] = f"تخصصات {lab}"
    New_female_keys[f"{key2} museums"] = f"متاحف {lab}"
    New_female_keys[f"governmental {key2} organizations"] = f"منظمات {lab} حكومية"
    New_female_keys[f"{key2} organizations"] = f"منظمات {lab}"
    New_female_keys[f"{key2} organization"] = f"منظمات {lab}"
    New_female_keys[f"{key2} facilities"] = f"مرافق {lab}"
    New_female_keys[f"{key2} bunkers"] = f"مخابئ {lab}"
    New_female_keys[f"{key2} industry"] = f"صناعة {lab}"
    New_female_keys[f"{key2} industry organisations"] = f"منظمات صناعة {lab}"
    New_female_keys[f"{key2} industry organizations"] = f"منظمات صناعة {lab}"

    New_female_keys[f"{key2} geology"] = f"جيولوجيا {lab}"
    New_female_keys[f"{key2} mining"] = f"تعدين {lab}"
    New_female_keys[f"{key2} technology"] = f"تقنيات {lab}"
    New_female_keys[f"{key2} disasters"] = f"كوارث {lab}"
    New_female_keys[f"{key2} issues"] = f"قضايا {lab}"
    # New_male_keys[f"{key2} economics"] = "اقتصاد {}".format(lab)

    New_female_keys[f"{key2} electricity"] = f"كهرباء {lab}"
    New_female_keys[f"{key2} fields"] = f"حقول {lab}"
    New_female_keys[f"{key2} infrastructure"] = f"بنية تحتية {lab}"
    New_female_keys[f"{key2} refineries"] = f"مصافي {lab}"
    New_female_keys[f"{key2} pipelines"] = f"خطوط أنابيب {lab}"

    New_female_keys[f"{key2} stations"] = f"محطات {lab}"
    New_female_keys[f"defunct {key2} stations"] = f"محطات {lab} سابقة"
    New_female_keys[f"disused {key2} stations"] = f"محطات {lab} مهجورة"
    New_female_keys["disused " + (f"{key2} stations")] = f"محطات {lab} مهجورة"
    # ---
    if lab.find("طاقة") == -1:
        New_female_keys[f"{key2} energy"] = f"طاقة {lab}"
        New_female_keys[f"{key2} power plants"] = f"محطات طاقة {lab}"
        New_female_keys[f"{key2} power stations"] = f"محطات طاقة {lab}"
        New_female_keys["proposed " + f"{key2} power stations"] = f"محطات طاقة {lab} مقترحة"
        New_female_keys["former " + f"{key2} power stations"] = f"محطات طاقة {lab} سابقة"
        New_female_keys["demolished " + f"{key2} power stations"] = f"محطات طاقة {lab} مدمرة"
    else:
        New_female_keys[f"{key2} power stations"] = f"محطات {lab}"
        New_female_keys[f"{key2} power plants"] = f"محطات {lab}"
        New_female_keys["proposed " + f"{key2} power stations"] = f"محطات {lab} مقترحة"
        New_female_keys["former " + f"{key2} power stations"] = f"محطات {lab} سابقة"
        New_female_keys["demolished " + f"{key2} power stations"] = f"محطات {lab} مدمرة"

    New_female_keys[f"{key2} politics"] = f"سياسة {lab}"
    New_female_keys[f"{key2} buildings"] = f"مبان {lab}"
    New_female_keys[f"{key2} structures"] = f"منشآت {lab}"
    New_female_keys[f"{key2} installations"] = f"منشآت {lab}"
    New_female_keys[f"{key2} logistics installations"] = f"منشآت لوجستية {lab}"
    New_female_keys[f"{key2} buildings and structures"] = f"مبان ومنشآت {lab}"
    New_female_keys[f"{key2} building and structure"] = f"مبان ومنشآت {lab}"
# ---
# New_male_keys[f"{key2} buildings on the national register of historic places in"] = "مباني {} في السجل الوطني للأماكن التاريخية في".format(lab)
# New_male_keys[f"{key2} buildings on the national register of historic places"] = "مباني {} في السجل الوطني للأماكن التاريخية".format(lab)
# ---
New_Company = {
    "privately held": "خاصة",
    "airliner": "طائرات",
    "condiment": "توابل",
    "academic": "أكاديمية",
    "magazine": "مجلات",
    "natural gas": "غاز طبيعي",
    "comics": "قصص مصورة",
    "marvel comics": "مارفال كومكس",
    "mass media": "وسائل إعلام",
    "television": "تلفاز",
    "manga": "مانغا",
    "coal": "فحم",
    "coal gas": "غاز الفحم",
    "oil shale": "صخر زيتي",
    "oil": "زيت الوقود",
    "gas": "غاز",
    "nuclear": "نووية",
    "renewable energy": "طاقة متجددة",
    "agriculture": "زراعة",
    "airlines": "طيران",
    "aluminium": "ألومنيوم",
    "architecture": "هندسة معمارية",
    "automotive": "سيارات",
    "banks": "بنوك",
    "holding": "قابضة",
    "biotechnology": "تقانة حيوية",
    "building materials": "مواد بناء",
    "cargo airlines": "شحن جوي",
    "aviation": "طيران",
    "airline": "خطوط جوية",
    "cement": "أسمنت",
    "chemical": "كيميائية",
    "clothing": "ملابس",
    "computer": "حوسبة",
    "construction": "بناء",
    "construction and civil engineering": "بناء وهندسة مدنية",
    "cosmetics": "مستحضرات التجميل",
    "defence": "دفاعية",
    "design": "تصميم",
    "distribution": "توزيع",
    "education": "تعليم",
    "electronics": "إلكترونيات",
    "energy": "طاقة",
    "photovoltaic": "خلايا كهروضوئية",
    "hydroelectric": "كهرمائية",
    "electric power": "طاقة كهربائية",
    "engineering": "هندسية",
    "electrical engineering": "هندسة كهربائية",
    # "entertainment":"ترفيهية",
    "entertainment": "ترفيه",
    "eyewear": "نظارات",
    "financial": "مالية",
    "financial services": "خدمات مالية",
    "business services": "خدمات أعمال تجارية",
    "food": "أطعمة",
    "food and drink": "أطعمة ومشروبات",
    "gambling": "مقامرة",
    "glassmaking": "الزجاج",
    "health care": "رعاية صحية",
    "health clubs": "نوادي صحية",
    "horticultural": "بستنة",
    "household and personal product": "المنتجات المنزلية والشخصية",
    "insurance": "تأمين",
    "internet": "إنترنت",
    "internet service providers": "تزويد خدمة الإنترنت",
    "investment": "استثمارية",
    "jewellery": "مجوهرات",
    # "law":"مؤسسات قانون",
    "management consulting": "استشارات إدارية",
    "manufacturing": "تصنيع",
    "map": "خرائط",
    "marketing": "تسويق",
    "media": "إعلامية",
    "metal": "معادن",
    "mining": "تعدين",
    "vehicle manufacturing": "تصنيع مركبات",
    # "motor vehicle manufacturers":"تصنيع السيارات",
    "motor vehicle manufacturers": "مصانع سيارات",
    "music": "الموسيقى",
    "paint and coatings": "رسم وطلاء",
    "pharmaceutical": "أدوية",
    "printing": "طباعة",
    "property": "ممتلكات",
    "public utilities": "مرافق عمومية",
    "cruise ships": "سفن سياحية",
    "music publishing": "نشر موسيقى",
    "publishing": "نشر",
    "pulp and paper": "اللب والورق",
    "submarine": "غواصات",
    "rail": "سكك حديدية",
    "railway": "سكك حديدية",
    "car rental": "تأجير السيارات",
    "real estate": "عقارية",
    "real estate services": "خدمات عقارية",
    "retail": "تجارة التجزئة",
    "security": "أمن",
    "fraternal service": "خدمات أخوية",
    "service": "خدمات",
    "shipbuilding": "سفن",
    "shipyards": "حوض بناء سفن",
    "software": "برمجيات",
    "sugar": "السكر",
    "technology": "تكنولوجيا",
    "information technology": "تكنولوجيا المعلومات",
    "tobacco": "التبغ",
    "transport": "نقل",
    "travel": "سفر",
    "travel insurance": "تأمين السفر",
    "travel and holiday": "السفر والعطلات",
    "urban regeneration": "تطوير حضري",
    "utilities": "مرافق عمومية",
    "veterinary": "بيطرة",
    "video game": "ألعاب فيديو",
    "waste management": "إدارة المخلفات",
    "hotel chains": "سلاسل فندقية",
    "hospitality": "ضيافة",
    "hotel and leisure": "فنادق وترفيه",
    "hotels": "فنادق",
    "road transport": "نقل بري",
    "water transport": "نقل مائي",
    "shipping": "نقل بحري",
    "wine": "نبيذ",
    "alcohol": "كحول",
    "drink": "مشروبات",
    "water": "مياه",
    "postal": "بريد",
    "storage": "تخزين",
    "trucking": "نقل بالشاحنات",
    "logistics": "لوجستية",
    "military logistics": "لوجستية عسكرية",
    "wholesalers": "بيع بالجملة",
}
# ---
for kes, lab in New_Company.items():  # Media company founders
    keys2 = kes.lower()
    # so = f"{keys2} %s"
    New_female_keys[f"{keys2} company"] = f"شركات {lab}"
    # ---
    New_female_keys[f"{keys2} offices"] = f"مكاتب {lab}"

    New_female_keys[f"{keys2} companies of"] = f"شركات {lab} في"
    New_female_keys[f"defunct {keys2} companies"] = f"شركات {lab} سابقة"
    New_female_keys[f"defunct-{keys2}-companies"] = f"شركات {lab} سابقة"
    New_female_keys[f"defunct {keys2}"] = f"{lab} سابقة"
    New_female_keys[f"defunct {keys2} of"] = f"{lab} سابقة في"
    New_female_keys[f"{keys2} firms of"] = f"شركات {lab} في"
    New_female_keys[f"{keys2} services"] = f"خدمات {lab}"
    New_female_keys[f"{keys2} firms"] = f"شركات {lab}"
    New_female_keys[f"{keys2} franchises"] = f"امتيازات {lab}"
    # ---
    New_female_keys[f"{keys2} accidents-and-incidents"] = f"حوادث {lab}"
    New_female_keys[f"{keys2} accidents and incidents"] = f"حوادث {lab}"
    New_female_keys[f"{keys2} accidents or incidents"] = f"حوادث {lab}"
    New_female_keys[f"{keys2} accidents"] = f"حوادث {lab}"
    New_female_keys[f"{keys2} incidents"] = f"حوادث {lab}"
    New_female_keys[f"{keys2} software"] = f"برمجيات {lab}"
    New_female_keys[f"{keys2} databases"] = f"قواعد بيانات {lab}"
    # ---
    New_female_keys[f"{keys2} agencies"] = f"وكالات {lab}"
    New_female_keys[f"{keys2} disciplines"] = f"تخصصات {lab}"
    New_female_keys[f"{keys2} museums"] = f"متاحف {lab}"
    New_female_keys[f"{keys2} organizations"] = f"منظمات {lab}"
    New_female_keys[f"{keys2} organization"] = f"منظمات {lab}"
    New_female_keys[f"{keys2} facilities"] = f"مرافق {lab}"
    New_female_keys[f"{keys2} bunkers"] = f"مخابئ {lab}"
    New_female_keys[f"{keys2} industry"] = f"صناعة {lab}"
    New_female_keys[f"{keys2} industry organisations"] = f"منظمات صناعة {lab}"
    New_female_keys[f"{keys2} industry organizations"] = f"منظمات صناعة {lab}"
    # New_female_keys[f"{key2} of"] = "{} في".format(lab)
# ---
for d_d in female_keys:
    # New_female_keys[d_d] = female_keys[d_d]
    New_female_keys[f"lgbt {d_d}"] = f"{female_keys[d_d]} مثلية"
    New_female_keys[f"secessionist {d_d}"] = f"{female_keys[d_d]} انفصالية"
    New_female_keys[f"defunct secessionist {d_d}"] = f"{female_keys[d_d]} انفصالية سابقة"
# ---
Lenth1 = {
    "New_female_keys": sys.getsizeof(New_female_keys),
    "All_Nat New_male_keys": sys.getsizeof(New_male_keys),
}
# ---
from ..helps import len_print

len_print.lenth_pri("male_keys.py", Lenth1)
# ---
if __name__ == "__main__":
    keyse = list(pop_key3_female.keys())
    # ---#
    for i in pop_key3_male:
        if i not in keyse:
            keyse.append(i)
    # ---#
    for k in keyse:
        mal = pop_key3_male.get(k, "")
        fem = pop_key3_female.get(k, "")
        sd = ' "' + k + '" :\t{"male":"' + mal + '"\t,\tu"female":"' + fem + '" }, '
        print(sd)
    printe.output(f' len pop_key3_female "{len(pop_key3_female)}" ')
    printe.output(f' len pop_key3_male "{len(pop_key3_male)}" ')
    printe.output(f' len keyse "{len(keyse)}" ')
# ---#
# ---
del Films_keys_male_female
