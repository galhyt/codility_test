from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        n = len(prices)

        while l < n - 1 and r < n:
            pl, pr= prices[l], prices[r]
            if pl >= pr:
                l = r
                r = l + 1
            else:
                profit = max(profit, pr-pl)
                r += 1

        return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    print(sol.maxProfit(prices))

