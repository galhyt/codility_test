import random
import re
from typing import List, Set

bin_len = 4

def solution(A, B, C):
    for con_a in get_conforms(A):
        pass


def get_conforms(A):
    a_zeroes = get_zeros(A)
    c = bin(A)[2:]
    c = "0" * (bin_len - len(c)) + c

    l = len(a_zeroes)
    for looper in range(2**l):
        bin_looper = bin(looper)[2:]
        bin_looper = "0" * (l-len(bin_looper)) + bin_looper
        for i in range(l):
            j = a_zeroes[i]
            c[j] = bin_looper[i]
            yield c


def get_zeros(A) -> List[int]:
    a = bin(A)
    a = a[2:]

    l = bin_len - len(a)
    a = "0"*l + a
    zeros = []
    for i in range(bin_len):
        if a[i] == "0": zeros.append(i)
    return zeros


def cor_num(A):
    b = bin(A)
    b = b[2:]
    gaps = re.split(r'1+', b)
    l = sum(map(len, gaps))
    l += bin_len - len(b)

    return 2**l


def shared_zeros(A, B) -> Set[int]:
    a = bin(A)
    b = bin(B)
    a = a[2:]
    b = b[2:]

    l = bin_len - len(a)
    a = "0"*l + a
    l = bin_len - len(b)
    b = "0" * l + b
    shared = set()
    for i in range(bin_len):
        if a[i] == "0" == b[i]: shared.add(i)
    return shared


if __name__ == '__main__':
    # A co B co C -> A co C
    # '0110'
    # '0101'
    # '1011'
    A = 6
    B = 5
    C = 11
    print(solution(A, B, C))