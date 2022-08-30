"""
С помощью декораторов реализовать конвейер сборки бургера

Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"


Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"

Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"

Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"

Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"

Написать функцию beef, которая:
 - печатает "### говядина ###"

Написать функцию chicken, которая:
 - печатает "|||| курица ||||"

1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка

2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""


def bread(function):
    def bread1(*args, **kwargs):
        print("</------------\\>")
        result = function(*args, **kwargs)
        print("<\\____________/>")
        return result
    return bread1


def tomato(function):
    def tomato1(*args, **kwargs):
        print("*** помидоры ****")
        result = function(*args, **kwargs)
        return result
    return tomato1


def salad(function):
    def salad1(*args, **kwargs):
        print("~~~~ салат ~~~~~")
        result = function(*args, **kwargs)
        return result
    return salad1


def cheese(function):
    def cheese1(*args, **kwargs):
        print("^^^^^ сыр ^^^^^^")
        result = function(*args, **kwargs)
        return result
    return cheese1


def onion(function):
    def onion1(*args, **kwargs):
        print("----- лук ------")
        result = function(*args, **kwargs)
        return result
    return onion1


@bread
@onion
@tomato
def beef():
    print("### говядина ###")


@bread
@cheese
@salad
def chicken():
    print("|||| курица ||||")
