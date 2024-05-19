from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars, key=lambda c: c[0], reverse=True)

        pre_p, prev_s = None, None
        fleets = 0
        i = 0
        while i < len(cars):
            if not pre_p:
                pre_p, prev_s = cars[i]
                fleets += 1
            else:
                p, s = cars[i]
                pre_t = (target - pre_p) / prev_s
                t = (target - p) / s
                if t > pre_t:
                    fleets += 1
                    pre_p, prev_s = cars[i]
            i += 1
        return fleets


if __name__ == '__main__':
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    sol = Solution()
    print(sol.carFleet(target, position, speed))
