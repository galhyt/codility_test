from typing import List


def _quick_sort(arr: List[int], start=0, end=None):
    if end is None:
        end = len(arr) - 1
    # [1, 4, 3, 9, 6, 7]

    if end <= start: return

    if end == start + 1:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
            return

    _start, _end = start, end

    while _start < _end:
        if arr[_start] <= arr[_end]:
            _start += 1
        else:
            arr[_end], arr[_end-1] = arr[_end-1], arr[_end]
            arr[_start], arr[_end] = arr[_end], arr[_start]
            _end -= 1

    _quick_sort(arr, start, _end-1)
    _quick_sort(arr, _end, end)


def quick_sort(arr: List[int]):
    return _quick_sort(arr)


if __name__ == '__main__':
    arr = [1, 4, 3, 9, 6, 7]
    quick_sort(arr)
    print(arr)