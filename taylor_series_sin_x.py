import math


def my_sin(x, n):
    x = x / 180 * math.pi
    q = x
    s = 0
    for i in range(1, n + 1):
        s = s + q
        q = q * (-1) * (x * x) / ((2 * i + 1) * (2 * i))
    return s


print(my_sin(float(input("Введите значение угла в градусах (x): ")),
             int(input("Введите количетсво элементов ряда Тейлора (n): "))))
