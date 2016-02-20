"""
enerpy.extras
contains the functions that do not compute to arbitrary precision
"""

import math
from decimal import Decimal as D

from enerpy import Num, Fnc, enerfy, PREC, _PrecType

FUNCTIONS2 = ["Sin", "Cos", "Tan", "ArcSin", "ArcCos", "ArcTan"]
FUNCTIONS3 = ["Sinh", "Cosh", "Tanh", "ArcSinh", "ArcCosh", "ArcTanh"]

__all__ = FUNCTIONS2 + FUNCTIONS3


PREC.prec = _PrecType.MIN.value


# Sin, Cos, Tan classes
class Sin(Fnc):
    """
    enerpy.Sin:
    Function class to get the Sine of a Num (input in radians).
    """
    def __init__(self, a):
        super().__init__()
        self.arg1 = enerfy(a)

    def __repr__(self):
        return "sin(" + repr(self.arg1) + ")"

    def eval(self):
        a = self.arg1.eval()
        result = Num()
        result.val = D(math.sin(a.val))
        result.var = D(math.cos(a.val) ** 2) * a.var
        return result


class Cos(Fnc):
    """
    enerpy.Cos:
    Function class to get the Cosine of a Num (input in radians).
    """
    def __init__(self, a):
        super().__init__()
        self.arg1 = enerfy(a)

    def __repr__(self):
        return "cos(" + repr(self.arg1) + ")"

    def eval(self):
        a = self.arg1.eval()
        result = Num()
        result.val = D(math.cos(a.val))
        result.var = D(math.sin(a.val) ** 2) * a.var
        return result


class Tan(Fnc):
    """
    enerpy.Tan:
    Function class to get the Tangent of a Num (input in radians).
    """
    def __init__(self, a):
        super().__init__()
        self.arg1 = enerfy(a)

    def __repr__(self):
        return "tan(" + repr(self.arg1) + ")"

    def eval(self):
        a = self.arg1.eval()
        result = Num()
        result.val = D(math.tan(a.val))
        result.var = D(math.cos(a.val) ** -4) * a.var
        return result


# ArcSin, ArcCos, ArcTan classes
class ArcSin(Fnc):
    """
    enerpy.ArcSin:
    Function class to get the inverse Sine of a Num (output in radians).
    """
    def __init__(self, a):
        super().__init__()
        self.arg1 = enerfy(a)

    def __repr__(self):
        return "arcsin(" + repr(self.arg1) + ")"

    def eval(self):
        a = self.arg1.eval()
        result = Num()
        result.val = D(math.asin(a.val))
        result.var = (1 / (1 - (a.val ** 2))) * a.var
        return result


class ArcCos(Fnc):
    """
    enerpy.ArcCos:
    Function class to get the inverse Cosine of a Num (output in radians).
    """
    def __init__(self, a):
        super().__init__()
        self.arg1 = enerfy(a)

    def __repr__(self):
        return "arccos(" + repr(self.arg1) + ")"

    def eval(self):
        a = self.arg1.eval()
        result = Num()
        result.val = D(math.acos(a.val))
        result.var = (1 / (1 - (a.val ** 2))) * a.var
        return result


class ArcTan(Fnc):
    """
    enerpy.ArcTan:
    Function class to get the inverse Tangent of a Num (output in radians).
    """
    def __init__(self, a):
        super().__init__()
        self.arg1 = enerfy(a)

    def __repr__(self):
        return "arctan(" + repr(self.arg1) + ")"

    def eval(self):
        a = self.arg1.eval()
        result = Num()
        result.val = D(math.atan(a.val))
        result.var = (1 / (1 + (a.val ** 2) ** 2)) * a.var
        return result


# Sinh, Cosh, Tanh classes
class Sinh(Fnc):
    """
    enerpy.Sinh:
    Function class to get the hyperbolic Sine of a Num.
    """
    def __init__(self, a):
        super().__init__()
        self.arg1 = enerfy(a)

    def __repr__(self):
        return "sinh(" + repr(self.arg1) + ")"

    def eval(self):
        a = self.arg1.eval()
        result = Num()
        result.val = D(math.sinh(a.val))
        result.var = D(math.cosh(a.val) ** 2) * a.var
        return result


class Cosh(Fnc):
    """
    enerpy.Cosh:
    Function class to get the hyperbolic Cosine of a Num .
    """
    def __init__(self, a):
        super().__init__()
        self.arg1 = enerfy(a)

    def __repr__(self):
        return "cosh(" + repr(self.arg1) + ")"

    def eval(self):
        a = self.arg1.eval()
        result = Num()
        result.val = D(math.cosh(a.val))
        result.var = D(math.sinh(a.val) ** 2) * a.var
        return result


class Tanh(Fnc):
    """
    enerpy.Sinh:
    Function class to get the hyperbolic Tangent of a Num.
    """
    def __init__(self, a):
        super().__init__()
        self.arg1 = enerfy(a)

    def __repr__(self):
        return "tanh(" + repr(self.arg1) + ")"

    def eval(self):
        a = self.arg1.eval()
        result = Num()
        result.val = D(math.tanh(a.val))
        result.var = D(((2 * math.cosh(a.val)) / (math.cosh(2 * a.val) + 1)) ** 2) * a.var
        return result


# ArcSinh, ArcCosh, ArcTanh classes
class ArcSinh(Fnc):
    """
    enerpy.ArcSinh:
    Function class to get the inverse hyperbolic Sine of a Num.
    """
    def __init__(self, a):
        super().__init__()
        self.arg1 = enerfy(a)

    def __repr__(self):
        return "arcsinh(" + repr(self.arg1) + ")"

    def eval(self):
        a = self.arg1.eval()
        result = Num()
        result.val = D(math.asinh(a.val))
        result.var = (1 / (1 + a.val ** 2)) * a.var
        return result


class ArcCosh(Fnc):
    """
    enerpy.ArcCosh:
    Function class to get the inverse hyperbolic Cosine of a Num.
    """
    def __init__(self, a):
        super().__init__()
        self.arg1 = enerfy(a)

    def __repr__(self):
        return "arccosh(" + repr(self.arg1) + ")"

    def eval(self):
        a = self.arg1.eval()
        result = Num()
        result.val = D(math.acosh(a.val))
        result.var = (1 / (a.val ** 2 - 1)) * a.var
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
        self.arg1 = enerfy(a)

    def __repr__(self):
        return "arctanh(" + repr(self.arg1) + ")"

    def eval(self):
        a = self.arg1.eval()
        result = Num()
        result.val = D(math.atanh(a.val))
        result.var = (1 / ((1 - (a.val ** 2)) ** 2)) * a.var
        return result


FUNCS_ONE_ARG2 = [Sin, Cos, Tan,
                  ArcSin, ArcCos, ArcTan,
                  Sinh, Cosh, Tanh,
                  ArcSinh, ArcCosh, ArcTanh]

