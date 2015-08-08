# enerpy

enerpy is a python package for gaussian error propagation.

## Usage

- If you want all and everything contained within the enerpy namespace, do:

`import enerpy`

- If you want to use all functions without namespace (beware name collisions), do:

```python
from enerpy.funcs import *
from enerpy.funcs_list import *
```

## API Introduction

Everything is an object (TM). The basic types are `Num`, `Fnc`, `NumList` and `ListFnc`.

### New in Version 0.1.0

Infix operators can now be used for most arithmetic operations supported by python3 itself (not bitwise operators). No more need for nesting `Fnc` objects!

### `Num`

Arguments to functions are automatically coerced into the internal `Num` object, per default with Standard Error of 0. Initialising a `Num` object manually is done like this:

```python
num1 = Num()      # "uninitialised" number object
num1.val = 3      # manually setting num1's value
num1.var = 1      # manually setting num1's variance

num2 = Num(0, 0)  # number object, initialised with value and standard error of 0
```

As of version 0.1.0, a `Num` object can be printed like any other object - or by invoking the `.prnt()` method on it.
Evaluating a `Num` object is possible (for compatibility with other classes) but returns only the object itself.

### `NumList`

A `NumList` is initialised with a list of numbers or a list of `Num` objects. A `NumList` object cannot be evaluated with `.eval()`, it can only be condensed into a `Num` object using the `.condense()` method, where the value of the returned `Num` is the mean of the list items and its standard error is the standard error of the mean.

```python
nlist1 = NumList([1, 2, 10, Num(19, 2.2), 11.1, Num(10, 1.2)])
nlist1.append(Num(22, 2.1))
nlist1_mean = nlist1.condense()
print(nlist1_mean)
# output: 10.72857142857143 +- 2.99466646070716
```

A `NumList` can also be printed by using the `.prnt()` method on the object. This prints the items of the `NumList`, together with indices.

```python
nlist1.prnt()
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

```python
addobj = Add(Num(2, 1), Num(3, 1))
numobj = addobj.eval()
print(numobj)
# output: 5 +- 1.4142135623731
```

Functions are only evaluated if you explicitly tell them to. Evaluating a function is done with the `.eval()` method - this returns a `Num` object, which then can be printed.

Nested functions are supported and are evaluated recursively, bottom up (inside out, depending on the perspective). The following example calculates a simple Boltzmann factor (`Rgas` is taken from wikipedia).

```python
deltaH = Num(2024.13, 0.25)
Rgas = Num(8.3144621, 0.0000075)
Temp = Num(300, 1)

Exp(Div(deltaH, Mul(Rgas, Temp))).eval().prnt()
# output: 2.25125909455595 +- 0.00609375728259
```

### `ListFnc`

Functions can also be applied to a `NumList`. `ListFnc` takes a `Fnc` object as argument and, depending on the function, one or two arguments - one of which must be a `NumList`.

Initialising the `ListFnc` will create a list of `Fnc` objects with corresponding arguments.

Evaluating the `ListFnc` with `.eval()` will return a `NumList`, which can then be condensed to a `Num` or used as argument for another `ListFnc`.

If both arguments are lists, they have to be of equal length. If only one of the arguments is a list, the other is converted to a list of equal length, containing repeating instances of the non-list argument.

If the `Fnc` is a one-argument-function, only one `NumList` is accepted as argument.

```python
nlist1 = NumList([9, 11, 10, Num(10, 1), 11, Num(12, 2), 9, 10])
nlist2 = NumList([9, 10, 11, Num(10, 1), 11, Num(12, 2), 9, 10])

addlist = ListFnc(Add, nlist1, nlist2)
sumlist = addlist.eval()

sumlist.prnt()
# output:
#0 : 18 +- 0.0
#1 : 21 +- 0.0
#2 : 21 +- 0.0
#3 : 20 +- 1.4142135623731
#4 : 22 +- 0.0
#5 : 24 +- 2.82842712474619
#6 : 18 +- 0.0
#7 : 20 +- 0.0

meanlist = sumlist.condense()
meanlist.prnt()
# output: 20.5 +- 0.81009258730098
```

If a `NumList` is used as an argument to a non-`ListFnc` function, it is automatically condensed to a `Num`.

```python
Add(nlist1, nlist2).eval().prnt()
# output: 20.5 +- 0.65123509031466
```
