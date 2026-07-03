# Identifier Translation Examples

Use these examples when deciding which identifiers to translate and how far the rename must propagate.

## Python

Source:

```python
nephews = ["Huey", "Dewey", "Louie"]
print(nephews[0])
```

Spanish localization:

```python
sobrinos = ["Hugo", "Paco", "Luis"]
print(sobrinos[0])
```

Translate:

- tutorial-owned variable names
- tutorial-owned sample values

Update every later reference.

## Java

Source:

```java
String message = "Original value";
System.out.println(message);
```

Spanish localization:

```java
String mensaje = "Valor original";
System.out.println(mensaje);
```

Translate:

- user-defined variable names
- tutorial-owned string literals

Do not translate:

- `String`
- `System.out.println`

## Go

Source:

```go
count := 3
fmt.Println(count)
```

Spanish localization:

```go
conteo := 3
fmt.Println(conteo)
```

If the file later uses `count`, leaving one old reference behind is a localization bug.

## Cross-language leakage

Bad Italian localization:

```java
String respuesta = "ciao";
```

Correct Italian localization:

```java
String risposta = "ciao";
```

If an Italian or Portuguese file contains a Spanish identifier, or vice versa, treat it as a bug and fix it.
