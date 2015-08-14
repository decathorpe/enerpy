#!/usr/bin/env python3

from enerpy.funcs import Add

from enerpy.lists import NumList
from enerpy.funcs_list import ListFnc

A = NumList([1, 3, 1, 2, 4, 2, 1.5, 2, 3])
B = NumList([1, 2, 3, 1, 2, 5, 2.1, 2, 4])

print("A", end=" ")
A.condense().prnt()

print("B", end=" ")
B.condense().prnt()

C = ListFnc(Add, A, B)
C.eval().prnt()
C.eval().condense().prnt()
