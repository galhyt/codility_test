"""
setTimerFunc(delay, func)
set_intervals(intervals: List[int], functions: List[Function])

example:
intervals [3, 5, 7]
functions [fn1, fn2, fn3]

fn1     3
fn2     5
fn1     6
fn3     7
fn1     9
fn2     10
fn1     12
fn3     14
...
"""
import time
from typing import List, Callable


def set_timer_func(delay: int, fn: Callable):
    time.sleep(delay)
    fn()


def set_intervals(intervals: List[int], functions: List[Callable]):
    _intervals = [
        (intervals[i], intervals[i], functions[i])
        for i in range(len(intervals))
    ]

    def set_new_interval(base_inter, inter, fn):
        new_inter = inter + base_inter
        if new_inter < _intervals[0][1]:
            _intervals.insert(0, (base_inter, new_inter, fn))
            return

        for i in range(len(_intervals)):
            if new_inter >= _intervals[i][1]:
                if i+1 < len(_intervals):
                    if new_inter <= _intervals[i+1][1]:
                        _intervals.insert(i+1, (base_inter, new_inter, fn))
                        break
                else:
                    _intervals.insert(i + 1, (base_inter, new_inter, fn))
                    break
        # print([(_inter[0], _inter[1], _inter[2].__name__) for _inter in _intervals])

    prev = 0
    while True:
        base_inter, inter, fn = _intervals.pop(0)
        set_new_interval(base_inter, inter, fn)
        set_timer_func(inter - prev, fn)
        prev = inter


if __name__ == '__main__':
    start = time.time()
    def fn1():
        print(f"\033[92mfn1\033[0m      {int(time.time() - start)}")
    def fn2():
        print(f"\033[91mfn2\033[0m      {int(time.time() - start)}")
    def fn3():
        print(f"\033[94mfn3\033[0m      {int(time.time() - start)}")

    intervals = [3, 5, 7]
    functions = [fn1, fn2, fn3]
    set_intervals(intervals, functions)
