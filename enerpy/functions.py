from enerpy.base import *
from enerpy.coerce import *
from enerpy.calc import *


# Add, Sub classes
class Add(Fnc):
	def __init__(self, a, b=Num(0, 0)):
		super().__init__()
		a = coerce(a)
		b = coerce(b)
		
		self.arg1 = a
		self.arg2 = b
	
	def eval(self):
		c = add(self.arg1.eval(), self.arg2.eval())
		return c


class Sub(Fnc):
	def __init__(self, a, b):
		super().__init__()
		a = coerce(a)
		b = coerce(b)
		
		self.arg1 = a
		self.arg2 = b
	
	def eval(self):
		c = sub(self.arg1.eval(), self.arg2.eval())
		return c


# Mul, Div classes
class Mul(Fnc):
	def __init__(self, a, b=Num(1, 0)):
		super().__init__()
		a = coerce(a)
		b = coerce(b)
		
		self.arg1 = a
		self.arg2 = b
	
	def eval(self):
		c = mul(self.arg1.eval(), self.arg2.eval())
		return c


class Div(Fnc):
	def __init__(self, a, b):
		super().__init__()
		a = coerce(a)
		b = coerce(b)
		
		self.arg1 = a
		self.arg2 = b
	
	def eval(self):
		c = div(self.arg1.eval(), self.arg2.eval())
		return c


# Pow, Log classes

# generic power: a raised to power b
class Pow(Fnc):
	def __init__(self, a, b):
		super().__init__()
		a = coerce(a)
		b = coerce(b)
		
		self.arg1 = a
		self.arg2 = b
	
	def eval(self):
		c = pow(self.arg1.eval(), self.arg2.eval())
		return c


# special case: (square) roots
class Roo(Fnc):
	def __init__(self, a, b=2):
		super().__init__()
		a = coerce(a)
		b = coerce(b)
		
		self.arg1 = a
		self.arg2 = Div(1, b)

	def eval(self):
		c = pow(self.arg1.eval(), self.arg2.eval())
		return c


# special case: exponent a, base e
class Exp(Fnc):
	def __init__(self, a):
		super().__init__()
		a = coerce(a)

		self.arg1 = a

	def eval(self):
		c = exp(self.arg1.eval())
		return c

# generic logarithm: argument a, base b
class Log(Fnc):
	def __init__(self, a, b):
		super().__init__()
		a = coerce(a)
		b = coerce(b)
		
		self.arg1 = a
		self.arg2 = b
	
	def eval(self):
		c = log(self.arg1.eval(), self.arg2.eval())
		return c


# Sin, Cos, Tan classes
class Sin(Fnc):
	def __init__(self, a):
		super().__init__()
		a = coerce(a)
		
		self.arg1 = a
	
	def eval(self):
		c = sin(self.arg1.eval())
		return c


class Cos(Fnc):
	def __init__(self, a):
		super().__init__()
		a = coerce(a)
		
		self.arg1 = a
	
	def eval(self):
		c = cos(self.arg1.eval())
		return c


class Tan(Fnc):
	def __init__(self, a):
		super().__init__()
		a = coerce(a)
		
		self.arg1 = a
	
	def eval(self):
		c = tan(self.arg1.eval())
		return c


# ArcSin, ArcCos, ArcTan classes
class ArcSin(Fnc):
	def __init__(self, a):
		super().__init__()
		a = coerce(a)
		
		self.arg1 = a
	
	def eval(self):
		c = arcsin(self.arg1.eval())
		return c


class ArcCos(Fnc):
	def __init__(self, a):
		super().__init__()
		a = coerce(a)
		
		self.arg1 = a
	
	def eval(self):
		c = arccos(self.arg1.eval())
		return c


class ArcTan(Fnc):
	def __init__(self, a):
		super().__init__()
		a = coerce(a)
		
		self.arg1 = a
	
	def eval(self):
		c = arctan(self.arg1.eval())
		return c


# Sinh, Cosh, Tanh classes
class Sinh(Fnc):
	def __init__(self, a):
		super().__init__()
		a = coerce(a)
		
		self.arg1 = a
	
	def eval(self):
		c = sinh(self.arg1.eval())
		return c


class Cosh(Fnc):
	def __init__(self, a):
		super().__init__()
		a = coerce(a)
		
		self.arg1 = a
	
	def eval(self):
		c = cosh(self.arg1.eval())
		return c


class Tanh(Fnc):
	def __init__(self, a):
		super().__init__()
		a = coerce(a)
		
		self.arg1 = a
	
	def eval(self):
		c = tanh(self.arg1.eval())
		return c


# ArcSinh, ArcCosh, ArcTanh classes
class ArcSinh(Fnc):
	def __init__(self, a):
		super().__init__()
		a = coerce(a)
		
		self.arg1 = a
	
	def eval(self):
		c = arcsinh(self.arg1.eval())
		return c


class ArcCosh(Fnc):
	def __init__(self, a):
		super().__init__()
		a = coerce(a)
		
		self.arg1 = a
	
	def eval(self):
		c = arccosh(self.arg1.eval())
		return c


class ArcTanh(Fnc):
	def __init__(self, a):
		super().__init__()
		a = coerce(a)
		
		self.arg1 = a
	
	def eval(self):
		c = arctanh(self.arg1.eval())
		return c
