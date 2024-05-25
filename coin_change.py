from functools import reduce
from typing import List, Dict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])

        return min_coins[-1] if min_coins[-1] != amount + 1 else -1


if __name__ == '__main__':
    coins = [411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422]
    amount = 9864
    # coins = [186,419,83,408]
    # amount = 6249
    sol = Solution()
    print(sol.coinChange(coins, amount))
