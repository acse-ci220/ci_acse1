import pytest
import numpy as np

from simple_functions import my_sum
from simple_functions.functions1 import factorial
from simple_functions.sine_compute import sin


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('number, expected', [
        (40, 0.642787609),
        (30, 0.5)
    ])
    def test_sin_x(self, number, expected):
        num = sin(number)

        assert np.isclose(num, expected)
