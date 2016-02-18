#!/usr/bin/env python3

from decimal import Decimal as D

from enerpy import *
from enerpy.extras import *

# from enerpy.funcs_list import *


a = Num(D("2.0"), D("0.5"))
b = Num(D("8.0"), D("0.4"))

# nlist1 = NumList([9, 11, 10, Num(10, 1), 11, Num(12, 2), 9, 10])
# nlist2 = NumList([9, 10, 11, Num(10, 1), 11, Num(12, 2), 9, 10])


# Some small tests
ADD_INFIX = a + b
ADD_FUNCS = Add(a, b)
IADD_TEST = a
IADD_TEST += b

ADD_CONST = a + 1
ADD_CONSX = Add(a, 1)
ADD_CONSR = 2 + a
ADD_CONSY = Add(2, a)

SUB_INFIX = a - b
SUB_FUNCS = Sub(a, b)
ISUB_TEST = a
ISUB_TEST -= b

SUB_CONST = b - 1
SUB_CONSX = Sub(b, 1)
SUB_CONSR = 1 - b
SUB_CONSY = Sub(1, b)

MUL_INFIX = a * b
MUL_FUNCS = Mul(a, b)
IMUL_TEST = a
IMUL_TEST *= b

MUL_CONST = a * 2
MUL_CONSX = Mul(a, 2)
MUL_CONSR = 3 * a
MUL_CONSY = Mul(3, a)

DIV_INFIX = a / b
DIV_FUNCS = Div(a, b)
IDIV_TEST = a
IDIV_TEST /= b

DIV_CONST = a / 2
DIV_CONSX = Div(a, 2)
DIV_CONSR = 3 / a
DIV_CONSY = Div(3, a)

POW_INFIX = a ** b
POW_FUNCS = Pwr(a, b)
IPOW_TEST = a
IPOW_TEST **= b

POW_CONST = a ** 2
POW_CONSX = Pwr(a, 2)
POW_CONSR = 2 ** a
POW_CONSY = Pwr(2, a)


# Unary operators
NEG_PREFIX = -a
POS_PREFIX = +NEG_PREFIX

ABS_FUNCX = abs(-a)
ABS_FUNCY = abs(+a)


# Math functions
LOG_FUNCX = Log(a)
LOG_FUNCY = Log(b, a)
EXP_FUNCX = Exp(a)

SIN_FUNCS = Sin(a)
COS_FUNCS = Cos(a)
TAN_FUNCS = Tan(a)

ARCSIN_FUNCS = ArcSin(a/3)
ARCCOS_FUNCS = ArcCos(a/3)
ARCTAN_FUNCS = ArcTan(a/3)

SINH_FUNCS = Sinh(a)
COSH_FUNCS = Cosh(a)
TANH_FUNCS = Tanh(a)

ARCSINH_FUNCS = ArcSinh(a/4)
ARCCOSH_FUNCS = ArcCosh(a*4)
ARCTANH_FUNCS = ArcTanh(a/4)

REV_SIN = Sin(ArcSin(a/4))
REV_COS = Cos(ArcCos(a/4))
REV_TAN = Tan(ArcTan(a/4))

REV_SINH = Sinh(ArcSinh(a/4))
REV_COSH = Cosh(ArcCosh(Num(2, 2)))
REV_TANH = Tanh(ArcTanh(a/4))

ROOT = Root(Num(2, 1))


# Node Tree (does not print result)
node1 = Num(2, "0.1")
node2 = Num(3, "0.2")
node3 = Num(1, 0)
node4 = Num(1, 0)

node5 = Div(node1, node2)
node6 = Sub(node3, node5)
node7 = Div(node4, node6)

result = node7.eval()


# NumLists
# sumlist = ListFnc(Add, nlist1, nlist2).eval()
# coslist = ListFnc(Cos, nlist1).eval()


# Print test results

print("Infix addition:                           ", ADD_INFIX)
print("Function addition:                        ", ADD_FUNCS)
print("Addition assignment:                      ", IADD_TEST)
print("Test status:                              ",
      ADD_INFIX.eval() == ADD_FUNCS.eval() == IADD_TEST.eval())
print()

print("Infix constant addition:                  ", ADD_CONST)
print("Function constant addition:               ", ADD_CONSX)
print("Test status:                              ",
      ADD_CONST.eval() == ADD_CONSX.eval())
print("Reverse infix constant addition:          ", ADD_CONSR)
print("Reverse function constant addition:       ", ADD_CONSY)
print("Test status:                              ",
      ADD_CONSR.eval() == ADD_CONSY.eval())
print()

print("Infix subtraction:                        ", SUB_INFIX)
print("Function subtraction:                     ", SUB_FUNCS)
print("Subtraction assignment:                   ", ISUB_TEST)
print("Test status:                              ",
      SUB_INFIX.eval() == SUB_FUNCS.eval() == ISUB_TEST.eval())
print()

print("Infix constant subtraction:               ", SUB_CONST)
print("Function constant subtraction:            ", SUB_CONSX)
print("Test status:                              ",
      SUB_CONST.eval() == SUB_CONSX.eval())
print("Reverse infix constant subtraction:       ", SUB_CONSR)
print("Reverse function constant subtraction:    ", SUB_CONSY)
print("Test status:                              ",
      SUB_CONSR.eval() == SUB_CONSY.eval())
print()

print("Infix multiplication:                     ", MUL_INFIX)
print("Function multiplication:                  ", MUL_FUNCS)
print("Multiplication assignment:                ", IMUL_TEST)
print("Test status:                              ",
      MUL_INFIX.eval() == MUL_FUNCS.eval() == IMUL_TEST.eval())
print()

print("Infix constant multiplication:            ", MUL_CONST)
print("Function constant multiplication:         ", MUL_CONSX)
print("Test status:                              ",
      MUL_CONST.eval() == MUL_CONSX.eval())
print("Reverse infix constant multiplication:    ", MUL_CONSR)
print("Reverse function constant multiplication: ", MUL_CONSY)
print("Test status:                              ",
      MUL_CONSR.eval() == MUL_CONSY.eval())
print()

print("Infix division:                           ", DIV_INFIX)
print("Function division:                        ", DIV_FUNCS)
print("Division assignment:                      ", IDIV_TEST)
print("Test status:                              ",
      DIV_INFIX.eval() == DIV_FUNCS.eval() == IDIV_TEST.eval())
print()

print("Infix constant division:                  ", DIV_CONST)
print("Function constant division:               ", DIV_CONSX)
print("Test status:                              ",
      DIV_CONST.eval() == DIV_CONSX.eval())
print("Reverse infix constant division:          ", DIV_CONSR)
print("Reverse function constant division:       ", DIV_CONSY)
print("Test status:                              ",
      DIV_CONSR.eval() == DIV_CONSY.eval())
print()

print("Infix powers:                             ", POW_INFIX)
print("Function powers:                          ", POW_FUNCS)
print("Powers assignment:                        ", IPOW_TEST)
print("Test status:                              ",
      POW_INFIX.eval() == POW_FUNCS.eval() == IPOW_TEST.eval())
print()

print("Infix constant powers:                    ", POW_CONST)
print("Function constant powers:                 ", POW_CONSX)
print("Test status:                              ",
      POW_CONST.eval() == POW_CONSX.eval())
print("Reverse infix constant powers:            ", POW_CONSR)
print("Reverse function constant powers:         ", POW_CONSY)
print("Test status:                              ",
      POW_CONSR.eval() == POW_CONSY.eval())
print()

print("Negative value:                           ", NEG_PREFIX)
print("Positive value:                           ", POS_PREFIX)
print("Test status:                              ",
      NEG_PREFIX.eval() == -POS_PREFIX.eval())
print()

print("Absolute value of negative:               ", ABS_FUNCX)
print("Absolute value of positive:               ", ABS_FUNCY)
print("Test status:                              ",
      ABS_FUNCX.eval() == ABS_FUNCY.eval())
print()

print("Logarithm base e:                         ", LOG_FUNCX)
print("                :                         ", LOG_FUNCX.eval())
print("Logarithm base b:                         ", LOG_FUNCY)
print("                :                         ", LOG_FUNCY.eval())
print("Exponent base e:                          ", EXP_FUNCX)
print("                :                         ", EXP_FUNCX.eval())
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

print("Argument:                                 ", (a/4).eval())
print("Sin of ArcSin:                            ", REV_SIN)
print("Test status:                              ",
      (a/4).eval() == REV_SIN)
print("Argument:                                 ", (a/4).eval())
print("Cos of ArcCos:                            ", REV_COS)
print("Test status:                              ",
      (a/4).eval() == REV_COS)
print("Argument:                                 ", (a/4).eval())
print("Tan of ArcTan:                            ", REV_TAN)
print("Test status:                              ",
      (a/4).eval() == REV_TAN, "(Expected failure.)")
print()

print("Argument:                                 ", (a/4).eval())
print("Sinh of ArcSinh:                          ", REV_SINH)
print("Test status:                              ",
      (a/4).eval() == REV_SINH)
print("Argument:                                 ", Num(2, 2))
print("Cosh of ArcCosh:                          ", REV_COSH)
print("Test status:                              ",
      Num(2, 2) == REV_COSH)
print("Argument:                                 ", (a/4).eval())
print("Tanh of ArcTanh:                          ", REV_TANH)
print("Test status:                              ",
      (a/4).eval() == REV_TANH, "(Expected failure.)")
print()

print("Square root of 2 +- 1:                    ", ROOT.eval())
print()

#print("List condensing:                          ", nlist1.condense())
#print("List of Add +1 functions, condensed:      ", ListFnc(Add, nlist1, 1).eval().condense())
#print("List of Add functions, condensed:         ", sumlist.condense())
#print("Sum of condensed Lists:                   ", Add(nlist1.condense(),nlist2.condense()).eval())
#print("List of Cos functions, condensed:         ", coslist.condense())
#print("List of Log functions, condensed:         ", ListFnc(Log, nlist1).eval().condense())
#print("List of Log base b functions, condensed:  ", ListFnc(Log, nlist1, nlist2).eval().condense())
#print("Automatically condensed Add of Lists:     ", Add(nlist1, nlist2).eval())
#print()

