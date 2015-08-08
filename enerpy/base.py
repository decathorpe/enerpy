import math


class Node:
    def __init__(self):
        self.name = ""


class Num(Node):
    def __init__(self, val=0.0, sdv=0.0):
        super().__init__()
        self.val = val
        self.var = math.pow(sdv, 2)

    def eval(self):
        return self

    def sdv(self):
        sdv = math.sqrt(self.var)
        return sdv

    def prnt(self):
        print(str(round(self.val, 14)) + " +- " + str(round(self.sdv(), 14)))

    def __add__(self, other):
        c = Num()
        c.val = self.val + other.val
        c.var = self.var + other.var
        return c

    def __sub__(self, other):
        c = Num()
        c.val = self.val - other.val
        c.var = self.var + other.var
        return c

    def __mul__(self, other):
        c = Num()
        c.val = self.val * other.val
        c.var = math.pow(c.val, 2) * ((self.var / (math.pow(self.val, 2))) + (other.var / (math.pow(other.val, 2))))
        return c

    def __truediv__(self, other):
        c = Num()
        c.val = self.val / other.val
        c.var = math.pow(c.val, 2) * ((self.var / (math.pow(self.val, 2))) + (other.var / (math.pow(other.val, 2))))
        return c

"""
class Var(Node):
    def __init__(self):
        super().__init__()
"""

class Fnc(Node):
    def __init__(self):
        super().__init__()


def enerfy(a):
    if isinstance(a, list):
        return a.condense()

    if isinstance(a, Node):
        return a

    if isinstance(a, int):
        return Num(a, 0.0)

    if isinstance(a, float):
        return Num(a, 0.0)

    raise(TypeError("Argument is not of any supported type."))

