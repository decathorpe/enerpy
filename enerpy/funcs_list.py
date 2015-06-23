from enerpy.base import *
from enerpy.calc import *
from enerpy.lists import *
from enerpy.funcs import *


class ListAdd(Fnc):
	def __init__(self, a, b):
		super().__init__()
		a = coerce(a)
		b = coerce(b)
		
		self.arg1 = a
		self.arg2 = b
	
	def eval(self):
		if isinstance(self.arg1, list) and isinstance(self.arg2, list):
			if len(self.arg1) != len(self.arg2):
				raise(TypeError("Lists must be of equal length to add them."))
			
			c = NumList()
			for i in len(self.arg1):
				c.append(Add(self.arg1[i], self.arg2[i]))
			return c
		
		if isinstance(self.arg1, list):
			c = NumList()
			for i in len(self.arg1):
				c.append(Add(coerce(self.arg1[i]), self.arg2))
			return c
		
		if isinstance(self.arg2, list):
			c = NumList()
			for i in len(self.arg2):
				c.append(Add(coerce(self.arg2[i]), self.arg1))
			return c

# TODO: Test case
