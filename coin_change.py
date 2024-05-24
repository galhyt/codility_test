from functools import reduce
from typing import List, Dict


class Solution:
    def _coinChange(self, coins: List[int], amount: int) -> Dict:
        coins = sorted(coins, reverse=True)
        min_comb = {}
        min_comb_umb = 2 ** 31
        for j in range(len(coins)):
            u = coins[j]
            n = amount // u
            comb = {u: n}
            if amount % u == 0:
                umb_num = reduce(lambda s, u: s + comb[u], comb, 0)
                if umb_num < min_comb_umb:
                    min_comb = comb.copy()
                    min_comb_umb = umb_num

            if j < len(coins) - 1:
                for i in range(n, -1, -1):
                    comb[u] = i
                    _comb = self._coinChange(coins[j+1:], amount - u*i)
                    if _comb:
                        comb.update(_comb)
                        umb_num = reduce(lambda s, u: s+comb[u] , comb, 0)
                        if umb_num < min_comb_umb:
                            min_comb = comb.copy()
                            min_comb_umb = umb_num
        return min_comb

    def coinChange(self, coins: List[int], amount: int) -> int:
        comb = self._coinChange(coins, amount)
        return reduce(lambda s, u: s+comb[u] , comb, 0) if comb else -1


if __name__ == '__main__':
    coins = [411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422]
    amount = 9864
    coins = [186,419,83,408]
    amount = 6249
    sol = Solution()
    print(sol.coinChange(coins, amount))
