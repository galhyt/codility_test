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
        _t_dict = t_dict.copy()

        while r < len(s):
            if s[r] in t:
                if _t_dict.get(s[r], 0):
                    _t_dict[s[r]] -= 1
                if s[r] in _t_dict:
                    _t_dict.pop(s[r])

                if not _t_dict:
                    if r - l + 1 < min_sub_len:
                        min_sub = s[l: r+1]
                        min_sub_len = len(min_sub)

                    _t_dict = t_dict.copy()
                    if _t_dict.get(s[l], 0):
                        _t_dict[s[l]] -= 1
                    if s[r] in _t_dict:
                        _t_dict.pop(s[l])
                    l += 1
                    while l < len(s) and s[l] not in t:
                        l += 1
                    if l == len(s):
                        return min_sub
            r += 1

        return min_sub


if __name__ == '__main__':
    s = "OUZODYXAZV"
    t = "XYZ"
    sol = Solution()
    print(sol.minWindow(s, t))
