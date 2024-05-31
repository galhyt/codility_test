from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        deque = [nums[0]]

        for i in range(1, k):
            while deque and nums[i] > deque[-1]:
                deque.pop(-1)

            deque.append(nums[i])

        res.append(deque[0])

        for l, r in zip(range(1, len(nums)-k+1), range(k, len(nums))):
            if deque:
                if nums[l-1] == deque[0]:
                    deque.pop(0)
                while deque and nums[r] > deque[-1]:
                    deque.pop(-1)

            deque.append(nums[r])
            res.append(deque[0])

        return res

if __name__ == '__main__':
    """
    [1, 2, 1, 0, 4, 3, 6]       k = 3
    [2, 1]     [2]
    [2, 1, 0]   [2, 2]
    [4]         [2, 2, 4]
    [4, 3]      [2, 2, 4, 4]
    """
    # nums = [1, -1]
    # k = 1
    nums = [1, 2, 1, 0, 4, 3, 6]
    k = 3
    sol = Solution()
    print(sol.maxSlidingWindow(nums, k))
