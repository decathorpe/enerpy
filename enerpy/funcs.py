"""
enerpy/funcs.py:
This module contains all the function classes.
Arguments will be coerced to Num objects.
"""

from enerpy.base import Num
from enerpy.base import Fnc
from enerpy.base import enerfy

from enerpy.calc import *


# Add, Sub classes
class Add(Fnc):
    def __init__(self, a, b):
        super().__init__()
        self.name = "Add"

        a = enerfy(a)
        b = enerfy(b)

        self.arg1 = a
        self.arg2 = b

    def eval(self):
        result = add(self.arg1.eval(), self.arg2.eval())
        return result


class Sub(Fnc):
    def __init__(self, a, b):
        super().__init__()
        self.name = "Sub"

        a = enerfy(a)
        b = enerfy(b)

        self.arg1 = a
        self.arg2 = b

    def eval(self):
        result = sub(self.arg1.eval(), self.arg2.eval())
        return result


# Mul, Div classes
class Mul(Fnc):
    def __init__(self, a, b):
        super().__init__()
        self.name = "Mul"

        a = enerfy(a)
        b = enerfy(b)

        self.arg1 = a
        self.arg2 = b

    def eval(self):
        result = mul(self.arg1.eval(), self.arg2.eval())
        return result


class Div(Fnc):
    def __init__(self, a, b):
        super().__init__()
        self.name = "Div"

        a = enerfy(a)
        b = enerfy(b)

        self.arg1 = a
        self.arg2 = b

    def eval(self):
        result = div(self.arg1.eval(), self.arg2.eval())
        return result


# Pow, Log classes

# generic power: a raised to power b
class Pwr(Fnc):
    def __init__(self, a, b):
        super().__init__()
        self.name = "Pwr"

        a = enerfy(a)
        b = enerfy(b)

        self.arg1 = a
        self.arg2 = b

    def eval(self):
        result = pwr(self.arg1.eval(), self.arg2.eval())
        return result


# special case: (square) roots
class Srt(Fnc):
    def __init__(self, a, b=2):
        super().__init__()
        self.name = "Srt"

        a = enerfy(a)
        b = enerfy(b)

        self.arg1 = a
        self.arg2 = Div(1, b)

    def eval(self):
        result = pwr(self.arg1.eval(), self.arg2.eval())
        return result


# special case: exponent a, base e
class Exp(Fnc):
    def __init__(self, a):
        super().__init__()
        self.name = "Exp"

        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = exp(self.arg1.eval())
        return result

# generic logarithm: argument a, base b (default: math.e)
class Log(Fnc):
    def __init__(self, a, b=math.e):
        super().__init__()
        self.name = "Log"

        a = enerfy(a)
        b = enerfy(b)

        self.arg1 = a
        self.arg2 = b

    def eval(self):
        result = log(self.arg1.eval(), self.arg2.eval())
        return result


# Sin, Cos, Tan classes
class Sin(Fnc):
    def __init__(self, a):
        super().__init__()
        self.name = "Sin"

        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = sin(self.arg1.eval())
        return result


class Cos(Fnc):
    def __init__(self, a):
        super().__init__()
        self.name = "Cos"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = cos(self.arg1.eval())
        return result


class Tan(Fnc):
    def __init__(self, a):
        super().__init__()
        self.name = "Tan"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = tan(self.arg1.eval())
        return result


# ArcSin, ArcCos, ArcTan classes
class ArcSin(Fnc):
    def __init__(self, a):
        super().__init__()
        self.name = "ArcSin"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = arcsin(self.arg1.eval())
        return result


class ArcCos(Fnc):
    def __init__(self, a):
        super().__init__()
        self.name = "ArcCos"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = arccos(self.arg1.eval())
        return result


class ArcTan(Fnc):
    def __init__(self, a):
        super().__init__()
        self.name = "ArcTan"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = arctan(self.arg1.eval())
        return result


# Sinh, Cosh, Tanh classes
class Sinh(Fnc):
    def __init__(self, a):
        super().__init__()
        self.name = "Sinh"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = sinh(self.arg1.eval())
        return result


class Cosh(Fnc):
    def __init__(self, a):
        super().__init__()
        self.name = "Cosh"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = cosh(self.arg1.eval())
        return result


class Tanh(Fnc):
    def __init__(self, a):
        super().__init__()
        self.name = "Tanh"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = tanh(self.arg1.eval())
        return result


# ArcSinh, ArcCosh, ArcTanh classes
class ArcSinh(Fnc):
    def __init__(self, a):
        super().__init__()
        self.name = "ArcSinh"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = arcsinh(self.arg1.eval())
        return result


class ArcCosh(Fnc):
    def __init__(self, a):
        super().__init__()
        self.name = "ArcCosh"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = arccosh(self.arg1.eval())
        return result


class ArcTanh(Fnc):
    def __init__(self, a):
        super().__init__()
        self.name = "ArcTanh"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = arctanh(self.arg1.eval())
        return result


FUNCS_TWO_ARG = [Add, Sub, Mul, Div, Pwr]
FUNCS_ONE_ARG = [Exp, \
                 Sin, Cos, Tan, \
                 ArcSin, ArcCos, ArcTan, \
                 Sinh, Cosh, Tanh, \
                 ArcSinh, ArcCosh, ArcTanh]
FUNCS_VAR_ARG = [Srt, Log]
