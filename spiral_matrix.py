from functools import reduce
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        run over first row then last column then last row backwards then first column backwards
        run recursively on inner matrix starts on matrix[1][1] - matrix[-2][-2]
        """
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return reduce(lambda s, l: s + l, matrix)
        if len(matrix[0]) == 0:
            return []

        res = []
        # spiral edges
        res = matrix[0] + list(map(lambda l: l[-1], matrix[1:])) + matrix[-1][-2::-1] + list(map(lambda l: l[0], matrix[-2:0:-1]))

        # run recursively on inner matrix
        res.extend(self.spiralOrder(list(map(lambda l: l[1:-1], matrix[1:-1]))))
        return res


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
    sol = Solution()
    res = sol.spiralOrder(matrix)
    print(res)
