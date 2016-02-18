# enerpy

enerpy is a python package for gaussian error propagation.

## Usage

- If you want only basic functionality and everything contained within the enerpy namespace, do:

```python
import enerpy
```

- If you want to use basic functions without namespace (beware name collisions), do:

```python
from enerpy import *
```

- If you need extra functionality (trig functions) or list functionality, do:

```python
from enerpy import *
from enerpy.lists import *
from enerpy.extras import *
```

## API Introduction

Everything is an object (TM). The basic types are `Num`, `Fnc`, `NumList` and `ListFnc`.


### New in Version 0.3.0

- This module now uses python's built-in support for arbitrary precision decimals. If you want to increase the default precision (50), use the following commands:

```python
from decimal import getcontext
getcontext().prec = PRECISION_YOU_WANT
```

Usage of the ```decimal``` module increases precision by a factor of 2-3 for normal computation. Trigonometric functions and logarithms with arbitrary bases are not supported, though, and fall back on float() computation.

- ```.prnt()``` methods have been removed and / or replaced by ```print()``` and ```repr()``` compatible code. enerpy objects should now print like any other python object.

- lists no longer automatically condense to ```Num``` objects when supplied to "normal" functions. Use ```.condense()``` manually, instead.

### New in Version 0.1.0

Infix operators can now be used for most arithmetic operations supported by python3 itself (not bitwise operators). No more need for nesting `Fnc` objects!


### `Num`

Arguments to functions are automatically coerced into the internal `Num` object, per default with Standard Error of 0. Initialising a `Num` object manually is done like this:

```python
# recommended (use strings for decimal values!):
num1 = Num(0, 0)  # number object, initialised with value and standard error of 0
num10 = Num("2.24029", "0.1241")

# possible:
from decimal import Decimal as D
num3 = Num()
num3.val = D(3)
num3.var = D(1)

# discouraged (does not use Decimals, may crash):
num2 = Num()      # "uninitialised" number object
num2.val = 3      # manually setting num1's value
num2.var = 1      # manually setting num1's variance
```

Evaluating a `Num` object is possible (for compatibility with other classes) but returns only the object itself.

### `NumList`

A `NumList` is initialised with a list of numbers or a list of `Num` objects. A `NumList` object cannot be evaluated with `.eval()`, it can only be condensed into a `Num` object using the `.condense()` method, where the value of the returned `Num` is the mean of the list items and its standard error is the standard error of the mean.

```python
nlist1 = NumList([1, 2, 10, Num(19, "2.2"), "11.1", Num(10, "1.2")])
nlist1.append(Num(22, "2.1"))
nlist1_mean = nlist1.condense()
print(nlist1_mean)
# output:
# 10.728571428571428571428571428571428571428571428571 ~ 2.9946664607071609138395536178331842901498927566998
```

A `NumList` can also be printed like any other object. This prints the items of the `NumList`, together with indices.

```python
print(nlist1)
# output:
# 0: 1
# 1: 2
# 2: 10
# 3: 19 ~ 2.2
# 4: 11.1
# 5: 10 ~ 1.2
# 6: 22 ~ 2.1
```

### `Fnc`

Function objects are initialised with the function argument(s). Some sunctions require two arguments, some only accept one argument, and a few work with one argument but two arguments can be specified. More than two arguments are not supported.

```python
addobj = Add(Num(2, 1), Num(3, 1))
numobj = addobj.eval()
print(numobj)
# output: 5 ~ 1.4142135623730950488016887242096980785696718753769
```

Functions are only evaluated if you explicitly tell them to. Evaluating a function is done with the `.eval()` method - this returns a `Num` object, which then can be printed.

Nested functions are supported and are evaluated recursively, bottom up (inside out, depending on the perspective). The following example calculates a simple Boltzmann factor (`Rgas` is taken from wikipedia).

```python
deltaH = Num(2024.13, 0.25)
Rgas = Num(8.3144621, 0.0000075)
Temp = Num(300, 1)

print(Exp(Div(deltaH, Mul(Rgas, Temp))).eval())
# output: 2.2512590945559546210695622831458962700776460897319 ~ 0.0060937572825927446436758473905032381143504791191817
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

print(sumlist)
# output:
# 0: 18
# 1: 21
# 2: 21
# 3: 20 ~ 1.4142135623730950488016887242096980785696718753769
# 4: 22
# 5: 24 ~ 2.8284271247461900976033774484193961571393437507539
# 6: 18
# 7: 20

meanlist = sumlist.condense()
print(meanlist)
# output: 20.5 ~ 0.81009258730098252887074592951099958221315053838229
```


## IMPORTANT

By default, this package uses 50 significant decimal digits for precision.
This does _not_ mean your results are necessarily that accurate.
Consider a number's value _and_ standard deviation to get a sense of "accuracy"
or significant figures.

In the future, a standardised method for reducing displayed digits to "significant" digits
(e.g. ```.sig()```)may be implemented

