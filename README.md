enerpy
======

enerpy is a python package for gaussian error propagation.

Usage:
------

- If you want all and everything contained within the enerpy namespace, do:
`import enerpy`

- If you want to use all functions without namespace (beware name collisions), do:
`from enerpy.functions import *`


Basic API:
----------

Everything is an object (TM).

Functions are only evaluated if you explicitly tell them to. `Add(num1, num2)` only creates an `Add` Function object with arguments `num1` and `num2`.

Evaluating a `Fnc` object is done with the `.eval()` method and returns a `Num` object.

Printing a `Num` object is done with the `.print()` method and prints value and the calculated standard error.


Example:
--------

This example calculates a simple Boltzmann factor (`Rgas` is taken from wikipedia).

```
deltaH = Num(2024.13, 0.25)
Rgas = Num(8.3144621, 0.0000075)
Temp = Num(300, 1)

Exp(Div(deltaH, Mul(Rgas, Temp))).eval().print()
```
