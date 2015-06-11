from enerpy.base import *

# coercible = list([Node, int, float, list, str])

coercible = list([int, float, Node])

def coerce(a):
	if isinstance(a, Node):
		return a
	elif isinstance(a, int):
		return Num(a, 0.0)
	elif isinstance(a, float):
		return Num(a, 0.0)
	else:
		raise(TypeError("Argument is not of any supported type."))

