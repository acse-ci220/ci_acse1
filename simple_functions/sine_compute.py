from numpy import sqrt
from simple_functions.functions1 import factorial
from functools import lru_cache
from simple_functions.constants import pi

__all__ = ['sin']


def sin(x):
    y = (x / 180) * pi()
    result = y - ((y ** 3) / factorial(3)) + ((y ** 5) / factorial(5)) - ((y ** 7) / factorial(7))
    return result
