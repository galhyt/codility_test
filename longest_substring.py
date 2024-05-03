

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        max_len = 0
        for c in s:
            try:
                idx = sub.index(c)
                for i in range(idx+1):
                    sub.pop(0)
            except ValueError:
                pass

            sub.append(c)
            max_len = max(len(sub), max_len)
        return max_len


if __name__ == '__main__':
    s = "pwwkew"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))

