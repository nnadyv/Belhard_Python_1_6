"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(number, summa=0):
    if number == 0:
        return summa
    else:
        n = number % 10
        summa = summa + n
        return sum_of_numbers(number // 10)
