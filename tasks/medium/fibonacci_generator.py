"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(num_count):
    n1 = 1
    n2 = 1
    if num_count <= 1:
        raise ValueError('Введите значение больше 1')
    else:
        while n1 <= num_count:
            yield n1
            n1, n2 = n2, n1 + n2
