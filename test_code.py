from quick import inplace_merge, is_sorted


def test_merge():
    arr = [2, 5, 9, 23, -5, 6, 8, 16]
    inplace_merge(arr, 0, 3, 4, 7)
    assert is_sorted(arr)