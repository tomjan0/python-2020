def flatten(l):
    """Generator spłaszczający listę"""
    for el in l:
        if type(el) == list:
            for _el in flatten(el):
                yield _el
        else:
            yield el
