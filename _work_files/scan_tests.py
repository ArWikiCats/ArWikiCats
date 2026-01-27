import ast
from pathlib import Path

TARGETS = {
    "from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test": [
        "dump_diff",
        "dump_same_and_not_same",
        "one_dump_test",
    ],
    # Add more rules here:
    # "from x import a, b, c": ["a", "b", "c"],
}


class ImportUsageVisitor(ast.NodeVisitor):
    def __init__(self):
        self.used_names = set()

    def visit_Name(self, node):
        self.used_names.add(node.id)
        self.generic_visit(node)


def get_used_names(filepath: Path) -> set:
    tree = ast.parse(filepath.read_text(encoding="utf-8"))
    visitor = ImportUsageVisitor()
    visitor.visit(tree)
    return visitor.used_names


def clean_file(filepath: Path, used_names: set):
    lines = filepath.read_text(encoding="utf-8").splitlines()
    new_lines = []
    changed = False

    for line in lines:
        stripped = line.strip()
        if stripped in TARGETS:
            names = set(TARGETS[stripped])
            if not (names & used_names):
                changed = True
                print(f"Removed: {filepath} -> {stripped}")
                continue
        new_lines.append(line)

    if changed:
        filepath.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def main():
    tests_dir = Path(__file__).parent.parent / "tests"
    for file in tests_dir.rglob("*.py"):
        try:
            if not get_used_names(file):
                clean_file(file)
        except Exception as e:
            print(f"Skipped (parse error): {file} -> {e}")


if __name__ == "__main__":
    main()
