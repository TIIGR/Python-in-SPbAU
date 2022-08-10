from typing import TypeVar, List, Union

T = TypeVar('T')  # Можем указывать любой тип данных
A = TypeVar('A', str, bytes)  # Можем указывать данные типов str и bytes


def repeat(x: T, n: int) -> List[T]:  # Функция при вводе x, n выводит массив (список) n элементов состоящих только из x
    return [x] * n


def longest(x: A, y: A) -> A:  # Функция определяет и возвращает результат такой строки, которая больше другой.
    return x if len(x) >= len(y) else y


def parse_int(value: Union[str, int]) -> int:  # Функция принимает на вход строки из чисел и целые числа
    return int(value)  # Но возвращает только числа


print(repeat('hello', 5))  # Выводит ['hello', 'hello', 'hello', 'hello', 'hello']
print(longest('hello', 'hi'))  # Выводит hello
print(parse_int('5496'))  # Выводит 5496
