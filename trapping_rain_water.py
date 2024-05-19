"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
can trap after raining.
"""
from functools import reduce
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = [0 for _ in range(len(height))], [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i-1])
        for j in range(len(height)-2, -1, -1):
            right[j] = max(right[j+1], height[j+1])

        s = reduce(lambda s, t: s + (min(t[:2])-t[2] if t[2] < min(t[:2]) else 0), zip(left, right, height), 0)
        return s


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    sol = Solution()
    print(sol.trap(height))
