import math

from enerpy.base import *


# Add, subtract
def add(a, b):
	c = Num()
	c.val = a.val + b.val
	c.var = a.var + b.var
	return c

def sub(a, b):
	c = Num()
	c.val = a.val - b.val
	c.var = a.var + b.var
	return c


# Multiply, divide
def mul(a, b):
	c = Num()
	c.val = a.val * b.val
	c.var = math.pow(c.val, 2) * ((a.var / (math.pow(a.val, 2))) + (b.var / (math.pow(b.val, 2))))
	return c

def div(a, b):
	c = Num()
	c.val = a.val / b.val
	c.var = math.pow(c.val, 2) * ((a.var / (math.pow(a.val, 2))) + (b.var / (math.pow(b.val, 2))))
	return c


# Powers, logarithms
def pow(a, b):
	c = Num()
	c.val = math.pow(b.val, a.val)
	c.var = math.pow(c.val, 2) * (math.pow((b.val/a.val), 2) * a.var + math.pow(math.log(a.val), 2) * b.var)
	return c

def log(a, b):
	c = Num()
	c.val = math.log(a.val, b.val)
	c.var = math.pow(c.val, 2) * (a.var / (math.pow(a.val, 2) * math.pow(math.log(a.val), 2)) + b.var * (math.pow(b.val, 2) * math.pow(math.log(b.val), 2)))
	return c

