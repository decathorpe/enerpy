#!/usr/bin/env python3

import math

from enerpy.base import *
from enerpy.math_base import *
from enerpy.math_trig import *
from enerpy.functions import *


# Some small tests
a = Num(2, 0.5)
b = Num(8, 0.4)

c = add(a, b)
d = mul(a, b)

C = AddNew(a, b).eval()
D = Mul(a, b).eval()


print(str(c.val) + " +- " + str(c.sdv()))
print(str(d.val) + " +- " + str(d.sdv()))

print(str(C.val) + " +- " + str(C.sdv()))
print(str(D.val) + " +- " + str(D.sdv()))



# Node Tree
node1 = Num(2, 0.1)
node2 = Num(3, 0.2)
node3 = Num(1, 0)
node4 = Num(1, 0)

node5 = Div(node1, node2)
node6 = Sub(node3, node5)
node7 = Div(node4, node6)

result = node7.eval()

print(str(result.val) + " +- " + str(result.sdv()))
