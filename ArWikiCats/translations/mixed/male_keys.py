"""Mappings for gender specific mixed keys."""

from ...helps import len_print
from ..companies import companies_data
from ..structures import structures_data
from ..utils.json_dir import open_json_file

RELIGIOUS_FEMALE_KEYS: dict[str, str] = {
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
    "bahá'í": "بهائية",
}

FEMALE_SUFFIXES: dict[str, str] = {
    "occupations": "مهن",
    "religious occupations": "مهن دينية",
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


POP3_KEYS: dict[str, dict[str, str]] = {
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

MALE_SUFFIXES: dict[str, str] = {
    "riots": "شغب",
    "food": "طعام",
    "impact": "أثر",
    "broadcasting": "بث لاسلكي",
    "science": "علم",
    "medicine": "طب",
    "outbreaks": "تفشي",
    "exchange": "تبادل",
    "repression": "قمع",
    "orientation": "توجه",
    "fiction": "خيال",
    "union": "اتحاد",
    "violence": "عنف",
}

FEMALE_EXPANSIONS: dict[str, str] = {
    "defunct {base} stations": "محطات {label} سابقة",
    "{base} ttelevision networks": "شبكات تلفزيونية {label}",
    "{base} television stations": "محطات تلفزيونية {label}",
    "{base} superfund sites": "مواقع استجابة بيئية شاملة {label}",
    "{base} stations": "محطات {label}",
    "{base} responses": "استجابات {label}",
    "{base} censorship": "رقابة {label}",
    "{base} communications": "اتصالات {label}",
    "{base} animals": "حيوانات {label}",
    "{base} philosophy": "فلسفة {label}",
    "{base} migration": "هجرة {label}",
    "{base} think tanks": "مؤسسات فكر ورأي {label}",
    "{base} positions": "مراكز {label}",
    "{base} accidents-and-incidents": "حوادث {label}",
    "{base} accidents and incidents": "حوادث {label}",
    "{base} accidents or incidents": "حوادث {label}",
    "{base} accidents": "حوادث {label}",
    "{base} incidents": "حوادث {label}",
    "{base} software": "برمجيات {label}",
    "{base} databases": "قواعد بيانات {label}",
    "{base} controversies": "خلافات {label}",
    "{base} agencies": "وكالات {label}",
    "{base} units and formations": "وحدات وتشكيلات {label}",
    "{base} squadrons‎": "أسراب {label}",
    "{base} ideologies": "أيديولوجيات {label}",
    "{base} occupations": "مهن {label}",
    "{base} organisations": "منظمات {label}",
    "{base} organizations": "منظمات {label}",
    "{base} organization": "منظمات {label}",
    "{base} facilities": "مرافق {label}",
    "{base} bunkers": "مخابئ {label}",
    "{base} research facilities": "مرافق بحثية {label}",
    "{base} training facilities": "مرافق تدريب {label}",
    "{base} industrial facilities": "مرافق صناعية {label}",
    "{base} warfare facilities": "مرافق حربية {label}",
    "{base} logistics": "لوجستية {label}",
    "{base} research": "أبحاث {label}",
    "{base} industry": "صناعة {label}",
    "{base} technology": "تقانة {label}",
    "{base} disasters": "كوارث {label}",
    "{base} writing": "كتابات {label}",
    "{base} issues": "قضايا {label}",
    "{base} rights": "حقوق {label}",
    "{base} communities": "مجتمعات {label}",
    "{base} culture": "ثقافة {label}",
    "{base} underground culture": "ثقافة باطنية {label}",
    "{base} companies of": "شركات {label} في",
    "{base} companies": "شركات {label}",
    "{base} firms of": "شركات {label} في",
    "{base} firms": "شركات {label}",
    "{base} museums": "متاحف {label}",
    "{base} politics": "سياسة {label}",
    "{base} banks": "بنوك {label}",
    "{base} buildings": "مبان {label}",
    "{base} structures": "منشآت {label}",
    "{base} installations": "منشآت {label}",
    "{base} building and structure": "مبان ومنشآت {label}",
    "{base} buildings and structures": "مبان ومنشآت {label}",
}


def _add_religious_entries() -> None:
    """Expand the registry with religion related suffixes."""
    data = {}
    for base, label in RELIGIOUS_FEMALE_KEYS.items():
        lowered = base.lower()
        data[f"{lowered} companies of"] = f"شركات {label} في"
        for suffix, suffix_label in FEMALE_SUFFIXES.items():
            key = f"{lowered} {suffix}"
            data[key] = f"{suffix_label} {label}"
            if "movements" in suffix:
                data[f"new {lowered} {suffix}"] = f"{suffix_label} {label} جديدة"
        data[f"{lowered} founders"] = f"مؤسسو {label}"
        data[f"{lowered} rights"] = f"حقوق {label}"
        data[f"{lowered} underground culture"] = f"ثقافة باطنية {label}"
        data[f"{lowered} culture"] = f"ثقافة {label}"
        data[f"{lowered} think tanks"] = f"مؤسسات فكر ورأي {label}"
        data[f"{lowered} temples"] = f"معابد {label}"
        data[f"{lowered} research"] = f"أبحاث {label}"
        data[f"{lowered} industry"] = f"صناعة {label}"
        data[f"{lowered} technology"] = f"تقانة {label}"
        data[f"{lowered} disasters"] = f"كوارث {label}"
        data[f"{lowered} politics"] = f"سياسة {label}"
        data[f"{lowered} banks"] = f"بنوك {label}"
        data[f"{lowered} buildings"] = f"مبان {label}"
        data[f"{lowered} buildings and structures"] = f"مبان ومنشآت {label}"
        data[f"{lowered} building and structure"] = f"مبان ومنشآت {label}"
    return data


def _add_film_entries() -> None:
    """Update the registry with film-based female categories."""

    Films_keys_male_female = open_json_file("media/Films_keys_male_female.json") or {}

    # Films_keys_male_female["superhero"] = {"male": "خارق", "female": "أبطال خارقين"}
    Films_keys_male_female["sports"] = {"male": "رياضي", "female": "رياضية"}

    data = {}
    for key, labels in Films_keys_male_female.items():
        label = labels.get("female", "")
        if not label:
            continue
        lowered = key.lower()
        data[f"{lowered} agencies"] = f"وكالات {label}"
        data[f"{lowered} occupations"] = f"مهن {label}"
        data[f"{lowered} organisations"] = f"منظمات {label}"
        data[f"{lowered} organizations"] = f"منظمات {label}"
        data[f"{lowered} organization"] = f"منظمات {label}"
        data[f"{lowered} research"] = f"أبحاث {label}"
        data[f"{lowered} industry"] = f"صناعة {label}"
        data[f"{lowered} technology"] = f"تقانة {label}"
        data[f"{lowered} disasters"] = f"كوارث {label}"
        data[f"{lowered} issues"] = f"قضايا {label}"
        data[f"{lowered} culture"] = f"ثقافة {label}"
        data[f"{lowered} companies"] = f"شركات {label}"
    return data


def build_female_keys() -> dict[str, str]:
    """Return the expanded mapping used for female-labelled categories."""

    data = _add_religious_entries()

    for base, labels in POP3_KEYS.items():
        if labels.get("female"):
            lowered = base.lower()
            for template, translation in FEMALE_EXPANSIONS.items():
                data[template.format(base=lowered)] = translation.format(label=labels.get("female"))

    films_data = _add_film_entries()
    data.update(films_data)
    data.update(structures_data)
    data.update(companies_data)

    for suffix, translation in FEMALE_SUFFIXES.items():
        data[f"lgbt {suffix}"] = f"{translation} مثلية"
        data[f"secessionist {suffix}"] = f"{translation} انفصالية"
        data[f"defunct secessionist {suffix}"] = f"{translation} انفصالية سابقة"

    return data


def build_male_keys() -> dict[str, str]:
    """Return the expanded mapping used for male-labelled categories."""

    data = {}

    for base, labels in POP3_KEYS.items():
        lowered = base.lower()
        if labels.get("male"):
            for suffix, suffix_label in MALE_SUFFIXES.items():
                data[f"{lowered} {suffix}"] = f"{suffix_label} {labels.get('male')}"

    return data


New_female_keys: dict[str, str] = build_female_keys()
New_male_keys: dict[str, str] = build_male_keys()


# رجالية بدون ألف ولام التعريف
# tab[Category:syrian descent] = "تصنيف:أصل سوري"

en_is_nat_ar_is_man: dict[str, str] = {
    "descent": "أصل {}",
    "military occupations": "احتلال عسكري {}",
    "integration": "تكامل {}",
    "innovation": "ابتكار {}",
    "design": "تصميم {}",
    "contemporary art": "فن معاصر {}",
    "art": "فن {}",
    "cuisine": "مطبخ {}",
    "calendar": "تقويم {}",
    "non fiction literature": "أدب غير خيالي {}",
    "non-fiction literature": "أدب غير خيالي {}",
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

__all__ = [
    "New_female_keys",
    "New_male_keys",
    "RELIGIOUS_FEMALE_KEYS",
]

len_print.data_len(
    "male_keys.py",
    {
        "New_female_keys": New_female_keys,
        "New_male_keys": New_male_keys,
        "RELIGIOUS_FEMALE_KEYS": RELIGIOUS_FEMALE_KEYS,
    },
)
