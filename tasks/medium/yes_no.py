"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(numbers):
    numbers_before = set()
    for n in numbers:
        if n in numbers_before:
            print("Yes")
        else:
            print("No")
