def qsort(l):
    """Funkcja wykonująca quick sort z użyciem składni funkcjonalnej"""
    if len(l) <= 1: 
        return l
    x, xs = l[0], l[1:]   
    higher = list(filter(lambda el: el >= x, xs))
    lower =  list(filter(lambda el: el < x, xs))
    return qsort(lower) + [x] + qsort(higher)