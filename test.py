#!/usr/bin/env python3

import math

from enerpy.functions import *


# Some small tests
a = Num(2.0, 0.5)
b = Num(8.0, 0.4)

c = add(a, b)
d = mul(a, b)

C = Add(a, b).eval()
D = Mul(a, b).eval()

E = Add(a).eval()

F = Log(Num(math.e, 0), Num(2, 0)).eval()
G = Pow(Num(math.e, 0), Num(2, 0.25)).eval()
X = Exp(Num(2, 0.25)).eval()

H = Sin(Num(0, 0.2)).eval()
I = Cos(Num(0, 0.2)).eval()
J = Tan(Num(0, 0.2)).eval()

K = ArcSin(Num(0, 0.2)).eval()
L = ArcCos(Num(0, 0.2)).eval()
M = ArcTan(Num(0, 0.2)).eval()

N = Sinh(Num(0, 0.2)).eval()
O = Cosh(Num(0, 0.2)).eval()
P = Tanh(Num(0, 0.2)).eval()

Q = ArcSinh(Num(0, 0.2)).eval()
R = ArcCosh(Num(2, 0.2)).eval()
S = ArcTanh(Num(0, 0.2)).eval()

c.print()
d.print()
C.print()
D.print()
E.print()

F.print()
G.print()
X.print()

H.print()
I.print()
J.print()

K.print()
L.print()
M.print()

N.print()
O.print()
P.print()

Q.print()
R.print()
S.print()


# Node Tree
node1 = Num(2, 0.1)
node2 = Num(3, 0.2)
node3 = Num(1, 0)
node4 = Num(1, 0)

node5 = Div(node1, node2)
node6 = Sub(node3, node5)
node7 = Div(node4, node6)

result = node7.eval()

result.print()
