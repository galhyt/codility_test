"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
can trap after raining.
"""
from typing import List


def get_trapped_rain(height: List[int]) -> int:
    """
    we'll calculate the water height in each index:
        - find sections in height list with differences of height and the height in the section is the minimum
    the rain trapped in each index = water height  - height
    :param height:
    :return:
    """
    try:
        n = len(height)
        first_non_zero = next(filter(lambda i, h: h > 0, enumerate(height)))
        start = first_non_zero[0]
        end = next(filter(lambda i: height[i] > 0, range(len(height)-1, start, -1)))
    except StopIteration:
        return 0

    water_height = height.copy()
    start_h = height[start]
    for i in range(start+1, end):
        water_height[i] = start_h
        if start_h <= height[i]:
            start_h = height[i]





