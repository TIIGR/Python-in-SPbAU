from math import *
from math import pi, e
from math import factorial as fact


def pf(x, m):
    n = 0;  taylor = n; p = 1
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

def relat(x):
    if x < 0:
        exit('Недопустимая область определения!')
    else:
        n = p = 0
        while n < floor(x):
            d = 2
            if p == 0:
                p += 1
                continue
            elif p == 1:
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
