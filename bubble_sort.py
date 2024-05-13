

def bubble_sort(arr):
    for i in range(len(arr)-1):
        sorted = True
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                sorted = False
        if sorted:
            break
    return arr


if __name__ == '__main__':
    arr = [5, 7, 2, 7, 3, 12, 3, 4, 1]
    print(bubble_sort(arr))