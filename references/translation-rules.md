# Translation Rules

## Preserve

- Language keywords
- Standard library APIs
- Official module paths
- Required command names such as `gleam`
- Compiler diagnostic text

## Translate

- Tutorial prose
- Comments
- User-defined identifiers
- Example project names
- Example data values when they are part of the teaching narrative

## Compiler Diagnostics

- Keep messages like `warning: Unused variable`, `Expected type`, and `Found type` unchanged.
- Update only the identifier shown inside the diagnostic source snippet when the localized code renamed it.

## Cross-Language Audit

Before finishing a non-English translation:

1. Search for obvious foreign-language residue from earlier passes.
2. Check renamed identifiers, especially:
   - numeric variables
   - tuple/point/list helpers
   - closure and decorator examples
   - dictionary and binary-data examples
3. Re-run the example if the language toolchain is available.
