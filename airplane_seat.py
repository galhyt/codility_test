
class Solution:
    def _nth_seat_free_after_mth_person_sat(self, n: int, m: int) -> float:
        """
            -  -  - . . . -
            1 2 3 ... n     1/n
            2 1 3 ... n     1/n * 1/n-1
            3 1 2 ... n     1/n ** 3
            . . .
            4 1 2 ... n
        """
        if m == 0:
            return 1
        prev_m = self._nth_seat_free_after_mth_person_sat(n, m-1)
        # m seat is free after m-1 sat. Actually it's the same as prev_m (problem: above event and following are not strange to each other)
        m_seat_free = prev_m
        # m seat is occupied after m-1 sat
        m_seat_occupied = 1 - m_seat_free
        # n - m / n -m + 1
        n_seat_free = m_seat_free + m_seat_occupied * (n - m) / (n - m + 1)

    def nthPersonGetsNthSeat(self, n: int) -> float:
        return self._nth_seat_free_after_mth_person_sat(n, n-1)

