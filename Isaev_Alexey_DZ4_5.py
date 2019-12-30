'''
Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа
от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
Пояснение: [5, 7, 14, 11] -> [5 * 7, 14, 11] -> [5 * 7 * 14, 11] -> 5 * 7 * 14 * 11, это по reduce.
'''

from functools import reduce
from pprint import pprint

my_list = [x for x in range(100, 1001) if not x % 2]
pprint(f'Список четных чисел от 100 до 1000 включая границы \n {my_list}')

my_list = [5, 7, 14, 11]
print(f'\nНовый массив, для вычисления произведения его чисел\n{my_list}')
for idx, el in enumerate(my_list):
    prod = reduce(lambda a, b: a * b, my_list[:idx + 1])
    print(f'Произведение первых {idx + 1} элементов равно {prod}')
