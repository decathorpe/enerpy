#!/usr/bin/env python3

from enerpy.funcs import *
from enerpy.funcs_list import *

def nprint(text):
    print(text, end="")

a = Num(2.0, 0.5)
b = Num(8.0, 0.4)


# Some small tests
ADD_INFIX = a + b
ADD_FUNCS = Add(a, b).eval()
IADD_TEST = a
IADD_TEST += b

ADD_CONST = a + 1
ADD_CONSX = Add(a, 1).eval()
ADD_CONSR = 2 + a
ADD_CONSY = Add(2, a).eval()

SUB_INFIX = a - b
SUB_FUNCS = Sub(a, b).eval()
ISUB_TEST = a
ISUB_TEST -= b

SUB_CONST = b - 1
SUB_CONSX = Sub(b, 1).eval()
SUB_CONSR = 1 - b
SUB_CONSY = Sub(1, b).eval()

MUL_INFIX = a * b
MUL_FUNCS = Mul(a, b).eval()
IMUL_TEST = a
IMUL_TEST *= b

MUL_CONST = a * 2
MUL_CONSX = Mul(a, 2).eval()
MUL_CONSR = 3 * a
MUL_CONSY = Mul(3, a).eval()

DIV_INFIX = a / b
DIV_FUNCS = Div(a, b).eval()
IDIV_TEST = a
IDIV_TEST /= b

DIV_CONST = a / 2
DIV_CONSX = Div(a, 2).eval()
DIV_CONSR = 3 / a
DIV_CONSY = Div(3, a).eval()

POW_INFIX = a ** b
POW_FUNCS = Pow(a, b).eval()
IPOW_TEST = a
IPOW_TEST **= b

POW_CONST = a ** 2
POW_CONSX = Pow(a, 2).eval()
POW_CONSR = 2 ** a
POW_CONSY = Pow(2, a).eval()


# Print test results
print("Infix addition:                           ", ADD_INFIX)
print("Function addition:                        ", ADD_FUNCS)
print("Addition assignment:                      ", IADD_TEST)
print("Test status:                              ", ADD_INFIX == IADD_TEST)
print()

print("Infix constant addition:                  ", ADD_CONST)
print("Function constant addition:               ", ADD_CONSX)
print("Test status:                              ", ADD_CONST == ADD_CONSX)
print("Reverse infix constant addition:          ", ADD_CONSR)
print("Reverse function constant addition:       ", ADD_CONSY)
print("Test status:                              ", ADD_CONSR == ADD_CONSY)
print()

print("Infix subtraction:                        ", SUB_INFIX)
print("Function subtraction:                     ", SUB_FUNCS)
print("Subtraction assignment:                   ", ISUB_TEST)
print("Test status:                              ", SUB_INFIX == ISUB_TEST)
print()

print("Infix constant subtraction:               ", SUB_CONST)
print("Function constant subtraction:            ", SUB_CONSX)
print("Test status:                              ", SUB_CONST == SUB_CONSX)
print("Reverse infix constant subtraction:       ", SUB_CONSR)
print("Reverse function constant subtraction:    ", SUB_CONSY)
print("Test status:                              ", SUB_CONSR == SUB_CONSY)
print()

print("Infix multiplication:                     ", MUL_INFIX)
print("Function multiplication:                  ", MUL_FUNCS)
print("Multiplication assignment:                ", IMUL_TEST)
print("Test status:                              ", MUL_INFIX == IMUL_TEST)
print()

print("Infix constant multiplication:            ", MUL_CONST)
print("Function constant multiplication:         ", MUL_CONSX)
print("Test status:                              ", MUL_CONST == MUL_CONSX)
print("Reverse infix constant multiplication:    ", MUL_CONSR)
print("Reverse function constant multiplication: ", MUL_CONSY)
print("Test status:                              ", MUL_CONSR == MUL_CONSY)
print()

print("Infix division:                           ", DIV_INFIX)
print("Function division:                        ", DIV_FUNCS)
print("Division assignment:                      ", IDIV_TEST)
print("Test status:                              ", DIV_INFIX == IDIV_TEST)
print()

print("Infix constant division:                  ", DIV_CONST)
print("Function constant division:               ", DIV_CONSX)
print("Test status:                              ", DIV_CONST == DIV_CONSX)
print("Reverse infix constant division:          ", DIV_CONSR)
print("Reverse function constant division:       ", DIV_CONSY)
print("Test status:                              ", DIV_CONSR == DIV_CONSY)
print()

print("Infix powers:                             ", POW_INFIX)
print("Function powers:                          ", POW_FUNCS)
print("Powers assignment:                        ", IPOW_TEST)
print("Test status:                              ", POW_INFIX == IPOW_TEST)
print()

print("Infix constant powers:                    ", POW_CONST)
print("Function constant powers:                 ", POW_CONSX)
print("Test status:                              ", POW_CONST == POW_CONSX)
print("Reverse infix constant powers:            ", POW_CONSR)
print("Reverse function constant powers:         ", POW_CONSY)
print("Test status:                              ", POW_CONSR == POW_CONSY)
print()

