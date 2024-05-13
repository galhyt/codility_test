from typing import List


def k_sum_closest(nums: List[int], k: int, target: int):
    candidate = sum(nums[:k])
    if candidate >= target:
        return candidate
    candidate = sum(nums[-k:])
    if candidate <= target:
        return candidate

    if k == 1:
        return min(nums, key=lambda n: abs(target-n))

    closest = sum(nums[:k])
    for i, n in enumerate(nums):
        _target = target - n
        candidate = k_sum_closest(nums[i+1:], k-1, _target) + n
        if abs(target - candidate) < abs(target - closest):
            closest = candidate
            if closest == target:
                return closest
    return closest


if __name__ == '__main__':
    nums = [0, 3, 97, 102, 200]
    nums = sorted(nums)
    target = 300
    print(k_sum_closest(nums, 3, target))
