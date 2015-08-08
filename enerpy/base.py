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

    def __repr__(self):
        return str(round(self.val, 14)) + " +- " + str(round(self.sdv(), 14))

    def prnt(self):
        print(str(round(self.val, 14)) + " +- " + str(round(self.sdv(), 14)))

    # Binary operators
    def __add__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = self.val + other.val
        c.var = self.var + other.var
        return c

    def __radd__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = other.val + self.val
        c.var = other.var + self.var
        return c

    def __iadd__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = self.val + other.val
        c.var = self.var + other.var
        return c

    def __sub__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = self.val - other.val
        c.var = self.var + other.var
        return c

    def __rsub__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = other.val - self.val
        c.var = other.var + self.var
        return c

    def __isub__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = self.val - other.val
        c.var = self.var + other.var
        return c

    def __mul__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = self.val * other.val
        c.var = math.pow(c.val, 2) * ((self.var / (math.pow(self.val, 2))) + (other.var / (math.pow(other.val, 2))))
        return c

    def __rmul__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = self.val * other.val
        c.var = math.pow(c.val, 2) * ((self.var / (math.pow(self.val, 2))) + (other.var / (math.pow(other.val, 2))))
        return c

    def __imul__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = self.val * other.val
        c.var = math.pow(c.val, 2) * ((self.var / (math.pow(self.val, 2))) + (other.var / (math.pow(other.val, 2))))
        return c

    def __truediv__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = self.val / other.val
        c.var = math.pow(c.val, 2) * ((self.var / (math.pow(self.val, 2))) + (other.var / (math.pow(other.val, 2))))
        return c

    def __rtruediv__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = other.val / self.val
        c.var = math.pow(c.val, 2) * ((self.var / (math.pow(self.val, 2))) + (other.var / (math.pow(other.val, 2))))
        return c

    def __itruediv__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = self.val / other.val
        c.var = math.pow(c.val, 2) * ((self.var / (math.pow(self.val, 2))) + (other.var / (math.pow(other.val, 2))))
        return c

    def __pow__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = self.val ** other.val
        c.var = math.pow(c.val, 2) * (math.pow(other.val/self.val, 2) * self.var + math.pow(math.log(self.val), 2) * other.var)
        return c

    def __rpow__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = self.val ** other.val
        c.var = math.pow(c.val, 2) * (math.pow(self.val/other.val, 2) * other.var + math.pow(math.log(other.val), 2) * self.var)
        return c

    def __ipow__(self, other):
        other = enerfy(other)
        c = Num()
        c.val = self.val ** other.val
        c.var = math.pow(c.val, 2) * (math.pow(other.val/self.val, 2) * self.var + math.pow(math.log(self.val), 2) * other.var)
        return c

    # Unary operators
    def __neg__(self):
        c = Num()
        c.val = -math.fabs(self.val)
        c.var = self.var
        return c

    def __pos__(self):
        c = Num()
        c.val = +math.fabs(self.val)
        c.var = self.var
        return c

    def __abs__(self):
        c = Num()
        c.val = math.fabs(self.val)
        c.var = self.var
        return c

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
        if (round(self.val, 14) == round(other.val, 14) and round(self.var, 14) == round(other.var, 14)):
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

