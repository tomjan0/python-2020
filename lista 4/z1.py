def timed(func):
    from time import time

    def modified_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print('Execution time: ', time() - start, 's')
        return result

    return modified_func
