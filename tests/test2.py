#!/usr/bin/env python3

from decimal import Decimal as D
from decimal import getcontext

from enerpy import *
from enerpy.lists import *


A = NumList([D(1), D(3), D(1), D(2), D(4), D(2), D("1.5"), D(2), D(3)])
B = NumList([D(1), D(2), D(3), D(1), D(2), D(5), D("2.1"), D(2), D(4)])

print("A", end=" ")
print(A.condense())

print("B", end=" ")
print(B.condense())

C = ListFnc(Add, A, B)
print(C)
print(C.eval())
print(C.eval().condense())

