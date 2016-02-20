#!/usr/bin/env python3

from decimal import Decimal as D
from decimal import getcontext

from enerpy import *


deltaH = Num(D("2024.13"), D("0.25"))
Rgas = Num(D("8.3144621"), D("0.0000075"))
Temp = Num(D(300), D(1))

print("R*T")
RT = Mul(Rgas, Temp).eval()
print(RT)

print("dH/RT")
E = Div(deltaH, RT).eval()
print(E)

print("e**(dH/RT)")
C = Exp(E).eval()
print(C)

print("one-shot: C")
print(Exp(Div(deltaH, Mul(Rgas, Temp))).eval())

print("one-shot with infix operators: C")
print(Exp(deltaH / (Rgas * Temp)).eval())

