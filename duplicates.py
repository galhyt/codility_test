from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self._remove_duplicates(nums, 0, len(nums) - 1)

    def _remove_duplicates(self, nums: List[int], s: int, e: int) -> int:
        # move over to find duplicates more than twice
        if s == e:
            return 1

        def _roleback():
            roleback_indx = i + 1 - appearences + 2
            k = self._remove_duplicates(nums, i + 1, e)
            # roleback k elements from roleback_indx+1 one place to roleback_indx
            self._roleback(nums, roleback_indx, i + 1, k)
            return roleback_indx - s + k

        appearences = 1
        for i in range(s, e):
            if nums[i] == nums[i+1]:
                appearences += 1
            else:
                if appearences > 2:
                    return _roleback()
                appearences = 1

        if appearences > 2:
            return _roleback()
        return e-s+1

    def _roleback(self, nums: List[int], trg_indx: int, from_indx: int, k: int):
        trg = trg_indx
        for i in range(from_indx, from_indx+k):
            nums[trg] = nums[i]
            trg += 1


class TwoPointerSolution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[k-1]:
                nums[k]=nums[i]
                k+=1
            elif nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k+=1
        return k

if __name__ == '__main__':
    s = TwoPointerSolution()
    test_cases = (([1,1,2,2,2,3], [1,1,2,2,3], 5),
                  ([1,1,1], [1,1], 2),
                  ([1], [1], 1),
                  ([0,0,1,1,1,1,2,3,3], [0,0,1,1,2,3,3], 7))
    for nums, expected, exp_k in test_cases:
        k = s.removeDuplicates(nums)
        assert nums[:k] == expected
        assert k == exp_k
        print(nums[:k])