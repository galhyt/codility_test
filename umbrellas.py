from typing import List


def min_set(umbrellas: List[int], people: int):
    umbrellas = sorted(umbrellas)
    r = len(umbrellas) - 1

    _sum = 0
    comb = []
    while r > 0:
        ur = umbrellas[r]
        un = (people - _sum) // ur
        if un > 0:
            _sum += ur * un
            comb.extend([ur] * un)
            if _sum == people:
                return comb
            r -= 1
        else:
            ur = comb.pop(-1)
            _sum -= ur

    return comb


if __name__ == '__main__':
    umbrellas = [1, 3, 6, 10, 13]
    people = 27
    print(min_set(umbrellas, people))
