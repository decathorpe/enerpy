from enerpy.base import *
from enerpy.calc import *
from enerpy.lists import *
from enerpy.funcs import *


def listify(num, length):
    # Do not create lists of lists erroneously
    if isinstance(num, list):
        return num

    tmp = list()
    for i in range(0, length):
        tmp.append(num)
    nlist = NumList(tmp)

    return nlist


class ListFnc(Fnc, list):
    def __init__(self, fnc, a, b=None):
        super().__init__()

        # FIXME, NO IDEA WHY THIS DOES NOT WORK
        # This is why there is the CATCHME-else-clause at the end.
        # Check if fnc argument is an instance of the Fnc() class
        #if not isinstance(fnc, Fnc):
        #    raise(TypeError("ListFnc requires a Fnc() class as fnc argument."))

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
                n = len(a)
                b = listify(b, n)

            if isinstance(b, list) and not isinstance(a, list):
                n = len(b)
                a = listify(a, n)

            if len(a) is not len(b):
                raise TypeError("Lists must be of equal length to perform functions on them.")

            for i in range(0, len(a)):
                self.append(self.fnc(a[i], b[i]))

        # CATCHME
        # Otherwise: Fnc does not seem to be supported, or fatal error
        else:
            raise TypeError("Either FATAL ERROR, or Fnc does not seem to be a supported function.")


    def eval(self):
        c = NumList()
        for i in range(0, len(self)):
            c.append(self[i].eval())
        return c

