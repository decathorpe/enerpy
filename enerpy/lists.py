"""
enerpy/lists.py
This module contains everything needed for calculations on lists.
"""

from decimal import Decimal as D

from enerpy import Node, Num, Fnc, enerfy
from enerpy import FUNCS_ONE_ARG1, FUNCS_TWO_ARG, FUNCS_VAR_ARG
from enerpy.extras import FUNCS_ONE_ARG2

FUNCS_ONE_ARG = FUNCS_ONE_ARG1 + FUNCS_ONE_ARG2


class NumList(Node, list):
    """
    enerpy.lists.NumList:
    Data class containing a list of Nums.
    It is initialised with a list() of numbers, e. g. [1, 2] or [Num(2, 1), 1].
    """
    def __init__(self, nlist=None):
        super().__init__()
        if nlist is None:
            nlist = list()
        for i in nlist:
            self.append(enerfy(i))

    def condense(self):
        """
        enerpy.lists.NumList.condense():
        The .condense() method returns the mean and standard error of the list.
        """
        result = Num()
        length = D(len(self))

        list_sumn = D(0)
        for i in self:
            list_sumn += + enerfy(i).val

        list_mean = list_sumn / length

        list_var = D(0)
        for i in self:
            list_var = list_var + (list_mean - enerfy(i).val) ** 2

        valu_var = D(0)
        for i in self:
            valu_var = valu_var + enerfy(i).var

        mean_vars = (1 / (length * (length - 1))) * list_var
        valu_vars = (1 / (length ** 2)) * valu_var

        result.val = list_mean
        result.var = mean_vars + valu_vars

        return result

    def eval(self):
        return self.condense()

    def __repr__(self):
        string = str()
        for i in range(0, len(self)):
            string += (str(i) + ": " + str(self[i]) + "\n")
        return string


def listify(candidate, length):
    """
    enerpy.lists.listify:
    This is the coersion function by which non-NumList-arguments to functions
    expecting NumLists are converted to NumList object.
    """
    # Do not create lists of lists erroneously
    if isinstance(candidate, list):
        return candidate

    return [candidate] * length


class ListFnc(Fnc, list):
    """
    enerpy.lists.ListFnc:
    This is the equivalent of a Fnc class for NumLists.
    It is initialised with a Fnc class, and, depending on how many arguments
    the function needs, one or two NumLists or Nums.
    Conversion to a list of Fnc instances is done at initialisation.
    At least one NumList is required, otherwise the Fnc itself should be used.
    Every ListFnc object can be evaluated to a NumList() containing
    all element-by-element results by use of the .eval() method.
    """
    def __init__(self, fnc, a, b=None):
        super().__init__()

        # FIX ME, NO IDEA WHY THIS DOES NOT WORK
        # This is why there is the CATCHME-else-clause at the end.
        # Check if fnc argument is an instance of the Fnc() class
        #if !isinstance(fnc, Fnc):
        #    raise TypeError("ListFnc requires a Fnc() class as fnc argument.")

        self.fnc = fnc

        # Check if neither a or b are lists
        if not isinstance(a, list) and not isinstance(b, list):
            raise TypeError("ListFnc should only be used for a list or two lists.")

        # Check for functions that accept only one argument
        if fnc in FUNCS_ONE_ARG:
            if b is not None:
                raise TypeError("This function only accepts one argument.")

            for i in range(0, len(a)):
                self.append(self.fnc(a[i]))

        # Check for functions that accept one or two arguments
        elif fnc in FUNCS_VAR_ARG:
            # No second argument
            if b is None:
                for i in range(0, len(a)):
                    self.append(self.fnc(a[i]))

            # Second argument already is a list
            elif isinstance(b, list):
                if len(a) is not len(b):
                    raise TypeError("Lists must be of equal length to perform functions on them.")

                for i in range(0, len(a)):
                    self.append(self.fnc(a[i], b[i]))

            # Second argument is not a list
            else:
                b = listify(b, len(a))
                for i in range(0, len(a)):
                    self.append(self.fnc(a[i], b[i]))

        # Check for functions that accept only two arguments
        elif fnc in FUNCS_TWO_ARG:
            if b is None:
                raise TypeError("This function requires two arguments.")

            # Listify non-list arguments
            if isinstance(a, list) and not isinstance(b, list):
                length = len(a)
                b = listify(b, length)

            if isinstance(b, list) and not isinstance(a, list):
                length = len(b)
                a = listify(a, length)

            if len(a) is not len(b):
                raise TypeError("Lists must be of equal length to perform functions on them.")

            for i in range(0, len(a)):
                self.append(self.fnc(a[i], b[i]))

        # CATCHME
        # Otherwise: Fnc does not seem to be supported, or fatal error
        else:
            raise TypeError("Either FATAL ERROR, or Fnc does not seem to be a supported function.")

    def __repr__(self):
        string = str()
        for i in range(0, len(self)):
            string += str(i) + ": " + repr(self[i]) + "\n"
        return string


    def eval(self):
        result = NumList()
        for i in range(0, len(self)):
            result.append(self[i].eval())
        return result

