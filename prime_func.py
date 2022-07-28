import matplotlib.pyplot as plt
from math import factorial as fact


def Pf(x, m):
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

def desmos(x_min, x_max, m):
    if m < 0 or x_max <= x_min:
        print('Недопустимые вводные данные')
        return -1
    X = []; Y = []; x_p = x_min
    while (x_min <= x_p <= x_max):
        X.append(x_p)
        Y.append(Pf(x_p, m))
        x_p += (x_max - x_min) / 10 ** 3
    plt.plot(X, Y)
    plt.title('"Простая" функа ' + str(m) + '-го порядка производной')
    plt.show()
    return 0

try:
    desmos(float(input('Начало локальной области определения функи: ')),
        float(input('Конец локальной области определения функи: ')),
        int(input('Порядок производной функи: ')))
except OverflowError:
    print('При вычислении невозможно обработать слишком большие числа ...')
except ValueError:
    print('Недопустимые вводные данные ...')