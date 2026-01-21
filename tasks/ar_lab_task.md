# AI Agent Work Plan for Refactoring the Category Labeling System
## target file: ArWikiCats/make_bots/ma_bots/ar_lab.py

## 1. Overview

This plan defines a structured workflow for an AI agent responsible for refactoring the current category-label generation module. The goal is to transition from a large, tightly coupled procedural file into a modular, domain-driven architecture composed of small services, clear responsibilities, and testable components.

---

## 2. Objectives

* Reduce code complexity and improve maintainability.
* Eliminate circular imports.
* Introduce clear domain boundaries.
* Increase test coverage and simplify mocking.
* Improve clarity of data flow through dedicated pipelines.
* Enable incremental migration without breaking existing behavior.

---

## 3. High-Level Architecture

The AI agent will reorganize the logic into four primary domains:

### A. Parsing Layer

Responsible for extracting and normalizing:

* `lab_type`
* `country`
* `separator`
* Lowercased representations

### B. lab_type Resolution Layer

Centralizes all type-related logic, including:

* NEW_P17_FINAL
* RELIGIOUS_KEYS_PP
* Players and jobs rules
* Fallback handlers (event2bot, films, nats, etc.)

### C. Country Resolution Layer

Resolves geographic entities via:

* bys
* team_work
* nats
* time_to_arabic
* get_pop_All_18

### D. Label Composition Layer

Responsible for building the final Arabic label using:

* pop_format tables
* ar_separator logic
* Keep_it_first / Keep_it_last
* Formatting rules ("في" / "من" / "حسب")

### E. Pipeline Layer

A single orchestrator that:

1. Parses the input category.
2. Resolves type.
3. Resolves country.
4. Builds the final Arabic label.

---

## 4. Deliverables

### Phase 1: Extraction Without Logic Change

* Copy all functions into new domain modules.
* Replace internal imports accordingly.
* Ensure all tests still pass.

### Phase 2: Parser Implementation

* Create `Parser` class.
* Move `get_type_country` and normalization logic.
* Output a structured `ParsedCategory` dataclass.

### Phase 3: TypeResolver Service

* Implement `TypeResolver.resolve()`.
* Insert all type-lookup rules.
* Apply caching via `@lru_cache`.

### Phase 4: CountryResolver Service

* Implement `CountryResolver.resolve()`.
* Apply all country-labeling logic.
* Add caching.

### Phase 5: LabelBuilder

* Centralize combination logic.
* Create pure functions to ensure testability.
* Add final formatting handlers.

### Phase 6: Pipeline Assembly

* Build `LabelPipeline` class.
* Replace direct dependencies with service composition.
* Introduce integration tests.

### Phase 7: Cleanup & Consolidation

* Remove duplicate logic from old modules.
* Resolve orphan functions.
* Add documentation and diagram.

---

## 5. Execution Flow for the AI Agent

1. Load existing code.
2. Detect domain boundaries automatically.
3. Generate new file structure.
4. Migrate functions incrementally.
5. Ensure import consistency.
6. Apply static analysis (isort, ruff, mypy).
7. Run full pytest suite.
8. Rewrite find_ar_label to use the new pipeline.
9. Optimize caching based on profiling results.

---

## 6. Constraints

* No behavioral changes during Phase 1–4.
* All outputs must be backward-compatible.
* No new dependencies unless approved.
* Use English comments inside code.

---

## 7. Future Enhancements

* Add performance logging hooks.
* Introduce profiling pipelines.
* Generate auto-documentation for all services.
* Add CI checks for architectural rules.

---

## 8. Final Notes

This plan ensures a controlled, safe refactor that preserves existing behavior while creating a long-term maintainable structure. The AI agent can execute tasks step-by-step or batch multiple phases depending on context and available resources.
