# Function to Write:
# intervals

# Input:
from typing import List

# Expected Output:
# [(1, 4), (10, 16), (40, 40), (100, 104)]

# def get_tolerated(timestamps, tolerance):
#     cand_indx = 0
#     output = []
#     arr_len = len(timestamps)
#     while True:
#         print(f"cand_indx={cand_indx}")
#         if cand_indx >= arr_len:
#             break
#         for i in range(cand_indx, arr_len - 1):
#             j = i + 1
#             print(f"i={i} j={j}")
#             if timestamps[j] - timestamps[i] > tolerance:
#                 output.append((timestamps[cand_indx], timestamps[i]))
#                 cand_indx = j
#                 break
#         if j >= arr_len - 1:
#             output.append((timestamps[cand_indx], timestamps[j]))
#             break
#
#     return output


def _get_tolerated(timestamps):
    for i in range(len(timestamps)-1):
        if timestamps[i+1] - timestamps[i] > tolerance:
            return (timestamps[0], timestamps[i]), i+1
    return (timestamps[0], timestamps[i+1]), None


def get_tolerated(timestamps: List[int], tolerance: int):
    output = []
    next_cand = 0
    while next_cand is not None:
        timestamps = timestamps[next_cand:]
        el, next_cand = _get_tolerated(timestamps)
        output.append(el)
    return output


if __name__ == '__main__':
    tolerance = 5
    timestamps = [1, 2, 3, 4, 10, 13, 16, 40, 100, 101, 102, 104]
    output = get_tolerated(timestamps, tolerance)
    print(output)