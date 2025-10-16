"""
from .Cities import N_cit_ies_s, tabe_lab_yy2, N_cit_ies_s_lower

zz

    SELECT DISTINCT #?item ?humanLabel
    #?ar
    #?page_en ?page_ar
    (concat('   "' , ?page_en , '":"' , ?page_ar  , '",')  as ?itemscds)
    WHERE {
    ?human wdt:P31/wdt:P279* wd:Q515.
    ?human wdt:P910 ?item .
    ?item wdt:P301 ?human.
    ?article schema:about ?item ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?page_en .
    ?article2 schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> ; schema:name ?page_ar .
    #FILTER NOT EXISTS {?article schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> . }.
    SERVICE wikibase:label {
        bd:serviceParam wikibase:language "ar,en".
    }
    ?item rdfs:label ?ar .  FILTER((LANG(?ar)) = "ar")

    }
    #LIMIT 100


    SELECT DISTINCT #?item ?humanLabel
    #?ar
    #?page_en ?page_ar
    (concat('   "' , ?page_en , '":"' , ?page_ar  , '",')  as ?itemscds)
    WHERE {
    #?human wdt:P31/wdt:P279* wd:Q515.#
    ?human wdt:P31/wdt:P279* wd:Q486972.
    ?human wdt:P910 ?item .
    ?item wdt:P301 ?human.
    ?article schema:about ?item ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?page_en .
    ?article2 schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> ; schema:name ?page_ar .
    #FILTER NOT EXISTS {?article schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> . }.
    SERVICE wikibase:label {
        bd:serviceParam wikibase:language "ar,en".
    }
    ?item rdfs:label ?ar .  FILTER((LANG(?ar)) = "ar")

    }
    #LIMIT 100


    SELECT #?item ?itemLabel ?en ?value
    (concat('  ,"', ?en , '"')  as ?ss)
    (concat(':')  as ?ss2)
    (concat('  "', ?value , '"')  as ?ss3)

    WHERE {
        ?item wdt:P31 wd:Q4167836.
        ?item wdt:P301 ?city .
        ?city wdt:P31 wd:Q1637706.
        { ?city rdfs:label ?value filter (lang(?value) = "ar") .
        } UNION { ?item rdfs:label ?value filter (lang(?value) = "ar") . }
        { ?item rdfs:label ?en filter (lang(?en) = "en") .
        }  UNION { ?city rdfs:label ?en filter (lang(?en) = "en") . }
        SERVICE wikibase:label {
            bd:serviceParam wikibase:language "en,ar".
        }

    }
    #  LIMIT 10000

    #python3 core8/pwb.py c18/scat t:test test:Black_studies
    #python3 core8/pwb.py c18/scat t:test test:by_position
    #python3 core8/pwb.py c18/scat t:test test:People_educated
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Ankara
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Berlin
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:University_of_the_Arts
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Baku
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Bangkok
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Athens
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Cali
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Bucharest
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Busan
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Chelyabinsk
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Kano
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Moscow
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Tokyo
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Tunis
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:treaties_of
    #python3 core8/pwb.py c18/scat noprint t:test -new2018 test:Grand_Duchy_of_Moscow

"""

# "bhopal":"بهوبال",
# "birmingham":"برمنغهام",
# "birmingham, west midlands":"برمنغهام",
# "ghaziabad, uttar pradesh":"غازي آباد",
# "hyderabad district, pakistan":"حيدر آباد (السند)",
# "mayors of almaty":"ألماتي",
# "mayors of lubumbashi":"لوبومباشي",
# "philadelphia":"فيلادلفيا (بنسلفانيا)",
# "philadelphia, pennsylvania":"فيلادلفيا",
# "recife":"ريسيفه",
# "san antonio":"سان أنطونيو (تكساس)",
# ---
# ---
import sys

from ..json_dir import open_json_file
from ...helps import len_print
import time

start = time.time()
# ---
# ---
N_cit_ies_s = open_json_file("all_cities") or {}
# ---
Cities_tab2 = open_json_file("Cities_tab2") or {}
# ---
# merge N_cit_ies_s and Cities_tab2
N_cit_ies_s |= Cities_tab2
# ---
del Cities_tab2
# ---
N_cit_ies_s_x = {
    "Tubas" : "طوباس",
    "Tulkarm" : "طولكرم",
    "Nablus" : "نابلس",
    "Zion" : "صهيون",
    "Ya'bad" : "يعبد",
    "Tarqumiyah" : "ترقوميا",
    "Shechem" : "شكيم",
    "Salfit" : "سلفيت",
    "Sa'ir" : "سعير",
    "Rawabi" : "روابي",
    "Ramallah" : "رام الله",
    "Rafah" : "رفح",
    "Qalqilya" : "قلقيلية",
    "Qabatiya" : "قباطية",
    "Melchizedek" : "ملكي صادق",
    "Knesset" : "كنيست",
    "Jerusalem" : "القدس",
    "Jericho" : "أريحا",
    "Jenin" : "جنين",
    "Antioch" : "أنطاكية",
    "Jebusites" : "يبوسيون",
    "Zoharei Chama Synagogue" : "كنيس زوهري شامة",
    "Zion Square" : "ميدان صهيون",
    "Zeev Sternhell" : "زئيف ستيرنهيل",
    "Zaki Nusseibeh" : "زكي نسيبة",
    "Yossi Harel" : "يوسي هاريل",
    "Yossi Cohen" : "يوسي كوهين",
    "Yosef Ba-Gad" : "يوسف با-غاد",
    "Yehuda Liebes" : "يهودا ليبيس",
    "Yehuda Burla" : "يهودا بورلا",
    "Yatta, Hebron" : "يطا",
    "Yahya Hammuda" : "يحيى حمودة",
    "Yad Kennedy" : "ياد كينيدي",
    "World Central Kitchen aid convoy" : "المطبخ المركزي العالمي",
    "West Jerusalem" : "القدس الغربية",
    "Walls of Jerusalem" : "أسوار القدس",
    "Walid Muhammed Sadi" : "وليد محمد السعدي",
    "Uzzi Ornan" : "عوزي أورنان",
    "Umm al-Nasr Mosque" : "مسجد أم النصر",
    "Tsvi Misinai" : "تسفي ميسيناي",
    "Tower of David" : "برج القلعة",
    "Tombs of the Kings" : "قبور السلاطين",
    "The Jerusalem Post" : "جيروزاليم بوست",
    "Temple Mount Faithful" : "أمناء جبل الهيكل",
    "Tell Balata" : "تل بلاطة",
    "Tel Aviv–Jerusalem railway" : "سكة حديد القدس - غانوت",
    "Talitha Kumi School" : "مدرسة طاليثا قومي",
    "Suha Arafat" : "سهى عرفات",
    "Strings of Freedom" : "سلاسل الحرية",
    "Stern House" : "بيت ستيرن",
    "Star Street" : "شارع النجمة",
    "Sirhan Sirhan" : "سرحان سرحان",
    "Shuhada al-Aqsa Hospital" : "مستشفى شهداء الأقصى الحكومي",
    "Shabab Rafah" : "شباب رفح",
    "Schwester Selma" : "سلمى مائير",
    "Sara Hestrin-Lerner" : "سارة هيسترين ليرنر",
    "Samer Tariq Issawi" : "سامر العيساوي",
    "Salwa Abu Libdeh" : "سلوى أبو لبدة",
    "Safra Square" : "ميدان صفرا",
    "Tell el-Ful" : "تل الفول",
    "Royal Palace, Tell el-Ful" : "قصر تل الفول",
    "Roni Alsheikh" : "روني الشيخ",
    "Ribhi Kamal" : "ربحي كمال",
    "Rhetorical school of Gaza" : "المدرسة البلاغية بغزة",
    "Ramat Rachel" : "رمات راحيل",
    "Rafah Elementary Co-Ed B School" : "مدرسة رفح الابتدائية كو-إد بي",
    "Rafah Border Crossing" : "معبر رفح",
    "Palestinian National Theatre" : "مسرح الحكواتي",
    "Palestinian National Library" : "المكتبة الوطنية الفلسطينية",
    "Palestinian Child Arts Center" : "مركز فنون الطفل الفلسطيني",
    "Orient House" : "بيت الشرق",
    "Olive wood carving" : "نحت خشب الزيتون",
    "Off the Wall Comedy Empire" : "ملهى العروض الكوميدية",
    "Nefesh B'Nefesh" : "نيفيش بنيفيش",
    "Nabulsi soap" : "صابون نابلسي",
    "Nabulsi cheese" : "جبن نابلسي",
    "Nablus Sanjak" : "سنجق نابلس",
    "Mujir al-Din" : "مجير الدين الحنبلي",
    "Mubarak Awad" : "مبارك عواد",
    "Mount of Olives" : "جبل الزيتون",
    "Mount Zion" : "جبل صهيون",
    "Mount Scopus" : "جبل المشارف",
    "Moses Montefiore" : "موشيه مونتيفيوري",
    "Mordechai Zaken" : "مردخاي زاكين",
    "Montefiore Windmill" : "طاحونة باب الخليل",
    "Mohammed Yousef El-Najar Hospital" : "مستشفى الشهيد أبو يوسف النجار الحكومي",
    "Mohammad Zuhdi Nashashibi" : "محمد زهدي النشاشيبي",
    "Modi'in Illit" : "موديعين عيليت",
    "Miriam Eshkol" : "مريام أشكول",
    "Mevo'ot Yeriho" : "ميفوت يريحو",
    "Menahem Yaari" : "مناحيم ياري",
    "Melkite Catholic Patriarchate" : "بطريركية الروم الملكيين الكاثوليك",
    "Marie-Alphonsine Danil Ghattas" : "ماري ألفونسين",
    "Manger Square" : "ساحة المهد",
    "Mandelbaum Gate" : "بوابة ماندلباوم",
    "Mamilla Pool" : "بركة مأمن الله",
    "Mamilla Mall" : "مول مأمن الله",
    "Malha Mall" : "مول المالحة",
    "Mahmoud al-Zahar" : "محمود الزهار",
    "Ma'ale Adumim" : "معاليه أدوميم",
    "Lina Abu Akleh" : "لينا أبو عاقلة",
    "Lily Serna" : "ليلي سيرنا",
    "Lara Khaldi" : "لارا الخالدي",
    "Kohelet Policy Forum" : "منتدى كوهيليت للسياسات",
    "Knesset Yisrael" : "كنيست يسرائيل",
    "Knesset Menorah" : "شمعدان الكنيست",
    "Kiryat Menachem Begin" : "كريات مناحيم بيغن",
    "Kiryat HaLeom" : "كريات هالوم",
    "Kidron Valley" : "وادي النار",
    "Khan Yunis" : "خان يونس",
    "Kenny Young" : "كيني يونغ",
    "Kamal Boullata" : "كمال بلاطة",
    "Kamal Adwan Hospital siege" : "حصار مستشفى كمال عدوان",
    "Joseph's Tomb" : "قبر يوسف",
    "Jonathan Apphus" : "يوناثان المكابي",
    "Jewish Agency for Israel" : "الوكالة اليهودية",
    "Jessica Cohen" : "جيسيكا كوهن",
    "Jerusalem syndrome" : "متلازمة القدس",
    "Jerusalem stone" : "حجر القدس",
    "Jerusalem mixed grill" : "مشاوي القدس المشكلة",
    "Latin Patriarchate of Jerusalem" : "بطريركية القدس للاتين",
    "Jerusalem Technology Park" : "حديقة القدس للتكنولوجيا",
    "Jerusalem Old Town Hall" : "مبنى بلدية القدس التاريخي",
    "Jerusalem Municipality" : "بلدية القدس",
    "Jerusalem Light Rail" : "قطار القدس الخفيف",
    "Jerusalem International YMCA" : "جمعية الشبان المسيحيين – القدس",
    "Jerusalem International Airport" : "مطار القدس الدولي",
    "Jerusalem Foundation" : "مؤسسة القدس",
    "Jerusalem Forest" : "غابة القدس",
    "Jerusalem Film Festival" : "مهرجان القدس السينمائي",
    "Jerusalem District" : "منطقة القدس",
    "Jerusalem Development Authority" : "هيئة تنمية القدس",
    "Jerusalem 24" : "القدس 24",
    "Jaffa–Jerusalem railway" : "خط سكك حديد يافا-القدس",
    "Jabal Al-Mukaber Club" : "نادي جبل المكبر",
    "Issaf Nashashibi Center for Culture and Literature" : "مكتبة دار إسعاف النشاشيبي",
    "Issa Kassissieh" : "عيسى قسيسية",
    "Issa Bandak" : "عيسى البندك",
    "Israeli Public Broadcasting Corporation" : "شركة البث العام الإسرائيلية",
    "Israel Postal Company" : "شركة البريد الإسرائيلي",
    "Israel Democracy Institute" : "المعهد الإسرائيلي للديمقراطية",
    "Israel Antiquities Authority" : "هيئة آثار إسرائيل",
    "Israel Academy of Sciences and Humanities" : "أكاديمية إسرائيل للعلوم والإنسانيات",
    "International Convention Center" : "مباني الأمة",
    "Institute for Zionist Strategies" : "معهد الإستراتيجيات الصهيونية",
    "Indonesia Hospital" : "المستشفى الإندونيسي",
    "Illés Relief" : "نموذج القدس لشتيفان إيلش",
    "Ibtisam Barakat" : "ابتسام بركات",
    "Ibrahim al-Maqadma Mosque missile strike" : "مجزرة مسجد إبراهيم المقادمة",
    "Huda Abuarquob" : "هدى أبو عرقوب",
    "Hitteen SC" : "نادي حطين",
    "Ramallah" : "رام الله",
    "Hilal Al-Quds Club" : "هلال القدس",
    "Henry Cattan" : "هنري قطان",
    "Hebron glass" : "زجاج الخليل",
    "Haseki Sultan Imaret" : "تكية خاصكي سلطان",
    "Har HaMenuchot" : "مقبرة هار همنوحوت",
    "Hanna Batatu" : "حنا بطاطو",
    "Haim Koren" : "حاييم كورين",
    "Gihon Spring" : "عين سلوان",
    "Generali Building" : "مبنى جنرالي",
    "mass graves" : "مقابر جماعية",
    "Gaza Sky Geeks" : "غزة سكاي جيكس",
    "Gaza City" : "غزة",
    "Gad Horowitz" : "غاد هوروويتز",
    "Fatima Bernawi" : "فاطمة برناوي",
    "Emi Palmor" : "إيمي بالمور",
    "Ein Lavan" : "عين لافان",
    "East Jerusalem" : "القدس الشرقية",
    "Dura, Hebron" : "دورا",
    "Dimitri Baramki" : "ديمتري برامكي",
    "Deir al-Balah" : "دير البلح",
    "Deir al-Balah Camp" : "مخيم دير البلح",
    "Damascus Gate" : "باب العامود",
    "Cremisan Valley" : "وادي كريمزان",
    "Cotton Merchants' Gate" : "باب القطانين",
    "Clal Center" : "مركز كلال",
    "Chords Bridge" : "جسر القدس الصاري المعلق",
    "Charles Warren" : "تشارلز وارن",
    "Burj al Luq Luq Community Centre and Society" : "جمعية مركز برج اللقلق المجتمعية",
    "Bethlehem Association" : "منظمة بيت لحم",
    "Benny Morris" : "بيني موريس",
    "Beitar Jerusalem F.C." : "بيتار القدس",
    "Beitar Illit" : "بيتار عيليت",
    "Beit Yonatan" : "بيت يوناتان",
    "Beit Sahour" : "بيت ساحور",
    "Beit Lahia" : "بيت لاهيا",
    "Beit Jala" : "بيت جالا",
    "Beit Jala Lions" : "ليونز بيت جالا",
    "Beit Hanoun" : "بيت حانون",
    "Beit HaNassi" : "بيت هاناسى",
    "Beit Aghion" : "بيت أغيون",
    "Bani Suheila" : "بني سهيلا",
    "Bani Na'im" : "بني نعيم",
    "Arson attack at Joseph's Tomb" : "قبر يوسف",
    "Arab Orthodox Society" : "جمعية حاملات الطيب الأرثوذكسية",
    "Anat Berko" : "عنات بيركو",
    "An-Najah National University" : "جامعة النجاح الوطنية",
    "Amnon Ben-Tor" : "أمنون بن تور",
    "Amin al-Husseini" : "أمين الحسيني",
    "All Nations Café" : "مقهى كل الأمم",
    "Albert Aghazarian" : "ألبرت أغازريان",
    "Al-Shati refugee camp" : "مخيم الشاطئ",
    "Al-Quds University" : "جامعة القدس",
    "Al-Nimr Palace" : "قصر النمر",
    "Al-Najah Secondary School" : "مدرسة النجاح الثانوية",
    "Al-Mashrabiya Building" : "بيت المشربية",
    "Al-Manara Square" : "ميدان المنارة",
    "Al-Aqsa University" : "جامعة الأقصى",
    "Ahli Qalqilyah" : "أهلي قلقيلية",
    "Agron House" : "بيت أغرون",
    "Abu Dis" : "أبو ديس",
    "Abu Daoud" : "محمد داود عودة",
    "Abd al-Qadir al-Husayni" : "عبد القادر الحسيني",
    "Abasan al-Kabira" : "عبسان الكبيرة",
    "Janzouri" : "جنزوري",
    "Jabalia" : "جباليا",
    "Idna" : "إذنا",
    "Hebron" : "الخليل",
    "Hanunu" : "هانونو",
    "Halhul" : "حلحول",
    "Gethsemane" : "جثسيماني",
    "Caphar" : "كفر",
    "Bethlehem" : "بيت لحم",
    "Bethany" : "بيت عبرة",
    "Beitunia" : "بيتونيا",
    "Az-Zawayda" : "الزوايدة",
    "As-Samu" : "السموع",
    "Ar-Rifa'iyya" : "الرفاعية",
    "Al-Yamun" : "اليامون",
    "Al-Ram" : "الرام",
    "Al-Mawazin" : "بائكة",
    "Al-Masyoun" : "الماصيون",
    "Al-Bireh" : "البيرة",
    "Ad-Dhahiriya" : "الظاهرية",
    "Ad-Deirat" : "الديرات",
}
# ---
# merge N_cit_ies_s and N_cit_ies_s_x
N_cit_ies_s |= N_cit_ies_s_x
# ---
tabe_lab_yy2 = open_json_file("yy2") or {}
N_cit_ies_s_lower = {x.lower(): xar for x, xar in N_cit_ies_s.items()}
# ---
# with open(f"{Dir2}/jsons/all_cities.json", "w", encoding="utf-8") as f:
#     json.dump(N_cit_ies_s, f, indent=2, ensure_ascii=False)
# ---
end = time.time()
print(f"Time: {end-start}")
# ---
Lenth_p = {
    "N_cit_ies_s": sys.getsizeof(N_cit_ies_s),
    "tabe_lab_yy2": sys.getsizeof(tabe_lab_yy2),
}
# ---

len_print.lenth_pri("cities.py", Lenth_p, Max=100)
