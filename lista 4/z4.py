import math
from inspect import getfullargspec
from collections import defaultdict


class Overload:
    functions = {}

    def __init__(self, function):
        self.functions = Overload.functions[function.__name__]
        if self.functions is None:
            self.functions = {}
        self.functions[len(getfullargspec(function).args)] = function

    def __call__(self, *args, **kwargs):
        return self.functions[len(args)](*args, **kwargs)


def overload(function):
    return Overload(function)


@overload
def norm(x, y):
    return math.sqrt(x * x + y * y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


@overload
def x(a):
    print(a)


@overload
def x(a, b):
    print(a, b)


print(norm(2, 4))
print(norm(2, 3, 4))
print(x(4, 1))
