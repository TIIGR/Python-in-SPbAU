from math import *
from math import pi, e
from math import factorial as fact
from random import *


def streplace(func):
    library = {
        '^': '**',
        'fi': '((1 + sqrt(5)) / 2)',
        'Pf(x)': 'pf(x, 0)'
    }
    for i, j in library.items():
        func = func.replace(i, j)
    return func

def pf(x, m):
    n = 0; taylor = n; p = 1
    while (abs((p * x ** abs(n - m)) / fact(abs(n - m))) >= 10 ** -6) or (n < m):
        d = 2
        while (n < m):
            d = 2
            p += 1
            while p % d != 0:
                d += 1
            if p == d:
                n += 1
        while (p % d != 0) and p != 1:
            d += 1
        if p == d and m == 0:
            n += 1
            taylor += (p * x ** n) / fact(n)
        elif p == d and m > 0:
            taylor += (p * x ** (n - m)) / fact(n - m)
            n += 1
        p += 1
    return taylor

def mcm(x):
    M, func, p = [], 0, 0
    if x < 1:
        exit('Недопустимая область определения!')
    while (2 ** p) % floor(x) not in M:
        M.append((2 ** p) % floor(x))
        func += (2 ** p) % floor(x)
        p += 1
    return (func % floor(x))

def relat(x):
    if x < 0:
        exit('Недопустимая область определения!')
    else:
        n = p = 0
        while n < floor(x):
            d = 2
            if p == 0 or p == 1:
                p += 1
                continue
            else:
                while (p % d != 0):
                    d += 1
                if p == d:
                    n += 1
                p += 1
    if p == 0:
        return p
    else:
        return ((p - 1) / fact(n))

def gaussf(x, a, b, c):
    return a * e ** -((x - b) ** 2 / (2 * c ** 2))