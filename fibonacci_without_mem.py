# these are the first elements of the sum
FIB1 = 1
FIB2 = 1

n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)

# there is an accumulation of the sum
i = 0
while i < n - 2:
    FIB_S = FIB1 + FIB2
    FIB1 = FIB2
    FIB2 = FIB_S
    i = i + 1

print(FIB2)
