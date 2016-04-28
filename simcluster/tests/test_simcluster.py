from simcluster import simulated_cluster
from .utils import compare_reference


@compare_reference
def test_defaults():
    return simulated_cluster()
