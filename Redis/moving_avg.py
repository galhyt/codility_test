from typing import List, Tuple


def moving_avg(data: List[Tuple[int, int]], window_sec: int) -> List[Tuple[int, int]]:
    n = len(data)
    output = []
    for i in range(n):
        j = min((j for j in range(i,-1,-1) if data[j][0] >= data[i][0]-window_sec))
        arr = [tu[1] for tu in data[j:i+1]]
        avg = int(sum(arr) / len(arr))
        output.append((data[i][0], avg))

    return output


if __name__ == '__main__':
    data = [(1, 2), (2, 4), (3, 3), (4, 2), (6, 8), (8, 2), (12, 1)]
    output = moving_avg(data, 2)
    print(output)
    print(moving_avg(data, 3))
