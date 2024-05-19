from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        stack = [(0, heights[0])]
        max_area = -2 ** 31

        for i in range(1, len(heights)):
            if stack:
                s_i, s_h = stack[-1]
                if heights[i] < s_h:
                    while stack and heights[i] < s_h:
                        max_area = max(max_area, s_h * (i - s_i))
                        poped_i, _ = stack.pop()
                        if stack:
                            s_i, s_h = stack[-1]
                    stack.append((poped_i, heights[i]))
                else:
                    stack.append((i, heights[i]))
            else:
                stack.append((i, heights[i]))
        i += 1
        while stack:
            s_i, s_h = stack.pop()
            max_area = max(max_area, s_h * (i - s_i))

        return max_area


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    sol = Solution()
    print(sol.largestRectangleArea(heights))
