# Trabajo Práctico - Teoría de Lenguajes

<!-- 
• Las modificaciones a la gramática o indicaciones adicionales que hayan sido necesarias para construir el parser.
• Descripción de cómo se implementó la solución.
• Información y requerimientos de software para ejecutar y recompilar el TP (versiones de compiladores, herramientas, plataforma, etc).
• Casos de prueba con expresiones sintácticamente correctas e incorrectas, resultados obtenidos y conclusiones.
-->

## Integrantes

| Nombre            | Mail                      | LU     |
| ----------------- | ------------------------- | ------ |
| Diego Senarruzza  | diegosenarruzza@gmail.com | 449/17 |
| Julian Zylber     | jzylber@dc.uba.ar         | 21/18  |
| Manuel Panichelli | panicmanu@gmail.com       | 72/18  |

## Implementación

No hicimos ninguna indicación adicional al parser, sino que modificamos la
gramática para que sea SLR. Pasamos de

<table>
<thead><tr><th>Original</th><th>Cambiada</th></tr></thead>
<tbody>
<tr><td>

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

</td><td>

```text
E -> E|C | C
C -> CU | U
U -> A* | A+ | A? | A
A -> . | char | (E)
```

</td></tr>
</tbody></table>

- Se implementó el lexer y parser con `ply`
- Se modifica la regex `R` para que sea `.*(R).*`
- El parser devuelve un objeto representado de forma estructura la regex provista
- Se realiza la derivación de la regex para construir un AFD (sin estado trampa)
- Se corre el AFD para cada línea para ver si la acepta, y en ese caso se imprime por stdout.

## Ejecutar

Para bajar las dependencias (solo `ply` y `dataclasses`),

```bash
pip3 install -r requirements.txt
```

Para correrlo,

```bash
$ python3 main.py files/telefonos.txt "54 9 11((43)?|(..))(43)+"
54 9 1156434343
54 9 1178434343
54 9 117843434343
```

Para ejecutar los tests,

```bash
$ python3 tests.py
.
----------------------------------------------------------------------
Ran 1 test in 1.107s

OK
```

## Casos de prueba

Para el siguiente archivo,

```text
# grep/files/telefonos.txt
54 9 1117428196
54 9 1156434343
54 9 1178434343
54 9 117843434343
cosas antes 54 9 1117428196 cosas despues
54 9 1112469424
5996714627827
59 9 6714627827
5685784939375769
```

- La regex `"54 9 11........"` da como resultado

  ```text
  54 9 1117428196
  54 9 1156434343
  54 9 1178434343
  54 9 117843434343
  cosas antes 54 9 1117428196 cosas despues
  54 9 1112469424
  ```

- La regex `"54 9 11((43)?|(..))(43)+"` da como resultado

  ```text
  54 9 1156434343
  54 9 1178434343
  54 9 117843434343
  ```

## Consultas

- `.` es cualquier caracter o solamente los especificados en el enunciado?

- AFD vs AFND, está bien haber hecho AFD directo?
