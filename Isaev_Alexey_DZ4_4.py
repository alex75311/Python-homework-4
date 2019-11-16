list = [68, 68, 68, 1, 0, 0, 5, 3, 4, 10, 10]
new_list = [el for el in list if list.count(el) == 1]
print(new_list)
