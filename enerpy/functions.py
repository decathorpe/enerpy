from enerpy.base import *

from enerpy.math_base import *
from enerpy.math_trig import *


class Add(Fnc):
	def __init__(self, a, b):
		super().__init__()
		self.arg1 = a
		self.arg2 = b
	
	def eval(self):
		c = add(self.arg1.eval(), self.arg2.eval())
		return c


class Sub(Fnc):
	def __init__(self, a, b):
		super().__init__()
		self.arg1 = a
		self.arg2 = b
	
	def eval(self):
		c = sub(self.arg1.eval(), self.arg2.eval())
		return c


class Mul(Fnc):
	def __init__(self, a, b):
		super().__init__()
		self.arg1 = a
		self.arg2 = b
	
	def eval(self):
		c = mul(self.arg1.eval(), self.arg2.eval())
		return c


class Div(Fnc):
	def __init__(self, a, b):
		super().__init__()
		self.arg1 = a
		self.arg2 = b
	
	def eval(self):
		c = div(self.arg1.eval(), self.arg2.eval())
		return c


class AddNew(Fnc):
	def __init__(self, a, b=None):
		super().__init__()
		
		if isinstance(a, Num) and isinstance(b, Num):
			self.arg1 = a
			self.arg2 = b
			self.argc = 2
		elif isinstance(a, Num) == True and isinstance(b, Num) != True:
			self.arg1 = a
			self.argc = 1
		elif isinstance(a, list):
			self.arg1 = a
			self.argc = len(a)
		else:
			raise(TypeError("Argument is not Num() or list()."))
	
	def eval(self):
		if isinstance(self.arg1, Num) and isinstance(self.arg2, Num):
			c = add(self.arg1, self.arg2)
			return c
		elif isinstance(a, Num) == True and isinstance(b, Num) != True:
			return self.arg1
		elif isinstance(self.arg1, list):
			c = addList(self.arg1)
			return c
		else:
			raise(TypeError("Argument is not Num() or list()."))

