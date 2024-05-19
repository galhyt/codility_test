from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        create array of n for each possible amount of element appearences
        """
        n = len(nums)
        count_arr = [[] for _ in range(n+1)]
        count_dict = {}
        for x in nums:
            count_dict.setdefault(x, 0)
            count_dict[x] += 1

        for x, m in count_dict.items():
            count_arr[m].append(x)

        output = []
        for a in list(filter(lambda a: a, count_arr))[-1::-1]:
            output.extend(a)
            if len(output) >= k:
                break

        if len(output) > k:
            output = output[:k]

        return output


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    # nums = [1]
    # k = 1
    #
    nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
    k = 10
    print(sol.topKFrequent(nums, k))


