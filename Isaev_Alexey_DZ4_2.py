'''
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
'''


from random import randint


def gen_max(arg):
    result = [x for idx, x in enumerate(arg[1:], 1) if x > arg[idx - 1]]
    return result


my_list = (44, 37, 35, 23, 5, 96, 71, 71, 55, 69, 98, 18, 69, 18, 95, 83, 76, 58, 76, 11, 89, 84, 11, 11, 76, 30, 88, 79)
gen = gen_max(my_list)
print(gen)

my_list = [randint(0, 100) for _ in range(0, 30)]
gen = gen_max(my_list)
print(my_list)
print(gen)
