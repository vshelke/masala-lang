# masala-language
"masala" programming language. Use "masala" to do everything! (Inspired by [Brainf**k](https://en.wikipedia.org/wiki/Brainfuck)).

# docs

It is yet another array based programming language which includes an array and a pointer.

| command | description                                     |
|---------|-------------------------------------------------|
| masala  | print masala                                    |
| Masala  | increase current pointer by 1                   |
| mAsala  | decrease current pointer by 1                   |
| maSala  | increase value at current pointer by 1          |
| masAla  | decrease value at current pointer by 1          |
| masaLa  | input 1 character at current pointer from STDIN |
| masalA  | output 1 character at current pointer to STDOUT |

# example

##### test.masala

```
masala maSala maSala maSala masalA Masala maSala maSala
maSala masalA Masala masalA Masala maSala masalA
```

##### run

```./masala.py test.masala```

> masala
> 3301
