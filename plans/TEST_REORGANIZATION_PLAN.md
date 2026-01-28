# خطة تنظيم اختبارات ArWikiCats

## ملخص التنفيذي

**السؤال:** هل من الأفضل إنشاء نوعين مختلفين من الاختبارات؟
1. **اختبارات نهائية (End-to-End)**: لاختبار الـ 30,000 تصنيف كاختبار أداء ونتائج متوقعة
2. **اختبارات وحدات (Unit Tests)**: لاختبار الوظائف وعملها بشكل منفصل

**الإجابة: نعم، هذا هو النهج الأمثل**

---

## الوضع الحالي

الكود لديه بالفعل مزيج من كلا النوعين، لكن ليس بشكل منظم:

| نوع الاختبار | الموقع الحالي | الحالة |
|--------------|--------------|--------|
| **End-to-End** | `tests/event_lists/` | موجود بشكل رئيسي (~28,500 اختبار) |
| **Unit Tests** | `tests/new_resolvers/`, `tests/translations/` | موجود جزئياً (~2,000 اختبار) |

### المشاكل الحالية

1. **عدم الوضوح**: غير واضح أي الاختبارات هي unit وأيها end-to-end
2. **صعوبة الصيانة**: عند فشل اختبار end-to-end، من الصعب معرفة أين المشكلة
3. **سرعة التنفيذ**: اختبارات end-to-end بطيئة، لكن لا يوجد وسيلة لتشغيل unit tests فقط بسرعة

---

## البنية المقترحة

```
tests/
├── conftest.py                    # التكوين العام (يظل في مكانه)
├── utils/                         # أدوات مساعدة مشتركة
│   ├── load_one_data.py          # دوال مقارنة البيانات
│   └── dump_runner.py            # مشغل الاختبارات بالدفعات
│
├── unit/                          # اختبارات الوحدات (سريعة)
│   ├── conftest.py               # تكوين خاص لـ unit (إن لزم)
│   │
│   ├── translations_formats/     # اختبارات نماذج التنسيق
│   │   ├── FormatData/
│   │   │   └── test_format_data_unit.py
│   │   ├── FormatDataV2/
│   │   ├── DataModelDouble/
│   │   └── format_multi_data/
│   │
│   ├── translations/             # اختبارات قواميس الترجمة
│   │   ├── data_builders/
│   │   │   └── test_build_jobs.py
│   │   ├── jobs/
│   │   ├── sports/
│   │   └── nationalities/
│   │
│   ├── time_formats/             # اختبارات تحويل الوقت
│   │   └── test_time_to_arabic.py
│   │
│   ├── fix/                      # اختبارات التنظيف والتطبيع
│   │   ├── fixtitle/
│   │   └── normalizations/
│   │
│   └── utils/                    # اختبارات دوال المساعدة
│       └── test_fixers.py
│
├── integration/                   # اختبارات التكامل (متوسطة)
│   ├── conftest.py               # تكوين خاص لـ integration
│   │
│   ├── resolvers/                # اختبارات interaction بين resolvers
│   │   ├── test_resolver_chain.py     # سلسلة الحل بالكامل
│   │   ├── test_jobs_with_nationalities.py
│   │   ├── test_sports_with_countries.py
│   │   └── test_time_with_jobs.py
│   │
│   └── formatters/               # اختبارات interaction بين components
│       ├── test_format_data_with_resolver.py
│       └── test_multi_data_formatter.py
│
└── e2e/                          # اختبارات النهاية (قد تكون بطيئة)
    ├── conftest.py               # تكوين خاص لـ e2e
    │
    ├── categories/               # اختبارات الفئات حسب النوع
    │   ├── deaths/              # من tests/event_lists/deaths/
    │   ├── geo/                 # من tests/event_lists/geo/
    │   ├── jobs/                # من tests/event_lists/jobs_bots/
    │   ├── sports/              # من tests/event_lists/sports/
    │   ├── people/              # من tests/event_lists/people/
    │   └── womens/              # من tests/event_lists/womens/
    │
    ├── countries/               # اختبارات حسب الدولة
    │   ├── test_yemen.py        # من tests/event_lists/
    │   ├── test_south_african.py
    │   ├── test_antigua_and_barbuda.py
    │   └── ...
    │
    └── regression/              # اختبارات regressions محددة
        ├── test_bug.py          # من tests/test_bug/
        ├── test_some_fixes.py   # من tests/test_some_fixes/
        └── to_fix_skip/         # من tests/to_fix_skip/
```

---

## خطة التنفيذ

### المرحلة 1: تحديث التكوينات

#### ملف: `tests/conftest.py`

```python
"""Test configuration for the test-suite."""

import os
import random

import pytest


def pytest_configure(config: pytest.Config) -> None:
    """
    Global test-suite normalization.
    - Force UTF-8 I/O (important on Windows for Arabic output)
    - Make random deterministic (avoid flaky order / generation)
    """
    os.environ.setdefault("PYTHONUTF8", "1")
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    random.seed(0)


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add custom command line options."""
    parser.addoption(
        "--rune2e",
        action="store_true",
        default=False,
        help="Run end-to-end tests (disabled by default in quick mode)",
    )


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """
    Automatically apply markers based on test location and add markers to unmarked tests.
    """
    run_e2e = config.getoption("--rune2e")

    for item in items:
        path_parts = item.fspath.parts

        if "unit" in path_parts:
            item.add_marker(pytest.mark.unit)
            item.add_marker(pytest.mark.fast)
        elif "integration" in path_parts:
            item.add_marker(pytest.mark.integration)
        elif "e2e" in path_parts:
            item.add_marker(pytest.mark.e2e)
            if not run_e2e:
                item.add_marker(pytest.mark.skip(reason="E2E tests disabled, use --rune2e"))
        else:
            # Fallback for tests not yet moved
            if "event_lists" in str(item.fspath):
                item.add_marker(pytest.mark.e2e)
                if not run_e2e:
                    item.add_marker(pytest.mark.skip(reason="E2E tests disabled"))
            elif any(x in str(item.fspath) for x in ["unit", "test_format_data", "test_build_jobs"]):
                item.add_marker(pytest.mark.unit)
                item.add_marker(pytest.mark.fast)
```

#### ملف: `pyproject.toml`

```toml
[tool.pytest.ini_options]
minversion = "7.0"
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]

# Markers definition
markers = [
    # Type markers
    "unit: Unit tests - test individual functions/classes in isolation (< 0.1s)",
    "integration: Integration tests - test interaction between components (< 1s)",
    "e2e: End-to-end tests - test the full system with real inputs (may be slow)",

    # Existing markers (keep for backward compatibility)
    "fast: Fast tests that run quickly",
    "slow: Slow tests that take longer to run",
    "dump: Data comparison tests",
    "dumpbig: Large dataset comparison tests",
]

addopts = [
    "-v",
    "--tb=short",
    "--strict-markers",
]
```

### المرحلة 2: إنشاء الأدلة الجديدة

```bash
mkdir -p tests/unit
mkdir -p tests/integration
mkdir -p tests/e2e
```

### المرحلة 3: نقل وتصنيف الاختبارات

#### نقل Unit Tests

```bash
# اختبارات نماذج التنسيق
git mv tests/new_resolvers/translations_formats/FormatData/test_format_data_unit.py tests/unit/translations_formats/FormatData/

# اختبارات data builders
git mv tests/translations/data_builders/test_build_jobs.py tests/unit/translations/data_builders/

# اختبارات الوقت
git mv tests/time_resolvers/test_time_to_arabic tests/unit/time_formats/
```

#### نقل Integration Tests

إنشاء اختبارات جديدة لاختبار interaction بين المكونات.

#### نقل E2E Tests

```bash
# اختبارات الفئات
git mv tests/event_lists/deaths tests/e2e/categories/
git mv tests/event_lists/geo tests/e2e/categories/
git mv tests/event_lists/jobs_bots tests/e2e/categories/jobs/
git mv tests/event_lists/sports tests/e2e/categories/

# اختبارات الدول
git mv tests/event_lists/test_yemen.py tests/e2e/countries/
git mv tests/event_lists/test_south_african.py tests/e2e/countries/
```

---

## طرق التشغيل

```bash
# التطوير اليومي - unit tests فقط (سريع جداً)
pytest -m unit

# قبل commit - unit + integration
pytest -m "unit or integration"

# قبل إصدار - كل الاختبارات
pytest -m "unit or integration or e2e"
# أو
pytest --rune2e

# تشغيل e2e فقط
pytest --rune2e --rune2e

# تشغيل اختبارات محددة
pytest tests/unit/test_time_to_arabic.py

# تشغيل مع تقرير التغطية
pytest -m unit --cov=ArWikiCats --cov-report=html
```

---

## معايير التصنيف

### 1. Unit Tests (`tests/unit/`)

**التعريف:** اختبارات دالة/كلاس واحدة معزولة

**المعايير:**
- لا تستخدم `resolve_label_ar()` أو `resolve_arabic_category_label()`
- لا تستخدم `batch_resolve_labels()` أو `EventProcessor`
- تختبر دالة واحدة من module واحد
- يمكن استخدام mock للdependencies

**أمثلة:**
```python
# ✓ صحيح - unit test
def test_format_data_search():
    bot = FormatData(...)
    result = bot.search("men's football")
    assert result == "كرة قدم رجال"

# ✗ خطأ - هذا e2e test
def test_category_translation():
    result = resolve_label_ar("Category:British footballers")
    assert result == "تصنيف:لاعبو كرة قدم بريطانيون"
```

### 2. Integration Tests (`tests/integration/`)

**التعريف:** اختبارات interaction بين 2-3 مكونات

**المعايير:**
- تختبر interaction بين عدة modules
- قد تستخدم resolver مباشرة لكن ليس السلسلة كاملة
- لا تختبر `resolve_label_ar()` (هذا e2e)

**أمثلة:**
```python
# ✓ صحيح - integration test
def test_jobs_resolver_with_nationalities():
    jobs_data = {...}
    nats_data = {...}
    result = resolve_jobs_with_nats(jobs_data, nats_data, "British footballers")
    assert result == "لاعبو كرة قدم بريطانيون"
```

### 3. E2E Tests (`tests/e2e/`)

**التعريف:** اختبارات النظام الكامل من المدخل للمخرج

**المعايير:**
- تستخدم `resolve_label_ar()` أو `resolve_arabic_category_label()`
- مدخلات فئات حقيقية كاملة
- تختبر النتيجة النهائية فقط

**أمثلة:**
```python
# ✓ صحيح - e2e test
@pytest.mark.parametrize("category,expected", [
    ("Category:British footballers", "تصنيف:لاعبو كرة قدم بريطانيون"),
    ("Category:2015 in Yemen", "تصنيف:2015 في اليمن"),
])
def test_full_translation(category, expected):
    result = resolve_label_ar(category)
    assert result == expected
```

---

## الفوائد المتوقعة

1. **سرعة التنمية**:
   - `pytest -m unit` → ثوانٍ قليلة أثناء التطوير
   - لا حاجة لانتظار 30,000 اختبار

2. **سهولة التصحيح**:
   - عند فشل unit test، المشكلة واضحة فوراً
   - عند فشل e2e test، يمكن تشغيل unit tests أولاً لعزل المشكلة

3. **ثبات النظام**:
   - e2e tests تضمن عدم كسر الترجمات الموجودة
   - unit tests تضمن أن كل دالة تعمل بشكل صحيح

4. **مرونة التنفيذ**:
   - تشغيل سريع أثناء التطوير
   - تشغيل شامل قبل الإصدار

---

## الملاحظات

1. **لا حاجة لحذف الاختبارات**: فقط نقلها وإعادة تنظيمها
2. **يمكن البدء تدريجياً**: لا تحتاج لنقل كل شيء دفعة واحدة
3. **الحفاظ على التاريخ**: استخدام `git mv` للحفاظ على تاريخ الملفات
4. **اختياري**: يمكن البدء بجزء صغير كـ pilot ثم تعميم النهج
