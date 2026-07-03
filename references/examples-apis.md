# API and Keyword Preservation Examples

Use these examples to separate tutorial-owned identifiers from language-owned syntax and APIs.

## Python

Source:

```python
result = json.loads(payload)
print(result)
```

Valid localization:

```python
resultado = json.loads(payload)
print(resultado)
```

Do not translate:

- `json.loads`
- `print`

## Java

Source:

```java
List<String> names = Arrays.asList("Alice", "Bob");
System.out.println(names);
```

Valid localization:

```java
List<String> nombres = Arrays.asList("Alice", "Bob");
System.out.println(nombres);
```

Do not translate:

- `List`
- `String`
- `Arrays.asList`
- `System.out.println`

## Go

Source:

```go
result := strings.TrimSpace(input)
fmt.Println(result)
```

Valid localization:

```go
resultado := strings.TrimSpace(input)
fmt.Println(resultado)
```

Do not translate:

- `strings.TrimSpace`
- `fmt.Println`
- language keywords such as `package`, `func`, `var`, `return`

## Commands and project names

Source:

```sh
tool new my_project
cd my_project
```

Spanish localization:

```sh
tool new mi_proyecto
cd mi_proyecto
```

Translate the project name. Do not translate the command name.
