"""
enerpy
gaussian error propagation with arbitrary precision, using the decimal module
"""

from enum import Enum

from decimal import Decimal as D
from decimal import getcontext


FUNCTIONS1 = ["Add", "Sub", "Mul", "Div", "Pwr", "Root", "Exp", "Log"]


# Importing enerpy with "from enerpy import *" will only include precise functions
# Trigonometric functions (not available with arbitrary precision) have to be
#   included seperately.

__all__ = ["Num"] + FUNCTIONS1


# Default precision for the enerpy module is 50 but can be overridden after import

getcontext().prec = 50

DECIMAL_E = D(1).exp()


class Node:
    """
    class enerpy.Node:
    This is the base class of enerpy.
    Rvery number and function is a Node, and Nodes will form a tree.
    The Node tree is evaluated by invoking .eval() on the root of the tree.
    The only thing every Node has in common is its (optional) name.
    """
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def eval(self):
        """
        enerpy.Node().eval():
        This method evaluates the value of the node.
        - If the node is a number, it returns itself.
        - If the node is a function, it returns its evaluated value.
        - Evaluation of nodes is recursive and works for Node trees, as expected.
        """
        pass


class Num(Node):
    """
    class enerpy.Num:
    This is the number class of enerpy.
    Every number used in enerpy functionsis coerced to a Num object.
    Every Num object has a value and a variance (square of standard deviation).
    """
    def __init__(self, val=D(0), sdv=D(0)):
        super().__init__()
        if isinstance(val, D):
            self.val = val
        else:
            self.val = D(val)

        if isinstance(sdv, D):
            self.var = sdv ** D(2)
        else:
            self.var = D(sdv) ** D(2)

    def eval(self):
        return self

    def sdv(self):
        """
        enerpy.Num().sdv():
        The .sdv() method returns the standard deviation of the number in self.val.
        """
        sdv = self.var.sqrt()
        return sdv

    def __repr__(self):
        if self.var == 0:
            return str(self.val)
        else:
            return str(self.val) + " ~ " + str(self.sdv())

    # Binary operators
    def __add__(self, other):
        return Add(self, other)

    def __radd__(self, other):
        return Add(other, self)

    def __iadd__(self, other):
        return Add(self, other)

    def __sub__(self, other):
        return Sub(self, other)

    def __rsub__(self, other):
        return Sub(other, self)

    def __isub__(self, other):
        return Sub(self, other)

    def __mul__(self, other):
        return Mul(self, other)

    def __rmul__(self, other):
        return Mul(other, self)

    def __imul__(self, other):
        return Mul(self, other)

    def __truediv__(self, other):
        return Div(self, other)

    def __rtruediv__(self, other):
        return Div(other, self)

    def __itruediv__(self, other):
        return Div(self, other)

    def __pow__(self, other):
        return Pwr(self, other)

    def __rpow__(self, other):
        return Pwr(other, self)

    def __ipow__(self, other):
        return Pwr(self, other)

    # Unary operators
    def __abs__(self):
        result = Num()
        result.val = abs(self.val)
        result.var = self.var
        return result

    def __neg__(self):
        result = Num()
        result.val = -abs(self.val)
        result.var = self.var
        return result

    def __pos__(self):
        result = Num()
        result.val = +abs(self.val)
        result.var = self.var
        return result

    # Comparisons
    def __lt__(self, other):
        other = enerfy(other)
        if self.eval().val < other.eval().val:
            return True
        else:
            return False

    def __le__(self, other):
        other = enerfy(other)
        if self.eval().val <= other.eval().val:
            return True
        else:
            return False

    def __eq__(self, other):
        other = enerfy(other)
        if round(self.eval().val, 14) == round(other.eval().val, 14) and \
           round(self.eval().var, 14) == round(other.eval().var, 14):
            return True
        else:
            return False

    def __ne__(self, other):
        other = enerfy(other)
        if round(self.eval().val, 14) != round(other.eval().val, 14):
            return True
        else:
            return False

    def __gt__(self, other):
        other = enerfy(other)
        if self.eval().val > other.eval().val:
            return True
        else:
            return False

    def __ge__(self, other):
        other = enerfy(other)
        if self.eval().val >= other.eval().val:
            return True
        else:
            return False


class Fnc(Node):
    """
    class enerpy.Fnc:
    This is the function class of enerpy.
    Every function object can be evaluated to a Num() by use of the .eval() method.
    """
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return repr(self.eval())


def enerfy(candidate):
    """
    enerpy.enerfy:
    This is the coersion function by which non-Num-arguments to functions are
    converted to a Num object themselves.
    """

    if isinstance(candidate, Node):
        return candidate

    if isinstance(candidate, int):
        return Num(D(candidate), D(0))

    if isinstance(candidate, float):
        return Num(D(candidate), D(0))

    if isinstance(candidate, D):
        return Num(candidate, D(0))

    if isinstance(candidate, str):
        return Num(D(candidate), D(0))

    raise TypeError("Argument is not of any supported type.")



# Add, Sub classes
class Add(Fnc):
    """
    enerpy.Add:
    Function class to add two Nums.
    """
    def __init__(self, a, b):
        super().__init__()

        self.arg1 = enerfy(a)
        self.arg2 = enerfy(b)

    def __repr__(self):
        return repr(self.arg1) + " + " + repr(self.arg2)

    def eval(self):
        a = self.arg1.eval()
        b = self.arg2.eval()
        result = Num()
        result.val = a.val + b.val
        result.var = a.var + b.var
        return result


class Sub(Fnc):
    """
    enerpy.Sub:
    Function class to subtract two Nums.
    """
    def __init__(self, a, b):
        super().__init__()

        self.arg1 = enerfy(a)
        self.arg2 = enerfy(b)

    def __repr__(self):
        return repr(self.arg1) + " - (" + repr(self.arg2) + ")"

    def eval(self):
        a = self.arg1.eval()
        b = self.arg2.eval()
        result = Num()
        result.val = a.val - b.val
        result.var = a.var + b.var
        return result


# Mul, Div classes
class Mul(Fnc):
    """
    enerpy.Mul:
    Function class to multiply two Nums.
    """
    def __init__(self, a, b):
        super().__init__()

        self.arg1 = enerfy(a)
        self.arg2 = enerfy(b)

    def __repr__(self):
        return repr(self.arg1) + " - (" + repr(self.arg2) + ")"

    def eval(self):
        a = self.arg1.eval()
        b = self.arg2.eval()
        result = Num()
        result.val = a.val * b.val
        result.var = (result.val ** D(2)) * \
                ((a.var / (a.val ** D(2))) + \
                (b.var / (b.val ** D(2))))
        return result


class Div(Fnc):
    """
    enerpy.Div:
    Function class to divide one Num by another.
    """
    def __init__(self, a, b):
        super().__init__()

        self.arg1 = enerfy(a)
        self.arg2 = enerfy(b)

    def __repr__(self):
        return repr(self.arg1) + " / (" + repr(self.arg2) + ")"

    def eval(self):
        a = self.arg1.eval()
        b = self.arg2.eval()
        result = Num()
        result.val = a.val / b.val
        result.var = (result.val ** D(2)) * \
                ((a.var / (a.val ** D(2))) + \
                (b.var / (b.val ** D(2))))
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

        self.arg1 = enerfy(a)
        self.arg2 = enerfy(b)

    def __repr__(self):
        return repr(self.arg1) + " ^ (" + repr(self.arg2) + ")"

    def eval(self):
        a = self.arg1.eval()
        b = self.arg2.eval()
        result = Num()
        result.val = a.val ** b.val
        result.var = (result.val ** D(2)) * \
                    (((b.val/a.val) ** D(2)) * a.var + \
                      ((a.val).ln() ** D(2)) * b.var)
        return result


# special case: (square) roots
class Root(Pwr):
    """
    enerpy.Root:
    Function class to get the Num-th root of another Num.
    Default is square root, other roots can be specified by optional second arg.
    """
    def __init__(self, a, b=D(2)):
        b = D(1) / b
        super().__init__(a, b)

        self.square = None

        if b == D(2):
            self.square = True
        else:
            self.square = False

    def __repr__(self):
        if self.square:
            return repr(self.arg1) + " sqrt(" + repr(self.arg2) + ")"
        else:
            return repr(self.arg1) + " root(" + repr(self.arg2) + ")(" + repr(self.arg2) + ")"


# special case: exponent a, base e
class Exp(Pwr):
    """
    enerpy.Exp:
    Function class to get e to the Num-th power.
    """
    def __init__(self, a):
        b = Num(D(1).exp(), D(0))
        super().__init__(b, a)

    def __repr__(self):
        return "exp(" + repr(self.arg2) + ")"


class LogType(Enum):
    """
    enerpy.funcs.LogType
    enum defining the Type of log function (natural, decimal, normal)
    """
    NOR = 0
    NAT = 1
    DEC = 2


# generic logarithm: argument a, base b (default: D(1).exp())
class Log(Fnc):
    """
    enerpy.Log:
    Function class to get the logarithm of a Num, base Num.
    Default is base Euler's Number "e", other bases can be specified by the
        optional second argument.
    """
    def __init__(self, a, b=DECIMAL_E):
        super().__init__()

        self.type = None

        if b == DECIMAL_E:
            b = enerfy(DECIMAL_E)
            self.type = LogType.NAT
        elif b == D(10):
            self.type = LogType.DEC
        else:
            self.type = LogType.NOR

        self.arg1 = enerfy(a)
        self.arg2 = enerfy(b)

    def __repr__(self):
        if self.type == LogType.NAT:
            return "ln(" + repr(self.arg1) + ")"
        elif self.type == LogType.DEC:
            return "lg(" + repr(self.arg1) + ")"
        else:
            return "log(" + repr(self.arg2) + ")(" + repr(self.arg1) + ")"

    def eval(self):
        a = self.arg1.eval()
        b = self.arg2.eval()

        result = Num()

        if self.type == LogType.NAT:
            # ATTENTION: This simplified and faster path ignores arg2 and
            # assumes that Euler's Number has .var == 0
            result.val = a.val.ln()
            result.var = a.var / (a.val ** D(2))
            return result

        elif self.type == LogType.DEC:
            # ATTENTION: This simplified and faster path ignores arg2 and
            # assumes that 10 has .var == 0
            result.val = a.val.ln()
            result.var = (1 / ((D(10).ln()) ** D(2))) * (a.var / (a.val ** D(2)))
            return result

        elif self.type == LogType.NOR:
            result.val = a.val.ln() / b.val.ln()
            result.var = (result.val ** 2) * ((1 / (a.val.ln() ** 2)) * (a.var / (a.val ** 2)) + \
                                              (1 / (b.val.ln() ** 2)) * (b.var / (b.val ** 2)))
            return result

        else:
            print("Error occurred, cannot continue.")
            raise SystemExit


FUNCS_TWO_ARG = [Add, Sub, Mul, Div, Pwr]
FUNCS_ONE_ARG1 = [Exp]
FUNCS_VAR_ARG = [Root, Log]

