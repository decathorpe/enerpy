"""
enerpy/base.py
This module defines the basic classes and methods.
It can be used standalone for basic arithmetic operations.
Functions other than +, -, *. /, **, etc. are included in rpmST/funcs.py.
"""

import math


class Node:
    """
    class enerpy.Node:
    This is the base class of enerpy.
    Rvery number and function is a Node, and Nodes will form a tree.
    The Node tree is evaluated by invoking .eval() on the root of the tree.
    The only thing every Node has in common is its (optional) name.
    """
    def __init__(self):
        self.name = ""

    def __repr__(self):
        return "Node:" + self.name

    def eval(self):
        """
        enerpy.Node().eval():
        An empty Node only evaluates to an empty Node.
        """
        return self

    def prnt(self):
        """
        enerpy.Node().prnt():
        An empty Node will print only that it is an empty Node.
        """
        print(self)


class Num(Node):
    """
    class enerpy.Num:
    This is the number class of enerpy.
    Every number used in enerpy functionsis coerced to a Num object.
    Every Num object has a value and a variance (square of standard deviation).
    """
    def __init__(self, val=0.0, sdv=0.0):
        super().__init__()
        self.val = val
        self.var = math.pow(sdv, 2)

    def eval(self):
        return self

    def sdv(self):
        """
        enerpy.Num().sdv():
        The .sdv() method returns the standard deviation of the number in self.val.
        """
        sdv = math.sqrt(self.var)
        return sdv

    def __repr__(self):
        return str(round(self.val, 14)) + " +- " + str(round(self.sdv(), 14))

    def prnt(self):
        print(str(round(self.val, 14)) + " +- " + str(round(self.sdv(), 14)))

    # Binary operators
    def __add__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = self.val + other.val
        result.var = self.var + other.var
        return result

    def __radd__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = other.val + self.val
        result.var = other.var + self.var
        return result

    def __iadd__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = self.val + other.val
        result.var = self.var + other.var
        return result

    def __sub__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = self.val - other.val
        result.var = self.var + other.var
        return result

    def __rsub__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = other.val - self.val
        result.var = other.var + self.var
        return result

    def __isub__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = self.val - other.val
        result.var = self.var + other.var
        return result

    def __mul__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = self.val * other.val
        result.var = math.pow(result.val, 2) * \
                ((self.var / (math.pow(self.val, 2))) + \
                (other.var / (math.pow(other.val, 2))))
        return result

    def __rmul__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = self.val * other.val
        result.var = math.pow(result.val, 2) * \
                ((self.var / (math.pow(self.val, 2))) + \
                (other.var / (math.pow(other.val, 2))))
        return result

    def __imul__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = self.val * other.val
        result.var = math.pow(result.val, 2) * \
                ((self.var / (math.pow(self.val, 2))) + \
                (other.var / (math.pow(other.val, 2))))
        return result

    def __truediv__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = self.val / other.val
        result.var = math.pow(result.val, 2) * \
                ((self.var / (math.pow(self.val, 2))) + \
                (other.var / (math.pow(other.val, 2))))
        return result

    def __rtruediv__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = other.val / self.val
        result.var = math.pow(result.val, 2) * \
                ((self.var / (math.pow(self.val, 2))) +
                 (other.var / (math.pow(other.val, 2))))
        return result

    def __itruediv__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = self.val / other.val
        result.var = math.pow(result.val, 2) *\
                ((self.var / (math.pow(self.val, 2))) + \
                (other.var / (math.pow(other.val, 2))))
        return result

    def __pow__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = self.val ** other.val
        result.var = math.pow(result.val, 2) * \
                (math.pow(other.val/self.val, 2) * self.var + \
                math.pow(math.log(self.val), 2) * other.var)
        return result

    def __rpow__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = self.val ** other.val
        result.var = math.pow(result.val, 2) * \
                (math.pow(self.val/other.val, 2) * other.var + \
                math.pow(math.log(other.val), 2) * self.var)
        return result

    def __ipow__(self, other):
        other = enerfy(other)
        result = Num()
        result.val = self.val ** other.val
        result.var = math.pow(result.val, 2) * \
                (math.pow(other.val/self.val, 2) * self.var + \
                math.pow(math.log(self.val), 2) * other.var)
        return result

    # Unary operators
    def __neg__(self):
        result = Num()
        result.val = -math.fabs(self.val)
        result.var = self.var
        return result

    def __pos__(self):
        result = Num()
        result.val = +math.fabs(self.val)
        result.var = self.var
        return result

    def __abs__(self):
        result = Num()
        result.val = math.fabs(self.val)
        result.var = self.var
        return result

    # Comparisons
    def __lt__(self, other):
        other = enerfy(other)
        if self.val < other.val:
            return True
        else:
            return False

    def __le__(self, other):
        other = enerfy(other)
        if self.val <= other.val:
            return True
        else:
            return False

    def __eq__(self, other):
        other = enerfy(other)
        if round(self.val, 14) == round(other.val, 14) and \
           round(self.var, 14) == round(other.var, 14):
            return True
        else:
            return False

    def __ne__(self, other):
        other = enerfy(other)
        if round(self.val, 14) != round(other.val, 14):
            return True
        else:
            return False

    def __gt__(self, other):
        other = enerfy(other)
        if self.val > other.val:
            return True
        else:
            return False

    def __ge__(self, other):
        other = enerfy(other)
        if self.val >= other.val:
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


def enerfy(candicate):
    """
    enerpy.enerfy:
    This is the coersion function by which non-Num-arguments to functions are
    converted to a Num object themselves.
    """
    if isinstance(candicate, list):
        return candicate.condense()

    if isinstance(candicate, Node):
        return candicate

    if isinstance(candicate, int):
        return Num(candicate, 0.0)

    if isinstance(candicate, float):
        return Num(candicate, 0.0)

    raise TypeError("Argument is not of any supported type.")

