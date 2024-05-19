from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Tuple, Union


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


class AbsoluteHint(Hint):

    def __init__(self, value: Tuple[Union[Hint.Floor, Hint.Animal], Union[Hint.Color, Hint.Animal]]):
        self.value = value


class RelativeHint(Hint):
    def __init__(self, value: Tuple[Union[Hint.Animal, Hint.Color], Union[Hint.Animal, Hint.Color], int]):
        self.value = value


class NeighbourHint(Hint):
    def __init__(self, value: Tuple[Union[Hint.Animal, Hint.Color], Union[Hint.Animal, Hint.Color]]):
        self.value = value
