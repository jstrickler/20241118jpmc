import pytest

from jpmc import sample_function
from jpmc import Jpmc

@pytest.fixture
def Jpmc_object():
    obj = Jpmc()
    return obj

def test_Jpmc_instance_has_sample_method(Jpmc_object):
    assert hasattr(Jpmc_object, "sample_method")

def test_jpmc_has_sample_function():
    assert sample_function() is None  # no return value
