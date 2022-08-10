from usrfuncs import *


def tanmethod_for_roots_of_Pf(x_p, a):
    for b in range(a + 1):
        x_1 = x_p - (Pf(x_p, b) / Pf(x_p, b + 1))
        x_0 = x_p
        while abs(x_0 - x_1) >= 10 ** -6:
            x_0 = x_1
            x_1 -= Pf(x_1, b) / Pf(x_1, b + 1)
        print('Корень "Простой" функи для', b,'порядка производной:', x_1)
    return 0

try:
    tanmethod_for_roots_of_Pf(float(input('нач. аргумент: ')),int(input('макс. порядок производной: ')))
except OverflowError:
    print('При вычислении невозможно обработать слишком большие числа ...')
except ValueError:
    print('Недопустимые вводные данные ...')