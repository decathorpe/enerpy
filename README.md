# enerpy

enerpy is a python package for gaussian error propagation.

## Usage

- If you want all and everything contained within the enerpy namespace, do:

`import enerpy`

- If you want to use all functions without namespace (beware name collisions), do:

```python3
from enerpy.funcs import *
from enerpy.funcs_list import *
```

## API Introduction

Everything is an object (TM). The basic types are `Num`, `Fnc`, `NumList` and `ListFnc`.

### `Num`

Arguments to functions are automatically coerced into the internal `Num` object, per default with Standard Error of 0. Initialising a `Num` object manually is done like this:

```python3
num1 = Num()      # "uninitialised" number object
num1.val = 3      # manually setting num1's value
num1.var = 1      # manually setting num1's variance

num2 = Num(0, 0)  # number object, initialised with value and standard error of 0
```

`Num` objects can be printed simply by invoking the `.print()` method on them.
Evaluating a `Num` object is possible but returns only the object itself.

### `NumList`

A `NumList` is initialised with a list of numbers or a list of `Num` objects. A `NumList` object cannot be evaluated with `.eval()`, it can only be condensed into a `Num` object using the `.condense()` method, where the value of the returned `Num` is the mean of the list items and its standard error is the standard error of the mean.

`NumList`s can also be printed by using the `.print()` method on the object. This prints the items of the `NumList`, together with indices.

```python3
nlist1 = NumList([1, 2, 10, Num(19, 2.2), 11.1, Num(10, 1.2)])
nlist1.append(Num(22, 2.1))
nlist1_mean = nlist1.condense()
nlist1_mean.print()
# output: 10.72857142857143 +- 2.99466646070716
nlist1.print()

# output:
#0 : 1 +- 0.0
#1 : 2 +- 0.0
#2 : 10 +- 0.0
#3 : 19 +- 2.2
#4 : 11.1 +- 0.0
#5 : 10 +- 1.2
#6 : 22 +- 2.1
```

### `Fnc`

Function objects are initialised with the function argument(s). Some sunctions require two arguments, some only accept one argument, and a few work with one argument but two arguments can be specified. More than two arguments are not supported.

```python3
addobj = Add(Num(2, 1), Num(3, 1))
numobj = addobj.eval()
numobj.print()
# output: 5 +- 1.4142135623731
```

Functions are only evaluated if you explicitly tell them to. Evaluating a function is done with the `.eval()` method - this returns a `Num` object, which then can be printed.

Nested functions are supported and are evaluated recursively, bottom up (inside out, depending on the perspective). The following example calculates a simple Boltzmann factor (`Rgas` is taken from wikipedia).

```python3
deltaH = Num(2024.13, 0.25)
Rgas = Num(8.3144621, 0.0000075)
Temp = Num(300, 1)

Exp(Div(deltaH, Mul(Rgas, Temp))).eval().print()
# output: 2.25125909455595 +- 0.00609375728259
```
