import functools
import math
import random
from enum import Enum, auto


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


Di = Direction


class The2048Bonacci():

    def __init__(self, game_area):
        self.game_area = game_area
        self.width = len(self.game_area[0])
        self.height = len(self.game_area)

    def get_tile(self, x, y):
        return self.game_area[y][x]

    def set_tile(self, x, y, fib_value):
        self.game_area[y][x] = fib_value

    def get_description(self):
        str_lines = []
        for line in self.game_area:
            str_line = " ".join(
                [
                    f"{fib_val:2d}" for fib_val in line
                ]
            )
            str_lines.append(str_line)
        return "\n".join(str_lines)


def is_primary(n: int):
    for p in range(2, int(n / 2)+1):
        if n % p == 0:
            return False
    return True


def primary_construct(n: int):
    """
    finds first 2 dividers (p, n/p) and find their primary division which constructs the original number primary division
    """
    p = 2
    for p in range(2, int(n / 2)+1):
        if n % p == 0:
            construction = [p]
            if not is_primary(p):
                construction = primary_construct(p)
            partial_const = primary_construct(int(n / p))
            construction.extend(partial_const)
            return construction

    return [n]


if __name__ == '__main__':
    di = Di(random.randint(1,4))
    # finds board dimensions
    elems_num = random.randint(2, 2**16)
    construction = primary_construct(elems_num)
    k = random.randint(1, len(construction))
    n = functools.reduce(lambda n, s: n*s, random.choices(construction, k=k))
    m = int(elems_num / n)
    # build game_area
    print(construction)