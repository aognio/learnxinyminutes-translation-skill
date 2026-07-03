# Learn X in Y Minutes Translations Skill

This skill provides rules, guidelines, and utilities for localizing "Learn X in Y Minutes" tutorial files safely. It is designed to ensure that tutorial prose is translated correctly while maintaining the correctness of embedded code, language keywords, standard library APIs, and compiler outputs.

## Directory Structure

The skill is organized as follows:

*   `SKILL.md`: The main entry point for the skill, outlining the overview, workflow, and validation rules.
*   `agents/`:
    *   `openai.yaml`: Configuration for the translation agent.
*   `references/`:
    *   `translation-rules.md`: Key translation rules (what to preserve, what to translate).
    *   `examples-identifiers.md`: Concrete examples of identifier translation across languages.
    *   `examples-apis.md`: Examples of API and keyword preservation.
    *   `examples-diagnostics.md`: Rules for maintaining compiler diagnostics.
*   `scripts/`:
    *   `extract_markdown_code_block.py`: A Python utility script to extract code blocks from Markdown files for verification.

## Getting Started

### Using the Translation Rules
When translating a tutorial file:
1. Refer to `references/translation-rules.md` to distinguish between prose to translate and code to preserve.
2. See the files in `references/` for language-specific examples (Go, Python, Java, etc.).

### Using the Extract Script
To extract a code block from a tutorial file for testing or compilation:
```bash
python scripts/extract_markdown_code_block.py <path_to_markdown_file> <block_index> <output_file_path> [--language <lang>]
```
For example, to extract the first Python block:
```bash
python scripts/extract_markdown_code_block.py tutorial.md 0 output.py --language python
```
