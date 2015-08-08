#!/usr/bin/env python3

from enerpy.funcs import *
from enerpy.funcs_list import *

a = NumList([1, 3, 1, 2, 4, 2, 1.5, 2, 3])
b = NumList([1, 2, 3, 1, 2, 5, 2.1, 2, 4])

print("a", end=" ")
a.condense().prnt()

print("b", end=" ")
b.condense().prnt()

c = ListFnc(Add, a, b)
c.eval().prnt()
c.eval().condense().prnt()
