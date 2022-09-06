from sympy import diff
from numpy import sign
from usrfuncs import *


def roots_for_func(func, x_min, x_max):
    if x_max <= x_min:
        exit('Недопустимые вводные данные')
    ROOTS = []; x = x_min
    dfunc = str(diff(func, 'x'))
    while (x_min <= x <= x_max):
        x_p = x + (x_max - x_min) / 10 ** 3
        if (eval(func) * eval(func.replace('x','x_p'))) / (eval(dfunc) * eval(dfunc.replace('x','x_p'))) <= 0:
            x_0 = x
            x_1 = x - (eval(func) / eval(dfunc))
            while (abs(x_0 - x_1) >= 10 ** -7 and (x_min <= x_1 <= x_max)):
                x_0 = x_1
                x_1 -= eval(func.replace('x','x_1')) / eval(dfunc.replace('x','x_1'))
            if x_min <= x_1 <= x_max:
                ROOTS.append(sign(round(x_1, 1))*abs(round(x_1, 5)))
        x += x_p - x
    if ROOTS != []:
        print('Для F(x) =', func, 'при x ∈ [' + str(x_min) + ', ' + str(x_max) + '] обнаружены корни:', ROOTS)
    else:
        print('Корни не обнаружены на заданом локальном области определения в вещественном поле чисел!')
    return 0


try:
    roots_for_func(str(input('Введите функу F(x): ')),
    float(input('Начало локальной области определения функи: ')),
    float(input('Конец локальной области определения функи: ')))
except ValueError:
    exit('Некорректно введенные данные ...')
except TypeError:
    exit('Некорректно введенные данные ...')