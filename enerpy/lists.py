import math

from enerpy.base import *
from enerpy.calc import *
from enerpy.funcs import *


class NumList(Node, list):
	def __init__(self, nlist=[]):
		super().__init__()
		for i in nlist:
			self.append(i)

	def condense(self):
		c = Num()
		n = len(self)
		
		list_sumn = 0
		for i in self:
			list_sumn = list_sumn + enerfy(i).val
		
		list_mean = list_sumn / n
		c.val = list_mean
		
		list_var = 0
		for i in self:
			list_var = list_var + math.pow(list_mean - enerfy(i).val, 2)
		
		valu_var = 0
		for i in self:
			valu_var = valu_var + enerfy(i).var
		
		mean_vars = (1 / (n * (n - 1))) * list_var
		valu_vars = (1 / math.pow(n, 2)) * valu_var
		
		c.var = mean_vars + valu_vars
		
		return c
	
	def prnt(self):
		for i in range(0, len(self)):
			print(str(i), ": ", end="")
			enerfy(self[i]).prnt()
