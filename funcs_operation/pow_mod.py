from usrfuncs import *
from time import *

def two(a, p, q):
    return a ** p % q

def two_v_1(a, p, q):
    i, c = 1, a
    while i <= p:
        b = c % q
        c = a * b
        i += 1
    return b

def two_v_2(a, p, q):
    return a ** (p % (q - 1)) % q

a = int(input())
p = int(input())
q = int(input())
t = time()
print(str(two(a, p, q)) + '  Выполнено за %s сек.' % (time() - t))
r = time()
print(str(two_v_1(a, p, q)) + '  Выполнено за %s сек.' % (time() - r))
s = time()
print(str(two_v_2(a, p, q)) +'  Выполнено за %s сек.' % (time() - s))