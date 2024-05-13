from time import time
from typing import List, Dict


class Solution:
    _combine_dict: Dict[str, List] = {}

    def combine(self, n: int, k: int) -> List[List[int]]:
        return self._combine(1, n, k)

    def _combine(self, s: int, n: int, k: int) -> List[List[int]]:
        key = f"{s}_{n}_{k}"
        if key in self._combine_dict:
            return self._combine_dict[key]

        if k == 1:
            return [[i] for i in range(s, n+1)]

        self._combine_dict[key] = []

        for p in range(s, n-k+2):
            combine_k_1 = self._combine(p+1, n, k-1)
            for comb in combine_k_1:
                new_comb = [p]
                new_comb.extend(comb)
                self._combine_dict[key].append(new_comb)
        return self._combine_dict[key]


if __name__ == '__main__':

    # test_cases = [((3, 2), [[1, 2], [1, 3], [2, 3]]),
    #               ((5,2), [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]),
    #               ((3,3), [[1, 2, 3]]),
    #               ((6, 3), [])]
    #
    # for input, expected in test_cases:
    #     combine = Solution().combine(*input)
    #     print(combine)
    #     # assert combine == expected
    start = time()
    s = Solution()
    # for n in range(1, 21):
    #     # print(f"(1, {n})")
    #     for k in range(1, n+1):
    #         combine = s.combine(n, k)
    #         print(f"  {combine}")
    print(s.combine(6, 3))
    print(f"{int(time()-start)}s")

