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

def tanmethod_for_roots_of_Pf(x_p, a):
    b = 0
    while b <= a:
        x_1 = x_p - (Pf(x_p, b) / Pf(x_p, b + 1))
        x_0 = x_p
        while abs(x_0 - x_1) >= 10 ** -6:
            x_0 = x_1
            x_1 -= Pf(x_1, b) / Pf(x_1, b + 1)
        print('Корень "Простой" функи для', b,'порядка производной:', x_1)
        b += 1
    return 0

try:
    tanmethod_for_roots_of_Pf(float(input('нач. аргумент: ')),int(input('макс. порядок производной: ')))
except OverflowError:
    print('При вычислении невозможно обработать слишком большие числа ...')
except ValueError:
    print('Недопустимые вводные данные ...')