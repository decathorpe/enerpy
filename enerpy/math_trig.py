import math

from enerpy.base import *


# Basic trigonometric functions
def sin(a):
	c = Num()
	c.val = math.sin(a.val)
	c.var = math.pow(math.cos(a.val), 2) * a.var
	return c

def cos(a):
	c = Num()
	c.val = math.cos(a.val)
	c.var = math.pow(math.sin(a.val), 2) * a.var
	return c

def tan(a):
	c = Num()
	c.val = math.tan(a.val)
	c.var = math.pow(math.cos(a.val), -4) * a.var
	return c


# Inverse trigonometric functions
def arcsin(a):
	c = Num()
	c.val = math.asin(a.val)
	c.var = (1 / (1 - math.pow(a.val, 2))) * a.var
	return c

def arccos(a):
	c = Num()
	c.val = math.acos(a.val)
	c.var = (1 / (1 - math.pow(a.val, 2))) * a.var
	return c

def arctan(a):
	c = Num()
	c.val = math.atan(a.val)
	c.var = (1 / math.pow(1 + math.pow(a.val, 2), 2)) * a.var
	return c


# Hyperbolic trigonometric functions
def sinh(a):
	c = Num()
	c.val = math.sinh(a.val)
	c.var = math.pow(math.cosh(a.val), 2) * a.var
	return c

def cosh(a):
	c = Num()
	c.val = math.cosh(a.val)
	c.var = math.pow(math.sinh(a.val), 2) * a.var
	return c

def tanh(a):
	c = Num()
	c.val = math.tanh(a.val)
	c.var = math.pow(math.cosh(a.val), -4)
	return c


# Inverse hyperbolic functions
def arcsinh(a):
	c = Num()
	c.val = math.asinh(a.val)
	c.var = (1 / (1 + math.pow(a.val, 2))) * a.var
	return c

def arccosh(a):
	c = Num()
	c.val = math.acosh(a.val)
	c.var = (1 / (math.pow(a.val, 2) - 1)) * a.var
	return c

def arctanh(a):
	c = Num()
	c.val = math.atanh(a.val)
	c.var = (1 / math.pow(1 - math.pow(a.val, 2), 2)) * a.var
	return c

