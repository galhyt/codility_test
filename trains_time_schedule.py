"""
Description:
    Given trains schedule between 2 stations (A and B), find minimum number of trains to be in each station in the
    beginning of the day
"""
import datetime
import time
from dataclasses import dataclass
from typing import Tuple, List, Optional


@dataclass
class TrainSchedule:
    src: str
    dest: str
    departure: float
    arrival: float


@dataclass
class Train:
    station: str
    available_from: Optional[float] = None


def find_and_pop_train(trains_pool: List[Train], schedule: TrainSchedule) -> Optional[Train]:
    try:
        indx = next(filter(lambda i: schedule.departure >= trains_pool[i].available_from, range(len(trains_pool))))
        return trains_pool.pop(indx)
    except StopIteration:
        return None


def min_pool(train_schedules: List[TrainSchedule]) -> Tuple[int, int]:
    a, b = 0, 0
    A, B = [], []
    train_schedules = sorted(train_schedules, key=lambda s: s.departure)
    for schedule in train_schedules:
        src_pool = locals()[schedule.src]
        trg_pool = locals()[schedule.dest]

        train = find_and_pop_train(src_pool, schedule) if src_pool else None
        if not train:
            train = Train(schedule.src)
            if schedule.src == 'A':
                a += 1
            else:
                b += 1

        # move the train to the target station
        train.available_from = schedule.arrival
        train.station = schedule.dest
        trg_pool.append(train)

    return a, b


if __name__ == '__main__':
    times = {
        ('A', 'B'): [(9, 10.5), (11, 11.75), (14, 15.5)],
        ('B', 'A'): [(10.5, 12.45), (11.5, 13), (16, 17)],
    }

    schedules = [TrainSchedule(*(st + sc))
                 for st, scheds in times.items() for sc in scheds]
    print(schedules)
    print(min_pool(schedules))
