import random
from typing import List


class Solution:
    def _rotate(self, nums: List[int], k: int, n: int, direction: str = 'right') -> None:
        i = 0 if direction == 'right' else n - 1
        next_val = nums[i]
        for _ in range(n):
            rotate_val = next_val
            if direction == 'right':
                i_k = i + k if i + k < n else (i + k) % n
            else:
                i_k = i - k if i - k >= 0 else n + i - k
            next_val = nums[i_k]
            nums[i_k] = rotate_val
            i = i_k

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        " [1,2,3,4,5,6,7], k = 3"
        n = len(nums)
        if k >= n: k = k % n
        if k == 0: return
        direction = 'right'
        if k > n/2:
            direction = 'left'
            k = n - k

        self._rotate(nums, k, n, direction)


if __name__ == '__main__':
    sol = Solution()
    _nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] #list(range(1, random.randint(10, 20)))
    nums = _nums.copy()
    n = len(nums)
    print(f"\033[32m{nums}\033[0m")
    sol.rotate(nums, 10)
    for k in (random.randint(0, 14) for _ in range(10)):
        sol.rotate(nums, k)
        print(f"    {nums}  k={k} ({k % n})")
        nums = _nums.copy()
