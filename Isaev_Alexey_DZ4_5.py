from functools import reduce

list = [x for x in range(100, 1001) if not x % 2]

prod = reduce(lambda a, b: a * b, list)
print(prod)
