from functools import reduce


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        min_sub = ""
        min_sub_len = 2**31

        while l < len(s) and s[l] not in t:
            l += 1
        if l == len(s):
            return ""

        r = l

        t_dict = {}
        for c in t:
            t_dict.setdefault(c, 0)
            t_dict[c] += 1

        while r < len(s):
            if s[r] in t_dict:
                if t_dict.get(s[r], 0):
                    t_dict[s[r]] -= 1
                else:
                    if s[l] == s[r]:
                        l += 1
                        while l < len(s) and s[l] not in t:
                            l += 1

                if not reduce(lambda s, c: s+t_dict[c], t_dict, 0):
                    print(f"{l}, {r}    {s[l: r+1]}")
                    if r - l + 1 < min_sub_len:
                        min_sub = s[l: r+1]
                        min_sub_len = len(min_sub)

                    if s[l] in t_dict: t_dict[s[l]] += 1
                    l += 1
                    while l < len(s) and s[l] not in t:
                        l += 1
                    if l == len(s):
                        return min_sub
            r += 1

        return min_sub


if __name__ == '__main__':
    s = "acbbaca"
    t = "aba"
    sol = Solution()
    print(f"{s}     {t}")
    print(sol.minWindow(s, t))
