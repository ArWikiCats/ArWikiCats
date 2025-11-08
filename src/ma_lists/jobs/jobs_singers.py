#!/usr/bin/python3
"""
# نوع موسيقي
SELECT DISTINCT #?en ?ar
(CONCAT('"' , ?en , '":') as ?aaa8ujua)
(CONCAT('"' , ?ar , '",') as ?aaaa)

WHERE {
  ?item wdt:P31 wd:Q188451.
   ?item rdfs:label ?ar filter (lang(?ar) = "ar") .
   ?item rdfs:label ?en filter (lang(?en) = "en") .
    }
#LIMIT 100

# ---
from .jobs_singers import singers_tab
from .jobs_singers import Men_Womens_Singers, films_type
"""
from ..utils.json_dir import open_json

# ---
Men_Womens_Singers = {}
# ---
Men_Womens_Singers = open_json("jobs/jobs_Men_Womens_Singers.json") or {}
singers_tab = open_json("jobs/singers_tab.json") or {}
# ---
singers_tab = {}
# "electronic dance":"الرقص الإلكترونية",
# "contemporary r&b":"آر إن بي",
# "electronic":"إلكترونيون",
# "salsa music":"موسيقى صلصة","a cappella":"أكابيلا",
# "march":"مارش",
# "performing":"الشعبي",
# ---
# ---
films_type = {
    "film": {"mens": "أفلام", "womens": "أفلام"},
    "silent film": {"mens": "أفلام صامتة", "womens": "أفلام صامتة"},
    "pornographic film": {"mens": "أفلام إباحية", "womens": "أفلام إباحية"},
    "television": {"mens": "تلفزيون", "womens": "تلفزيون"},
    "musical theatre": {"mens": "مسرحيات موسيقية", "womens": "مسرحيات موسيقية"},
    "stage": {"mens": "مسرح", "womens": "مسرح"},
    "radio": {"mens": "راديو", "womens": "راديو"},
    "voice": {"mens": "أداء صوتي", "womens": "أداء صوتي"},
    "video game": {"mens": "ألعاب فيديو", "womens": "ألعاب فيديو"},
    # "voice":       {"mens":"أداء صوتي", "womens":"أداء صوتي"},
}
# ---
# ,"classical violinists":  {"mens":"عازفو كمان كلاسيكيون", "womens":"عازفات كمان كلاسيكيات"}
# ---
singers_main_tab = {
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
# ---
singers3_tab = {
    "abidat rma": "عبيدات الرما",
    "algerian chaabi": "الشعبي",
    "algerian hip hop": "هيب هوب جزائري",
    "andalusian classical music": "طرب أندلسي",
    "bakersfield sound": "موسيقى بيكرسفيلد",
    "bluegrass music": "بلوغراس",
    "canzone napoletana": "أغنية نابولية",
    "chaoui music": "شاوي",
    "country music": "كانتري",
    "electro": "موسيقى كهربائية",
    "electroacoustic music": "إليكتروكوستيك",
    "electronica": "إلكترونيكا",
    "french hip hop": "هيب هوب فرنسي",
    "gharnati music": "طرب غرناطي",
    "glitch": "موسيقى الخلل",
    "gospel music": "غوسبل",
    "gregorian chant": "الغناء الجريجوري",
    "heavy metal": "موسيقى الميتال",
    "hip hop music": "هيب هوب",
    "house music": "هاوس",
    "khaliji": "موسيقى خليجية",
    "musique concrète": "موسيقى ملموسة",
    "música popular brasileira": "موسيقى شعبية برازيلية",
    "new wave of british heavy metal": "الموجة الجديدة لموسيقى الهيفي ميتال البريطانية",
    "parody music": "موسيقي كوميدية",
    "patriotic song": "أغنية وطنية",
    "peruvian waltz": "الفالس البيروفي",
    "progressive house": "موسيقى هاوس تقدمية",
    "romance": "موسيقى رومانسية",
    "sawt": "فن الصوت",
    "swing music": "سوينغ",
    "technical death metal": "ديث ميتال الفني",
    "trap music": "تراب",
}
# ---
for sx, sx_l in singers_tab.items():
    singers_main_tab[sx] = sx_l
# ---
# # "educators" : {"mens":"مربون", "womens":"مربيات"},
singers_after = {
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
# ---
for sx, llab in singers_main_tab.items():
    kjab = f"{sx} %s"
    for sim, sim_t in singers_after.items():
        lale = kjab % sim
        Men_Womens_Singers[lale] = {}
        vfvfv = f"{sim_t['mens']} {llab}"
        Men_Womens_Singers[lale]["mens"] = vfvfv
        # print('lale : "%s"' % lale)
        # print('vfvfv : "%s"' % vfvfv)
        Men_Womens_Singers[lale]["womens"] = f"{sim_t['womens']} {llab}"
        # MenWomensJobsPP[lale] = Men_Womens_Singers[lale]
    # ---
    # Men_Womens_Singers[ f"{sx} singers" ] = { "mens": "مغنو %s"  % llab ,"womens": f"مغنيات {llab}" }
    # Men_Womens_Singers[ f"{sx} writers" ] = { "mens": "كتاب %s"  % llab ,"womens": f"كاتبات {llab}" }
    # Men_Womens_Singers[ f"{sx} authors" ] = { "mens": "مؤلفو %s"  % llab ,"womens": f"مؤلفات {llab}" }
    # Men_Womens_Singers[ f"{sx} journalists" ] = { "mens": "صحفيو %s"  % llab ,"womens": f"صحفيات {llab}" }
    # Men_Womens_Singers[ f"{sx} bandleaders" ] = { "mens": "قادة فرق %s"  % llab ,"womens": f"قائدات فرق {llab}" }
    # Men_Womens_Singers[ f"{sx} cheerleaders" ] = { "mens": "قادة تشجيع %s"  % llab ,"womens": f"قائدات تشجيع {llab}" }
# ---
# non_fiction_tab = {
# "garden":  {"mens": " , "womens": "},
# "health and wellness":  {"mens": " , "womens": "},
# "self-help":  {"mens": " , "womens": "},

non_fiction_tab = {
    "non-fiction": {"mens": "غير روائيون", "womens": "غير روائيات"},
    "non-fiction environmental": {
        "mens": "بيئة غير روائيون",
        "womens": "بيئة غير روائيات",
    },
    "detective": {"mens": "بوليسيون", "womens": "بوليسيات"},
    "military": {"mens": "عسكريون", "womens": "عسكريات"},
    "nautical": {"mens": "بحريون", "womens": "بحريات"},
    "maritime": {"mens": "بحريون", "womens": "بحريات"},
}
# ---
non_fiction_keys = {
    "environmental": "بيئة",
    "economics": "إقتصاد",
    "hymn": "ترانيم",
    "architecture": "عمارة",
    "magazine": "مجلات",
    "medical": "طب",
    "organized crime": "جريمة منظمة",
    "crime": "جريمة",
    "legal": "قانون",
    "business": "أعمال تجارية",
    "nature": "طبيعة",
    "political": "سياسة",
    "art": "فن",
    "food": "طعام",
    "travel": "سفر",
    "spiritual": "روحانية",
    "arts": "فنون",
    "social sciences": "علوم اجتماعية",
    "music": "موسيقى",
    "science": "علم",
    "technology": "تقنية",
    "comedy": "كوميدي",
}
# ---
for en, ar in non_fiction_keys.items():
    non_fiction_tab[en] = {"mens": ar, "womens": ar}
# ---
for sx, labs in non_fiction_tab.items():
    Men = labs["mens"]
    Women = labs["womens"]
    # ---
    Men_Womens_Singers[f"{sx} historian"] = {
        "mens": f"مؤرخو {Men}",
        "womens": f"مؤرخات {Women}",
    }
    Men_Womens_Singers[f"{sx} authors"] = {
        "mens": f"مؤلفو {Men}",
        "womens": f"مؤلفات {Women}",
    }
    Men_Womens_Singers[f"{sx} bloggers"] = {
        "mens": f"مدونو {Men}",
        "womens": f"مدونات {Women}",
    }
    Men_Womens_Singers[f"{sx} writers"] = {
        "mens": f"كتاب {Men}",
        "womens": f"كاتبات {Women}",
    }
    Men_Womens_Singers["non-fiction %s writers" % sx] = {
        "mens": "كتاب %s غير روائيون" % Men,
        "womens": "كاتبات %s غير روائيات" % Women,
    }
    Men_Womens_Singers[f"{sx} journalists"] = {
        "mens": f"صحفيو {Men}",
        "womens": f"صحفيات {Women}",
    }
# ---
for fop, fop_a in films_type.items():
    Men_Womens_Singers[f"{fop} actors"] = {"mens": "ممثلو " + fop_a["mens"], "womens": ""}

FILMS_TYPE = films_type
MEN_WOMENS_SINGERS = Men_Womens_Singers
