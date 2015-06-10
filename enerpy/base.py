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


class Var(Node):
	def __init__(self):
		super().__init__()


class Fnc(Node):
	def __init__(self):
		super().__init__()
