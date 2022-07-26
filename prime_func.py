import matplotlib.pyplot as plt
from math import factorial as fact


def Pf(x, eps):
    m = 0; taylor = m; p = 2
    while abs((p * x ** m) / fact(m)) >= eps:
        d = 2
        while p % d != 0:
            d += 1
        if p == d:
            m += 1
            taylor += (p * x ** m) / fact(m)
        p += 1
    return taylor

def desmos(x_min, x_max, step, eps):
    if (step <= 0 or eps <= 0):
        print('Недопустимые вводные данные')
        return -1
    X = []; Y = []; x_p = x_min
    while (x_min <= x_p <= x_max):
        X.append(x_p)
        Y.append(Pf(x_p, eps))
        x_p += step
    plt.plot(X, Y)
    plt.title('"Простая" функа')
    plt.show()
    return 0

try:
    desmos(float(input('Начало локальной области определения функи: ')),
        float(input('Конец локальной области определения функи: ')),
        float(input('Шаг построения точек функи: ')),
        float(input('Погрешность значения функи: ')))
except ValueError:
    print('Недопустимые вводные данные (ValueError)')
except OverflowError:
    print('Недопустимые вводные данные (OverflowError)')