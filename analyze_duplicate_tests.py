#!/usr/bin/env python3
"""
أداة لتحليل الاختبارات المكررة في ملفات tests/event_lists

هذا السكريبت يقوم بـ:
1. تحليل جميع ملفات Python في tests/event_lists
2. استخراج أزواج المفاتيح-القيم من القواميس
3. حساب عدد التكرارات لكل زوج
4. عرض النتائج مع إمكانية إزالة المكررات
"""

import ast
import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple


class DuplicateTestAnalyzer:
    """محلل الاختبارات المكررة"""

    def __init__(self, base_path: str):
        """
        تهيئة المحلل

        Args:
            base_path: المسار الأساسي لمجلد tests/event_lists
        """
        self.base_path = Path(base_path)
        # تخزين الأزواج: {(key, value): [(file_path, dict_name, line_number), ...]}
        self.test_pairs: Dict[Tuple[str, str], List[Tuple[str, str, int]]] = defaultdict(list)
        # تخزين محتوى الملفات
        self.file_contents: Dict[str, List[str]] = {}

    def extract_dict_from_node(self, node: ast.Dict, file_path: str, dict_name: str = "unknown") -> None:
        """
        استخراج أزواج المفاتيح-القيم من عقدة قاموس AST

        Args:
            node: عقدة القاموس في AST
            file_path: مسار الملف
            dict_name: اسم القاموس
        """
        for key_node, value_node in zip(node.keys, node.values, strict=False):
            # تجاهل العناصر None (في حالة dictionary unpacking)
            if key_node is None or value_node is None:
                continue

            # استخراج القيم الحرفية فقط (strings)
            if isinstance(key_node, ast.Constant) and isinstance(value_node, ast.Constant):
                if isinstance(key_node.value, str) and isinstance(value_node.value, str):
                    key = key_node.value
                    value = value_node.value
                    line_number = key_node.lineno

                    # تخزين الزوج مع معلومات موقعه
                    self.test_pairs[(key, value)].append((file_path, dict_name, line_number))

    def analyze_file(self, file_path: Path) -> None:
        """
        تحليل ملف Python واحد

        Args:
            file_path: مسار الملف
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                lines = content.splitlines()

            # حفظ محتوى الملف للاستخدام لاحقاً
            self.file_contents[str(file_path)] = lines

            # تحليل الملف باستخدام AST
            tree = ast.parse(content, filename=str(file_path))

            # تتبع العقد التي تم معالجتها لتجنب التكرار
            processed_nodes = set()

            # البحث عن جميع القواميس في الملف
            for node in ast.walk(tree):
                # البحث عن تعيينات القواميس (مثل: data1 = {...})
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and isinstance(node.value, ast.Dict):
                            # استخدام id العقدة لتجنب المعالجة المكررة
                            if id(node.value) not in processed_nodes:
                                dict_name = target.id
                                self.extract_dict_from_node(node.value, str(file_path), dict_name)
                                processed_nodes.add(id(node.value))

        except Exception as e:
            print(f"⚠️  خطأ في تحليل الملف {file_path}: {e}")

    def scan_directory(self) -> None:
        """مسح جميع ملفات Python في المجلد"""
        print(f"🔍 جاري مسح المجلد: {self.base_path}")

        # البحث عن جميع ملفات .py
        python_files = list(self.base_path.rglob("*.py"))

        # استبعاد ملفات __pycache__ و __init__.py
        python_files = [f for f in python_files if "__pycache__" not in str(f) and f.name != "__init__.py"]

        print(f"📁 تم العثور على {len(python_files)} ملف Python")

        for file_path in python_files:
            self.analyze_file(file_path)

    def get_duplicates(self) -> Dict[Tuple[str, str], List[Tuple[str, str, int]]]:
        """
        الحصول على الأزواج المكررة فقط

        Returns:
            قاموس بالأزواج المكررة ومواقعها
        """
        return {pair: locations for pair, locations in self.test_pairs.items() if len(locations) > 1}

    def print_statistics(self) -> None:
        """
        Print analysis statistics summarizing extracted key-value pairs and duplicates.

        Prints the total number of unique pairs, the number of pairs that appear in more than one location, the total duplicate occurrences across all files, and the percentage of unique pairs that are duplicated.
        """
        duplicates = self.get_duplicates()
        total_pairs = len(self.test_pairs)
        duplicate_pairs = len(duplicates)

        # حساب إجمالي التكرارات
        total_occurrences = sum(len(locations) for locations in duplicates.values())

        print("\n" + "=" * 80)
        print("📊 إحصائيات التحليل")
        print("=" * 80)
        print(f"إجمالي الأزواج الفريدة: {total_pairs:,}")
        print(f"عدد الأزواج المكررة: {duplicate_pairs:,}")
        print(f"إجمالي التكرارات: {total_occurrences:,}")
        if total_pairs > 0:
            print(f"نسبة التكرار: {(duplicate_pairs / total_pairs * 100):.2f}%")
        print("=" * 80 + "\n")

    def print_duplicates(self, limit: int = 20) -> None:
        """
        طباعة الأزواج المكررة

        Args:
            limit: الحد الأقصى لعدد الأزواج المعروضة
        """
        duplicates = self.get_duplicates()

        if not duplicates:
            print("✅ لا توجد اختبارات مكررة!")
            return

        # ترتيب حسب عدد التكرارات (الأكثر تكراراً أولاً)
        sorted_duplicates = sorted(duplicates.items(), key=lambda x: len(x[1]), reverse=True)

        print(f"\n🔍 عرض أول {min(limit, len(sorted_duplicates))} زوج مكرر:\n")

        for idx, ((key, value), locations) in enumerate(sorted_duplicates[:limit], 1):
            print(f"\n{idx}. تكرر {len(locations)} مرة:")
            print(f"   المفتاح: {key}")
            print(f"   القيمة: {value}")
            print("   المواقع:")

            for file_path, dict_name, line_num in locations:
                rel_path = Path(file_path).relative_to(self.base_path.parent)
                print(f"      - {rel_path} (القاموس: {dict_name}, السطر: {line_num})")

        if len(sorted_duplicates) > limit:
            print(f"\n... و {len(sorted_duplicates) - limit} زوج مكرر آخر")

    def save_report(self, output_file: str = "duplicate_tests_report.json") -> None:
        """
        Write a JSON report of duplicate key–value pairs and their locations to a file.

        The report contains a "summary" with total unique pairs, number of duplicate pairs, and total occurrences, and a "duplicates" list where each entry includes the key, value, occurrence count, and a list of locations (file path relative to the analyzer's parent base path, dictionary name, and line number).

        Parameters:
            output_file (str): Path to the output JSON file (default: "duplicate_tests_report.json").
        """
        duplicates = self.get_duplicates()

        report = {
            "summary": {
                "total_unique_pairs": len(self.test_pairs),
                "duplicate_pairs": len(duplicates),
                "total_occurrences": sum(len(locs) for locs in duplicates.values()),
            },
            "duplicates": [],
        }

        for (key, value), locations in sorted(duplicates.items(), key=lambda x: len(x[1]), reverse=True):
            report["duplicates"].append(
                {
                    "key": key,
                    "value": value,
                    "count": len(locations),
                    "locations": [
                        {
                            "file": str(Path(fp).relative_to(self.base_path.parent)),
                            "dict_name": dn,
                            "line": ln,
                        }
                        for fp, dn, ln in locations
                    ],
                }
            )

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)

        print(f"\n💾 تم حفظ التقرير في: {output_file}")

    def remove_duplicates_interactive(self) -> None:
        """إزالة المكررات بشكل تفاعلي"""
        duplicates = self.get_duplicates()

        if not duplicates:
            print("✅ لا توجد اختبارات مكررة للإزالة!")
            return

        print("\n" + "=" * 80)
        print("🗑️  وضع إزالة المكررات")
        print("=" * 80)
        print("سيتم الاحتفاظ بأول ظهور لكل زوج وإزالة التكرارات الأخرى")

        response = input("\nهل تريد المتابعة؟ (نعم/لا): ").strip().lower()

        if response not in ["نعم", "yes", "y", "ن"]:
            print("❌ تم الإلغاء")
            return

        # تجميع الأسطر المراد حذفها حسب الملف
        lines_to_remove: Dict[str, Set[int]] = defaultdict(set)

        for (_key, _value), locations in duplicates.items():
            # الاحتفاظ بأول ظهور، حذف الباقي
            for file_path, _dict_name, line_num in locations[1:]:
                lines_to_remove[file_path].add(line_num)

        # إزالة الأسطر من كل ملف
        files_modified = 0
        lines_removed = 0

        for file_path, line_numbers in lines_to_remove.items():
            try:
                lines = self.file_contents[file_path]

                # إنشاء محتوى جديد بدون الأسطر المكررة
                new_lines = []
                for idx, line in enumerate(lines, 1):
                    if idx not in line_numbers:
                        new_lines.append(line)
                    else:
                        lines_removed += 1

                # كتابة الملف المحدث
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(new_lines))
                    if new_lines and not new_lines[-1].endswith("\n"):
                        f.write("\n")

                files_modified += 1
                rel_path = Path(file_path).relative_to(self.base_path.parent)
                print(f"✅ تم تحديث: {rel_path} (حذف {len(line_numbers)} سطر)")

            except Exception as e:
                print(f"❌ خطأ في تحديث {file_path}: {e}")

        print("\n✨ تم الانتهاء!")
        print(f"   - الملفات المعدلة: {files_modified}")
        print(f"   - الأسطر المحذوفة: {lines_removed}")


def main():
    """الدالة الرئيسية"""
    # المسار الأساسي
    base_path = Path(__file__).parent / "tests"

    if not base_path.exists():
        print(f"❌ المسار غير موجود: {base_path}")
        return

    # إنشاء المحلل
    analyzer = DuplicateTestAnalyzer(str(base_path))

    # مسح الملفات
    analyzer.scan_directory()

    # عرض الإحصائيات
    analyzer.print_statistics()

    # عرض المكررات
    analyzer.print_duplicates(limit=30)

    # حفظ التقرير
    analyzer.save_report()

    # سؤال المستخدم عن إزالة المكررات
    print("\n" + "=" * 80)
    response = input("هل تريد إزالة الاختبارات المكررة؟ (نعم/لا): ").strip().lower()

    if response in ["نعم", "yes", "y", "ن"]:
        analyzer.remove_duplicates_interactive()
    else:
        print("✅ تم الاحتفاظ بالملفات كما هي")


if __name__ == "__main__":
    main()
