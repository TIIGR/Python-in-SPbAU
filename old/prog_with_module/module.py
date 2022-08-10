_fib_cache = {1: 1, 2: 1}


def fib(p):
    result = _fib_cache.get(p)
    if result is None:
        result = fib(p - 2) + fib(p - 1)
        _fib_cache[p] = result
    return result
