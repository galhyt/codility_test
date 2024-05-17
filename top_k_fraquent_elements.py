from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_frequent = [[0, 0]] * k
        nums = sorted(nums)

        while len(nums) > 0:
            x = nums[0]
            n = 0
            while x == nums[0]:
                nums.pop(0)
                n += 1
                if len(nums) == 0:
                    break

            for i in range(k):
                k_n, k_c = k_frequent[i]
                if k_c < n:
                    for j in range(k-2, i-1, -1):
                        k_frequent[j+1] = k_frequent[j]
                    k_frequent[i] = [x, n]
                    break

        return [n for n, c in k_frequent]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    # nums = [1]
    # k = 1
    #
    # nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
    # k = 10
    print(sol.topKFrequent(nums, k))


