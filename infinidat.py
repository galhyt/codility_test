import random
from functools import reduce
from time import time


def time_span(func):
    def _func(*args):
        start = time()
        ret = func(*args)
        print(time()-start)
        return ret
    return _func


def factorial(n):
    if n == 1:
        return 1

    return n*factorial(n-1)


def factorial2(n):
    return reduce(lambda a, b: a*b, range(1, n+1))


@time_span
def func(n: int):
    arr = list(range(1, n+1))
    output = []
    while len(arr) > 0:
        m = random.choice(arr)
        output.append(m)
        arr.remove(m)

    return output


@time_span
def func1(n: int):
    arr = list(range(1, n+1))
    output = []
    while len(arr) > 0:
        i = random.choice(range(len(arr)))
        output.append(arr[i])
        arr.pop(i)

    return output


def _func2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return _func2(n-1) + _func2(n-2) + _func2(n-3)


def func2(n):
    return _func2(n)


if __name__ == '__main__':
    print(func(15000))
    print(func1(15000))
