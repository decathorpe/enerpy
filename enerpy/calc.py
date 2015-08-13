"""
enerpy.base.py:
This module contains all the math neccessary.
Arguments are expected to be Num objects.
"""

import math

from enerpy.base import Num


# Add, subtract
def add(arg1, arg2):
    """
    enerpy.add:
    Function to add two Nums.
    """
    assert isinstance(arg1, Num)
    assert isinstance(arg2, Num)
    result = Num()
    result.val = arg1.val + arg2.val
    result.var = arg1.var + arg2.var
    return result

def sub(arg1, arg2):
    """
    enerpy.sub:
    Function to subtract two Nums.
    """
    assert isinstance(arg1, Num)
    assert isinstance(arg2, Num)
    result = Num()
    result.val = arg1.val - arg2.val
    result.var = arg1.var + arg2.var
    return result


# Multiply, divide
def mul(arg1, arg2):
    """
    enerpy.mul:
    Function to multiply two Nums.
    """
    assert isinstance(arg1, Num)
    assert isinstance(arg2, Num)
    result = Num()
    result.val = arg1.val * arg2.val
    result.var = math.pow(result.val, 2) * \
            ((arg1.var / (math.pow(arg1.val, 2))) + \
            (arg2.var / (math.pow(arg2.val, 2))))
    return result

def div(arg1, arg2):
    """
    enerpy.div:
    Function to divide two Nums.
    """
    assert isinstance(arg1, Num)
    assert isinstance(arg2, Num)
    result = Num()
    result.val = arg1.val / arg2.val
    result.var = math.pow(result.val, 2) * \
            ((arg1.var / (math.pow(arg1.val, 2))) + \
            (arg2.var / (math.pow(arg2.val, 2))))
    return result


# Powers, logarithms
def pwr(arg1, arg2):
    """
    enerpy.pow:
    Function to return a to the power b.
    """
    assert isinstance(arg1, Num)
    assert isinstance(arg2, Num)
    result = Num()
    result.val = math.pow(arg1.val, arg2.val)
    result.var = math.pow(result.val, 2) * \
                (math.pow(arg2.val/arg1.val, 2) * \
                arg1.var + math.pow(math.log(arg1.val), 2) * arg2.var)
    return result

def exp(arg1):
    """
    enerpy.exp:
    Function to return e to the a.
    """
    assert isinstance(arg1, Num)
    result = Num()
    result.val = math.exp(arg1.val)
    result.var = math.pow(result.val, 2) * arg1.var
    return result

def log(arg1, arg2):
    """
    enerpy.log:
    Function to return log a, base b.
    """
    assert isinstance(arg1, Num)
    assert isinstance(arg2, Num)
    result = Num()
    result.val = math.log(arg1.val, arg2.val)
    result.var = math.pow(result.val, 2) * \
            ((arg1.var) / (math.pow(arg1.val, 2) * math.pow(math.log(arg1.val), 2)) + \
            (arg2.var) / (math.pow(arg2.val, 2) * math.pow(math.log(arg2.val), 2)))
    return result


# Basic trigonometric functions
def sin(arg1):
    """
    enerpy.sin:
    Function to return sin a.
    """
    assert isinstance(arg1, Num)
    result = Num()
    result.val = math.sin(arg1.val)
    result.var = math.pow(math.cos(arg1.val), 2) * arg1.var
    return result

def cos(arg1):
    """
    enerpy.cos:
    Function to return cos a.
    """
    assert isinstance(arg1, Num)
    result = Num()
    result.val = math.cos(arg1.val)
    result.var = math.pow(math.sin(arg1.val), 2) * arg1.var
    return result

def tan(arg1):
    """
    enerpy.tan:
    Function to return tan a.
    """
    assert isinstance(arg1, Num)
    result = Num()
    result.val = math.tan(arg1.val)
    result.var = math.pow(math.cos(arg1.val), -4) * arg1.var
    return result


# Inverse trigonometric functions
def arcsin(arg1):
    """
    enerpy.arcsin:
    Function to return arcsin a.
    """
    assert isinstance(arg1, Num)
    result = Num()
    result.val = math.asin(arg1.val)
    result.var = (1 / (1 - math.pow(arg1.val, 2))) * arg1.var
    return result

def arccos(arg1):
    """
    enerpy.arccos:
    Function to return arccos a.
    """
    assert isinstance(arg1, Num)
    result = Num()
    result.val = math.acos(arg1.val)
    result.var = (1 / (1 - math.pow(arg1.val, 2))) * arg1.var
    return result

def arctan(arg1):
    """
    enerpy.arctan:
    Function to return arctan a.
    """
    assert isinstance(arg1, Num)
    result = Num()
    result.val = math.atan(arg1.val)
    result.var = (1 / math.pow(1 + math.pow(arg1.val, 2), 2)) * arg1.var
    return result


# Hyperbolic trigonometric functions
def sinh(arg1):
    """
    enerpy.sinh:
    Function to return sinh a.
    """
    assert isinstance(arg1, Num)
    result = Num()
    result.val = math.sinh(arg1.val)
    result.var = math.pow(math.cosh(arg1.val), 2) * arg1.var
    return result

def cosh(arg1):
    """
    enerpy.cosh:
    Function to return cosh a.
    """
    assert isinstance(arg1, Num)
    result = Num()
    result.val = math.cosh(arg1.val)
    result.var = math.pow(math.sinh(arg1.val), 2) * arg1.var
    return result

def tanh(arg1):
    """
    enerpy.tanh:
    Function to return tanh a.
    """
    assert isinstance(arg1, Num)
    result = Num()
    result.val = math.tanh(arg1.val)
    result.var = math.pow((2 * math.cosh(arg1.val)) / \
            (math.cosh(2 * arg1.val) + 1), 2) * arg1.var
    return result


# Inverse hyperbolic functions
def arcsinh(arg1):
    """
    enerpy.arcsinh:
    Function to return arcsinh a.
    """
    assert isinstance(arg1, Num)
    result = Num()
    result.val = math.asinh(arg1.val)
    result.var = (1 / (1 + math.pow(arg1.val, 2))) * arg1.var
    return result

def arccosh(arg1):
    """
    enerpy.arccosh:
    Function to return arccosh a.
    """
    assert isinstance(arg1, Num)
    result = Num()
    result.val = math.acosh(arg1.val)
    result.var = (1 / (math.pow(arg1.val, 2) - 1)) * arg1.var
    return result

def arctanh(arg1):
    """
    enerpy.arctanh:
    Function to return arctanh a.
    Error calculation is not correct, no idea why.
    """
    assert isinstance(arg1, Num)
    result = Num()
    result.val = math.atanh(arg1.val)
    result.var = (1 / math.pow(1 - math.pow(arg1.val, 2), 2)) * arg1.var
    return result

