from functools import reduce
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        elif n == 2:
            return ['(())', '()()']

        arr = []
        for i in range(1, int(n/2)+1):
            _parenthesis1 = self.generateParenthesis(i)
            if i < n - i:
                _parenthesis2 = self.generateParenthesis(n-i)
                arr += reduce(lambda l, s: s+l, map(lambda x1: list(map(lambda x2: f'{x1}{x2}', _parenthesis1)), _parenthesis2), [])
                arr += reduce(lambda l, s: s+l, map(lambda x1: list(map(lambda x2: f'{x1}{x2}', _parenthesis2)), _parenthesis1), [])
                if i == 1:
                    arr += list(map(lambda x: f'({x})', _parenthesis2))
            else:
                arr += list(map(lambda x: f'{x}{x}', _parenthesis1))
        return list(set(arr))


if __name__ == '__main__':
    sol = Solution()
    arr = sol.generateParenthesis(6)
    print(arr)
    print(len(arr))
