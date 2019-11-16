def fibo_gen():
    for n in range(2, 17):
        result = 1
        for el in range(1, n):
            result = result * el
        yield result


# g = fibo_gen()
for el in fibo_gen():
    print(el)


# next fibo_gen(1))
