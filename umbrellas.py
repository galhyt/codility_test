import itertools
from typing import List


def min_set(umbrellas: List[int], people: int):
    umbrellas = sorted(umbrellas, reverse=True)
    for j in range(len(umbrellas)):
        u = umbrellas[j]
        n = people // u
        comb = {u: n}
        if people % u == 0:
            return comb

        if j < len(umbrellas) - 1:
            for i in range(n, 0, -1):
                comb[u] = i
                _comb = min_set(umbrellas[j+1:], people - u*i)
                if _comb:
                    comb.update(_comb)
                    return comb

    return []


if __name__ == '__main__':
    umbrellas = [3, 6, 7, 8, 19, 21, 31]
    people = 51
    # 7: 3, 6: 4, 3: 8
    print(min_set(umbrellas, people))
