import random
from typing import List


class Solution:
    def _rotate(self, nums: List[int], start: int, k: int, n: int) -> None:
        next_val = nums[start]
        i = start
        i_k = -1
        iterations = 0
        while i_k != start:
            rotate_val = next_val
            i_k = i + k if i + k < n else (i + k) % n
            next_val = nums[i_k]
            nums[i_k] = rotate_val
            iterations += 1
            i = i_k

        return iterations

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        " [1,2,3,4,5,6], k = 4"
        n = len(nums)
        if k >= n: k = k % n
        if k == 0: return

        start = 0
        iteration = 0
        while iteration < n:
            iteration += self._rotate(nums, start, k, n)
            start += 1


if __name__ == '__main__':
    sol = Solution()
    _nums = list(range(1, random.randint(10, 50)))
    nums = _nums.copy()
    n = len(nums)
    print(f"\033[32m{nums}\033[0m")
    for k in (random.randint(0, 100) for _ in range(10)):
        sol.rotate(nums, k)
        print(f"    {nums}  k={k} ({k % n})")
        nums = _nums.copy()
