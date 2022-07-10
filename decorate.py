def repetition(k):
    def function(f):
        def argument(x):
            for i in range(k):
                x = f(x)
            return x
        return argument
    return function


a = int(input("Ваше число: "))
n = int(input("Сколько раз прибавлять 3 к числу? "))


# Функция, которая прибавляет к введенному числу 3 в группе целых чисел с вычетом по модулю 5 (Z/5)+ = {0,1,2,3,4}.
# При вводе отрицательного числа a, в этой группе оно будет равно 5 - (|a| mod 5)
@repetition(n)  # Выполняем эту функцию n раз.
def sum_in_cycle_sum_group(g):
    g = (g + 3) % 5
    return g


print(sum_in_cycle_sum_group(a))
