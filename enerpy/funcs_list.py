"""
enerpy/funcs_list.py:
This module contains all the functionality for dealing with lists of Nums.
The native type is NumList, and lists and numbers are coerced to it.
"""

from enerpy.base import Fnc
from enerpy.lists import NumList
from enerpy.funcs import FUNCS_ONE_ARG, FUNCS_TWO_ARG, FUNCS_VAR_ARG


def listify(num, length):
    """
    enerpy.listify:
    This is the coersion function by which non-NumList-arguments to functions
    expecting NumLists are converted to NumList object.
    """
    # Do not create lists of lists erroneously
    if isinstance(num, list):
        return num

    tmp = list()
    for i in range(0, length):
        tmp[i] = num
    nlist = NumList(tmp)

    return nlist


class ListFnc(Fnc, list):
    """
    enerpy.ListFnc:
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


    def eval(self):
        result = NumList()
        for i in range(0, len(self)):
            result.append(self[i].eval())
        return result

