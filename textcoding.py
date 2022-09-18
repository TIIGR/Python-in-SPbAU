

def de_en_code(text):
    code = ''
    if len(text) == 0:
        return print('Текстовый файл пуст!')
    elif ord(text[0]) == 1423:
        for Ord in range(1, len(text)):
            if ord(text[Ord]) < 1423:
                code += chr((ord(text[Ord]) + ((-1) ** Ord) * Ord) % 1423)
            else:
                return print('Присутствуют недопустимые символы! Один из таких:', text[Ord])
    else:
        for Ord in range(0, len(text)):
            if ord(text[Ord]) < 1423:
                code += chr((ord(text[Ord]) + ((-1) ** Ord) * (Ord + 1)) % 1423)
            else:
                return print('Присутствуют недопустимые символы! Один из таких:', text[Ord])
        code = chr(1423) + code
    open(Directory, 'w+', encoding='utf-8').write(code)
    if len(text) < len(code):
        return print('Текст зашифрован!')
    else:
        return print('Текст расшифрован!')


Directory = str(input('Укажите полный путь к текстовому файлу: '))
try:
    de_en_code(open(Directory, 'r', encoding='utf-8').read())
except FileNotFoundError:
    print('Файл по указанному пути не существует!')
except UnicodeDecodeError:
    print('Файл не подходит для использования!')
