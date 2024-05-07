from functools import reduce
from typing import List


class Solution:
    def _gen_matrix(self, n: int, matrix: List[List[int]], start: int):
        if n == 1:
            matrix[0][0] = start
            return

        val = start
        # first row
        for j in range(n):
            matrix[0][j] = val
            val += 1
        # last column
        for i in range(1, n):
            matrix[i][n-1] = val
            val += 1
        # last row backwards
        for j in range(n-2, -1, -1):
            matrix[n-1][j] = val
            val += 1
        # first column backwards
        for i in range(n-2, 0, -1):
            matrix[i][0] = val
            val += 1

        if n-2 > 0:
            _matrix = reduce(lambda s, l: s + [l[1: n-1]], matrix[1:n-1], [])
            self._gen_matrix(n-2, _matrix, val)
            _i, _j = 0, 0
            for i in range(1, n-1):
                for j in range(1, n-1):
                    matrix[i][j] = _matrix[_i][_j]
                    _j += 1
                _j = 0
                _i += 1

    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        self._gen_matrix(n, matrix, 1)
        return matrix


if __name__ == '__main__':
    sol = Solution()
    matrix = sol.generateMatrix(1)
    print(matrix)