
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[j]


def inplace_merge(arr, s1, e1, s2, e2):
    buffer_s = e1 + 1
    buffer_e = s2 - 1


def inplace_merge_sort(arr, s, e):
    if s == e: return

    n = e - s + 1
    s2 = s + int(n/2) - 1
    inplace_merge_sort(arr, s2, e)
    devider = 4
    s1 = s
    while True:
        e1 = s1 + int(n/devider) - 1
        inplace_merge_sort(arr, s1, e1)
        inplace_merge(arr, s1, e1, s2, e)
        s2 = e1 + 1
        devider *= 2



def merge_sort(arr):
    n = len(arr)
    inplace_merge_sort(arr, 0, n-1)


def is_sorted(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:return False
    return True


if __name__ == '__main__':
    arr = [95, 58, 88, 56, 3,9,4,6]
    merge_sort(arr)
    print(arr)
