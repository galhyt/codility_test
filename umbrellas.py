from functools import reduce
from typing import List


def min_set(umbrellas: List[int], people: int):
    umbrellas = sorted(umbrellas, reverse=True)
    min_comb = {}
    min_comb_umb = 2 ** 31
    for j in range(len(umbrellas)):
        u = umbrellas[j]
        n = people // u
        comb = {u: n}
        if people % u == 0:
            umb_num = reduce(lambda s, u: s + comb[u], comb, 0)
            if umb_num < min_comb_umb:
                min_comb = comb.copy()
                min_comb_umb = umb_num

        if j < len(umbrellas) - 1:
            for i in range(n, 0, -1):
                comb[u] = i
                _comb = min_set(umbrellas[j+1:], people - u*i)
                if _comb:
                    comb.update(_comb)
                    umb_num = reduce(lambda s, u: s+comb[u] , comb, 0)
                    if umb_num < min_comb_umb:
                        min_comb = comb.copy()
                        min_comb_umb = umb_num
    return min_comb


if __name__ == '__main__':
    umbrellas = [186,419,83,408]
    people = 6249
    # umbrellas = [2, 3, 6, 7, 8]
    # people = 66
    print(min_set(umbrellas, people))
