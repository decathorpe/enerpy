#!/usr/bin/env python3

from enerpy.funcs import *
from enerpy.funcs_list import *


a = Num(2.0, 0.5)
b = Num(8.0, 0.4)


# Some small tests
ADD_INFIX = a + b
ADD_FUNCS = Add(a, b).eval()

"""
#TODO This doesn't work yet anymore. Needs more work.
ADD_CONST = a + 1
ADD_CONSX = Add(a, 1).eval()
"""

SUB_INFIX = a - b
SUB_FUNCS = Sub(a, b).eval()

MUL_INFIX = a * b
MUL_FUNCS = Mul(a, b).eval()

DIV_INFIX = a / b
DIV_FUNCS = Div(a, b).eval()

"""
D = Mul(a, b).eval()

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

T = Roo(Num(2, 1)).eval()

F.prnt()
G.prnt()
X.prnt()

H.prnt()
I.prnt()
J.prnt()

K.prnt()
L.prnt()
M.prnt()

N.prnt()
O.prnt()
P.prnt()

Q.prnt()
R.prnt()
S.prnt()

T.prnt()


# Node Tree
node1 = Num(2, 0.1)
node2 = Num(3, 0.2)
node3 = Num(1, 0)
node4 = Num(1, 0)

node5 = Div(node1, node2)
node6 = Sub(node3, node5)
node7 = Div(node4, node6)

result = node7.eval()

result.prnt()


# NumLists
nlist = NumList([9, 10, 11, Num(10, 1), 11, Num(12, 2), 9, 10])
# nlist.condense().prnt()

nlist1 = NumList([9, 11, 10, Num(10, 1), 11, Num(12, 2), 9, 10])
nlist2 = NumList([9, 10, 11, Num(10, 1), 11, Num(12, 2), 9, 10])

sumlist = ListFnc(Add, nlist1, nlist2).eval()
sumlist.prnt()
sumlist.condense().prnt()
Add(nlist1.condense(),nlist2.condense()).eval().prnt()

coslist = ListFnc(Cos, nlist1).eval()
coslist.prnt()
coslist.condense().prnt()

ListFnc(Add, nlist1, 1).eval().condense().prnt()

ListFnc(Log, nlist1).eval().condense().prnt()
ListFnc(Log, nlist1, nlist2).eval().condense().prnt()

# Test automatic condensing
Add(nlist1, nlist2).eval().prnt()
"""

# Test infix operators
ADD_INFIX.prnt()
ADD_FUNCS.prnt()

SUB_INFIX.prnt()
SUB_FUNCS.prnt()

MUL_INFIX.prnt()
MUL_FUNCS.prnt()

DIV_INFIX.prnt()
DIV_FUNCS.prnt()
