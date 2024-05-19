from functools import reduce
from typing import List


class Solution:
    
    def _without_repiteation(self, nums: List[str]):
        h = list(filter(lambda n: n != '.', nums))
        return len(h) == len(list(set(h)))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])

        for row in board:
            if not self._without_repiteation(row):
                return False

        columns = [[row[j] for row in board] for j in range(m)]
        for col in columns:
            if not self._without_repiteation(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid = reduce(lambda s, row: s+ row[j: j+3], board[i: i+3], [])
                if not self._without_repiteation(grid):
                    return False

        return True


if __name__ == '__main__':
    board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

    sol = Solution()
    print(sol.isValidSudoku(board))