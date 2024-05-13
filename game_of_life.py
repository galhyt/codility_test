from functools import reduce
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        1 0 1 0 0 1 1
        0 1 1 0 0 0 1
        0 0 1 0 1 1 1
        1 0 0 1 0 1 0
        1 1 0 0 0 1 0
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                neighboars = (board[i-1][max(j-1, 0):min(j+2, n)] if i > 0 else []) +\
                             ([board[i][j-1] if j > 0 else 0, board[i][j+1] if j < n-1 else 0]) +\
                             (board[i+1][max(j-1, 0):min(j+2, n)] if i+1 < m else [])
                leaving_neighboars = reduce(lambda s, n: s+n%2, neighboars, 0)
                if board[i][j] == 1:
                    if 2 <= leaving_neighboars <= 3:
                        board[i][j] += 2
                else:
                    if leaving_neighboars == 3:
                        board[i][j] += 2

        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] >=2 else 0


if __name__ == '__main__':
    sol = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    sol.gameOfLife(board)
    m = len(board)
    n = len(board[0])
    expected = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    assert all(map(lambda idx: board[idx[0]][idx[1]] == expected[idx[0]][idx[1]], ((i, j) for i in range(m) for j in range(n))))
