import matplotlib.pyplot as plot
from usrfuncs import *

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
    plot.plot(X, Y)
    plot.title('F(x) = ' + func)
    plot.show()
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
    print('Поддерживается только следующие функции и константы: pi, e, pf(x, m) и другие стандартные функции ...')