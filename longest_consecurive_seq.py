from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = 0
        for i in nums:
            if i-1 not in s:
                x = i
                n = 0
                while x in s:
                    n += 1
                    x += 1
                l = max(l, n)
        return l


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    print(sol.longestConsecutive(nums))
