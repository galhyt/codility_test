from typing import List, Optional


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # calculate prefixes
        output = [1]
        for i in range(1,n):
            output.append(output[i-1] * nums[i-1])

        postfix = 1
        for i in range(-2,-n-1,-1):
            postfix *= nums[i+1]
            output[i] *= postfix

        return output


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    sol = Solution()
    answer = sol.productExceptSelf(nums)
    print(answer)
