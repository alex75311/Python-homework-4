'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''

from itertools import count
from itertools import cycle
from time import sleep


def gen_int():
    x = int(input('Введите число с которого начать БЕСКОНЕЧНУЮ генерацию '))
    for el in count(x):
        print(el)
        sleep(0.1)


def replay_list():
    list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

    for el in cycle(list):
        print(el)
        sleep(0.1)


try:
    usr_ans = int(
        input('Введите 1 чтобы запустить БЕСКОНЕЧНЦЮ генерацию чисел или 2 чтобы запустить БЕСКОНЕЧНЫЙ повтор списка '))
    if usr_ans == 1:
        gen_int()
    elif usr_ans == 2:
        replay_list()
    else:
        print('Неизвестынй ответ')
except ValueError:
    print('Неизвестынй ответ')
