# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import functools
import itertools
import random

import numpy


def solution(a):
    b = set(a)
    b = list(sorted(b))
    print(b)
    s = 1
    i = 0
    while i < len(b):
        if s < b[i]:
            return s
        if b[i] == s:
            s += 1

        i += 1
    return s


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = []
    n = random.randint(2, 1000)
    for _ in range(n-1):
        sel = random.randint(-10 ** 2, 10 ** 2)
        a.append(sel)
    print(solution(a))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
