from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        is_even = n % 2 == 0
        i, j = 0, 0
        median_idx = int(n/2) if not is_even else int(n/2)
        m1 = None

        while i + j <= median_idx and i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                if m1 is None:
                    m1 = nums1[i]
                m2, m1 = m1, nums1[i]
                i += 1
            else:
                if m1 is None:
                    m1 = nums2[j]
                m2, m1 = m1, nums2[j]
                j += 1

        if i + j <= median_idx:
            rem = median_idx - (i+j)
            if i == len(nums1):
                j += rem
                if j > 0:
                    if m1 is None:
                        m1 = nums2[j - 1]
                    elif nums2[j-1] > m1:
                        m1 = nums2[j-1]
                m2, m1 = m1, nums2[j]
            if j == len(nums2):
                i += rem
                if i > 0:
                    if m1 is None:
                        m1 = nums1[i - 1]
                    elif nums1[i-1] > m1:
                        m1 = nums1[i-1]
                m2, m1 = m1, nums1[i]

        return (m1+m2)/2 if is_even else m1


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2, 4, 5, 6]
    # nums1 = [0,0,0,0,0]
    # nums2 = [-1,0,0,0,0,0,1]
    sol = Solution()
    median = sol.findMedianSortedArrays(nums1, nums2)
    print(median)