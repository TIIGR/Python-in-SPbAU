def conversion(value, old, new):
    if 2 <= old <= 36 or 2 <= new <= 36:
        if isinstance(value, str):
            n = int(value, old)
        else:
            n = int(value)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < new:
            return alphabet[n]
        else:
            return conversion(n // new, old, new) + alphabet[n % new]
    else:
        return "Введенные вами сс, противоречат возможностям программы"


print("Ответ: ", conversion(input("Введите число (от 0 до z): "),
    int(input("Введите основание сс введенного числа (не превыш. 36): ")),
    int(input("Введите конечное основание сс (не превыш. 36): "))))
