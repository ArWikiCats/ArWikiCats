#!/usr/bin/env python3
"""Automatic type hint injector for the codebase."""
from __future__ import annotations

import argparse
import ast
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

import libcst as cst
from libcst import matchers as m


SKIP_DIRS = {"venv", ".venv", "migrations", "__pycache__", ".pytest_cache"}


@dataclass
class FileSummary:
    file: str
    functions_updated: int = 0
    classes_updated: int = 0
    functions_skipped: int = 0

    def to_dict(self) -> Dict[str, int | str]:
        return {
            "file": self.file,
            "functions_updated": self.functions_updated,
            "classes_updated": self.classes_updated,
            "functions_skipped": self.functions_skipped,
        }


def _canonicalize_type_string(value: str) -> str:
    value = value.strip()
    value = value.replace("typing.", "")
    if value.endswith("?"):
        base = _canonicalize_type_string(value[:-1])
        return f"{base} | None"
    # Normalise Optional/Union forms to ``| None`` syntax.
    optional_match = re.fullmatch(r"Optional\[(.*)]", value)
    if optional_match:
        inner = _canonicalize_type_string(optional_match.group(1))
        return f"{inner} | None"
    union_match = re.fullmatch(r"Union\[(.*)]", value)
    if union_match:
        parts = [part.strip() for part in union_match.group(1).split(",")]
        cleaned = [_canonicalize_type_string(part) for part in parts]
        return " | ".join(cleaned)

    replacements = {
        "List": "list",
        "Tuple": "tuple",
        "Dict": "dict",
        "Set": "set",
        "Sequence": "Sequence",
        "Iterable": "Iterable",
        "Boolean": "bool",
        "Integer": "int",
        "Float": "float",
        "String": "str",
        "NoneType": "None",
    }
    for original, replacement in replacements.items():
        value = re.sub(rf"\b{original}\b", replacement, value)

    # Replace textual " or None" with union syntax.
    value = re.sub(r"\bor None\b", "| None", value)
    value = re.sub(r"\bor bool\b", "| bool", value)

    return value


def _get_docstring(func: cst.FunctionDef) -> Optional[str]:
    if not func.body.body:
        return None
    first = func.body.body[0]
    if not isinstance(first, cst.SimpleStatementLine):
        return None
    if len(first.body) != 1:
        return None
    expr = first.body[0]
    if not isinstance(expr, cst.Expr):
        return None
    value = expr.value
    if not isinstance(value, cst.SimpleString):
        return None
    try:
        return ast.literal_eval(value.value)
    except (ValueError, SyntaxError):
        return None


def _parse_docstring_types(func: cst.FunctionDef) -> Tuple[Dict[str, str], Optional[str]]:
    docstring = _get_docstring(func)
    if not docstring:
        return {}, None

    param_types: Dict[str, str] = {}
    return_type: Optional[str] = None
    section: Optional[str] = None

    for line in docstring.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        lower = stripped.lower()
        if lower in {"args:", "arguments:", "parameters:"}:
            section = "params"
            continue
        if lower in {"returns:", "return:"}:
            section = "returns"
            continue

        if section == "params":
            match = re.match(r"(\w+)\s*\(([^)]+)\):", stripped)
            if match:
                name, type_part = match.groups()
                param_types[name] = _canonicalize_type_string(type_part)
                continue
            match = re.match(r"(\w+)\s*:\s*([^\s-]+)", stripped)
            if match:
                name, type_part = match.groups()
                param_types[name] = _canonicalize_type_string(type_part)
                continue
        elif section == "returns" and return_type is None:
            match = re.match(r"([^:\s]+)", stripped)
            if match:
                return_type = _canonicalize_type_string(match.group(1))

    return param_types, return_type


def _infer_literal_type(expr: cst.BaseExpression | None) -> Optional[str]:
    if expr is None:
        return None
    if isinstance(expr, cst.SimpleString):
        return "str"
    if isinstance(expr, cst.Integer):
        return "int"
    if isinstance(expr, cst.Float):
        return "float"
    if isinstance(expr, cst.Imaginary):
        return "complex"
    if isinstance(expr, cst.Name):
        if expr.value in {"True", "False"}:
            return "bool"
        if expr.value == "None":
            return "None"
    if isinstance(expr, cst.List):
        element_types: Set[str] = set()
        for element in expr.elements:
            if element is None or element.value is None:
                continue
            element_type = _infer_literal_type(element.value)
            if element_type is None:
                return "list[Any]"
            element_types.add(element_type)
        if not element_types:
            return "list[Any]"
        if len(element_types) == 1:
            inner = next(iter(element_types))
            return f"list[{inner}]"
        if "None" in element_types:
            element_types.discard("None")
            if len(element_types) == 1:
                inner = next(iter(element_types))
                return f"list[{inner} | None]"
        return "list[Any]"
    if isinstance(expr, cst.Tuple):
        element_types: List[str] = []
        for element in expr.elements:
            if element is None or element.value is None:
                element_types.append("Any")
            else:
                element_type = _infer_literal_type(element.value)
                element_types.append(element_type or "Any")
        joined = ", ".join(element_types) if element_types else "Any"
        return f"tuple[{joined}]"
    if isinstance(expr, cst.Dict):
        key_types: Set[str] = set()
        value_types: Set[str] = set()
        for element in expr.elements:
            if element is None:
                continue
            key_type = _infer_literal_type(element.key)
            value_type = _infer_literal_type(element.value)
            if key_type is None:
                key_types.add("Any")
            else:
                key_types.add(key_type)
            if value_type is None:
                value_types.add("Any")
            else:
                value_types.add(value_type)
        key = next(iter(key_types)) if len(key_types) == 1 else "Any"
        value = next(iter(value_types)) if len(value_types) == 1 else "Any"
        return f"dict[{key}, {value}]"
    if isinstance(expr, cst.Set):
        element_types: Set[str] = set()
        for element in expr.elements:
            if element is None:
                continue
            element_type = _infer_literal_type(element.value)
            if element_type is None:
                return "set[Any]"
            element_types.add(element_type)
        if not element_types:
            return "set[Any]"
        if len(element_types) == 1:
            return f"set[{next(iter(element_types))}]"
        return "set[Any]"
    if isinstance(expr, cst.Call):
        func = expr.func
        if isinstance(func, cst.Name):
            if func.value in {"list", "set", "dict", "tuple"}:
                return f"{func.value}[Any]"
    return None


def _combine_optional(base: Optional[str], allow_none: bool) -> Optional[str]:
    if not allow_none:
        return base
    if base is None or base == "Any":
        return "Any | None"
    if base.endswith("| None") or "| None" in base:
        return base
    return f"{base} | None"


class _ReturnCollector(cst.CSTVisitor):
    def __init__(self) -> None:
        self.types: Set[str] = set()
        self.unknown = False

    def visit_Return(self, node: cst.Return) -> Optional[bool]:
        if node.value is None:
            self.types.add("None")
            return None
        inferred = _infer_literal_type(node.value)
        if inferred is None:
            self.unknown = True
        else:
            self.types.add(inferred)
        return None


class TypeHintAdder(cst.CSTTransformer):
    """CST transformer that injects type annotations where missing."""

    def __init__(self) -> None:
        super().__init__()
        self.any_import_needed = False
        self._typing_imports_any = False
        self._class_stack: List[bool] = []
        self._class_changed_stack: List[bool] = []
        self._function_stack: List[bool] = []
        self.functions_updated = 0
        self.functions_skipped = 0
        self.classes_updated = 0

    # ------------------------------------------------------------------
    # Helper utilities
    # ------------------------------------------------------------------
    def _annotation_from_string(self, type_str: str) -> cst.Annotation:
        if re.search(r"\bAny\b", type_str):
            self.any_import_needed = True
        return cst.Annotation(annotation=cst.parse_expression(type_str))

    def _annotate_param(
        self, param: cst.Param, doc_types: Dict[str, str]
    ) -> tuple[cst.Param, bool]:
        if param.annotation is not None:
            return param, False
        name = param.name.value
        if name in {"self", "cls"}:
            return param, False

        inferred: Optional[str] = None
        doc_type = doc_types.get(name)
        if doc_type:
            inferred = doc_type
        default = getattr(param, "default", None)
        if inferred is None and default is not None:
            default_type = _infer_literal_type(default)
            if default_type == "None":
                inferred = _combine_optional(doc_type, True) or "Any | None"
            elif default_type is not None:
                inferred = default_type
        if inferred is None:
            inferred = doc_type
        if inferred is None:
            inferred = "Any"
        annotation = self._annotation_from_string(inferred)
        annotated_param = param.with_changes(annotation=annotation)
        return annotated_param, True

    def _updated_params(
        self, params: cst.Parameters, doc_types: Dict[str, str]
    ) -> tuple[cst.Parameters, bool]:
        modified = False

        def process_param_list(items: Iterable[cst.Param]) -> List[cst.Param]:
            nonlocal modified
            new_items: List[cst.Param] = []
            for item in items:
                new_item, changed = self._annotate_param(item, doc_types)
                if changed:
                    modified = True
                new_items.append(new_item)
            return new_items

        posonly = process_param_list(params.posonly_params)
        positional = process_param_list(params.params)
        kwonly = process_param_list(params.kwonly_params)

        star_arg = params.star_arg
        if isinstance(star_arg, cst.Param):
            new_star_arg, changed = self._annotate_param(star_arg, doc_types)
            if changed:
                modified = True
            star_arg = new_star_arg

        star_kwarg = params.star_kwarg
        if isinstance(star_kwarg, cst.Param):
            new_star_kwarg, changed = self._annotate_param(star_kwarg, doc_types)
            if changed:
                modified = True
            star_kwarg = new_star_kwarg

        if not modified:
            return params, False

        updated_params = params.with_changes(
            posonly_params=tuple(posonly),
            params=tuple(positional),
            kwonly_params=tuple(kwonly),
            star_arg=star_arg,
            star_kwarg=star_kwarg,
        )
        return updated_params, True

    def _infer_return_annotation(
        self, original_node: cst.FunctionDef, doc_return: Optional[str]
    ) -> Optional[cst.Annotation]:
        if doc_return:
            return self._annotation_from_string(doc_return)

        collector = _ReturnCollector()
        original_node.body.visit(collector)
        if collector.unknown:
            return None
        if not collector.types:
            return None
        types = set(collector.types)
        allow_none = "None" in types
        types.discard("None")
        if not types:
            return self._annotation_from_string("None")
        if len(types) == 1:
            base = next(iter(types))
            annotated = _combine_optional(base, allow_none)
            if annotated is None:
                return None
            return self._annotation_from_string(annotated)
        return None

    # ------------------------------------------------------------------
    # Visitor overrides
    # ------------------------------------------------------------------
    def visit_Module(self, node: cst.Module) -> Optional[bool]:
        for statement in node.body:
            if not isinstance(statement, cst.SimpleStatementLine):
                continue
            for small in statement.body:
                if not isinstance(small, cst.ImportFrom):
                    continue
                module = small.module
                if module is None:
                    continue
                if not isinstance(module, cst.Name) or module.value != "typing":
                    continue
                names = small.names
                if isinstance(names, cst.ImportStar):
                    self._typing_imports_any = True
                    continue
                if isinstance(names, tuple):
                    for alias in names:
                        name_node = alias.name
                        if isinstance(name_node, cst.Name) and name_node.value == "Any":
                            self._typing_imports_any = True
        return None

    def visit_ClassDef(self, node: cst.ClassDef) -> Optional[bool]:
        self._class_stack.append(True)
        self._class_changed_stack.append(False)
        return None

    def visit_FunctionDef(self, node: cst.FunctionDef) -> Optional[bool]:
        self._function_stack.append(True)
        return None

    def leave_ClassDef(
        self, original_node: cst.ClassDef, updated_node: cst.ClassDef
    ) -> cst.BaseStatement:
        self._class_stack.pop()
        changed = self._class_changed_stack.pop()
        if changed:
            self.classes_updated += 1
        return updated_node

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        self._function_stack.pop()
        doc_types, doc_return = _parse_docstring_types(original_node)
        params, params_changed = self._updated_params(updated_node.params, doc_types)

        returns = updated_node.returns
        returns_changed = False
        if returns is None:
            if original_node.name.value == "__init__":
                returns = self._annotation_from_string("None")
                returns_changed = True
            else:
                inferred = self._infer_return_annotation(original_node, doc_return)
                if inferred is not None:
                    returns = inferred
                    returns_changed = True
                elif doc_return:
                    returns = self._annotation_from_string(doc_return)
                    returns_changed = True
                else:
                    returns = self._annotation_from_string("Any")
                    returns_changed = True

        if params_changed or returns_changed:
            self.functions_updated += 1
            updated_node = updated_node.with_changes(params=params, returns=returns)
        else:
            self.functions_skipped += 1

        return updated_node

    def leave_Assign(
        self, original_node: cst.Assign, updated_node: cst.Assign
    ) -> cst.BaseSmallStatement:
        if not self._class_stack or self._function_stack:
            return updated_node
        if len(updated_node.targets) != 1:
            return updated_node
        target = updated_node.targets[0].target
        if not isinstance(target, cst.Name):
            return updated_node
        inferred = _infer_literal_type(updated_node.value)
        if inferred == "None":
            inferred = "Any | None"
        if inferred is None:
            inferred = "Any"
        annotation = self._annotation_from_string(inferred)
        self._class_changed_stack[-1] = True
        return cst.AnnAssign(target=target, annotation=annotation, value=updated_node.value)

    def leave_Module(self, original_node: cst.Module, updated_node: cst.Module) -> cst.Module:
        if not self.any_import_needed or self._typing_imports_any:
            return updated_node

        body: List[cst.CSTNode] = list(updated_node.body)
        typing_import_index: Optional[int] = None

        for idx, statement in enumerate(body):
            if not isinstance(statement, cst.SimpleStatementLine):
                continue
            if len(statement.body) != 1:
                continue
            small = statement.body[0]
            if not isinstance(small, cst.ImportFrom):
                continue
            module = small.module
            if module is None or not isinstance(module, cst.Name) or module.value != "typing":
                continue
            names = small.names
            if isinstance(names, cst.ImportStar):
                self._typing_imports_any = True
                return updated_node
            if isinstance(names, tuple):
                existing = list(names)
                if any(
                    isinstance(alias.name, cst.Name) and alias.name.value == "Any"
                    for alias in existing
                ):
                    self._typing_imports_any = True
                    return updated_node
                existing.append(cst.ImportAlias(name=cst.Name("Any")))
                new_small = small.with_changes(names=tuple(existing))
                body[idx] = statement.with_changes(body=[new_small])
                self._typing_imports_any = True
                return updated_node.with_changes(body=tuple(body))

        insert_index = 0
        if body and m.matches(body[0], m.SimpleStatementLine(body=[m.Expr(value=m.SimpleString())])):
            insert_index = 1

        while insert_index < len(body):
            stmt = body[insert_index]
            if isinstance(stmt, cst.SimpleStatementLine) and len(stmt.body) == 1:
                small = stmt.body[0]
                if isinstance(small, cst.ImportFrom):
                    module = small.module
                    if module is not None and isinstance(module, cst.Name) and module.value == "__future__":
                        insert_index += 1
                        continue
            break

        typing_import = cst.SimpleStatementLine(
            body=[
                cst.ImportFrom(
                    module=cst.Name("typing"),
                    names=[cst.ImportAlias(name=cst.Name("Any"))],
                )
            ]
        )
        body.insert(insert_index, typing_import)
        self._typing_imports_any = True
        return updated_node.with_changes(body=tuple(body))


# ----------------------------------------------------------------------
# Utility functions
# ----------------------------------------------------------------------

def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def collect_python_files(root: Path) -> List[Path]:
    files: List[Path] = []
    for path in root.rglob("*.py"):
        if should_skip(path):
            continue
        files.append(path)
    return files


def process_file(path: Path, apply: bool) -> Optional[FileSummary]:
    source = path.read_text(encoding="utf-8")
    try:
        module = cst.parse_module(source)
    except cst.ParserSyntaxError:
        return None

    transformer = TypeHintAdder()
    modified_module = module.visit(transformer)

    if module.code == modified_module.code:
        return None

    if apply:
        path.write_text(modified_module.code, encoding="utf-8")

    summary = FileSummary(
        file=str(path),
        functions_updated=transformer.functions_updated,
        classes_updated=transformer.classes_updated,
        functions_skipped=transformer.functions_skipped,
    )
    return summary


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Automatically add type hints to Python files.")
    parser.add_argument("paths", nargs="*", default=["src"], help="Paths to scan for Python files")
    parser.add_argument("--apply", action="store_true", help="Persist changes to disk")
    args = parser.parse_args(argv)

    summaries: List[Dict[str, int | str]] = []

    for path_str in args.paths:
        root = Path(path_str)
        if root.is_file() and root.suffix == ".py":
            paths = [root]
        else:
            paths = collect_python_files(root)
        for path in sorted(paths):
            summary = process_file(path, apply=args.apply)
            if summary is not None:
                summaries.append(summary.to_dict())

    output = json.dumps(summaries, indent=2)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
