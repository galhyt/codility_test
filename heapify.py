import random


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def heapify(arr, n, i):
    largest = i
    l = i*2+1
    r = i*2+2
    if l >= n and r >= n: return
    if l < n:
        if arr[i] < arr[l]:
            largest = l
    if r < n:
        if arr[largest] < arr[r]:
            largest = r
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    for i in range(int(n/2-1), -1, -1):
        heapify(arr, n, i)

    for m in range(n-1, 0, -1):
        swap(arr, 0, m)
        heapify(arr, m, 0)


def is_sorted(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:return False
    return True


if __name__ == '__main__':
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'
    
    for _ in range(10):
        n = random.randint(10,20)
        arr = [random.randint(1, 101) for _ in range(n)]
        print(f"arr = {arr}")
        heapsort(arr)
        color = GREEN if is_sorted(arr) else RED
        print(f"    {color}sorted = {arr}{RESET}")

