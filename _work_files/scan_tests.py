import ast
from pathlib import Path

TARGET_MODULE = "load_one_data"
TARGET_NAMES = {"dump_diff", "dump_same_and_not_same", "one_dump_test"}


class ImportUsageVisitor(ast.NodeVisitor):
    def __init__(self):
        self.used_names = set()

    def visit_Name(self, node):
        self.used_names.add(node.id)
        self.generic_visit(node)


def file_uses_any_target(filepath: Path) -> bool:
    tree = ast.parse(filepath.read_text(encoding="utf-8"))
    visitor = ImportUsageVisitor()
    visitor.visit(tree)
    return bool(TARGET_NAMES & visitor.used_names)


def clean_file(filepath: Path):
    lines = filepath.read_text(encoding="utf-8").splitlines()
    new_lines = []

    removed = False
    for line in lines:
        if line.strip() == (
            "from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test"
        ):
            removed = True
            continue
        new_lines.append(line)

    if removed:
        filepath.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        print(f"Cleaned: {filepath}")


def main():
    tests_dir = Path(__file__).parent.parent / "tests"
    for file in tests_dir.rglob("*.py"):
        try:
            if not file_uses_any_target(file):
                clean_file(file)
        except Exception as e:
            print(f"Skipped (parse error): {file} -> {e}")


if __name__ == "__main__":
    main()
