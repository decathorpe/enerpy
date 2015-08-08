import math

from enerpy.base import *

# Exponents and logarithms
def exp(a):
    assert isinstance(a, Num)
    c = Num()
    c.val = math.exp(a.val)
    c.var = math.pow(c.val, 2) * a.var
    return c

def log(a, b):
    assert isinstance(a, Num)
    assert isinstance(b, Num)
    c = Num()
    c.val = math.log(a.val, b.val)
    c.var = math.pow(c.val, 2) * ( (a.var) / (math.pow(a.val, 2) * math.pow(math.log(a.val), 2)) + (b.var) / (math.pow(b.val, 2) * math.pow(math.log(b.val), 2)) )
    return c


# Basic trigonometric functions
def sin(a):
    assert isinstance(a, Num)
    c = Num()
    c.val = math.sin(a.val)
    c.var = math.pow(math.cos(a.val), 2) * a.var
    return c

def cos(a):
    assert isinstance(a, Num)
    c = Num()
    c.val = math.cos(a.val)
    c.var = math.pow(math.sin(a.val), 2) * a.var
    return c

def tan(a):
    assert isinstance(a, Num)
    c = Num()
    c.val = math.tan(a.val)
    c.var = math.pow(math.cos(a.val), -4) * a.var
    return c


# Inverse trigonometric functions
def arcsin(a):
    assert isinstance(a, Num)
    c = Num()
    c.val = math.asin(a.val)
    c.var = (1 / (1 - math.pow(a.val, 2))) * a.var
    return c

def arccos(a):
    assert isinstance(a, Num)
    c = Num()
    c.val = math.acos(a.val)
    c.var = (1 / (1 - math.pow(a.val, 2))) * a.var
    return c

def arctan(a):
    assert isinstance(a, Num)
    c = Num()
    c.val = math.atan(a.val)
    c.var = (1 / math.pow(1 + math.pow(a.val, 2), 2)) * a.var
    return c


# Hyperbolic trigonometric functions
def sinh(a):
    assert isinstance(a, Num)
    c = Num()
    c.val = math.sinh(a.val)
    c.var = math.pow(math.cosh(a.val), 2) * a.var
    return c

def cosh(a):
    assert isinstance(a, Num)
    c = Num()
    c.val = math.cosh(a.val)
    c.var = math.pow(math.sinh(a.val), 2) * a.var
    return c

def tanh(a):
    assert isinstance(a, Num)
    c = Num()
    c.val = math.tanh(a.val)
    c.var = math.pow(math.cosh(a.val), -4)
    return c


# Inverse hyperbolic functions
def arcsinh(a):
    assert isinstance(a, Num)
    c = Num()
    c.val = math.asinh(a.val)
    c.var = (1 / (1 + math.pow(a.val, 2))) * a.var
    return c

def arccosh(a):
    assert isinstance(a, Num)
    c = Num()
    c.val = math.acosh(a.val)
    c.var = (1 / (math.pow(a.val, 2) - 1)) * a.var
    return c

def arctanh(a):
    assert isinstance(a, Num)
    c = Num()
    c.val = math.atanh(a.val)
    c.var = (1 / math.pow(1 - math.pow(a.val, 2), 2)) * a.var
    return c

