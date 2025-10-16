#!/usr/bin/python3
r"""
\{\s*"mens"\s*:\s*""\s*,\s*"womens"\s*:\s*""\s*\}\s*,
{"mens":"", "womens":""},


\{\s*['"]mens['"]\s*:\s*['"]([\w\s]+|)['"]\s*,\s*['"]womens['"]\s*:\s*['"]([\w\s]+|)['"]\s*\}
{"mens":"$1", "womens":"$2"}



\{\s*['"]([\w\s]+|)['"]\s*:\s*['"]([\w\s]+|)['"]\s*,\s*['"]([\w\s]+|)['"]\s*:\s*['"]([\w\s]+|)['"]\s*\}
{"$1":"$2", "$3":"$4"}

\{\s*['"]([\w\s\d]+|)['"]\s*:\s*['"]([\w\s\d]+|)['"]\s*,\s*['"]([\w\s\d]+|)['"]\s*:\s*['"]([\w\s\d]+|)['"]\s*,\s*['"]([\w\s\d]+|)['"]\s*:\s*['"]([\w\s\d]+|)['"]\s*\}
{"$1":"$2", "$3":"$4", "$5":"$6"}

\{\s*['"]([\w\s\d]+|)['"]\s*:\s*['"]([\w\s\d]+|)['"]\s*,\s*['"]([\w\s\d]+|)['"]\s*:\s*['"]([\w\s\d]+|)['"]\s*,\s*['"]([\w\s\d]+|)['"]\s*:\s*['"]([\w\s\d]+|)['"]\s*,\s*['"]([\w\s\d]+|)['"]\s*:\s*['"]([\w\s\d]+|)['"]\s*\}
{"$1":"$2", "$3":"$4", "$5":"$6", "$7":"$8"}


jsub -mem 1g sh/a1.sh
jsub -mem 1g sh/a2.sh
jsub -mem 1g sh/a3.sh
jsub -mem 1g sh/a4.sh
jsub -mem 1g sh/a5.sh

"""

from pathlib import Path
import json

Dir2 = Path(__file__).parent

"""

الأسطر المخفية تبدأ بـ
#o

"""
# ---
from ..json_dir import open_json_file
Jobs_3333 = {}
Jobs_2 = {}
# ---
Jobs_22 = open_json_file("Jobs_22")
# ---
jobs_3 = open_json_file("jobs_3")
# ---
# "biochemists"    : {"mens":"أخصائيو كيمياء حيوية", "womens":""},
# "coastal engineering" : {"mens":"هندسة الشواطئ", "womens":""},
# "confidence tricksters" : {"mens":"أكبر المحتالين", "womens":""},
# "coptologists" : {"mens":"مختصون بالدراسات القبطية", "womens":""},
# "daimyo" : {"mens":"دايميو", "womens":""},
# "film preservation" : {"mens":"حفظ الأفلام", "womens":""},
# "fraudsters" : {"mens":"غشاشون", "womens":""},
# "geisha" : {"mens":"غايشا", "womens":""},
# "hacking (computer security)" : { "mens": "اختراق (حماية الحاسوب)" ,"womens": "" },
# "heavy metal guitarists" : {"mens":"عازفو هيفي ميتال", "womens":"عازفات هيفي ميتال"},
# "illustrators" : {"mens":"رسامون توضيحيون", "womens":""},
# "literary editors" : {"mens":"محرر أدبي", "womens":""},
# "ninja" : {"mens":"نينجا", "womens":""},
# "pharmacologists" : {"mens":"اختصاصيو علم الأدوية", "womens":""},
# "prophets of islam" : {"mens":"أنبياء ورسل بحسب المعتقد الإسلامي", "womens":""},
# "prophets" : {"mens":"أنبياء ورسل", "womens":""},
# "psycholinguists" : {"mens":"لسانيات ذهنية", "womens":""},
# "scientific illustrators" : {"mens":"رسامون في المجال العلمي", "womens":""},
# "topologists" : {"mens":"عاملون في الطوبولوجيا", "womens":""},
# ---
# "agriculturalists"  : {"mens":"مزارعون", "womens":"مزارعات"},
# "astrophysicists"    : {"mens":"فيزيائيون فلكيون", "womens":"فيزيائيات فلكيات"},
# "book publishers (people)": {"mens":"ناشرو كتب", "womens":""},
# "farmers" : {"mens":"مزارعون", "womens":"مزارعات"},
# "fencers" : {"mens":"مبارزون", "womens":"مبارزات"},
# "justices of the peace" : {"mens":"", "womens":""},
# "mass media owners": {"mens":"ملاك وسائل إعلام", "womens":"مالكات وسائل إعلام"},
# "music historians" : {"mens":"مؤرخو موسيقى", "womens":"مؤرخات موسيقى"},
# "music people" : {"mens":"أعلام موسيقى", "womens":""},
# "newspaper people" : {"mens":"شخصيات صحفية", "womens":"شخصيات صحفية"},
# "paleontologists":  {"mens":"إحاثيون", "womens":"إحاثيات"},
# "people in the sex industry" : {"mens":"", "womens":""},
# "polynesian sports coaches": {"mens":"", "womens":""},
# "priests" : {"mens":"قساوسة", "womens":""},
# "printmakers" : {"mens":"نقاشون", "womens":"نقاشات"},
# "prostitutes" : {"mens":"", "womens":"عاهرات"},
# "punk rock groups" : {"mens":"", "womens":""},
# "railway mechanical engineers" : {"mens":"", "womens":""},
# "stained glass artists and manufacturers" : {"mens":"", "womens":""},
# "telecommunications engineers" : {"mens":"", "womens":""},
# "television news anchors" : {"mens":"", "womens":""},
# علماء $1" ,"womens": "عالمات $1"
# علماء (.*)\" \,\u\"womens\"\:  \u\"\"
# ---
Main_scientists = {
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
# ---
scholars_table = {
    "islamic studies": "دراسات إسلامية",
    "native american studies": "دراسات الأمريكيين الأصليين",
    "strategic studies": "دراسات إستراتيجية",
    "romance studies": "دراسات رومانسية",
    "black studies": "دراسات إفريقية",
    "literary studies": "دراسات أدبية",
}
# ---
for sci in Main_scientists:
    lab = Main_scientists[sci]
    Jobs_2[sci.lower()] = {"mens": f"علماء {lab}", "womens": f"عالمات {lab}"}
# ---
for sci in scholars_table:
    lab = scholars_table[sci]
    Jobs_2[f"{sci.lower()} scholars"] = {"mens": f"علماء {lab}", "womens": f"عالمات {lab}"}
# ---
for joj in jobs_3.keys():
    Jobs_3333[joj.lower()] = jobs_3[joj]
    if joj.lower() not in Jobs_2 and jobs_3[joj]["mens"]:
        Jobs_2[joj.lower()] = jobs_3[joj]
# ---
nano = 0
for jowj in Jobs_22.keys():
    if jowj.lower() in Jobs_3333:
        # printe.output('jobs2: "%s" : { "mens": "%s" ,"womens": "%s" },' %  (jowj , Jobs_22[jowj]["mens"],Jobs_22[jowj]["womens"]))
        nano += 1
    # else:
    if jowj.lower() not in Jobs_2:
        if Jobs_22[jowj]["mens"] or Jobs_22[jowj]["womens"]:
            Jobs_2[jowj.lower()] = Jobs_22[jowj]
# ---
job2_opo = {
    "air force generals": "جنرالات القوات الجوية",
    "air force officers": "ضباط القوات الجوية",
    "architecture critics": "نقاد عمارة",
    "businesspeople in advertising": "رجال وسيدات أعمال إعلانيون",
    "businesspeople in shipping": "شخصيات أعمال في نقل بحري",
    "child actors": "ممثلون أطفال",
    "child psychiatrists": "أخصائيو طب نفس الأطفال",
    "child singers": "مغنون أطفال",
    "christian clergy": "رجال دين مسيحيون",
    "competitors in athletics": "لاعبو قوى",
    "computer occupations": "مهن الحاسوب",
    "contributors to the encyclopédie": "مشاركون في وضع موسوعة الإنسيكلوبيدي",
    "critics of religions": "نقاد الأديان",
    "daimyo": "دايميو",
    "eugenicists": "علماء متخصصون في تحسين النسل",
    "founders of religions": "مؤسسو أديان",
    "french navy officers": "ضباط بحرية فرنسيون",
    "geisha": "غايشا",
    "hacking (computer security)": "اختراق (حماية الحاسوب)",
    "health occupations": "مهن صحية",
    "historians of christianity": "مؤرخو مسيحية",
    "historians of mathematics": "مؤرخو رياضيات",
    "historians of philosophy": "مؤرخو فلسفة",
    "historians of religion": "مؤرخو دين",
    "historians of science": "مؤرخو علم",
    "historians of technology": "مؤرخو تقنية",
    "human computers": "أجهزة حواسيب بشرية",
    "japanese voice actors": "ممثلو أداء صوتي يابانيون",
    "literary editors": "محرر أدبي",
    "midwives": "قابلات",
    "military doctors": "أطباء عسكريون",
    "muslim scholars of islam": "مسلمون باحثون عن الإسلام",
    "ninja": "نينجا",
    "nuns": "راهبات",
    "physiologists": "علماء وظائف الأعضاء",
    "political commentators": "نقاد سياسيون",
    "political consultants": "استشاريون سياسيون",
    "political scientists": "علماء سياسة",
    "political theorists": "منظرون سياسيون",
    "prophets": "أنبياء ورسل",
    "prostitutes": "داعرات",
    "religious writers": "كتاب دينيون",
    "service occupations": "مهن خدمية",
    "sports scientists": "علماء رياضيون",
    "women writers": "كاتبات",
}
# ---
"""
lal = 'jobs2: "%s" : { "mens": "%s" ,"womens": "%s" },'
# ---
same = 0
notsame = 0
notin = 0
for c in job2_opo:
    if c.lower() in Jobs_2 :
        if job2_opo[c] != Jobs_2[c.lower()]["mens"] :
            #printe.output('"%s" : { "job2_opo": "%s" ,"Jobs_2": "%s" },' % (c , job2_opo[c] , Jobs_2[c.lower()]["mens"])   )
            #printe.output('"%s" : "%s",' % (c , job2_opo[c])   )
            notsame += 1
        else:
            same += 1
    else:
        #printe.output('"%s" : "%s",' % (c , job2_opo[c]) )
        notin += 1
        #printe.output(lal % (c , job2_opo[c] , "")   )
printe.output("jobs2: same:%d" % same)
printe.output("jobs2: notsame:%d" % notsame)
"""
# ---
del Jobs_22
del Main_scientists
del scholars_table
del jobs_3
del job2_opo
