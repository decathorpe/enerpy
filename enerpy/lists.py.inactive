"""
enerpy/lists.py:
This module contains the class definition of a NumList.
"""

import math

from enerpy.base import Node, Num, enerfy


class NumList(Node, list):
    """
    enerpy.NumList:
    Data class containing a list of Nums.
    It is initialised with a list() of numbers, e. g. [1, 2] or [Num(2, 1), 1].
    """
    def __init__(self, nlist=None):
        super().__init__()
        if nlist is None:
            nlist = list()
        for i in nlist:
            self.append(i)

    def condense(self):
        """
        enerpy.NumList().condense():
        The .condense() method returns the mean and standard error of the list.
        """
        result = Num()
        length = len(self)

        list_sumn = 0
        for i in self:
            list_sumn = list_sumn + enerfy(i).val

        list_mean = list_sumn / length

        list_var = 0
        for i in self:
            list_var = list_var + math.pow(list_mean - enerfy(i).val, 2)

        valu_var = 0
        for i in self:
            valu_var = valu_var + enerfy(i).var

        mean_vars = (1 / (length * (length - 1))) * list_var
        valu_vars = (1 / math.pow(length, 2)) * valu_var

        result.val = list_mean
        result.var = mean_vars + valu_vars

        return result

    def prnt(self):
        """
        enerpy.NumList().prnt():
        The .prnt() method prints the NumList contents in a human-readable way.
        """
        for i in range(0, len(self)):
            print(str(i), ": ", end="")
            enerfy(self[i]).prnt()

