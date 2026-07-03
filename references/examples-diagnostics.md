# Compiler and Runtime Diagnostic Examples

Use these examples when the tutorial includes copied compiler output, warning blocks, or stack traces.

## Preserve diagnostic text

Keep the diagnostic message unchanged if it comes from the compiler or runtime:

```text
warning: Unused variable
Hint: You can ignore it with an underscore: `_resultado`.
```

Do not rewrite the diagnostic into another language unless the user explicitly asks for that.

## Update only localized identifiers inside snippets

Source diagnostic:

```text
warning: Unused variable
  12 | let message = "hello"
     |     ^^^^^^^ This variable is never used
```

Spanish-localized code snippet:

```text
warning: Unused variable
  12 | let mensaje = "hola"
     |     ^^^^^^^ This variable is never used
```

Change:

- the shown identifier if the code was localized
- the shown source line if it mirrors localized code

Keep:

- `warning: Unused variable`
- `This variable is never used`

## Validation example

For a runnable tutorial:

1. Extract the runnable code block to a temporary project.
2. Compile or run it with the language toolchain.
3. If the failure is due to inconsistent renaming, fix the localization.
4. If the only remaining issues are upstream `TODO`, placeholder, or deliberately pedagogical warnings, report them and stop there.
