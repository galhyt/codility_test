from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Tuple, Union, List, Optional


@dataclass
class Hint:
    value: Tuple = None

    class Floor(Enum):
        first = auto()
        second = auto()
        third = auto()
        fourth = auto()
        fifth = auto()

    class Animal(Enum):
        bird = auto()
        grasshopper = auto()
        frog = auto()
        chicken = auto()
        rabbit = auto()

    class Color(Enum):
        red = auto()
        green = auto()
        blue = auto()
        yellow = auto()
        orange = auto()

    def is_assignment_valid(self, floors: List[List[Union[Color, Animal]]]) -> bool:
        raise NotImplemented(f"is_assignment_valid not implemented in {self.__class__}")

    def search_animal_floor(self, floors: List[List[Union[Color, Animal]]], animal: Animal) -> Optional[int]:
        try:
            f = next(filter(lambda i: floors[i][1] == animal, range(len(floors))))
            return f
        except StopIteration:
            return None

    def search_color_floor(self, floors: List[List[Union[Color, Animal]]], color: Color) -> Optional[int]:
        try:
            f = next(filter(lambda i: floors[i][0] == color, range(len(floors))))
            return f
        except StopIteration:
            return None


class AbsoluteHint(Hint):

    def __init__(self, value: Tuple[Union[Hint.Floor, Hint.Animal], Union[Hint.Color, Hint.Animal]]):
        self.value = value

    def is_assignment_valid(self, floors: List[List[Union[Hint.Color, Hint.Animal]]]) -> bool:
        a, b = self.value
        if isinstance(a, Hint.Floor):
            color, animal = floors[a.value-1]
            return color == b if isinstance(b, Hint.Color) else animal == b
        else:
            a_f = self.search_animal_floor(floors, a)
            color, animal = floors[a_f]
            return b == color


class RelativeHint(Hint):
    def __init__(self, value: Tuple[Union[Hint.Animal, Hint.Color], Union[Hint.Animal, Hint.Color], int]):
        # value - how many floors the first element in the tuple resides below the second one
        self.value = value

    def is_assignment_valid(self, floors: List[List[Union[Hint.Color, Hint.Animal]]]) -> bool:
        a, b, n = self.value
        a_f = self.search_animal_floor(floors, a) if isinstance(a, Hint.Animal) else self.search_color_floor(floors, a)
        b_f = self.search_animal_floor(floors, b) if isinstance(b, Hint.Animal) else self.search_color_floor(floors, b)

        return b_f - a_f == n

class NeighbourHint(Hint):
    def __init__(self, value: Tuple[Union[Hint.Animal, Hint.Color], Union[Hint.Animal, Hint.Color]]):
        self.value = value

    def is_assignment_valid(self, floors: List[List[Union[Hint.Color, Hint.Animal]]]) -> bool:
        a, b = self.value
        a_f = self.search_animal_floor(floors, a) if isinstance(a, Hint.Animal) else self.search_color_floor(floors, a)
        b_f = self.search_animal_floor(floors, b) if isinstance(b, Hint.Animal) else self.search_color_floor(floors, b)

        arr = sorted([a_f, b_f])
        return arr[1] == arr[0]+1
