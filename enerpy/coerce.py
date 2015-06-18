import math

from enerpy.base import *
from enerpy.calc import *

# coercible = list([Node, int, float, list, str])

coercible = list([int, float, Node])

def coerce(a):
	if isinstance(a, Node):
		return a
	
	if isinstance(a, int):
		return Num(a, 0.0)
	
	if isinstance(a, float):
		return Num(a, 0.0)
	
	raise(TypeError("Argument is not of any supported type."))
