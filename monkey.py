import os
import subprocess
from pathlib import Path
from tqdm import tqdm
import sqlite3

SRC_DIR = Path(__file__).parent / "src"
OUT_DIR = Path(__file__).parent / "src_new"
OUT_DIR.mkdir(exist_ok=True)


def iter_modules(src_dir: Path):
    """Yield all Python modules inside src_dir as dotted import paths."""
    all_files = []
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".py"):
                full_path = Path(root) / file
                rel_path = full_path.relative_to(src_dir)
                module = str(rel_path.with_suffix("")).replace(os.sep, ".")
                all_files.append(module)
    return all_files


modules = subprocess.check_output(["monkeytype", "list-modules"], text=True, encoding="utf-8").splitlines()
# modules = iter_modules(SRC_DIR)


DB_PATH = Path(__file__).parent / "monkeytype.sqlite3"

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT module FROM monkeytype_call_traces ORDER BY module;")
    modulesx = [row[0] for row in cursor.fetchall()]

print(f"len of sql modules: {len(modulesx)}")
print(f"len of modules: {len(modules)}")

for module in tqdm(modules):
    module = module.strip()
    print(module)

    if not module:
        continue

    try:
        result = subprocess.check_output(
            ["python", "-m", "monkeytype", "apply", module, "--ignore-existing-annotations"],
            text=True,
            encoding="utf-8",
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        print(f"Failed on {module}: {e.output}")
