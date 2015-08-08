#!/usr/bin/env python3

from enerpy.funcs import *

deltaH = Num(2024.13, 0.25)
Rgas = Num(8.3144621, 0.0000075)
Temp = Num(300, 1)

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
