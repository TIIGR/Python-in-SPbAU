a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print("gcd(a,b) =", a + b)
