"""
search for any test file with: `from ArWikiCats import resolve_arabic_category_label`
replace it with `from ArWikiCats import resolve_label_ar`

and search for any item like this:
    "Category:20th century members of maine legislature": "تصنيف:أعضاء هيئة مين التشريعية في القرن 20",
replace it with:
    "20th century members of maine legislature": "أعضاء هيئة مين التشريعية في القرن 20",
"""
import os
import re
from pathlib import Path
TASKS_DIR = Path(__file__).resolve().parent
