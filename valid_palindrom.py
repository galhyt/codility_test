import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub(r'[\W_]', '', s).lower()
        m = int(len(new_s) / 2)
        r = m if len(new_s) % 2 != 0 else m - 1
        return new_s[:m] == new_s[:r:-1]


if __name__ == '__main__':
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    s = "race e car"
    s = "ab_a"
    print(sol.isPalindrome(s))
