from inspect import getfullargspec


class Overload:
    functions = {}

    def __init__(self, function):
        Overload.functions[(function.__name__, len(getfullargspec(function).args))] = function
        self.name = function.__name__

    def __call__(self, *args, **kwargs):
        return Overload.functions[(self.name, len(args))](*args, **kwargs)


def overload(function):
    return Overload(function)
