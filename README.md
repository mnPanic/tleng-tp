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
