#!/usr/bin/env python3

from decimal import Decimal as D
from decimal import getcontext

from enerpy.funcs import Add

from enerpy.lists import NumList
from enerpy.funcs_list import ListFnc

getcontext().prec = 50


A = NumList([D(1), D(3), D(1), D(2), D(4), D(2), D("1.5"), D(2), D(3)])
B = NumList([D(1), D(2), D(3), D(1), D(2), D(5), D("2.1"), D(2), D(4)])

print("A", end=" ")
A.condense().prnt()

print("B", end=" ")
B.condense().prnt()

C = ListFnc(Add, A, B)
C.eval().prnt()
C.eval().condense().prnt()

