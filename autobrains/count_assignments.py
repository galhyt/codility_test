import itertools
from typing import List, Union

from hint import Hint, AbsoluteHint, NeighbourHint, RelativeHint


def count_assignments(hints: List[Hint]) -> int:
    floors: List[List[Union[Hint.Color, Hint.Animal, None]]] = [[None, None] for _ in range(5)]
    cand_colors = list(Hint.Color)
    cand_animals = list(Hint.Animal)

    def _get_animal_free_floors():
        return list(filter(lambda i: floors[i][1] is None, range(len(floors))))

    def _get_color_free_floors():
        return list(filter(lambda i: floors[i][0] is None, range(len(floors))))

    def _set_absolute_floor_hint(hint: AbsoluteHint):
        a, b = hint.value
        if isinstance(b, Hint.Color):
            floors[a.value-1][0] = b
            cand_colors.remove(b)
        else:
            floors[a.value-1][1] = b
            cand_animals.remove(b)

    for hint in filter(lambda h: isinstance(h, AbsoluteHint) and isinstance(h.value[0], Hint.Floor), hints):
        _set_absolute_floor_hint(hint)

    valid_assignments = 0

    color_free = _get_color_free_floors()
    animal_free = _get_animal_free_floors()

    for colors_comb in itertools.permutations(cand_colors, len(cand_colors)):
        for i, f in enumerate(color_free):
            floors[f][0] = colors_comb[i]
        for animal_comb in itertools.permutations(cand_animals, len(cand_animals)):
            for j, f in enumerate(animal_free):
                floors[f][1] = animal_comb[j]
            # check if assignment valid
            if all((h.is_assignment_valid(floors) for h in hints)):
                valid_assignments += 1

    return valid_assignments


def print_hints(hints: List[Hint]):
    for hint in hints:
        print(f"    {hint}")


if __name__ == '__main__':
    hints = [AbsoluteHint((Hint.Floor.first, Hint.Animal.rabbit)),
             AbsoluteHint((Hint.Floor.second, Hint.Animal.chicken)),
             AbsoluteHint((Hint.Floor.third, Hint.Color.yellow)),
             AbsoluteHint((Hint.Floor.fifth, Hint.Animal.bird)),
             AbsoluteHint((Hint.Animal.grasshopper, Hint.Color.blue)),
             NeighbourHint((Hint.Color.red, Hint.Color.green))]
    c = count_assignments(hints)
    print(f"\033[32mHints 1\033[0m")
    print_hints(hints)
    print(f"\n\033[34mPossible assignments:\033[0m {c}")
    assert c == 2

    hints = [AbsoluteHint((Hint.Floor.fifth, Hint.Animal.bird)),
             AbsoluteHint((Hint.Floor.first, Hint.Color.green)),
             AbsoluteHint((Hint.Animal.frog, Hint.Color.yellow)),
             NeighbourHint((Hint.Animal.frog, Hint.Animal.grasshopper)),
             NeighbourHint((Hint.Color.red, Hint.Color.orange)),
             RelativeHint((Hint.Animal.chicken, Hint.Color.blue, 4))]
    c = count_assignments(hints)
    print(f"\n\033[32mHints 2\033[0m")
    print_hints(hints)
    print(f"\n\033[34mPossible assignments:\033[0m {c}")
    assert c == 4
