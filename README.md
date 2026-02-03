# مكتبة ArWikiCats — نظام تعريب تلقائي لتصنيفات ويكيبيديا العربية

[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Python](https://img.shields.io/badge/Python-3.10+-blue)]()
[![Status](https://img.shields.io/badge/status-Beta-orange)]()
[![Tests](https://img.shields.io/badge/tests-60000+-success)]()

---

# جدول المحتويات

- [لماذا ArWikiCats](#لماذا-arwikicats)
- [1. المزايا الرئيسية](#1-المزايا-الرئيسية)
- [2. داخل محرك ArWikiCats](#2-داخل-محرك-arwikicats)
- [3. المتطلبات والتثبيت](#3-المتطلبات-والتثبيت)
- [4. الاستخدام السريع](#4-الاستخدام-السريع)
- [5. إعدادات النظام](#5-إعدادات-النظام)
- [6. توسيع النظام](#6-توسيع-النظام)
- [7. بنية المشروع](#7-بنية-المشروع)
- [8. الاختبارات](#8-الاختبارات)
- [9. الأداء](#9-الأداء)
- [10. ملاحظات للمساهمين](#10-ملاحظات-للمساهمين)
- [11. القيود الحالية](#11-القيود-الحالية)
- [12. خارطة الطريق](#12-خارطة-الطريق)
- [13. الخلاصة](#13-الخلاصة)

---

## لماذا ArWikiCats

تعريب تصنيفات ويكيبيديا العربية يمثل تحديًا بسبب العدد الهائل من التصنيفات الإنجليزية والأنماط المتداخلة.
يهدف مشروع **ArWikiCats** إلى معالجة هذه المشكلة عبر بناء نظام قادر على:

* توحيد أسلوب الترجمة.
* معالجة التصنيفات بدقة عالية.
* تنفيذ أنماط زمنية وجغرافية ووظيفية ورياضية معقدة.
* دعم عمل البوتات ومهام الإنتاج التحريري.
* معالجة الفئات المركبة التي تتضمن جنسيات ورياضات ووظائف معًا.

---

# 1. المزايا الرئيسية

* **سرعة عالية للغاية** بعد التحسينات الأخيرة.
* **قواعد ترجمة واسعة** تغطي آلاف الأنماط (سنوات – بلدان – وظائف – رياضة – إعلام).
* **تخزين مؤقت داخلي** لتسريع الأداء في كل خطوة باستخدام `functools.lru_cache`.
* **نظام وحدات (Bots)** قابل للتوسعة بسهولة.
* **نتائج دقيقة وموحّدة** متوافقة مع أسلوب ويكيبيديا العربية.
* **قدرة على معالجة دفعات ضخمة** تشمل آلاف أو مئات آلاف التصنيفات.
* **محللات متعددة المستويات** لحل الفئات المعقدة (وظائف، جنسيات، رياضات، أسماء بلدان).

---

# 2. داخل محرك ArWikiCats

المعالجة الكاملة تمر عبر المراحل التالية:
* التصنيف الخام → التطبيع → اكتشاف الأنماط الزمنية → المحللات المتخصصة (وظائف/رياضات/جنسيات/بلدان) → مطابقة القواعد والترجمات → وحدة الحل الرئيسية → تنسيق العربية → التسمية النهائية (تصنيف:)


---

## 2.1 التطبيع (Normalization)

تنظيف التصنيف قبل التحليل:

* إزالة الشرطات السفلية.
* توحيد المسافات.
* إزالة الرموز غير الضرورية.
* حذف بادئة Category:.

---

## 2.2 اكتشاف الأنماط
* التعامل مع الحالات الزمنية مثل:
    - المدى الزمني:
    - السنوات (2015 - 10BC)
    - العقود: 1550s
    - القرون: 20th century
    - الألفيات:

مثال:

```
Category:1550s establishments in Namibia → تصنيف:تأسيسات عقد 1550 في ناميبيا

````

---

## 2.3 القواعد والقواميس

يشمل ذلك:
* **[الجنسيات](ArWikiCats/jsons/nationalities)**:
	- صيغ المذكر والمؤنث والجمع والمفرد واسم البلد العربي والإنجليزي.
* **[الجغرافيا](ArWikiCats/jsons/geography) و[المدن](ArWikiCats/jsons/cities)**:
	- المدن والدول والمناطق والأقاليم والمحافظات والبلديات والمقاطعات والتقسيمات الإدارية الأخرى.
* **[الوظائف والمهن](ArWikiCats/jsons/jobs)**:
	- مختلف مسميات الوظائف والمهن والأعمال. وتصنيفها حسب الجنس (للرجال/للسيدات) يشمل ذلك الوظائف الرياضية والوظائف السينمائية والمهن العلمية والدينية.
* **[الرياضات](ArWikiCats/jsons/sports)**:
    - التسميات والفرق والوظائف والألعاب الأولمبية، والتنسيقات الرياضية، وأسماء الفرق، ومراكز اللاعبين، ومصطلحات مختلف الرياضات، والرياضات النسائية والشبابية.
* **[الأفلام والتلفزيون](ArWikiCats/jsons/media)**:
	- الأفلام وأنواعها ومهن صناعة السينما، مثل صناع الأفلام والمخرجين والممثلين، وأنواع وتنسيقات التلفزيون وكافة المصطلحات المتعلقة بالأفلام والتلفزيون.
* **الجوائز والأحداث**:
	- جوائز الأفلام والمسابقات الرياضية والجوائز الموسيقية، والأحداث والمناسبات حسب الشهر والسنة.
* **[المفاهيم](ArWikiCats/jsons/keys)**:
	- الأيديولوجيات السياسية، والفترات التاريخية، والمجالات العلمية، والمفاهيم الاقتصادية، واللغات.
* **[الكيانات والأشياء](ArWikiCats/jsons/population)**:
	- المباني والبنية التحتية والمركبات والأسلحة والكتب والألبومات.
* **[الأنواع](ArWikiCats/jsons/taxonomy)**:
	- الأنواع الحيوانية والنباتية.
* **[الأشخاص](ArWikiCats/jsons/people)**:
	- الشخصيات التي تملك تصنيفات باسمائها مثل أصحاب المناصب الرسمية والفنانون والمخرجون.
---

## 2.4 المحرك المركزي لحل التسمية

المسؤول عن التنظيم:

`main_processers/main_resolve.py`

وظيفته:

* تجربة المحللات المتخصصة حسب الأولوية (وظائف ← رياضات ← جنسيات ← بلدان).
* معالجة الأنماط الزمنية (سنوات، عقود، قرون).
* التوقف عند أول تطابق صحيح.
* ضمان الاتساق بين التصنيفات.
* استخدام التخزين المؤقت لتحسين الأداء.

---

## 2.5 تنسيق النتيجة النهائية

يشمل:

* تحسين الصياغة العربية.
* تنسيق العبارات.
* تمرير النتيجة عبر `fixlabel`.

---

## 2.6 إضافة بادئة "تصنيف:"

عبر دالة:

`EventProcessor._prefix_label()`

---

# 3. المتطلبات والتثبيت

## 3.1 المتطلبات

* Python 3.10 أو أحدث
* مكتبات مثبتة من `requirements.in`

## 3.2 التثبيت

```bash
pip install ArWikiCats --pre
```
or
```bash
git clone https://github.com/MrIbrahem/ArWikiCats.git
cd ArWikiCats
pip install -r requirements.in
````

---

# 4. الاستخدام السريع

## 4.1 معالجة تصنيف واحد

```python
from ArWikiCats import resolve_arabic_category_label

label = resolve_arabic_category_label("Category:2015 in Yemen")
print(label)
# تصنيف:2015 في اليمن
```

## 4.2 معالجة قائمة كاملة

```python
from ArWikiCats import batch_resolve_labels

categories = [
    "Category:2015 American television",
    "Category:1999 establishments in Europe",
    "Category:Belgian cyclists",
    "Category:American basketball coaches",
]

result = batch_resolve_labels(categories)

print(f"تم ترجمة: {len(result.labels)} تصنيف")
print(f"لم يُترجم: {len(result.no_labels)} تصنيف")
print(f"أنماط مكتشفة: {result.category_patterns}")

# عرض النتائج
for en, ar in result.labels.items():
    print(f"  {en} → {ar}")
```

## 4.3 استخدام دالة الترجمة المباشرة

```python
from ArWikiCats import resolve_label_ar

# بدون بادئة "تصنيف:"
label = resolve_label_ar("American basketball players")
print(label)
# لاعبو كرة سلة أمريكيون
```

## 4.4 معالجة تصنيف مع تفاصيل كاملة

```python
from ArWikiCats import EventProcessor

processor = EventProcessor()
result = processor.process_single("Category:British footballers")

print(f"الأصلي: {result.original}")
print(f"المُعيّر: {result.normalized}")
print(f"التسمية الخام: {result.raw_label}")
print(f"التسمية النهائية: {result.final_label}")
print(f"تم إيجاد تسمية: {result.has_label}")
```

## 4.5 تشغيل الأمثلة

```bash
python examples/run.py           # مثال بسيط
python examples/5k.py            # معالجة 5000 تصنيف
```

---

# 5. إعدادات النظام

يمكن تخصيص سلوك النظام باستخدام متغيرات البيئة أو معاملات سطر الأوامر:

| الإعداد | الوصف |
|---------|-------|
| `SAVE_DATA_PATH` | مسار حفظ البيانات المؤقتة |

تفاصيل كل متغير موجودة في:

`ArWikiCats/config.py`

---

# 6. توسيع النظام

## 6.1 إضافة ترجمات جديدة

ضع القواميس داخل:

`ArWikiCats/translations/`

مثال:

```python
# في ArWikiCats/translations/jobs/Jobs.py
jobs_mens_data = {
    "footballers": "لاعبو كرة قدم",
    "painters": "رسامون",
}

jobs_womens_data = {
    "footballers": "لاعبات كرة قدم",
    "painters": "رسامات",
}
```

## 6.2 إضافة محلل جديد

أضف محللك في `ArWikiCats/new_resolvers/` واربطه في `reslove_all.py`:

```python
# في ArWikiCats/new_resolvers/reslove_all.py
from .your_resolver import resolve_your_category

def all_new_resolvers(category: str) -> str:
    category_lab = (
        main_jobs_resolvers(category) or
        resolve_your_category(category) or  # المحلل الجديد
        main_sports_resolvers(category) or
        ""
    )
    return category_lab
```

## 6.3 إضافة بوت جديد

```text
ArWikiCats/make_bots/yourdomain_bot.py
```

مع:

1. دوال المعالجة
2. ربط البوت في resolver
3. إضافة اختبارات في `tests/`

## 6.4 استخدام تنسيقات البيانات

```python
from ArWikiCats.translations_formats import FormatData, format_multi_data

# تنسيق بسيط بعنصر واحد
formatter = FormatData(
    formatted_data={"{sport} players": "لاعبو {sport_ar}"},
    data_list={"football": "كرة القدم"},
    key_placeholder="{sport}",
    value_placeholder="{sport_ar}",
)
result = formatter.search("football players")

# تنسيق مركب بعنصرين
multi_formatter = format_multi_data(
    formatted_data={"{nat} {sport} players": "لاعبو {sport_ar} {nat_ar}"},
    data_list={"british": "بريطانيون"},
    data_list2={"football": "كرة القدم"},
    key_placeholder="{nat}",
    value_placeholder="{nat_ar}",
)
```

---

# 7. بنية المشروع

```
ArWikiCats/
│
├── __init__.py              # نقطة الدخول الرئيسية والتصدير العام
├── config.py                # إعدادات النظام والمتغيرات
├── event_processing.py      # معالجة دفعات التصنيفات
│
├── fix/                     # أدوات تصحيح وتنسيق النصوص العربية
│   ├── fixlists.py
│   ├── fixtitle.py
│   └── specific_normalizations.py
│
├── main_processers/         # المحرك المركزي لحل التسميات
│   ├── main_resolve.py      # نقطة الدخول الرئيسية للترجمة
│   ├── event2bot.py         # معالجة الأحداث والتصنيفات الزمنية
│   └── event_lab_bot.py     # محلل التسميات المتقدم
│
├── new_resolvers/           # المحللات الجديدة المتخصصة
│   ├── reslove_all.py       # نقطة الدخول للمحللات الجديدة
│   ├── jobs_resolvers/      # محللات الوظائف والمهن
│   ├── sports_resolvers/    # محللات الرياضات والفرق
│   ├── nationalities_resolvers/  # محللات الجنسيات
│   ├── countries_names_resolvers/ # محللات أسماء البلدان
│   └── time_and_jobs_resolvers/ # محللات الترجمة المتقدمة
│   └── genders_resolvers/       # محللات الجنس (مذكر/مؤنث)
│
├── patterns_resolvers/      # محللات الأنماط المركبة
│   ├── country_time_pattern.py
│   └── nat_males_pattern.py
│
├── time_formats/          # معالجة الأنماط الزمنية
│   ├── time_to_arabic.py    # تحويل التواريخ للعربية
│   └── with_years_bot.py    # معالجة التصنيفات مع السنوات
│
├── make_bots/               # البوتات المتخصصة
│   ├── date_bots/           # بوتات التواريخ
│   ├── jobs_bots/           # بوتات الوظائف
│   ├── media_bots/          # بوتات الأفلام والتلفزيون
│   ├── sports_bots/         # بوتات الرياضة
│   ├── format_bots/         # بوتات التنسيق
│   ├── languages_bot/       # بوتات اللغات
│   ├── lazy_data_bots/      # بوتات التحميل الكسول
│   └── matables_bots/       # بوتات الجداول
│
├── ma_bots/                 # بوتات المعالجة الأساسية
│   ├── country_bot.py
│   └── general_resolver.py
│
├── ma_bots/                # بوتات المعالجة المتقدمة
│   ├── ar_lab/
│   ├── country2_bots/
│   └── year_or_typeo/
│
├── translations/            # قواميس الترجمة
│   ├── geo/                 # الجغرافيا والمدن
│   ├── sports/              # الرياضات والفرق
│   ├── jobs/                # الوظائف والمهن
│   ├── nats/                # الجنسيات
│   ├── tv/                  # الأفلام والتلفزيون
│   ├── medical/             # المصطلحات الطبية
│   ├── politics/            # السياسة والحكومات
│   ├── entertainments/      # الترفيه
│   └── mixed/               # بيانات مختلطة
│
├── translations_formats/    # تنسيق قوالب الترجمة
│   ├── DataModel/           # نماذج البيانات الأساسية
│   ├── data_with_time.py    # تنسيق البيانات مع الوقت
│   └── multi_data.py        # تنسيق البيانات المتعددة
│
├── jsons/                   # ملفات JSON للبيانات
│   ├── nationalities/
│   ├── geography/
│   ├── cities/
│   ├── jobs/
│   ├── sports/
│   ├── media/
│   ├── keys/
│   ├── people/
│   ├── population/
│   └── taxonomy/
│
├── helps/                   # أدوات مساعدة
│   ├── log.py               # نظام التسجيل
│   ├── memory.py            # مراقبة الذاكرة
│   └── jsonl_dump.py        # تصدير JSONL
│
└── utils/                   # أدوات عامة
    ├── fixing.py
    └── match_relation_word.py

tests/                       # اختبارات (+60,000 اختبار)
│   ├── unit/                # اختبارات الوحدات (سريعة)
│   ├── integration/         # اختبارات التكامل (متوسطة)
│   └── e2e/                 # اختبارات شاملة (+15,000 تصنيف)
│   └── big/                 # اختبارات مجموعة بيانات (+26,000 تصنيف)
examples/                    # أمثلة الاستخدام
```

---

# 8. الاختبارات

بعد أي تحديث:

```bash
pytest
```

يغطي المشروع أكثر من **60,000 اختبار** مُنظّمة في أربع فئات رئيسية:

## 8.1 فئات الاختبارات

### اختبارات الوحدات (`tests/unit/`)
اختبارات سريعة تختبر الدوال والكلاسات بشكل منفصل (أقل من 0.1 ثانية لكل اختبار).

```bash
pytest tests/unit/
pytest -m unit
```

### اختبارات التكامل (`tests/integration/`)
اختبارات تختبر التفاعل بين المكونات المختلفة (أقل من 1 ثانية لكل اختبار).

```bash
pytest tests/integration/
pytest -m integration
```

### اختبارات شاملة (`tests/e2e/`)
اختبارات النظام الكامل من المدخل للمخرج (قد تكون بطيئة) - تحتوي على أكثر من **15,000 تصنيف**

```bash
pytest tests/e2e/
pytest --rune2e
```

### اختبارات مجموعة بيانات (`tests/big/`)
اختبارات النظام كامل (بطيئة) - تحتوي على أكثر من **26,000 تصنيف**

```bash
pytest tests/big/ -m big
```

### تشغيل كافة الاختبارات الأربعة
تشغيل أكثر من **60,000 اختبار** من جميع الأنواع:

```bash
pytest --rune2e -m "not skip2" -n 16
```

## 8.2 ما تغطيه الاختبارات

* الوظائف الأساسية
* الأنماط الزمنية (سنوات، عقود، قرون، ألفيات، قبل الميلاد)
* البلدان والجنسيات ومختلف حالات التصنيفات
* الأنماط المعقدة (جنسية + رياضة + وظيفة)
* الحالات النادرة
* أداء النظام
* مطابقة القواميس
* الفرق الرياضية والمسابقات
* الأفلام والتلفزيون
* محللات الوظائف المتقدمة

## 8.3 تشغيل جزء معين

```bash
pytest -k "jobs"
pytest tests/test_languages/
```

## 8.4 الاختبارات البطيئة

```bash
pytest -m slow
```

---

# 9. الأداء

* استهلاك الذاكرة: حُسن الاستهلاك مقارنة مقارنة [بالإصدار السابق](https://github.com/MrIbrahem/make2) **2GB إلى أقل من 100 ميجا**
* الاختبارات:  **23 ثانية** (باستخدام `pytest`)
* القدرة على معالجة أكثر من **+5,000 تصنيف** في ثوان. [examples/5k.py](examples/5k.py)

تشغيل Scalene:

```bash
python -m scalene run.py
```

---

# 10. ملاحظات للمساهمين

* أي إضافة يجب أن تشمل قاعدة + قاموس + اختبار.
* الالتزام بـ Black (طول السطر: 120) وIsort (نمط black) وRuff للفحص.
* منع إضافة قواعد بلا اختبارات.
* استخدام f-strings للتسجيل: `logger.debug(f"part1={a} part2={b}")`
* الحفاظ على ترميز UTF-8 للنصوص العربية.

تشغيل أدوات التنسيق:

```bash
black ArWikiCats/
isort ArWikiCats/
ruff check ArWikiCats/
```

---

# 11. القيود الحالية

* بعض التصنيفات النادرة قد تحتاج معالجة يدوية.
* نتائج بعض الأنماط تتوقف على توفر بيانات في القواميس.
* أنماط معقدة جدًا قد تمر إلى `no_labels`.

---

# 12. خارطة الطريق

* تحسين وحدة الرياضة (Sport Formatter v3). ✅
* توسيع تغطية التصنيفات الإعلامية والموسيقية.
* تحسين دعم التصنيفات متعددة العناصر.
* إضافة دعم للمزيد من اللغات والترجمات.

---

# 13. الخلاصة

نظام **ArWikiCats** هو نظام مرن، عالي الأداء، قابل للتوسعة، ويدعم عدد كبير جدًا من التصنيفات بسهولة.
يعتمد على:

* قواعد ترجمة متخصصة
* محللات متعددة المستويات (وظائف، رياضات، جنسيات، بلدان)
* تخزين مؤقت متقدم
* اختبارات صارمة (+60,000 اختبار)
* تصميم قابل للتطوير
* تنسيقات بيانات مرنة (FormatData, MultiDataFormatter)

ويعد مناسبًا للبوتات، الأعمال التحريرية، والمشاريع الضخمة في ويكيبيديا العربية.

---

## الواجهة البرمجية (API)

الوظائف والفئات المُصدّرة الرئيسية:

```python
from ArWikiCats import (
    resolve_arabic_category_label,  # ترجمة تصنيف واحد مع البادئة
    resolve_label_ar,               # ترجمة تصنيف واحد بدون البادئة
    batch_resolve_labels,           # ترجمة قائمة تصنيفات
    EventProcessor,                 # معالج الأحداث المفصل
    getLogger,                     # نظام التسجيل
    print_memory,                   # طباعة استهلاك الذاكرة
    dump_all_len,                   # طباعة أطوال البيانات
)
```
