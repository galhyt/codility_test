from typing import List, Tuple, Optional, Dict, Callable, Union, Any

from hint import Hint, AbsoluteHint, NeighbourHint, RelativeHint


def count_assignments(hints: List[Hint]):
    floors: List[List[Union[Hint.Color, Hint.Animal, None]]] = [[None, None] for _ in range(5)]

    def _search_animal_floor(animal: Hint.Animal):
        try:
            f = next(filter(lambda i: floors[i][1] == animal, range(len(floors))))
            return f
        except StopIteration:
            return None

    def _search_color_floor(color: Hint.Color):
        try:
            f = next(filter(lambda i: floors[i][0] == color, range(len(floors))))
            return f
        except StopIteration:
            return None

    def _get_animal_free_floors():
        return set(filter(lambda i: floors[i][1] is None, range(len(floors))))

    def _get_color_free_floors():
        return set(filter(lambda i: floors[i][0] is None, range(len(floors))))

    def _set_absolute_floor_hint(hint: AbsoluteHint):
        a, b = hint.value
        if isinstance(a, Hint.Floor):
            if isinstance(b, Hint.Color):
                floors[a.value-1][0] = b
            else:
                floors[a.value-1][1] = b

    def _set_absolute_animal_hint(hint: AbsoluteHint):
        a, c = hint.value
        a_f = _search_animal_floor(a)
        c_f = _search_color_floor(c)
        if a_f is not None:
            floors[a_f][0] = c
        elif c_f is not None:
            floors[c_f][1] = a
        else:
            animal_free = _get_animal_free_floors()
            color_free = _get_color_free_floors()
            candidates = animal_free.intersection(color_free)
            if len(candidates) == 1:
                i = candidates.pop()
                floors[i] = [c, a]

    def _set_neighbour_hint(hint: NeighbourHint):
        def _get_b_f(a, b, a_f, b_f):
            if a_f is None and b_f is None:
                return
            if a_f is None:
                a_f, b_f = b_f, a_f
                a, b = b, a
            if a_f == 0:
                b_f = 1
            elif a_f == 4:
                b_f = 3
            elif floors[a_f-1][1]:
                b_f = a_f + 1
            elif floors[a_f+1][1]:
                b_f = a_f - 1

            return b, b_f

        a, b = hint.value
        if isinstance(a, Hint.Animal):
            a_f, b_f = _search_animal_floor(a), _search_animal_floor(b)
        else:
            a_f, b_f = _search_color_floor(a), _search_color_floor(b)

        b, b_f = _get_b_f(a, b, a_f, b_f)
        if b_f is not None:
            floors[b_f][1] = b

    def _set_relative_hint(hint: RelativeHint):
        a, b, n = hint.value
        a_f = _search_animal_floor(a) if isinstance(a, Hint.Animal) else _search_color_floor(a)
        b_f = _search_animal_floor(b) if isinstance(a, Hint.Animal) else _search_color_floor(b)



    for hint in filter(lambda h: isinstance(h, AbsoluteHint) and isinstance(h.value[0], Hint.Floor), hints):
        _set_absolute_floor_hint(hint)

    for hint in filter(lambda h: isinstance(h, AbsoluteHint) and isinstance(h.value[0], Hint.Animal), hints):
        _set_absolute_animal_hint(hint)

    for hint in filter(lambda h: isinstance(h, NeighbourHint), hints):
        _set_neighbour_hint(hint)

    for hint in filter(lambda h: isinstance(h, RelativeHint), hints):
        _set_relative_hint(hint)

if __name__ == '__main__':
    hints = [AbsoluteHint((Hint.Floor.first, Hint.Animal.rabbit)),
             AbsoluteHint((Hint.Floor.second, Hint.Animal.chicken)),
             AbsoluteHint((Hint.Floor.third, Hint.Color.yellow)),
             AbsoluteHint((Hint.Floor.fifth, Hint.Animal.bird)),
             AbsoluteHint((Hint.Animal.grasshopper, Hint.Color.blue)),
             NeighbourHint((Hint.Color.red, Hint.Color.green))]

    count_assignments(hints)
