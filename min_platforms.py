from typing import List


def min_platforms(arr: List[float], dep: List[float]) -> int:
    min_p = 1
    p = 1
    arr, dep = sorted(arr), sorted(dep)

    dep_i = 0
    arr_i = 0
    while arr_i < len(arr) and dep_i < len(dep):
        # calculate how much platforms freed for use
        while dep_i < len(dep) and dep[dep_i] <= arr[arr_i]:
            p += 1
            dep_i += 1
        # check if there's free platform for use
        if p > 0:
            p -= 1 # train entered station and occupies one platform
        else:
            min_p += 1

        arr_i += 1

    if arr_i < len(arr):
        trains_to_arrive = len(arr) - arr_i
        if p > 0:
            trains_to_arrive -= p
        if trains_to_arrive > 0:
            min_p += trains_to_arrive

    return min_p


if __name__ == '__main__':
    arr = [9, 9.66, 9.833, 11, 15, 18]
    dep = [9.16, 12, 11.33, 115, 19, 20]
    min_p = min_platforms(arr, dep)
    print(f"min platforms: {min_p}")
    assert min_p == 3

    arr = [9, 9.66]
    dep = [9.16, 12]
    min_p = min_platforms(arr, dep)
    print(f"min platforms: {min_p}")
    assert min_p == 1
