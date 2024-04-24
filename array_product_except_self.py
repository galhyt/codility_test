from typing import List, Optional


class Solution:
    def _product_except_self(self, nums: List[int], answer: List[Optional[int]], start: int, n: int):
        answer[start] = nums[start+1] * answer[start+1]
        for i in range(start+1, n):
            answer[i] *= nums[start]
        start -= 1
        if start >= 0:
            self._product_except_self(nums, answer, start, n)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [None] * (n-1) + [1]
        self._product_except_self(nums, answer, n-2, n)
        return answer


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    sol = Solution()
    answer = sol.productExceptSelf(nums)
    print(answer)
