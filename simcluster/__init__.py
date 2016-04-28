from .simcluster import *


def test():
    try:
        import pytest
    except ImportError:
        print("py.test is required to run the test suite for simcluster")
        return

    import os
    path = os.path.join(os.path.dirname(__file__), 'tests')
    os.chdir(path)
    pytest.main([os.path.relpath(path)])
