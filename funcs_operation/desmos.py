import matplotlib.pyplot as plot
from usrfuncs import *

def desmos(func, x_min, x_max):
    if x_max <= x_min:
        exit('Недопустимые вводные данные')
    X = []; Y = []; x = x_min; percents = 0
    while x_min <= x <= x_max:
        X.append(x)
        Y.append(eval(func.replace('^', '**')))
        percents += 0.1
        print('Загрузка: ' + f'{round(percents, 2)}' + '%\r', end = '', flush = True)
        x += (x_max - x_min) / 10 ** 3
    plot.plot(X, Y)
    plot.title('F(x) = ' + func)
    plot.show()
    return 0

try:
    desmos(str(input('Введите функу (к примеру, e^x): ')),
        float(input('Начало локальной области определения функи: ')),
        float(input('Конец локальной области определения функи: ')))
except OverflowError:
    exit('При вычислении невозможно обработать слишком большие числа ...')
except ValueError:
    exit('Произошла ошибка при вычислении ...')
except NameError:
    exit('Поддерживается только следующие функции и константы: pi, e, pf(x, m), relat(x) и другие стандартные функции ...')