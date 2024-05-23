import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if h == n:
            return max(piles)

        def _hours(k):
            _h = 0
            for p in piles:
                _h += math.ceil(p / k)
            return _h

        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + ((r - l) // 2)
            _h = _hours(k)
            if _h <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res


if __name__ == '__main__':
    piles = [312884470]
    h = 312884469
    sol = Solution()
    print(sol.minEatingSpeed(piles, h))
