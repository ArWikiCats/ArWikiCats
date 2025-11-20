# make2 — Automatic Arabic Category Label Generator for Wikipedia

[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Python](https://img.shields.io/badge/Python-3.10+-blue)]()
[![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen)]()
[![Tests](https://img.shields.io/badge/tests-Pytest-success)]()

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [How It Works](#how-it-works)
4. [Installation](#installation)
5. [Quick Usage](#quick-usage)
6. [Environment Flags](#environment-flags)
7. [Extending the System](#extending-the-system)
8. [Project Structure](#project-structure)
9. [Testing](#testing)
10. [Performance](#performance)
11. [Contributing](#contributing)

---

## Overview
**make2** is a complete, extensible, and high‑performance engine for converting Wikipedia category names (mostly English) into consistent Arabic labels ready for publishing as:

`تصنيف:إطلاق نار عشوائي 1550 في أوقيانوسيا`

It processes time expressions, geography, job titles, sports, film/media patterns, and more, using layered processing bots and optimized caching.

---

## Features
- Extremely fast (500K categories < 2 minutes)
- Modular, extensible bot‑based architecture
- Comprehensive translation dictionaries
- Automatic detection of:
  - Year, decade, century
  - Jobs and occupational groups
  - Geographic forms
  - Sports teams and competitions
  - Media titles
- Batch processing support
- Automatic prefixing with `تصنيف:`
- Reports missing/untranslated categories
- Highly optimized memory usage

---

## How It Works
Processing flows through six major phases:

1. **Normalization**
2. **Time Pattern Detection**
3. **Dictionary & Rule Matching**
4. **Core Label Resolution**
5. **Arabic Title Formatting**
6. **Prefixing with “تصنيف:”**

Internally orchestrated by the core resolver:
`src/main_processers/main_resolve.py`

---

## Installation
```bash
git clone https://github.com/yourname/make2
cd make2

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.in
```

---

## Quick Usage

### Single category
```python
from src import new_func_lab_final_label
print(new_func_lab_final_label("Category:2015 American television"))
```

### Batch processing
```python
from make2 import EventProcessor

processor = EventProcessor()
result = processor.process([
    "Category:2015 American television",
    "Category:Belgian cyclists"
])

print(result.labels)
print(result.no_labels)
```

---

## Environment Flags
Control behavior with:

- `ENABLE_WIKIDATA=1`
- `ENABLE_KOOORA=1`
- `YEMENTEST=1`
- `ALL_PRINT_OFF=1`
- `NOPRINT=1`
- `MAKEERR`, `STUBS`, etc.

---

## Extending the System

### Adding new translation datasets
Place files inside:

```
src/translations/
│── geo/
│── jobs/
│── sports/
│── medical/
```

### Adding new bots
Create file in:
```
src/make2_bots/<your_bot>.py
```

Then register inside:
```
main_processers/main_resolve.py
```

### Adding new rules
Modify logic inside:
```
src/main_processers/main_resolve.py
```

---

## Project Structure
```
src/
├── main.py
├── event_processing.py
├── main_processers/
│   ├── main_resolve.py
│   ├── event2bot.py
│   └── event_lab_bot.py
├── make2_bots/
├── translations/
├── translations_formats/
├── helps/
├── utils/
└── tests/
```

---

## Testing
Run all tests:

```bash
pytest
```

Tests cover:
- jobs
- sports
- geography
- years/time patterns
- special cases
- performance
- unknown categories handling

---

## Performance
Latest benchmarks:
- Memory reduced from **2GB → 183MB**
- End‑to‑end processing improved from **5 minutes → <4 seconds** in tests
- Full batch: **500,000 categories in <2 minutes**

For profiling:
```bash
python -m scalene run.py
```

---

## Contributing
- Follow project conventions
- Write tests for all new rules or dictionaries
- Keep modules clean and optimized
- Ensure Black + Isort + Ruff formatting

---

