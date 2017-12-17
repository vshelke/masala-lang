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
| masaLa  | input 1 number at current pointer from STDIN    |
| masalA  | output 1 number at current pointer to STDOUT    |
| maSAla  | output 1 ASCII at current pointer to STDOUT     |


# example

##### io.masala

```
masaLa Masala masaLa Masala masaLa Masala masaLa Masala masaLa Masala
masaLa Masala masaLa Masala masaLa Masala masaLa Masala masaLa Masala
maSAla mAsala maSAla mAsala maSAla mAsala maSAla mAsala maSAla mAsala
maSAla mAsala maSAla mAsala maSAla mAsala maSAla mAsala maSAla mAsala
maSAla mAsala
```

##### run

```
./masala.py io.masala
```

| input       | output               |
|-------------|----------------------|
| helloworld  | dlrowolleh           |


```
./masala.py masala.masala
```

| input       | output               |
|-------------|----------------------|
|             | masala               |
