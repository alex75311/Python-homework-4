'''
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор.
'''


my_list = [68, 68, 68, 1, 0, 0, 5, 3, 4, 10, 10]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)
