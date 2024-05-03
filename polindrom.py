class Solution:
    def is_palindrom(self, s: str):
        n = len(s)
        return all((s[i] == s[-i-1] for i in range(int(n/2))))

    def longestPalindrome(self, s: str) -> str:

        def _longest(s: str, i: int):
            if len(s) <= 1:
                return s
            j = -1
            while True:
                while s[i] != s[j]:
                    j -= 1
                sub = s[i+1:j]
                if i == len(s) + j:
                    return s[i]
                if self.is_palindrom(sub):
                    return s[i] + sub + s[j]
                j -= 1

        max_sub = _longest(s, 0)
        n = len(s)
        for i in range(1, n):
            if n - i <= len(max_sub):
                return max_sub
            _sub = _longest(s, i)
            if len(_sub) > len(max_sub):
                max_sub = _sub
        return max_sub


if __name__ == '__main__':
    s = "cbbdbbcr"
    # s = "aacabdkacaa"
    sol = Solution()
    print(sol.longestPalindrome(s))
