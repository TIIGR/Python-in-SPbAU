import matplotlib.pyplot as plt
from math import factorial as fact


def Pf(x, eps):
    n = 0; taylor = n; p = 2
    while abs((p * x ** n) / fact(n)) >= eps:
        d = 2
        while p % d != 0:
            d += 1
        if p == d:
            n += 1
            taylor += (p * x ** n) / fact(n)
        p += 1
    return taylor

def desmos(x_min, x_max, eps):
    if (eps <= 0):
        print('Недопустимые вводные данные')
        return -1
    X = []; Y = []; x_p = x_min
    while (x_min <= x_p <= x_max):
        X.append(x_p)
        Y.append(Pf(x_p, eps))
        x_p += (x_max - x_min) / 1000
    plt.plot(X, Y)
    plt.title('"Простая" функа')
    plt.show()
    return 0

try:
    desmos(float(input('Начало локальной области определения функи: ')),
        float(input('Конец локальной области определения функи: ')),
        float(input('Погрешность значения функи: ')))
except ValueError:
    print('Недопустимые вводные данные (ValueError)')
except OverflowError:
    print('Недопустимые вводные данные (OverflowError)')