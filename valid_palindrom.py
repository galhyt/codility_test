import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub(r'[\W_]', '', s).lower()
        m = int(len(new_s) / 2)
        r = m if len(new_s) % 2 != 0 else m - 1
        for l, r in zip(range(m), range(len(new_s)-1, r, -1)):
            if new_s[l] != new_s[r]:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    # s = "race e car"
    # s = "ab_a"
    print(sol.isPalindrome(s))
