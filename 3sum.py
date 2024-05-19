from functools import reduce
from typing import List, Optional


class Solution:

    def _twosum(self, nums: List[int], target: int) -> Optional[List[int]]:
        i, j = 0, len(nums) - 1
        output = []
        while i < j:
            if i-1 >= 0:
                if nums[i] == nums[i-1]:
                    i += 1
                    continue
            s = nums[i] + nums[j]
            if s == target:
                output.append([nums[i], nums[j]])
                i += 1
            elif s < target:
                i += 1
            else:
                j -= 1
        return output

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        for i in range(len(nums)-2):
            if i-1 >= 0:
                if nums[i] == nums[i-1]:
                    continue
            _twosum = self._twosum(nums[i+1:], -nums[i])
            if _twosum:
                output = reduce(lambda s, a: s + ([[nums[i]]+a]), _twosum, output)
        return output


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    sol = Solution()
    print(sol.threeSum(nums))


