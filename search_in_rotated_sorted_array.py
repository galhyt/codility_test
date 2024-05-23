from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        min_val = (0, nums[0])  # index of min value initialized at 0

        while l <= r:
            if nums[l] <= nums[r]:
                if nums[l] < min_val[1]:
                    min_val = (l, nums[l])
                    break

            m = (l + r) // 2
            if nums[m] < min_val[1]:
                min_val = (m, nums[m])
            if nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1

        s = min_val[0]
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            i = (m + s) % n
            if nums[i] == target:
                return i
            elif nums[i] < target:
                l = m + 1
            else:
                r = m - 1

        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    # nums = [3, 1]
    # target = 1
    # nums = [5,1,3]
    # target = 5
    sol = Solution()
    print(sol.search(nums, target))
