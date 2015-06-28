from enerpy.base import *
from enerpy.calc import *
from enerpy.lists import *
from enerpy.funcs import *


class ListFnc(Fnc):
	def __init__(self, fnc, a, b):
		super().__init__()
		
		a = coerce(a)
		b = coerce(b)
		
		self.fnc = fnc
		self.arg1 = a
		self.arg2 = b
	
	def eval(self):
		if isinstance(self.arg1, list) and isinstance(self.arg2, list):
			if len(self.arg1) != len(self.arg2):
				raise(TypeError("Lists must be of equal length to add them."))
			
			c = NumList()
			for i in range(0, len(self.arg1)):
				c.append(self.fnc(self.arg1[i], self.arg2[i]).eval())
			return c
		
		if isinstance(self.arg1, list):
			c = NumList()
			for i in range(0, len(self.arg1)):
				c.append(self.fnc(coerce(self.arg1[i]), self.arg2).eval())
			return c
		
		if isinstance(self.arg2, list):
			c = NumList()
			for i in range(0, len(self.arg2)):
				c.append(self.fnc(coerce(self.arg2[i]), self.arg1).eval())
			return c

