from typing import List


def twosum(arr: List[int], target: int) -> List[int]:
    """
    [1, 3, 6, 8, 10, 12]
    """
    d = {}
    for i, v in enumerate(arr):
        d.setdefault(v, []).append(i)

    output = []

    for i, v in enumerate(arr):
        f = target - v
        if f in d:
            indices = d[f]
            indices = [j for j in indices if j > i]
            if len(indices) > 0:
                output.append(i)
                output.extend(indices)

    return output


if __name__ == '__main__':
    arr = [4,5,7,3,4,6,5]
    t = 8
    output = twosum(arr, t)
    print(output)