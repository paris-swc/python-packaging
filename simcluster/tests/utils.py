import os
import types
import numpy as np


REFERENCE_PATH = os.path.join(os.path.dirname(__file__), 'refs')



class compare_reference(object):
    def __new__(cls, filename):
        if isinstance(filename, types.FunctionType):
            # No argument version; take the filename from the function
            # name
            func = filename
            filename = func.__name__
            inst = super(compare_reference, cls).__new__(cls)
            inst.__init__(filename)
            return inst(func)
        else:
            return super(compare_reference, cls).__new__(cls)

    def __init__(self, filename):
        self.filename = filename

    def __call__(self, func):
        def wrapper():
            # Wrap the function to always use the same RNG seed
            def func2():
                with NumpyRNGContext(0xF00D):
                    return func()

            filename = os.path.join(REFERENCE_PATH, self.filename) + '.npy'
            if not os.path.exists(filename):
                print("Regenerating reference file {0}".format(self.filename))
                os.makedirs(REFERENCE_PATH, exist_ok=True)
                ref = func2()
                np.save(filename, ref)
            else:
                ref = np.load(filename)

            assert np.all(ref == func2())

        return types.FunctionType(wrapper.__code__, wrapper.__globals__,
                                  func.__name__, (), wrapper.__closure__)


class NumpyRNGContext(object):
    """
    A context manager (for use with the ``with`` statement) that will seed the
    numpy random number generator (RNG) to a specific value, and then restore
    the RNG state back to whatever it was before.

    This is primarily intended for use in the astropy testing suit, but it
    may be useful in ensuring reproducibility of Monte Carlo simulations in a
    science context.

    Parameters
    ----------
    seed : int
        The value to use to seed the numpy RNG

    Examples
    --------
    A typical use case might be::

        with NumpyRNGContext(<some seed value you pick>):
            from numpy import random

            randarr = random.randn(100)
            ... run your test using `randarr` ...

        #Any code using numpy.random at this indent level will act just as it
        #would have if it had been before the with statement - e.g. whatever
        #the default seed is.


    """
    def __init__(self, seed):
        self.seed = seed

    def __enter__(self):
        from numpy import random

        self.startstate = random.get_state()
        random.seed(self.seed)

    def __exit__(self, exc_type, exc_value, traceback):
        from numpy import random

        random.set_state(self.startstate)
