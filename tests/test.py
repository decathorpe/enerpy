#!/usr/bin/env python3

from enerpy.base import Num
from enerpy.funcs import *
from enerpy.funcs_list import *

def nprint(text):
    print(text, end="")

a = Num(2.0, 0.5)
b = Num(8.0, 0.4)

nlist1 = NumList([9, 11, 10, Num(10, 1), 11, Num(12, 2), 9, 10])
nlist2 = NumList([9, 10, 11, Num(10, 1), 11, Num(12, 2), 9, 10])


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
POW_FUNCS = Pwr(a, b).eval()
IPOW_TEST = a
IPOW_TEST **= b

POW_CONST = a ** 2
POW_CONSX = Pwr(a, 2).eval()
POW_CONSR = 2 ** a
POW_CONSY = Pwr(2, a).eval()


# Unary operators
NEG_PREFIX = -a
POS_PREFIX = +NEG_PREFIX

ABS_FUNCX = abs(-a)
ABS_FUNCY = abs(+a)


# Comparison operators
LT_INFIX = (a < b)
GT_INFIX = (b > a)
LE_INFIX = (a <= b)
LE_INFIY = (a <= a)
EQ_INFIX = (a == a)
NE_INFIX = (a != b)
GE_INFIX = (b >= a)
GE_INFIY = (b >= b)


# Math functions
LOG_FUNCX = Log(a).eval()
LOG_FUNCY = Log(b, a).eval()
EXP_FUNCX = Exp(a).eval()

SIN_FUNCS = Sin(a).eval()
COS_FUNCS = Cos(a).eval()
TAN_FUNCS = Tan(a).eval()

ARCSIN_FUNCS = ArcSin(a/3).eval()
ARCCOS_FUNCS = ArcCos(a/3).eval()
ARCTAN_FUNCS = ArcTan(a/3).eval()

SINH_FUNCS = Sinh(a).eval()
COSH_FUNCS = Cosh(a).eval()
TANH_FUNCS = Tanh(a).eval()

ARCSINH_FUNCS = ArcSinh(a/4).eval()
ARCCOSH_FUNCS = ArcCosh(a*4).eval()
ARCTANH_FUNCS = ArcTanh(a/4).eval()

REV_SIN = Sin(ArcSin(a/4)).eval()
REV_COS = Cos(ArcCos(a/4)).eval()
REV_TAN = Tan(ArcTan(a/4)).eval()

REV_SINH = Sinh(ArcSinh(a/4)).eval()
REV_COSH = Cosh(ArcCosh(a*4)).eval()
REV_TANH = Tanh(ArcTanh(a/4)).eval()

ROOT = Root(Num(2, 1)).eval()


# Node Tree
node1 = Num(2, 0.1)
node2 = Num(3, 0.2)
node3 = Num(1, 0)
node4 = Num(1, 0)

node5 = Div(node1, node2)
node6 = Sub(node3, node5)
node7 = Div(node4, node6)

result = node7.eval()


# NumLists
sumlist = ListFnc(Add, nlist1, nlist2).eval()
coslist = ListFnc(Cos, nlist1).eval()


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

print("Negative value:                           ", NEG_PREFIX)
print("Positive value:                           ", POS_PREFIX)
print("Test status:                              ", NEG_PREFIX == -POS_PREFIX)
print()

print("Absolute value of negative:               ", ABS_FUNCX)
print("Absolute value of positive:               ", ABS_FUNCY)
print("Test status:                              ", ABS_FUNCX == ABS_FUNCY)
print()

print("Infix less than:                          ", LT_INFIX)
print("Infix greater than:                       ", GT_INFIX)
print("Infix less than or equal:                 ", LE_INFIX)
print("Infix greater than or equal:              ", GE_INFIX)
print("Equality:                                 ", EQ_INFIX)
print("Non-equality:                             ", NE_INFIX)
print("Test status:                              ", LE_INFIY == GE_INFIY)
print()

print("Logarithm base e:                         ", LOG_FUNCX)
print("Logarithm base b:                         ", LOG_FUNCY)
print("Exponent base e:                          ", EXP_FUNCX)
print()

print("Sin:                                      ", SIN_FUNCS)
print("Cos:                                      ", COS_FUNCS)
print("Tan:                                      ", TAN_FUNCS)
print("ArcSin:                                   ", ARCSIN_FUNCS)
print("ArcCos:                                   ", ARCCOS_FUNCS)
print("ArcTan:                                   ", ARCTAN_FUNCS)
print()

print("Sinh:                                     ", SINH_FUNCS)
print("Cosh:                                     ", COSH_FUNCS)
print("Tanh:                                     ", TANH_FUNCS)
print("ArcSinh:                                  ", ARCSINH_FUNCS)
print("ArcCosh:                                  ", ARCCOSH_FUNCS)
print("ArcTanh:                                  ", ARCTANH_FUNCS)
print()

print("Argument:                                 ", a/4)
print("Sin of ArcSin:                            ", REV_SIN)
print("Test status:                              ", (a/4) == REV_SIN)
print("Argument:                                 ", a/4)
print("Cos of ArcCos:                            ", REV_COS)
print("Test status:                              ", (a/4) == REV_COS)
print("Argument:                                 ", a/4)
print("Tan of ArcTan:                            ", REV_TAN)
print("Test status:                              ", (a/4) == REV_TAN)
print()

print("Argument:                                 ", a/4)
print("Sinh of ArcSinh:                          ", REV_SINH)
print("Test status:                              ", (a/4) == REV_SINH)
print("Argument:                                 ", a*4)
print("Cosh of ArcCosh:                          ", REV_COSH)
print("Test status:                              ", (a*4) == REV_COSH)
print("Argument:                                 ", a/4)
print("Tanh of ArcTanh:                          ", REV_TANH)
print("Test status:                              ", (a/4) == REV_TANH)
print()

print("Square root of 2 +- 1:                    ", ROOT)
print()

print("List condensing:                          ", nlist1.condense())
print("List of Add +1 functions, condensed:      ", ListFnc(Add, nlist1, 1).eval().condense())
print("List of Add functions, condensed:         ", sumlist.condense())
print("Sum of condensed Lists:                   ", Add(nlist1.condense(),nlist2.condense()).eval())
print("List of Cos functions, condensed:         ", coslist.condense())
print("List of Log functions, condensed:         ", ListFnc(Log, nlist1).eval().condense())
print("List of Log base b functions, condensed:  ", ListFnc(Log, nlist1, nlist2).eval().condense())
print("Automatically condensed Add of Lists:     ", Add(nlist1, nlist2).eval())
print()

