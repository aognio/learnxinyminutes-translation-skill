---
name: learnxinyminutes-translations
description: Localize Learn X in Y Minutes tutorial files with consistent terminology, code-aware translations, and validation. Use when Codex needs to translate or review tutorial Markdown files that embed source code, comments, compiler output, or example commands, especially when identifiers, sample values, and localized prose must be adapted without changing language keywords or APIs.
---

# Learnxinyminutes Translations

## Overview

Localize tutorial prose and embedded code examples without breaking the tutorial.
Translate human-facing content aggressively, but preserve executable semantics.

Read `references/translation-rules.md` before editing when the file contains code examples, compiler diagnostics, or localized identifiers.
Read `references/examples-identifiers.md`, `references/examples-apis.md`, and `references/examples-diagnostics.md` when you need concrete examples of safe translation patterns.
Use `scripts/extract_markdown_code_block.py` when you need to extract a specific fenced code block by position for compilation or execution.

## Workflow

1. Inspect the source tutorial and identify:
   - prose and comments
   - code identifiers
   - language keywords and standard APIs
   - compiler/runtime output blocks
   - example commands, file names, and project names
2. Translate prose, comments, and custom identifiers into the target language.
3. Keep language keywords, standard library APIs, and tool/module names unchanged.
4. Update example values and names consistently across code, comments, and sample outputs.
5. Audit for leakage from another target language.
6. If the tutorial contains runnable code, extract the relevant code block and compile or run it.

## Rules

- Translate comments and explanatory prose completely.
- Translate custom variable names, function names, type names, labels, and example literals when they are tutorial-owned rather than language-owned.
- Keep only keywords, built-in syntax, module paths, standard APIs, and required tool names unchanged.
- Use ASCII-only identifiers unless the user explicitly asks otherwise.
- Keep compiler diagnostics in their original language. If a diagnostic block includes a source line, update only the shown identifier names so they match the localized code.
- Keep sample code internally consistent: if one identifier changes, update every reference.
- Do not let one target language leak into another. Re-audit localized files for foreign words before finishing.
- Preserve pedagogical intent. Warnings and `todo` examples that already exist upstream should remain unless the user asks to change them.

## Validation

- Extract the relevant code block into a temporary project when the tutorial is runnable.
- Run the language toolchain if available.
- Treat compile failures caused by inconsistent renames as localization bugs and fix them before finishing.
- Report warnings separately from errors. If warnings already exist in the upstream tutorial, note that rather than rewriting the lesson.

## Notes

- For Learn X in Y Minutes Markdown files, the first fenced block often contains the main runnable tutorial program.
- Some articles contain multiple fenced blocks. Do not assume the first one is always the runnable program.
- Prefer small, surgical edits over paraphrasing the whole tutorial.
- Translate example project names and folder names when they are tutorial-owned, but do not translate the tool command that creates them.
