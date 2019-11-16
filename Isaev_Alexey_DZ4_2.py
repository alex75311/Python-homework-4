from random import randint


def gen_max(list):
    result = [x for idx, x in enumerate(list) if list[idx - 1] < list[idx]]
    return result


list = (44, 37, 35, 23, 5, 96, 71, 71, 55, 69, 98, 18, 69, 18, 95, 83, 76, 58, 76, 11, 89, 84, 11, 11, 76, 30, 88, 79)
# gen = [x for idx, x in enumerate(list) if list[idx - 1] < list[idx]]
gen = gen_max(list)
print(gen)

list = [randint(0, 100) for _ in range(0, 30)]
# gen = [y for idx, y in enumerate(list) if list[idx - 1] < list[idx]]
gen = gen_max(list)
print(list)
print(gen)
