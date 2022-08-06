from math import *
from math import pi, e
from math import factorial as fact
import matplotlib.pyplot as plt


def Pf(x, m):
    n = 0;  taylor = n; p = 1
    while (abs((p * x ** abs(n - m)) / fact(abs(n - m))) >= 10 ** -6) or (n < m):
        d = 2
        while n < m:
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


def pF(x, m):
    n = taylor = 0; p = 1
    while (abs((p * x ** abs(n - m))) >= 10 ** -6) or (n < m):
        d = 2
        while n < m:
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
            taylor += (p * x ** n)
        elif p == d and m > 0:
            taylor += (p * x ** (n - m))
            n += 1
        p += 1
    return taylor

def desmos(func, x_min, x_max):
    if x_max <= x_min:
        print('Недопустимые вводные данные')
        return -1
    X = []; Y = []; x = x_min; q = progress = 0
    while x_min <= x <= x_max:
        q += 1
        X.append(x)
        Y.append(eval(func.replace('^', '**')))
        if q % 10 == 0:
            progress += 1
            print('Loading progress: ' + f'{str(progress)}\r', end = '', flush = True)
        x += (x_max - x_min) / 10 ** 3
    plt.plot(X, Y)
    plt.title('F(x) = ' + func)
    plt.show()
    return 0

try:
    desmos(str(input('Введите функу (к примеру, e^x): ')),
        float(input('Начало локальной области определения функи: ')),
        float(input('Конец локальной области определения функи: ')))
except OverflowError:
    print('При вычислении невозможно обработать слишком большие числа ...')
except ValueError:
    print('Произошла ошибка при вычислении ...')
except NameError:
    print('Поддерживается только следующие функции и константы: pi, e, Pf(x, m) и другие стандартные функции ...')