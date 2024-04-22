import random
import re


def solution(N):
    b = bin(N)
    # gaps = re.findall(r'1(0+)1', b)
    gaps = re.split(r'1+', b)
    gaps.pop(0)
    gaps.pop(len(gaps)-1)
    if not gaps:
        return 0
    return max(map(len, gaps))


if __name__ == '__main__':
    for i in range(1, 10):
        n = random.randint(1, 2**31)
        print(f"{i}. n = {n}   bin = {bin(n)}  gap = {solution(n)}")
