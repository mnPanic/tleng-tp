# tleng-tp
TP de Teoría de Lenguajes - DC UBA

## Reescritura

Pasamos de

```text
E -> E E
  | E | E
  | E *
  | E +
  | E ?
  | ( E )
  | caracter
  | .
```

a

```text
E -> E|C | C
C -> CU | U
U -> A* | A+ | A? | A
A -> . | char | (E)
```

Nota:

- Para usar * escapealo

  ```
  python3 main.py test.txt .\*
  ```

TODO:

- "(a|a|b|b)" no simplifica? deberia ser "(a|a|b)"

Consultas:

- `.` es cualquier caracter o solamente los especificados en el enunciado?

- AFD vs AFND, está bien haber hecho AFD directo?
