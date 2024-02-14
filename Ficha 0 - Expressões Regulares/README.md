```
+  <=> 1..N
*  <=> 0..N
```
\
**Exercício 1**
```
1 - O vazio, ou a sequência de um ou mais caractéres entre "a escolha" de 'a' ou 'b'.

    1. E
    1. a
    1. b
    1. aa
    1. bb
    1. ab
    1. (a..a)b
    1. a(b..b)
    1. (ab..ab..ab)
```
```
2 - Uma sequência de um ou mais caractéres 'a', ou a palavra vazia.

    2. a
    2. aa
    2. a..a
    2. E
```
```
3 - A sequência dos caractéres 'ab' pelo menos uma vez, podendo ser repetidos N vezes,
   e a opcionalidade do aparecimento de um ou mais caractéres 'a'.

    3. ab
    3. (ab..ab)
    3. (ab)a
    3. ab(a..a)
    3. (ab..ab)a
    3. (ab..ab)(a..a)
```
```
4 - O aparecimento do caractér 'a', seguido do caractér 'b', sendo que, pelo meio,
   podemos encontrar a sequência, arbitraria, entre 'a' e 'b', uma ou mais vezes.

    4. ab
    4. a(a)b
    4. a(b)b
    4. a(a..a)b
    4. a(b..b)b
    4. a(ab)b
    4. a(ba)b
    4. a(ab..ab)b
    4. a(ba..ba)b
    4. a(baa..bba)b
```
```
5 - O aparecimento do caractér 'a', pelo menos uma vez, seguido da possibilidade
   do aparecimento do caractér 'b' N vezes.

    5. a
    5. aa
    5. ab
    5. a..ab
    5. a..ab..b
    5. ab..b
```
\
\
**Exercício 2**
```
1 -
    1. ba
```
```
2 -
    2. c
```
```
3 -
    3. bc
```
\
\
\
```| <=> ou```\
\
\
**Exercício 3**
```
 ________________________________
|             |                  |
|     ER      |      Captura     |
|_____________|__________________|
|    (ab)+    |       abab       |
|             |                  |
|     c       |        c         |
|             |                  |
|   (d|fe+b)* |      feebd       |
|             |                  |
|     a       |        a         |
|_____________|__________________|
```
