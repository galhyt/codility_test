import math
from enum import Enum, auto
from typing import Optional, Callable


class Shape(Enum):
    Rectangle = auto()
    Triangle = auto()
    Circle = auto()


calculation = {Shape.Rectangle: lambda n, m: n*m,
               Shape.Triangle: lambda n, m: n*m/2,
               Shape.Circle: lambda n, m: math.pi * n**2}


def calculate_area(n: int, m: Optional[int] = None, shape: Shape = Shape.Rectangle, calculate_func: Optional[Callable] = None,
                   **kwargs) -> Optional[float]:
    if n <= 0:
        print(f"Error: n parameter {n}")
    if m is None:
        m = n

    if calculate_func:
        return calculate_func(n, m, **kwargs)

    if shape not in calculation:
        print(f"shape {shape.name} not supported")
        return None

    func = calculation[shape]
    return func(n, m)


if __name__ == '__main__':
    print(f"square: {calculate_area(20)}")
    print(f"Rectangle: {calculate_area(20, 30)}")
    print(f"Triangle: {calculate_area(20, 30, Shape.Triangle)}")
    print(f"Circle: {calculate_area(20, None, Shape.Circle)}")
    print(f"Shape: {calculate_area(20, None, calculate_func=lambda a, b, c: a*b*c, c=40)}")