import math


class Node:
	def __init__(self):
		self.name = ""


class Num(Node):
	def __init__(self, a=0.0, b=0.0):
		super().__init__()
		self.val = a
		self.var = math.pow(b, 2)

	def eval(self):
		return self

	def sdv(self):
		sdv = math.sqrt(self.var)
		return sdv
	
	def print(self):
		print(str(round(self.val, 14)) + " +- " + str(round(self.sdv(), 14)))


class Var(Node):
	def __init__(self):
		super().__init__()


class Fnc(Node):
	def __init__(self):
		super().__init__()
		self.name = ""


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

