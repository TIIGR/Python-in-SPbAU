import matplotlib.pyplot as graph
from usrfuncs import *
from time import *


def desmos(FUNC, X_MIN, X_MAX):
    error = 0
    if (len(FUNC) != len(X_MIN)) or (len(FUNC) != len(X_MAX)) or (len(X_MIN) != len(X_MAX)):
        exit('Недопустимые вводные данные!')
    for c in range(len(FUNC)):
        t = time()
        if (X_MAX[c] <= X_MIN[c]):
            print('Недопустимый интервал сканирования для %s-й функи, пропускаем её построение.' % (c + 1))
            error += 1
            continue
        X, Y = [], []; x, percents = X_MIN[c], 0
        while X_MIN[c] <= x <= X_MAX[c]:
            X.append(x)
            Y.append(eval(streplace(FUNC[c], 'there')))
            percents += 0.1
            print('Построение ' + str(c + 1) + '-й функи: ' + f'{round(percents, 2)}' + '%\r', end = '', flush = True)
            x += (X_MAX[c] - X_MIN[c]) / 10 ** 3
        graph.plot(X, Y)
        print('Построение ' + str(c + 1) + '-й функи завершено за %s сек.' % round((time() - t), 3))
    if error != len(FUNC):
        graph.title('График фунок: ' + str(FUNC))
        graph.show()
    return 0

try:
    count = int(input('Количество исследуемых фунок: '))
    FUNC, X_MIN, X_MAX = [], [], []
    for c in range(count):
        FUNC.append(str(input('Введите %s-ю функу: ' % (c + 1))))
        X_MIN.append(float(input('Введите начало области определения %s-й функи: ' % (c + 1))))
        X_MAX.append(float(input('Введите конец области определения %s-й функи: ' % (c + 1))))
    desmos(FUNC, X_MIN, X_MAX)
except KeyboardInterrupt:
    desmos(FUNC, X_MIN, X_MAX)
except OverflowError:
    exit('При вычислении невозможно обработать слишком большие числа ...')
except ValueError as error:
    if str(error) == 'math domain error':
        exit('Заданная область определения выходит за рамки определенной области определения для заданной функи ...')
    exit('Произошла ошибка при вычислении ...')
except NameError:
    exit('Поддерживается только следующие функции и константы: pi, e, pf(x, m), relat(x) и другие стандартные функции ...')