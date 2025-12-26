"""
pytest tests/big_data/test_big.py -m dumpbig
"""

import json
from pathlib import Path

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label


@pytest.fixture
def load_json_data(request):
    file_path = request.param
    if not file_path.exists():
        return {}  # أو pytest.skip(f"File {file_path} not found")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# 2. دالة مساعدة لتجنب تكرار الكود داخل الاختبارات (Helper)


def run_dump_logic(name, data):
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    expected2 = {x: v for x, v in expected.items() if v and x in diff_result}
    dump_diff(expected2, f"{name}_expected")

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


# --- الاختبار الأول: لجميع الملفات في المجلد ---
DATA_DIR = Path(__file__).parent
JSON_FILES = list(DATA_DIR.glob("*.json"))


@pytest.mark.dumpbig
@pytest.mark.parametrize("load_json_data", JSON_FILES, indirect=True, ids=lambda p: f"test_big_{p.name}")
def test_religions_big_data(load_json_data, request) -> None:
    # سيتم تحميل الملف هنا فقط
    name = request.node.callspec.id  # الحصول على الاسم من الـ ID
    run_dump_logic(name, load_json_data)


# --- الاختبار الثاني: لملف محدد (religions2.json) ---
FILE2 = Path(__file__).parent / "religions2.json"


@pytest.mark.dumpbig
@pytest.mark.parametrize("load_json_data", [FILE2], indirect=True, ids=["test_big_data_2"])
def test_religions_big_data_2(load_json_data, request) -> None:
    run_dump_logic(request.node.callspec.id, load_json_data)


# --- الاختبار الثالث: لملف محدد (religions3.json) ---
FILE3 = Path(__file__).parent / "religions3.json"


@pytest.mark.dumpbig
@pytest.mark.parametrize("load_json_data", [FILE3], indirect=True, ids=["test_big_data_3"])
def test_religions_big_data_3(load_json_data, request) -> None:
    run_dump_logic(request.node.callspec.id, load_json_data)
