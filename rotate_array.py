import random
from typing import List


class Solution:
    def _rotate(self, nums: List[int], start: int, k: int, n: int,rotate_iterations: int) -> None:
        i = start
        next_val = nums[i]
        for _ in range(rotate_iterations):
            rotate_val = next_val
            i_k = i + k if i + k < n else (i + k) % n
            next_val = nums[i_k]
            nums[i_k] = rotate_val
            i = i_k

    def is_primary(self, n: int):
        for p in range(2, int(n / 2)+1):
            if n % p == 0:
                return False
        return True

    def primary_construct(self, n: int):
        p = 2
        for p in range(2, int(n / 2)+1):
            if n % p == 0:
                construction = [p]
                if not self.is_primary(p):
                    construction = self.primary_construct(p)
                partial_const = self.primary_construct(int(n / p))
                construction.extend(partial_const)
                return construction

        return [n]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        " [1,2,3,4,5,6], k = 4"
        n = len(nums)
        if k >= n: k = k % n
        if k == 0: return

        iterations = 1
        if not self.is_primary(n):
            p_n = self.primary_construct(n)
            p_k = self.primary_construct(k)
            inter = set(p_n).intersection(p_k)
            iterations = min(inter) if inter else 1
        start = 0
        rotate_iterations = int(n / iterations)
        for _ in range(iterations):
            self._rotate(nums, start, k, n, rotate_iterations)
            start += 1


if __name__ == '__main__':
    sol = Solution()
    _nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54] #list(range(1, random.randint(10, 20)))
    nums = _nums.copy()
    n = len(nums)
    print(f"\033[32m{nums}\033[0m")
    for k in (45,):#(random.randint(0, 14) for _ in range(10)):
        sol.rotate(nums, k)
        print(f"    {nums}  k={k} ({k % n})")
        nums = _nums.copy()
