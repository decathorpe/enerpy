"""
enerpy/funcs.py:
This module contains all the function classes.
Arguments will be coerced to Num objects.
"""

import math

from enerpy.base import Fnc
from enerpy.base import enerfy

from enerpy.calc import add, sub, mul, div, pwr, log, exp
from enerpy.calc import sin, cos, tan, arcsin, arccos, arctan
from enerpy.calc import sinh, cosh, tanh, arcsinh, arccosh, arctanh


# Add, Sub classes
class Add(Fnc):
    """
    enerpy.Add:
    Function class to add two Nums.
    """
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
    """
    enerpy.Sub:
    Function class to subtract two Nums.
    """
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
    """
    enerpy.Mul:
    Function class to multiply two Nums.
    """
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
    """
    enerpy.Div:
    Function class to divide one Num by another.
    """
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
    """
    enerpy.Pwr:
    Function class to raise one Num to the power of another Num.
    """
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
class Root(Fnc):
    """
    enerpy.Root:
    Function class to get the Num-th root of another Num.
    Default is square root, other roots can be specified by optional second arg.
    """
    def __init__(self, a, b=2):
        super().__init__()
        self.name = "Root"

        a = enerfy(a)
        b = enerfy(b)

        self.arg1 = a
        self.arg2 = Div(1, b)

    def eval(self):
        result = pwr(self.arg1.eval(), self.arg2.eval())
        return result


# special case: exponent a, base e
class Exp(Fnc):
    """
    enerpy.Exp:
    Function class to get e to the Num-th power.
    """
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
    """
    enerpy.Log:
    Function class to get the logarithm of a Num, base Num.
    Default is base e, other bases can be specified by optional second arg.
    """
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
    """
    enerpy.Sin:
    Function class to get the Sine of a Num (input in radians).
    """
    def __init__(self, a):
        super().__init__()
        self.name = "Sin"

        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = sin(self.arg1.eval())
        return result


class Cos(Fnc):
    """
    enerpy.Cos:
    Function class to get the Cosine of a Num (input in radians).
    """
    def __init__(self, a):
        super().__init__()
        self.name = "Cos"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = cos(self.arg1.eval())
        return result


class Tan(Fnc):
    """
    enerpy.Tan:
    Function class to get the Tangent of a Num (input in radians).
    """
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
    """
    enerpy.ArcSin:
    Function class to get the inverse Sine of a Num (output in radians).
    """
    def __init__(self, a):
        super().__init__()
        self.name = "ArcSin"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = arcsin(self.arg1.eval())
        return result


class ArcCos(Fnc):
    """
    enerpy.ArcCos:
    Function class to get the inverse Cosine of a Num (output in radians).
    """
    def __init__(self, a):
        super().__init__()
        self.name = "ArcCos"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = arccos(self.arg1.eval())
        return result


class ArcTan(Fnc):
    """
    enerpy.ArcTan:
    Function class to get the inverse Tangent of a Num (output in radians).
    """
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
    """
    enerpy.Sinh:
    Function class to get the hyperbolic Sine of a Num.
    """
    def __init__(self, a):
        super().__init__()
        self.name = "Sinh"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = sinh(self.arg1.eval())
        return result


class Cosh(Fnc):
    """
    enerpy.Cosh:
    Function class to get the hyperbolic Cosine of a Num .
    """
    def __init__(self, a):
        super().__init__()
        self.name = "Cosh"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = cosh(self.arg1.eval())
        return result


class Tanh(Fnc):
    """
    enerpy.Sinh:
    Function class to get the hyperbolic Tangent of a Num.
    """
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
    """
    enerpy.ArcSinh:
    Function class to get the inverse hyperbolic Sine of a Num.
    """
    def __init__(self, a):
        super().__init__()
        self.name = "ArcSinh"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = arcsinh(self.arg1.eval())
        return result


class ArcCosh(Fnc):
    """
    enerpy.ArcCosh:
    Function class to get the inverse hyperbolic Cosine of a Num.
    """
    def __init__(self, a):
        super().__init__()
        self.name = "ArcCosh"
        a = enerfy(a)

        self.arg1 = a

    def eval(self):
        result = arccosh(self.arg1.eval())
        return result


class ArcTanh(Fnc):
    """
    enerpy.ArcTanh:
    Function class to get the inverse hyperbolic Tangent of a Num.
    # FIXME
    This might not return the correct result for the number's standard error.
    """
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
FUNCS_VAR_ARG = [Root, Log]
