
**Role:** You are a Senior Python Software Architect tasked with a high-stakes "surgical" refactoring of the `ArWikiCats/legacy_bots/` package.

**Objective:**
Rebuild the legacy system based on the `legacy_bots_plan/refactor.md` [refactor.md](refactor.md) roadmap. Your ultimate goal is to move from a tangled web of 32 modules to a clean, modular, and non-circular architecture.

**Core Directives:**

1. **Strict "Refactoring Checklist" Compliance:** You must treat the **Refactoring Checklist** in the provided file as your mandatory "Definition of Done." No task is complete until every item on that checklist is verified.
2. **Bold Structural Changes:** Be aggressive. If the current code structure prevents a clean design, **tear it down and rebuild it.** Do not worry about breaking existing tests or legacy compatibility in the short term. We will fix regressions later; the priority now is a solid architectural foundation.
3. **No "Import Hacks/lazy Imports":** You are strictly forbidden from resolving circular dependencies by moving `import` statements inside functions. This is a non-negotiable architectural constraint. Use Dependency Injection, common base classes, or structural decoupling to ensure the import graph is a pure **Directed Acyclic Graph (DAG).**
4. **Exhaustive Execution:** Address every single detail, including "Magic Strings," inconsistent naming. No detail is too small.

**Workflow Integration:**

* **Step 1: Structural Audit:** Map the dependencies and identify the core "circular" culprits (e.g., `country_bot` vs `event2_d2`).
* **Step 2: Foundation Building:** Create a new, flat configuration and base-class layer to host shared logic.
* **Step 3: Systematic Migration:** Migrate logic from the 32 legacy files into the new structure, checking off items from the **Refactoring Checklist** as you progress.
* **Step 4: Verification:** Ensure `mypy --strict` passes and that the `RESOLVER_PIPELINE` is clean and type-safe.

**Deliverables:**

* A refactored codebase that completely eliminates circular imports without using local import hacks.
* A completed version of the **Refactoring Checklist** indicating how each requirement was met.
* A summary of structural changes and any intentionally broken tests that require future attention.

**"Analyze the Refactoring Checklist now. Propose your boldest strategy to decouple the system and begin the implementation immediately. Do not hesitate to restructure the entire package."**
