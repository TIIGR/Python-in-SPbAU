def prime(n):
    if n <= 0:
        return "Число не является натуральным!"
    else:
        if n == 1:
            return "True"
        else:
            d = 2
            while n % d != 0:
                d += 1
            return d == n


print(prime(int(input("Введите число: "))))
