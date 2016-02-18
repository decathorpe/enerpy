#!/usr/bin/env python3

from decimal import Decimal as D
from decimal import getcontext

from enerpy.base import Num
from enerpy.funcs import Mul, Div, Exp

getcontext().prec = 50


deltaH = Num(D("2024.13"), D("0.25"))
Rgas = Num(D("8.3144621"), D("0.0000075"))
Temp = Num(D(300), D(1))

print("R*T")
RT = Mul(Rgas, Temp).eval()
RT.prnt()

print("dH/RT")
E = Div(deltaH, RT).eval()
E.prnt()

print("e**(dH/RT)")
C = Exp(E).eval()
C.prnt()

print("one-shot: C")
Exp(Div(deltaH, Mul(Rgas, Temp))).eval().prnt()
# output: 2.25125909455595 +- 0.00609375728259

# IT WORKS!
