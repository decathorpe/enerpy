# enerpy

enerpy is a python package for gaussian error propagation.

## Usage

- If you want all and everything contained within the enerpy namespace, do:

`import enerpy`

- If you want to use all functions without namespace (beware name collisions), do:

`from enerpy.functions import *`


## API Introduction

Everything is an object (TM). The basic types are `Num`, `Fnc`, `NumList` and `ListFnc`.

### `Num`

Arguments to functions are automatically coerced into the internal `Num` object, per default with Standard Error of 0. Initialising a `Num` object manually is done like this:

```python
num1 = Num()      # "uninitialised" number object
num1.val = 3      # manually setting num1's value
num1.var = 1      # manually setting num1's variance

num2 = Num(0, 0)  # number object, initialised with value and standard error of 0
```

`Num` objects can be printed simply by invoking the `.print()` method on them.
Evaluating a `Num` object is possible but returns only the object itself.

 ### `NumList`

A `NumList` is initialised with a list of numbers or a list of `Num` objects. A `NumList` object cannot be evaluated with `.eval()`, it can only be condensed into a `Num` object using the `.condense()` method, where the value of the returned `Num` is the mean of the list items and its standard error is the standard error of the mean.

```python
nlist1 = NumList([1, 2, 10, Num(19, 2.2), 11.1, Num(10, 1.2)])
nlist1.append(Num(22,2.1))
nlist1_mean =nlist1.condense()
nlist_mean.print()
```

### `Fnc`

Functions are only evaluated if you explicitly tell them to. `Add(num1, num2)` only creates an `Add` Function object with arguments `num1` and `num2`, and `num1` and `num2` are coerced before the object is created.

Evaluating a `Fnc` object is done with the `.eval()` method and returns a `Num` object.

Printing a `Num` object is done with the `.print()` method and prints value and the calculated standard error.


## Example:

This example calculates a simple Boltzmann factor (`Rgas` is taken from wikipedia).

```python
deltaH = Num(2024.13, 0.25)
Rgas = Num(8.3144621, 0.0000075)
Temp = Num(300, 1)

Exp(Div(deltaH, Mul(Rgas, Temp))).eval().print()
# output: 2.25125909455595 +- 0.00609375728259
```
